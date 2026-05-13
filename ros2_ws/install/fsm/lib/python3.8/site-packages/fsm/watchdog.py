#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
watchdog.py
FSM Watchdog — topic timeout izleme
"""

import time


class FSMWatchdog:
    """
    FSM topic timeout izleyici.
    """

    def __init__(self, timeout_ms: float = 600.0, clock=None, mod_degistir_fn=None):
        self._timeout_ms = timeout_ms
        self._clock = clock
        self._mod_degistir_fn = mod_degistir_fn
        self._last_stamps: dict = {}

    def update(self, topic: str):
        """Topic mesajı gelince timestamp güncelle."""
        self._last_stamps[topic] = time.monotonic_ns()

    def is_stale(self, topic: str) -> bool:
        """Topic timeout'a düştü mü?"""
        if topic not in self._last_stamps:
            return True
        elapsed_ms = (time.monotonic_ns() - self._last_stamps[topic]) / 1e6
        return elapsed_ms > self._timeout_ms

    def check(self):
        """Tüm topic'leri kontrol et, stale varsa callback çağır."""
        stale = self.get_stale_topics()
        if stale and self._mod_degistir_fn:
            pass  # FSM mod geçişi burada yapılabilir
        return stale

    def get_stale_topics(self) -> list:
        """Tüm stale topic'leri döndür."""
        return [t for t in self._last_stamps if self.is_stale(t)]

    def elapsed_ms(self, topic: str) -> float:
        """Son mesajdan bu yana geçen süre (ms)."""
        if topic not in self._last_stamps:
            return float('inf')
        return (time.monotonic_ns() - self._last_stamps[topic]) / 1e6

    def kontrol(self, current_mode=None):
        """FSM döngüsünde çağrılır — stale topic kontrolü."""
        return self.check()
