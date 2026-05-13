#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
timeout_checker.py

Algoritma 17: FSM-Planner Timeout ve Mesaj Denetleyici
"""

import time
from dataclasses import dataclass, field
from typing import Dict, Optional, Set


# ─── Topic Timeout Sabitleri, ms ───────────────────────────────────────────
TIMEOUT_MS = {
    '/perception/lane_model': 500,
    '/perception/obstacle_tracks': 500,
    '/perception/traffic_light_state': 300,
    '/perception/traffic_signs': 1000,
    '/perception/stop_target': 500,

    '/localization/pose': 300,
    '/localization/odometry': 200,
    '/localization/status': 300,
    '/localization/map_origin': None,

    '/controller/feedback': 500,

    '/fsm/current_mode': 500,
    '/fsm/mission_state': 1000,
}

# STALE = timeout_ms aşımı
# STOP = timeout_ms * STOP_MULTIPLIER aşımı
STOP_MULTIPLIER = 2.0

# Node ilk açıldığında veri gelmeden önce uyarı basmamak için grace süresi
STARTUP_GRACE_MS = 1500.0


@dataclass
class TopicStatus:
    name: str
    timeout_ms: Optional[int]
    last_recv_ns: Optional[int] = None
    stale: bool = False
    timed_out: bool = False
    warning_flags: list = field(default_factory=list)


class TimeoutChecker:
    """
    Mesajların son geliş zamanını izler ve fallback kararı üretir.
    """

    def __init__(self, required_topics: Optional[Set[str]] = None):
        self._start_ns = time.monotonic_ns()
        self._topics: Dict[str, TopicStatus] = {}

        self._required_topics = required_topics

        for topic, timeout_ms in TIMEOUT_MS.items():
            self._topics[topic] = TopicStatus(
                name=topic,
                timeout_ms=timeout_ms,
            )

    def update(self, topic: str) -> None:
        """Mesaj alındığında timestamp günceller."""
        if topic not in self._topics:
            self._topics[topic] = TopicStatus(
                name=topic,
                timeout_ms=500,
            )

        status = self._topics[topic]
        status.last_recv_ns = time.monotonic_ns()
        status.stale = False
        status.timed_out = False
        status.warning_flags = []

    def check_all(self) -> dict:
        """
        Tüm topic'leri kontrol eder.
        """
        now_ns = time.monotonic_ns()
        startup_elapsed_ms = (now_ns - self._start_ns) / 1e6

        warnings = []
        stale_topics = []
        timeout_topics = []

        emergency = False
        stop_approach = False
        speed_reduce = False
        fallback_reason = ''

        for topic, status in self._topics.items():
            if self._required_topics is not None and topic not in self._required_topics:
                continue

            if status.timeout_ms is None:
                continue

            timeout_ms = float(status.timeout_ms)
            stop_ms = timeout_ms * STOP_MULTIPLIER

            if status.last_recv_ns is None:
                if startup_elapsed_ms < STARTUP_GRACE_MS:
                    continue

                status.stale = True
                status.timed_out = False
                stale_topics.append(topic)
                warnings.append(f'NO_DATA:{topic}')

                # Kritik topic hiç gelmediyse güvenli duruş
                result = self._handle_no_data(topic)
                if result == 'EMERGENCY':
                    emergency = True
                    fallback_reason = topic
                elif result == 'STOP_APPROACH':
                    stop_approach = True
                    if not fallback_reason:
                        fallback_reason = topic
                elif result == 'SPEED_REDUCE':
                    speed_reduce = True

                continue

            elapsed_ms = (now_ns - status.last_recv_ns) / 1e6

            if elapsed_ms > stop_ms:
                status.stale = True
                status.timed_out = True

                timeout_topics.append(topic)
                warnings.append(f'TIMEOUT:{topic}:{elapsed_ms:.0f}ms')

                result = self._handle_timeout(topic)

                if result == 'EMERGENCY':
                    emergency = True
                    fallback_reason = topic

                elif result == 'STOP_APPROACH':
                    stop_approach = True
                    if not fallback_reason:
                        fallback_reason = topic

                elif result == 'SPEED_REDUCE':
                    speed_reduce = True
                    if not fallback_reason:
                        fallback_reason = topic

            elif elapsed_ms > timeout_ms:
                status.stale = True
                status.timed_out = False

                stale_topics.append(topic)
                warnings.append(f'STALE:{topic}:{elapsed_ms:.0f}ms')
                speed_reduce = True

                if not fallback_reason:
                    fallback_reason = topic

            else:
                status.stale = False
                status.timed_out = False
                status.warning_flags = []

        return {
            'warnings': warnings,
            'stale_topics': stale_topics,
            'timeout_topics': timeout_topics,
            'emergency': emergency,
            'stop_approach': stop_approach,
            'speed_reduce': speed_reduce,
            'fallback_reason': fallback_reason,
        }

    def is_topic_ok(self, topic: str) -> bool:
        if topic not in self._topics:
            return False

        status = self._topics[topic]

        if status.timeout_ms is None:
            return True

        if status.last_recv_ns is None:
            return False

        elapsed_ms = (time.monotonic_ns() - status.last_recv_ns) / 1e6
        return elapsed_ms <= float(status.timeout_ms)

    def is_topic_stale(self, topic: str) -> bool:
        if topic not in self._topics:
            return True

        self.check_all()
        return self._topics[topic].stale

    def is_topic_timed_out(self, topic: str) -> bool:
        if topic not in self._topics:
            return True

        self.check_all()
        return self._topics[topic].timed_out

    def elapsed_ms(self, topic: str) -> float:
        if topic not in self._topics:
            return float('inf')

        status = self._topics[topic]

        if status.last_recv_ns is None:
            return float('inf')

        return (time.monotonic_ns() - status.last_recv_ns) / 1e6

    def get_warning_flags(self) -> list:
        return self.check_all()['warnings']

    def reset_topic(self, topic: str) -> None:
        if topic in self._topics:
            self._topics[topic].last_recv_ns = None
            self._topics[topic].stale = False
            self._topics[topic].timed_out = False
            self._topics[topic].warning_flags = []

    def _handle_no_data(self, topic: str) -> str:
        """
        Hiç veri gelmeyen topic için başlangıç sonrası davranış.
        """
        if topic in (
            '/localization/pose',
            '/localization/status',
            '/controller/feedback',
            '/fsm/current_mode',
        ):
            return 'STOP_APPROACH'

        if topic == '/perception/obstacle_tracks':
            return 'STOP_APPROACH'

        return 'SPEED_REDUCE'

    def _handle_timeout(self, topic: str) -> str:
        """
        Timeout olan topic için fallback kararı.
        """
        if topic == '/controller/feedback':
            return 'EMERGENCY'

        if topic in (
            '/localization/pose',
            '/localization/status',
            '/fsm/current_mode',
        ):
            return 'STOP_APPROACH'

        if topic == '/localization/odometry':
            return 'SPEED_REDUCE'

        if topic == '/perception/lane_model':
            return 'STOP_APPROACH'

        if topic == '/perception/obstacle_tracks':
            return 'STOP_APPROACH'

        if topic == '/perception/traffic_light_state':
            return 'STOP_APPROACH'

        if topic == '/perception/stop_target':
            return 'SPEED_REDUCE'

        if topic == '/perception/traffic_signs':
            return 'SPEED_REDUCE'

        if topic == '/fsm/mission_state':
            return 'STOP_APPROACH'

        return 'SPEED_REDUCE'
