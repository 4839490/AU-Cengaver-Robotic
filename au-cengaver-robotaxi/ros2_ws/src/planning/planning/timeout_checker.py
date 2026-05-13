#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
timeout_checker.py

Algoritma 17: FSM-Planner Timeout ve Mesaj Denetleyici
  Tüm perception ve localization topic'lerinin zaman aşımını izler
  Fallback kararı üretir

Sözleşme: Planner ↔ Controller Contract v1.3 §13
  - /perception/lane_model timeout → 2s son model, sonra STOP_APPROACH
  - /perception/obstacle_tracks timeout → engel varmış gibi davran
  - /localization/pose timeout → 500ms son pose, sonra STOP_APPROACH
  - /localization/status timeout → status=LOST gibi davran
  - /controller/feedback timeout → status=EMERGENCY

MVP'nin ilk yazılacak komponenti — Algoritma Tablosu v2.0 §5
"""

import time
from dataclasses import dataclass, field
from typing import Dict, Optional


# ─── Topic Timeout Sabitleri (ms) ──────────────────────────────────────────
TIMEOUT_MS = {
    '/perception/lane_model':        500,
    '/perception/obstacle_tracks':   500,
    '/perception/traffic_light_state': 300,
    '/perception/traffic_signs':     1000,
    '/perception/stop_target':       500,
    '/localization/pose':            300,
    '/localization/odometry':        200,
    '/localization/status':          300,
    '/localization/map_origin':      None,   # latching — timeout yok
    '/controller/feedback':          500,
    '/fsm/current_mode':             500,
    '/fsm/mission_state':            1000,
}

# ─── Fallback Kademeleri ───────────────────────────────────────────────────
# Planner ↔ Controller Contract v1.3 §13
STALE_MS  = 500    # STALE kademe — hız düşür, devam
STOP_MS   = 1000   # STOP kademe — STOP_APPROACH


@dataclass
class TopicStatus:
    """Tek bir topic'in izleme durumu."""
    name:          str
    timeout_ms:    Optional[int]
    last_recv_ns:  Optional[int] = None   # nanosaniye
    stale:         bool          = False
    timed_out:     bool          = False
    warning_flags: list          = field(default_factory=list)


