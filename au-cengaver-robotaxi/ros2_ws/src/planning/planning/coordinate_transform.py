#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
coordinate_transform.py

Algoritma 5: Koordinat Dönüşümü (Lat/Lon → ENU map frame)
  GPS lat/lon verisini map frame'de metrik lokal kartezyen koordinata çevirir

Sözleşme: Localization ↔ Planner Contract v1.2
  - FIX-4: GeoJSON front_bumper referansı → base_link dönüşümü
  - FIX-5: yaw standardı ENU — yaw=0 +x(Doğu), pozitif CCW, [-π,π]
  - FIX-7: Planner /localization/raw_gps okumaz
           Koordinat dönüşümü bu modül tarafından yapılır

Algoritma Tablosu v2.0 §4 Algoritma 5:
  x = R · cos(lat_ref·π/180) · (lon−lon_ref) · π/180
  y = R · (lat−lat_ref) · π/180
  R = 6371000m
"""

import math
from typing import Tuple


# ─── Sabitler ──────────────────────────────────────────────────────────────
R_EARTH = 6371000.0   # Dünya yarıçapı (metre)

# BEE1 front_bumper offset — base_link → front_bumper
# Localization Contract v1.2 FIX-4
# Gerçek araçta kalibrasyon ile ölçülecek
L_FRONT_BUMPER = 2.0   # metre (TBD — kalibrasyon gerekli)


class CoordinateTransform:
    """
    Algoritma 5 — Koordinat Dönüşümü.

    Lat/lon → ENU map frame (x, y) metre cinsinden.
    Equirectangular projeksiyon — küçük alanlar için yeterli (<5km).

    Kullanım:
        ct = CoordinateTransform()
        ct.set_origin(lat_ref=40.789949, lon_ref=29.508726)
        x, y = ct.latlon_to_map(lat, lon)
    """

    def __init__(self):
        self._lat_ref: float = 0.0
        self._lon_ref: float = 0.0
        self._yaw_ref: float = 0.0
        self._locked:  bool  = False

    # ───────────────────────────────────────────────────────────────────────
    # ORIGIN
    # ───────────────────────────────────────────────────────────────────────

    def set_origin(
        self,
        lat_ref: float,
        lon_ref: float,
        yaw_ref: float = 0.0
    ):
        """
        Map origin'i ayarla.
        Localization Contract FIX-3: locked=true gelince çağrılır.
        """
        self._lat_ref = lat_ref
        self._lon_ref = lon_ref
        self._yaw_ref = self._normalize_angle(yaw_ref)
        self._locked  = True

    @property
    def is_locked(self) -> bool:
        """Origin kilitli mi?"""
        return self._locked

    @property
    def origin(self) -> Tuple[float, float, float]:
        """(lat_ref, lon_ref, yaw_ref)"""
        return self._lat_ref, self._lon_ref, self._yaw_ref

    # ───────────────────────────────────────────────────────────────────────
    # DÖNÜŞÜM FONKSİYONLARI
    # ───────────────────────────────────────────────────────────────────────

    def latlon_to_map(
        self,
        lat: float,
        lon: float
    ) -> Tuple[float, float]:
        """
        Lat/lon → map frame (x, y) metre.
        Algoritma 5 — Equirectangular projeksiyon.

        FIX-5: ENU standardı
          x = R · cos(lat_ref·π/180) · Δlon · π/180  → Doğu (+x)
          y = R · Δlat · π/180                        → Kuzey (+y)
        """
        if not self._locked:
            raise RuntimeError(
                'CoordinateTransform: origin henüz kilitlenmedi! '
                'set_origin() çağrılmadan dönüşüm yapılamaz.'
            )

        dlat = lat - self._lat_ref
        dlon = lon - self._lon_ref

        x = R_EARTH * math.cos(math.radians(self._lat_ref)) \
            * math.radians(dlon)
        y = R_EARTH * math.radians(dlat)

        return x, y

    def map_to_latlon(
        self,
        x: float,
        y: float
    ) -> Tuple[float, float]:
        """
        Map frame (x, y) → lat/lon (ters dönüşüm).
        Debug ve test amaçlı.
        """
        if not self._locked:
            raise RuntimeError(
                'CoordinateTransform: origin henüz kilitlenmedi!'
            )

        dlat = y / R_EARTH
        dlon = x / (R_EARTH * math.cos(math.radians(self._lat_ref)))

        lat = self._lat_ref + math.degrees(dlat)
        lon = self._lon_ref + math.degrees(dlon)

        return lat, lon

    def front_bumper_to_base_link(
        self,
        x_wp: float,
        y_wp: float,
        yaw: float,
        l_fb: float = L_FRONT_BUMPER
    ) -> Tuple[float, float]:
        """
        GeoJSON front_bumper referansını base_link'e çevir.
        Localization Contract v1.2 FIX-4.

        GeoJSON noktaları front_bumper'a göre tanımlıdır.
        Planner base_link'e çevirip kullanır.

        x_base = x_wp - L_fb * cos(yaw)
        y_base = y_wp - L_fb * sin(yaw)
        """
        x_base = x_wp - l_fb * math.cos(yaw)
        y_base = y_wp - l_fb * math.sin(yaw)
        return x_base, y_base

    def base_link_to_front_bumper(
        self,
        x_base: float,
        y_base: float,
        yaw: float,
        l_fb: float = L_FRONT_BUMPER
    ) -> Tuple[float, float]:
        """base_link → front_bumper (ters dönüşüm)."""
        x_wp = x_base + l_fb * math.cos(yaw)
        y_wp = y_base + l_fb * math.sin(yaw)
        return x_wp, y_wp

    def map_to_base_link(
        self,
        target_x_map: float,
        target_y_map: float,
        ego_x: float,
        ego_y: float,
        ego_yaw: float
    ) -> Tuple[float, float]:
        """
        Map frame → base_link frame dönüşümü.
        Planner ↔ Controller Contract v1.3 FIX-4:
          active_route_context base_link frame'inde yayınlanır.

        dx = target_x - ego_x
        dy = target_y - ego_y
        x_bl =  dx * cos(yaw) + dy * sin(yaw)
        y_bl = -dx * sin(yaw) + dy * cos(yaw)
        """
        dx = target_x_map - ego_x
        dy = target_y_map - ego_y

        x_bl =  dx * math.cos(ego_yaw) + dy * math.sin(ego_yaw)
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
        """base_link → map frame (ters dönüşüm)."""
        x_map = ego_x + x_bl * math.cos(ego_yaw) \
                      - y_bl * math.sin(ego_yaw)
        y_map = ego_y + x_bl * math.sin(ego_yaw) \
                      + y_bl * math.cos(ego_yaw)
        return x_map, y_map

    def distance_between(
        self,
        x1: float, y1: float,
        x2: float, y2: float
    ) -> float:
        """İki map frame noktası arası Öklid mesafesi."""
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # ───────────────────────────────────────────────────────────────────────
    # YARDIMCI
    # ───────────────────────────────────────────────────────────────────────

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-π, π] aralığına normalize et."""
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle