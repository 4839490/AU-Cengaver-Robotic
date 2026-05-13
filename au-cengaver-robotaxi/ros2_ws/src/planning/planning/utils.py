#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
utils.py — Ortak yardımcı fonksiyonlar
"""

import math


def normalize_angle(angle: float) -> float:
    """Açıyı [-π, π] aralığına normalize et."""
    while angle >  math.pi: angle -= 2.0 * math.pi
    while angle < -math.pi: angle += 2.0 * math.pi
    return angle


def euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """İki nokta arası Öklid mesafesi."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def heading_error(yaw1: float, yaw2: float) -> float:
    """İki yaw açısı arasındaki fark — [-π, π]."""
    return normalize_angle(yaw1 - yaw2)


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Değeri [min, max] aralığına kısıtla."""
    return max(min_val, min(max_val, value))