class TimeoutChecker:
    """
    Algoritma 17 — FSM-Planner Timeout ve Mesaj Denetleyici.

    Kullanım:
        checker = TimeoutChecker()
        checker.update('/perception/lane_model')   # mesaj gelince
        result = checker.check_all()               # her döngüde
    """

    def __init__(self):
        self._topics: Dict[str, TopicStatus] = {}

        for topic, timeout_ms in TIMEOUT_MS.items():
            self._topics[topic] = TopicStatus(
                name=topic,
                timeout_ms=timeout_ms
            )

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API
    # ───────────────────────────────────────────────────────────────────────

    def update(self, topic: str):
        """Mesaj alındığında timestamp güncelle."""
        if topic in self._topics:
            self._topics[topic].last_recv_ns = time.monotonic_ns()
            self._topics[topic].stale       = False
            self._topics[topic].timed_out   = False
            self._topics[topic].warning_flags = []

    def check_all(self) -> dict:
        """
        Tüm topic'leri kontrol et.

        Returns:
            {
                'warnings':        [str] — aktif uyarılar
                'stale_topics':    [str] — STALE durumundaki topic'ler
                'timeout_topics':  [str] — TIMEOUT durumundaki topic'ler
                'emergency':       bool  — EMERGENCY_STOP gerekiyor mu
                'stop_approach':   bool  — STOP_APPROACH gerekiyor mu
                'speed_reduce':    bool  — hız düşür
                'fallback_reason': str   — sebep
            }
        """
        now_ns = time.monotonic_ns()

        warnings       = []
        stale_topics   = []
        timeout_topics = []
        emergency      = False
        stop_approach  = False
        speed_reduce   = False
        fallback_reason = ''

        for topic, status in self._topics.items():
            if status.timeout_ms is None:
                continue   # latching topic — timeout yok

            if status.last_recv_ns is None:
                # Hiç mesaj gelmedi
                warnings.append(f'NO_DATA:{topic}')
                stale_topics.append(topic)
                status.stale = True
                continue

            elapsed_ms = (now_ns - status.last_recv_ns) / 1e6

            if elapsed_ms > STOP_MS:
                # STOP kademesi
                status.timed_out = True
                status.stale     = True
                timeout_topics.append(topic)
                warnings.append(f'TIMEOUT:{topic}')

                result = self._handle_timeout(topic)
                if result == 'EMERGENCY':
                    emergency = True
                    fallback_reason = topic
                elif result == 'STOP_APPROACH':
                    stop_approach = True
                    if not fallback_reason:
                        fallback_reason = topic

            elif elapsed_ms > STALE_MS:
                # STALE kademesi — hız düşür
                status.stale = True
                stale_topics.append(topic)
                warnings.append(f'STALE:{topic}')
                speed_reduce = True

            else:
                status.stale     = False
                status.timed_out = False

        return {
            'warnings':        warnings,
            'stale_topics':    stale_topics,
            'timeout_topics':  timeout_topics,
            'emergency':       emergency,
            'stop_approach':   stop_approach,
            'speed_reduce':    speed_reduce,
            'fallback_reason': fallback_reason,
        }

    def is_topic_ok(self, topic: str) -> bool:
        """Topic sağlıklı mı? (timeout yok, stale değil)"""
        if topic not in self._topics:
            return False
        status = self._topics[topic]
        if status.timeout_ms is None:
            return True   # latching
        if status.last_recv_ns is None:
            return False
        elapsed_ms = (time.monotonic_ns() - status.last_recv_ns) / 1e6
        return elapsed_ms <= STALE_MS

    def is_topic_stale(self, topic: str) -> bool:
        """Topic stale mi?"""
        if topic not in self._topics:
            return True
        return self._topics[topic].stale

    def is_topic_timed_out(self, topic: str) -> bool:
        """Topic timeout'a düştü mü?"""
        if topic not in self._topics:
            return True
        return self._topics[topic].timed_out

    def elapsed_ms(self, topic: str) -> float:
        """Son mesajdan bu yana geçen süre (ms)."""
        if topic not in self._topics:
            return float('inf')
        status = self._topics[topic]
        if status.last_recv_ns is None:
            return float('inf')
        return (time.monotonic_ns() - status.last_recv_ns) / 1e6

    def get_warning_flags(self) -> list:
        """Tüm aktif uyarı flag'lerini döndür."""
        result = self.check_all()
        return result['warnings']

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE
    # ───────────────────────────────────────────────────────────────────────

    def _handle_timeout(self, topic: str) -> str:
        """
        Timeout olan topic için fallback kararı.
        Sözleşme: Planner ↔ Controller Contract v1.3 §13

        Returns:
            'EMERGENCY'     — tam fren
            'STOP_APPROACH' — jerk sınırlı dur
            'SPEED_REDUCE'  — hız düşür
            'OK'            — devam
        """
        if topic == '/controller/feedback':
            # Contract §13: feedback kesilirse → status=EMERGENCY
            return 'EMERGENCY'

        if topic == '/localization/pose':
            # 500ms son pose koru → STOP_APPROACH
            return 'STOP_APPROACH'

        if topic == '/localization/status':
            # status=LOST gibi davran → STOP_APPROACH
            return 'STOP_APPROACH'

        if topic == '/localization/odometry':
            # odometry kesilirse son hız koru → SPEED_REDUCE
            return 'SPEED_REDUCE'

        if topic == '/perception/lane_model':
            # 2s son model koru → STOP_APPROACH
            return 'STOP_APPROACH'

        if topic == '/perception/obstacle_tracks':
            # Engel varmış gibi davran → STOP_APPROACH
            return 'STOP_APPROACH'

        if topic == '/perception/traffic_light_state':
            # stop-zone bağlamına göre RED veya kontrollü
            return 'STOP_APPROACH'

        if topic == '/fsm/current_mode':
            # Son modu 1s koru → STOP_APPROACH
            return 'STOP_APPROACH'

        return 'SPEED_REDUCE'