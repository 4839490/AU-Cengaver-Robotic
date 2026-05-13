#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
geojson_loader.py

Algoritma 1: GeoJSON Rota Parser
  Yarışma günü rota dosyasını okuyarak waypoint listesi üretir

Algoritma Tablosu v2.0 §4 Algoritma 1:
  - json.load ile GeoJSON oku
  - Her Feature için lat/lon al
  - EKF referans noktasından map frame'e dönüştür
  - Waypoint listesini (id, x, y, type) bellekte sakla
  - active_waypoint_id=0 ile başlat

Sözleşme: Localization ↔ Planner Contract v1.2
  - FIX-4: GeoJSON front_bumper referansı → base_link dönüşümü
  - FIX-7: Planner raw_gps okumaz — dönüşüm bu modül yapar
  - map_origin.locked=true gelmeden waypoint işleme
"""

import json
import math
from dataclasses import dataclass
from typing import List, Optional

from .coordinate_transform import CoordinateTransform


# ─── Waypoint Tipleri ──────────────────────────────────────────────────────
WAYPOINT_TYPE_MAP = {
    'WAYPOINT':   0,
    'PICKUP':     1,
    'DROPOFF':    2,
    'PARK_ENTRY': 3,
    'PARK':       3,   # alias
}

WAYPOINT_TYPE_NAMES = {v: k for k, v in WAYPOINT_TYPE_MAP.items()}


@dataclass
class Waypoint:
    """Tek bir waypoint."""
    id:        int
    x:         float    # map frame, metre
    y:         float    # map frame, metre
    yaw:       float    # hedef yön (radyan) — ENU
    type:      int      # WAYPOINT=0, PICKUP=1, DROPOFF=2, PARK_ENTRY=3
    lat:       float    # orijinal enlem (debug)
    lon:       float    # orijinal boylam (debug)
    name:      str      # GeoJSON feature name

    @property
    def type_name(self) -> str:
        return WAYPOINT_TYPE_NAMES.get(self.type, 'UNKNOWN')

    def __repr__(self):
        return (
            f'Waypoint(id={self.id}, type={self.type_name}, '
            f'x={self.x:.2f}, y={self.y:.2f}, yaw={self.yaw:.3f})'
        )


class GeoJsonLoader:
    """
    Algoritma 1 — GeoJSON Rota Parser.

    GeoJSON dosyasını okur, waypoint listesi üretir.
    Koordinat dönüşümü için CoordinateTransform kullanır.

    Kullanım:
        loader = GeoJsonLoader(coord_transform)
        waypoints = loader.load('/path/to/mission.geojson')
    """

    def __init__(self, coord_transform: CoordinateTransform):
        self._ct = coord_transform
        self._waypoints: List[Waypoint] = []
        self._loaded = False

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API
    # ───────────────────────────────────────────────────────────────────────

    def load(self, filepath: str) -> List[Waypoint]:
        """
        GeoJSON dosyasını yükle ve waypoint listesi üret.

        Algoritma 1 adımları:
          1. json.load ile oku
          2. Her Feature için lat/lon al
          3. map frame'e dönüştür
          4. Waypoint listesi oluştur
          5. active_waypoint_id=0 ile başlat

        Raises:
            RuntimeError: map_origin kilitli değilse
            FileNotFoundError: dosya bulunamazsa
            ValueError: GeoJSON formatı yanlışsa
        """
        if not self._ct.is_locked:
            raise RuntimeError(
                'GeoJsonLoader: CoordinateTransform origin kilitlenmedi! '
                'map_origin.locked=true gelmeden waypoint işlenemez.'
            )

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if data.get('type') != 'FeatureCollection':
            raise ValueError(
                f'GeoJSON formatı hatalı: type=FeatureCollection bekleniyor, '
                f'bulunan: {data.get("type")}'
            )

        features = data.get('features', [])
        if not features:
            raise ValueError('GeoJSON dosyasında hiç Feature bulunamadı.')

        waypoints = []
        for i, feature in enumerate(features):
            wp = self._parse_feature(i, feature)
            if wp is not None:
                waypoints.append(wp)

        # ID'ye göre sırala
        waypoints.sort(key=lambda w: w.id)

        self._waypoints = waypoints
        self._loaded    = True

        return self._waypoints

    def load_from_string(self, geojson_str: str) -> List[Waypoint]:
        """GeoJSON string'den yükle (test amaçlı)."""
        if not self._ct.is_locked:
            raise RuntimeError('map_origin kilitlenmedi!')

        data = json.loads(geojson_str)
        features = data.get('features', [])
        waypoints = []

        for i, feature in enumerate(features):
            wp = self._parse_feature(i, feature)
            if wp is not None:
                waypoints.append(wp)

        waypoints.sort(key=lambda w: w.id)
        self._waypoints = waypoints
        self._loaded    = True

        return self._waypoints

    @property
    def waypoints(self) -> List[Waypoint]:
        return self._waypoints

    @property
    def is_loaded(self) -> bool:
        return self._loaded

    def get_waypoint(self, wp_id: int) -> Optional[Waypoint]:
        """ID'ye göre waypoint getir."""
        for wp in self._waypoints:
            if wp.id == wp_id:
                return wp
        return None

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE
    # ───────────────────────────────────────────────────────────────────────

    def _parse_feature(self, index: int, feature: dict) -> Optional[Waypoint]:
        """
        Tek bir GeoJSON Feature'ı Waypoint'e dönüştür.

        GeoJSON format:
        {
          "type": "Feature",
          "properties": {
            "name": "PICKUP_1",
            "id": 1,
            "type": "PICKUP",
            "yaw_deg": 90.0
          },
          "geometry": {
            "type": "Point",
            "coordinates": [lon, lat]  ← GeoJSON'da lon önce!
          }
        }
        """
        try:
            geometry   = feature.get('geometry', {})
            properties = feature.get('properties', {})

            if geometry.get('type') != 'Point':
                return None

            # GeoJSON'da koordinat sırası: [lon, lat]
            coords = geometry.get('coordinates', [])
            if len(coords) < 2:
                return None

            lon = float(coords[0])
            lat = float(coords[1])

            # Lat/lon → map frame
            x_map, y_map = self._ct.latlon_to_map(lat, lon)

            # FIX-4: front_bumper → base_link dönüşümü
            # yaw önce bilinmeli — properties'ten al
            yaw_deg = float(properties.get('yaw_deg', 0.0))
            yaw_rad = math.radians(yaw_deg)
            yaw_rad = self._normalize_angle(yaw_rad)

            x_base, y_base = self._ct.front_bumper_to_base_link(
                x_map, y_map, yaw_rad
            )

            # Waypoint tipi
            type_str = properties.get('type', 'WAYPOINT').upper()
            wp_type  = WAYPOINT_TYPE_MAP.get(type_str, 0)

            # ID
            wp_id = int(properties.get('id', index))

            # İsim
            name = properties.get('name', f'wp_{wp_id}')

            return Waypoint(
                id=wp_id,
                x=x_base,
                y=y_base,
                yaw=yaw_rad,
                type=wp_type,
                lat=lat,
                lon=lon,
                name=name,
            )

        except (KeyError, ValueError, TypeError) as e:
            # Hatalı feature'ı atla
            return None

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-π, π] aralığına normalize et."""
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle


# ─── Örnek GeoJSON ─────────────────────────────────────────────────────────
SAMPLE_GEOJSON = """
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "id": 0,
        "name": "START",
        "type": "WAYPOINT",
        "yaw_deg": 0.0
      },
      "geometry": {
        "type": "Point",
        "coordinates": [29.508726, 40.789949]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "id": 1,
        "name": "PICKUP_1",
        "type": "PICKUP",
        "yaw_deg": 90.0
      },
      "geometry": {
        "type": "Point",
        "coordinates": [29.509000, 40.790200]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "id": 2,
        "name": "DROPOFF_1",
        "type": "DROPOFF",
        "yaw_deg": 180.0
      },
      "geometry": {
        "type": "Point",
        "coordinates": [29.509500, 40.790500]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "id": 3,
        "name": "PARK_ENTRY",
        "type": "PARK_ENTRY",
        "yaw_deg": 270.0
      },
      "geometry": {
        "type": "Point",
        "coordinates": [29.510000, 40.790800]
      }
    }
  ]
}
"""