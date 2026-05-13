#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
geojson_loader.py

Algoritma 1: GeoJSON Rota Parser
"""

import json
import math
from dataclasses import dataclass
from typing import List, Optional

from .coordinate_transform import CoordinateTransform


# Contract uyumlu waypoint tipleri
# planning_msgs/GoalReached.msg ile aynı tutulmalı:
# PICKUP=0, DROPOFF=1, WAYPOINT=2, PARK_ENTRY=3
WAYPOINT_PICKUP = 0
WAYPOINT_DROPOFF = 1
WAYPOINT_NORMAL = 2
WAYPOINT_PARK_ENTRY = 3

WAYPOINT_TYPE_MAP = {
    'PICKUP': WAYPOINT_PICKUP,
    'DROPOFF': WAYPOINT_DROPOFF,
    'WAYPOINT': WAYPOINT_NORMAL,
    'NORMAL': WAYPOINT_NORMAL,
    'START': WAYPOINT_NORMAL,
    'PARK_ENTRY': WAYPOINT_PARK_ENTRY,
    'PARK': WAYPOINT_PARK_ENTRY,
}

WAYPOINT_TYPE_NAMES = {
    WAYPOINT_PICKUP: 'PICKUP',
    WAYPOINT_DROPOFF: 'DROPOFF',
    WAYPOINT_NORMAL: 'WAYPOINT',
    WAYPOINT_PARK_ENTRY: 'PARK_ENTRY',
}


@dataclass
class Waypoint:
    """Tek bir waypoint."""
    id: int
    x: float          # map frame, metre, base_link referanslı
    y: float          # map frame, metre, base_link referanslı
    yaw: float        # hedef yön, rad, ENU
    type: int         # PICKUP=0, DROPOFF=1, WAYPOINT=2, PARK_ENTRY=3
    lat: float        # debug
    lon: float        # debug
    name: str

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
    GeoJSON dosyasını okur ve waypoint listesi üretir.
    Koordinat dönüşümü için CoordinateTransform kullanır.
    """

    def __init__(self, coord_transform: CoordinateTransform):
        self._ct = coord_transform
        self._waypoints: List[Waypoint] = []
        self._loaded = False

    def load(self, filepath: str) -> List[Waypoint]:
        """GeoJSON dosyasını yükle."""
        if not filepath:
            raise ValueError('GeoJsonLoader: mission_file boş olamaz.')

        if not self._ct.is_locked:
            raise RuntimeError(
                'GeoJsonLoader: CoordinateTransform origin kilitlenmedi. '
                'map_origin.locked=true gelmeden waypoint işlenemez.'
            )

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        return self._load_from_dict(data)

    def load_from_string(self, geojson_str: str) -> List[Waypoint]:
        """GeoJSON string üzerinden yükle. Test için kullanılır."""
        if not geojson_str:
            raise ValueError('GeoJsonLoader: geojson_str boş olamaz.')

        if not self._ct.is_locked:
            raise RuntimeError(
                'GeoJsonLoader: CoordinateTransform origin kilitlenmedi.'
            )

        data = json.loads(geojson_str)
        return self._load_from_dict(data)

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

    def _load_from_dict(self, data: dict) -> List[Waypoint]:
        """GeoJSON dict içeriğini waypoint listesine çevirir."""
        if data.get('type') != 'FeatureCollection':
            raise ValueError(
                f'GeoJSON formatı hatalı: type=FeatureCollection bekleniyor, '
                f'bulunan: {data.get("type")}'
            )

        features = data.get('features', [])
        if not features:
            raise ValueError('GeoJSON dosyasında hiç Feature bulunamadı.')

        waypoints: List[Waypoint] = []

        for i, feature in enumerate(features):
            wp = self._parse_feature(i, feature)
            if wp is not None:
                waypoints.append(wp)

        if not waypoints:
            raise ValueError('GeoJSON içinde geçerli waypoint bulunamadı.')

        waypoints.sort(key=lambda w: w.id)

        self._waypoints = waypoints
        self._loaded = True

        return self._waypoints

    def _parse_feature(self, index: int, feature: dict) -> Optional[Waypoint]:
        """
        Tek bir GeoJSON Feature'ı Waypoint'e dönüştürür.

        Beklenen format:
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
            "coordinates": [lon, lat]
          }
        }
        """
        geometry = feature.get('geometry', {})
        properties = feature.get('properties', {})

        if geometry.get('type') != 'Point':
            return None

        coords = geometry.get('coordinates', [])
        if len(coords) < 2:
            return None

        try:
            lon = float(coords[0])
            lat = float(coords[1])

            if not math.isfinite(lat) or not math.isfinite(lon):
                return None

            x_map, y_map = self._ct.latlon_to_map(lat, lon)

            yaw_deg = float(properties.get('yaw_deg', 0.0))
            yaw_rad = self._normalize_angle(math.radians(yaw_deg))

            # GeoJSON waypoint front_bumper referanslı kabul edilir.
            # Planner içinde base_link referansına çevrilir.
            x_base, y_base = self._ct.front_bumper_to_base_link(
                x_map,
                y_map,
                yaw_rad,
            )

            type_str = str(properties.get('type', 'WAYPOINT')).upper()
            wp_type = WAYPOINT_TYPE_MAP.get(type_str, WAYPOINT_NORMAL)

            wp_id = int(properties.get('id', index))
            name = str(properties.get('name', f'wp_{wp_id}'))

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

        except (ValueError, TypeError):
            return None

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-pi, pi] aralığına normalize eder."""
        while angle > math.pi:
            angle -= 2.0 * math.pi

        while angle < -math.pi:
            angle += 2.0 * math.pi

        return angle


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
