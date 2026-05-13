#!/usr/bin/env python3
import time


class _TopicWatchdog:
    def __init__(self, timeout_ms=600.0):
        self._timeout_ms = timeout_ms
        self._last_ns = None

    def besle(self, clock=None):
        self._last_ns = time.monotonic_ns()

    def is_stale(self):
        if self._last_ns is None:
            return True
        elapsed = (time.monotonic_ns() - self._last_ns) / 1e6
        return elapsed > self._timeout_ms


class FSMWatchdog:
    def __init__(self, timeout_ms=600.0, clock=None, mod_degistir_fn=None):
        self._timeout_ms = timeout_ms
        self._clock = clock
        self._mod_degistir_fn = mod_degistir_fn
        self.lokalizasyon  = _TopicWatchdog(timeout_ms)
        self.serit         = _TopicWatchdog(timeout_ms)
        self.engeller      = _TopicWatchdog(timeout_ms)
        self.trafik_isigi  = _TopicWatchdog(timeout_ms)
        self.planner       = _TopicWatchdog(timeout_ms)
        self._last_stamps  = {}

    def update(self, topic):
        self._last_stamps[topic] = time.monotonic_ns()

    def kontrol(self, current_mode=None):
        return self.get_stale_topics()

    def check(self):
        return self.get_stale_topics()

    def is_stale(self, topic):
        if topic not in self._last_stamps:
            return True
        elapsed = (time.monotonic_ns() - self._last_stamps[topic]) / 1e6
        return elapsed > self._timeout_ms

    def get_stale_topics(self):
        return [t for t in self._last_stamps if self.is_stale(t)]

    def elapsed_ms(self, topic):
        if topic not in self._last_stamps:
            return float('inf')
        return (time.monotonic_ns() - self._last_stamps[topic]) / 1e6
