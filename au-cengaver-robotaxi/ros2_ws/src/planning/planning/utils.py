#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
utils.py — Ortak yardımcı fonksiyonlar
"""

import math
from typing import Any


def safe_float(value: Any, fallback: float = 0.0) -> float:
    """Değeri güvenli şekilde float'a çevirir; NaN/inf gelirse fallback döner."""
    try:
        value = float(value)
    except Exception:
        return fallback

    if not math.isfinite(value):
        return fallback

    return value


def normalize_angle(angle: float) -> float:
    """Açıyı [-pi, pi] aralığına normalize eder."""
    angle = safe_float(angle, 0.0)
    return math.atan2(math.sin(angle), math.cos(angle))


def euclidean_distance(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> float:
    """İki nokta arası Öklid mesafesi."""
    x1 = safe_float(x1)
    y1 = safe_float(y1)
    x2 = safe_float(x2)
    y2 = safe_float(y2)

    return math.hypot(x2 - x1, y2 - y1)


def heading_error(
    target_yaw: float,
    current_yaw: float,
) -> float:
    """
    Hedef yaw ile mevcut yaw arasındaki hata.

    Pozitif değer: hedef, mevcut yöne göre CCW tarafta.
    """
    return normalize_angle(target_yaw - current_yaw)


def clamp(
    value: float,
    min_val: float,
    max_val: float,
) -> float:
    """Değeri [min_val, max_val] aralığına kısıtlar."""
    value = safe_float(value)
    min_val = safe_float(min_val)
    max_val = safe_float(max_val)

    if min_val > max_val:
        min_val, max_val = max_val, min_val

    return max(min_val, min(max_val, value))


def is_finite_number(value: Any) -> bool:
    """Değer sonlu bir sayıya çevrilebiliyor mu?"""
    try:
        return math.isfinite(float(value))
    except Exception:
        return False
