#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
emergency_stop.py
Yazılımsal EMERGENCY_STOP yönetimi
"""

from enum import Enum


class EmergencySource(Enum):
    PLANNER = "planner"
    WATCHDOG = "watchdog"
    MANUAL = "manual"
    TRAJECTORY_TIMEOUT = "trajectory_timeout"


class EmergencyType(Enum):
    SOFT_BRAKE = "soft_brake"
    FULL_BRAKE = "full_brake"
    AUTONOMOUS_EMERGENCY = "autonomous_emergency"


class EmergencyStopManager:
    """
    Yazılımsal tam fren yönetimi.
    AUTONOMOUS_EMERGENCY → safety supervisor sorumluluğundadır.
    """

    def __init__(self, on_software_estop=None, on_hardware_estop=None):
        self._on_software_estop = on_software_estop
        self._on_hardware_estop = on_hardware_estop
        self._active = False
        self._source = None
        self._type = None

    def trigger(self, source: EmergencySource, etype: EmergencyType = EmergencyType.FULL_BRAKE):
        self._active = True
        self._source = source
        self._type = etype

    def clear(self):
        self._active = False
        self._source = None
        self._type = None

    @property
    def is_active(self) -> bool:
        return self._active

    @property
    def source(self):
        return self._source

    @property
    def type(self):
        return self._type
