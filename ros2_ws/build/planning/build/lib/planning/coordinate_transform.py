#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
coordinate_transform.py

Algoritma 5: Koordinat Dönüşümü (Lat/Lon → ENU map frame)

Görev:
  GPS / GeoJSON lat-lon koordinatlarını map frame'de metrik ENU koordinatlara çevirir.

Sözleşme: Localization ↔ Planner Contract v1.2
  - FIX-4: GeoJSON front_bumper referansı → base_link dönüşümü
  - FIX-5: yaw standardı ENU — yaw=0 +x(Doğu), pozitif CCW, [-π, π]
  - FIX-7: Planner /localization/raw_gps okumaz

Not:
  Bu modül map frame'i ENU kabul eder:
    +x = Doğu
    +y = Kuzey

  yaw_ref lat/lon projeksiyonunu döndürmek için kullanılmaz.
  Sadece referans yön / metadata olarak saklanır.
"""

import math
from typing import Tuple


# ─── Sabitler ──────────────────────────────────────────────────────────────
R_EARTH = 6371000.0

# base_link → front_bumper offset
# Gerçek araçta kalibrasyonla güncellenmeli.
L_FRONT_BUMPER = 2.0


class CoordinateTransform:
    """
    Lat/lon → ENU map frame dönüşümü.

    Küçük alanlar için equirectangular projeksiyon kullanılır.
    Robotaksi parkuru gibi kısa mesafeli alanlarda yeterlidir.
    """

    def __init__(self):
        self._lat_ref: float = 0.0
        self._lon_ref: float = 0.0
        self._yaw_ref: float = 0.0
        self._locked: bool = False

    # ───────────────────────────────────────────────────────────────────────
    # ORIGIN
    # ───────────────────────────────────────────────────────────────────────

    def set_origin(
        self,
        lat_ref: float,
        lon_ref: float,
        yaw_ref: float = 0.0
    ) -> None:
        """
        Map origin'i ayarlar.

        Localization Contract FIX-3:
        /localization/map_origin locked=true gelince çağrılmalıdır.
        """
        if not math.isfinite(lat_ref) or not math.isfinite(lon_ref):
            raise ValueError(
                'CoordinateTransform: lat_ref/lon_ref geçersiz veya NaN.'
            )

        if lat_ref < -90.0 or lat_ref > 90.0:
            raise ValueError(
                f'CoordinateTransform: lat_ref aralık dışı: {lat_ref}'
            )

        if lon_ref < -180.0 or lon_ref > 180.0:
            raise ValueError(
                f'CoordinateTransform: lon_ref aralık dışı: {lon_ref}'
            )

        self._lat_ref = float(lat_ref)
        self._lon_ref = float(lon_ref)
        self._yaw_ref = self._normalize_angle(float(yaw_ref))
        self._locked = True

    @property
    def is_locked(self) -> bool:
        """Origin kilitli mi?"""
        return self._locked

    @property
    def origin(self) -> Tuple[float, float, float]:
        """(lat_ref, lon_ref, yaw_ref) döndürür."""
        return self._lat_ref, self._lon_ref, self._yaw_ref

    # ───────────────────────────────────────────────────────────────────────
    # LAT/LON ↔ MAP
    # ───────────────────────────────────────────────────────────────────────

    def latlon_to_map(
        self,
        lat: float,
        lon: float
    ) -> Tuple[float, float]:
        """
        Lat/lon → map frame (x, y) metre.

        ENU standardı:
          x = Doğu (+x)
          y = Kuzey (+y)

        Formül:
          x = R * cos(lat_ref) * delta_lon
          y = R * delta_lat
        """
        self._require_locked()

        if not math.isfinite(lat) or not math.isfinite(lon):
            raise ValueError('CoordinateTransform: lat/lon geçersiz veya NaN.')

        dlat = float(lat) - self._lat_ref
        dlon = float(lon) - self._lon_ref

        x = (
            R_EARTH
            * math.cos(math.radians(self._lat_ref))
            * math.radians(dlon)
        )
        y = R_EARTH * math.radians(dlat)

        return x, y

    def map_to_latlon(
        self,
        x: float,
        y: float
    ) -> Tuple[float, float]:
        """
        map frame (x, y) metre → lat/lon.

        Debug, test ve doğrulama için kullanılır.
        """
        self._require_locked()

        if not math.isfinite(x) or not math.isfinite(y):
            raise ValueError('CoordinateTransform: x/y geçersiz veya NaN.')

        cos_lat = math.cos(math.radians(self._lat_ref))
        if abs(cos_lat) < 1e-9:
            raise RuntimeError(
                'CoordinateTransform: lat_ref kutuplara çok yakın, '
                'map_to_latlon güvenli değil.'
            )

        dlat = float(y) / R_EARTH
        dlon = float(x) / (R_EARTH * cos_lat)

        lat = self._lat_ref + math.degrees(dlat)
        lon = self._lon_ref + math.degrees(dlon)

        return lat, lon

    # ───────────────────────────────────────────────────────────────────────
    # FRONT_BUMPER ↔ BASE_LINK
    # ───────────────────────────────────────────────────────────────────────

    def front_bumper_to_base_link(
        self,
        x_wp: float,
        y_wp: float,
        yaw: float,
        l_fb: float = L_FRONT_BUMPER
    ) -> Tuple[float, float]:
        """
        GeoJSON front_bumper referanslı waypoint'i base_link'e çevirir.

        Contract FIX-4:
          x_base = x_wp - L_fb * cos(yaw)
          y_base = y_wp - L_fb * sin(yaw)
        """
        yaw = self._normalize_angle(float(yaw))

        x_base = float(x_wp) - float(l_fb) * math.cos(yaw)
        y_base = float(y_wp) - float(l_fb) * math.sin(yaw)

        return x_base, y_base

    def base_link_to_front_bumper(
        self,
        x_base: float,
        y_base: float,
        yaw: float,
        l_fb: float = L_FRONT_BUMPER
    ) -> Tuple[float, float]:
        """
        base_link referanslı noktayı front_bumper referansına çevirir.
        """
        yaw = self._normalize_angle(float(yaw))

        x_wp = float(x_base) + float(l_fb) * math.cos(yaw)
        y_wp = float(y_base) + float(l_fb) * math.sin(yaw)

        return x_wp, y_wp

    # ───────────────────────────────────────────────────────────────────────
    # MAP ↔ BASE_LINK
    # ───────────────────────────────────────────────────────────────────────

    def map_to_base_link(
        self,
        target_x_map: float,
        target_y_map: float,
        ego_x: float,
        ego_y: float,
        ego_yaw: float
    ) -> Tuple[float, float]:
        """
        map frame → base_link frame dönüşümü.

        Planner ↔ Controller Contract v1.3 FIX-4:
        /planning/active_route_context base_link frame'inde yayınlanır.

        Formül:
          dx = target_x - ego_x
          dy = target_y - ego_y

          x_bl =  dx*cos(yaw) + dy*sin(yaw)
          y_bl = -dx*sin(yaw) + dy*cos(yaw)
        """
        ego_yaw = self._normalize_angle(float(ego_yaw))

        dx = float(target_x_map) - float(ego_x)
        dy = float(target_y_map) - float(ego_y)

        x_bl = dx * math.cos(ego_yaw) + dy * math.sin(ego_yaw)
        y_bl = -dx * math.sin(ego_yaw) + dy * math.cos(ego_yaw)

        return x_bl, y_bl

    def base_link_to_map(
        self,
        x_bl: float,
        y_bl: float,
        ego_x: float,
        ego_y: float,
        ego_yaw: float
    ) -> Tuple[float, float]:
        """
        base_link frame → map frame dönüşümü.
        """
        ego_yaw = self._normalize_angle(float(ego_yaw))

        x_map = (
            float(ego_x)
            + float(x_bl) * math.cos(ego_yaw)
            - float(y_bl) * math.sin(ego_yaw)
        )
        y_map = (
            float(ego_y)
            + float(x_bl) * math.sin(ego_yaw)
            + float(y_bl) * math.cos(ego_yaw)
        )

        return x_map, y_map

    # ───────────────────────────────────────────────────────────────────────
    # GEOMETRY HELPERS
    # ───────────────────────────────────────────────────────────────────────

    @staticmethod
    def distance_between(
        x1: float,
        y1: float,
        x2: float,
        y2: float
    ) -> float:
        """İki map frame noktası arası Öklid mesafesi."""
        return math.hypot(float(x2) - float(x1), float(y2) - float(y1))

    # ───────────────────────────────────────────────────────────────────────
    # YARDIMCI
    # ───────────────────────────────────────────────────────────────────────

    def _require_locked(self) -> None:
        """Origin kilitli değilse hata verir."""
        if not self._locked:
            raise RuntimeError(
                'CoordinateTransform: origin henüz kilitlenmedi. '
                'Önce set_origin() çağrılmalı.'
            )

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-pi, pi] aralığına normalize eder."""
        while angle > math.pi:
            angle -= 2.0 * math.pi

        while angle < -math.pi:
            angle += 2.0 * math.pi

        return angle
