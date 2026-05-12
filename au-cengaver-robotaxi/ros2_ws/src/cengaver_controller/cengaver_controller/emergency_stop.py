"""
Emergency Stop Modülü
=====================
Yol Haritası v1.1 — Controller Paketi

İKİ FARKLI ACİL DURUM:

1. EMERGENCY_STOP (Yazılımsal)
   → Planner tetikler (reason=8 veya /planning/status status=5)
   → Controller Byte2=0x81 gönderir (motor durur)
   → Güç kesilmez, sistem yeniden başlatılabilir
   → Bu dosya yönetir

2. AUTONOMOUS_EMERGENCY (Donanımsal)
   → Safety supervisor tetikler
   → Donanım kanalından aracın gücü kesilir
   → Controller sadece izler ve loglar
   → Bu dosya izler ama tetiklemez

SUBSCRİBE:
  /emergency                olay  std_msgs/Bool  → donanımsal
  /safety_supervisor/status 10Hz  std_msgs/String → safety durumu

PUBLISH:
  /controller/emergency_status  10Hz  std_msgs/String → debug
"""

import time
import json
from enum import IntEnum
from dataclasses import dataclass, field
from typing import Callable, Optional


# ─── Acil Durum Tipleri ───────────────────────────────────────────────────────

class EmergencyType(IntEnum):
    NONE                 = 0   # Normal — acil durum yok
    SOFTWARE_ESTOP       = 1   # Yazılımsal — planner reason=8
    TRAJECTORY_TIMEOUT   = 2   # Trajectory 1000ms gelmedi
    TARGET_SPEED_TIMEOUT = 3   # TargetSpeed 1000ms gelmedi
    PLANNING_EMERGENCY   = 4   # /planning/status status=5
    HARDWARE_ESTOP       = 5   # Donanımsal — safety supervisor
    WATCHDOG_TIMEOUT     = 6   # Feedback gönderilmedi, watchdog


class EmergencySource(IntEnum):
    PLANNER          = 0   # /planning/target_speed reason=8
    PLANNING_STATUS  = 1   # /planning/status status=5
    TRAJECTORY       = 2   # Trajectory timeout
    TARGET_SPEED     = 3   # TargetSpeed timeout
    HARDWARE         = 4   # /emergency topic (donanımsal)
    WATCHDOG         = 5   # Watchdog mekanizması


# ─── Acil Durum Kaydı ─────────────────────────────────────────────────────────

@dataclass
class EmergencyEvent:
    """Tek bir acil durum olayı."""
    emergency_type:   EmergencyType
    source:           EmergencySource
    timestamp:        float
    message:          str
    resolved:         bool = False
    resolved_at:      float = 0.0

    def resolve(self):
        self.resolved    = True
        self.resolved_at = time.monotonic()

    def to_dict(self) -> dict:
        return {
            'type':        self.emergency_type.name,
            'source':      self.source.name,
            'timestamp':   round(self.timestamp, 3),
            'message':     self.message,
            'resolved':    self.resolved,
        }


# ─── Ana Emergency Stop Sınıfı ────────────────────────────────────────────────

class EmergencyStopManager:
    """
    Tüm acil durum mantığını yönetir.

    controller_node.py içinde oluşturulur ve kullanılır:

        self.emergency_mgr = EmergencyStopManager(
            on_software_estop = self.can_if.emergency_stop,
            on_hardware_estop = self._log_hardware_estop
        )

        # Planner EMERGENCY_STOP gönderdi:
        self.emergency_mgr.trigger_software(
            EmergencySource.PLANNER,
            "reason=8 geldi"
        )

        # Trajectory timeout:
        self.emergency_mgr.trigger_software(
            EmergencySource.TRAJECTORY,
            "1000ms gelmedi"
        )

        # Döngüde kontrol:
        if self.emergency_mgr.is_active:
            return  # döngüden çık
    """

    def __init__(self,
                 on_software_estop: Callable,
                 on_hardware_estop: Optional[Callable] = None):
        """
        Args:
            on_software_estop: Yazılımsal acil durumda çağrılacak fonksiyon.
                               Genellikle can_if.emergency_stop()
            on_hardware_estop: Donanımsal acil durumda çağrılacak fonksiyon.
                               Opsiyonel — sadece loglama için kullanılır.
        """
        self._on_software_estop = on_software_estop
        self._on_hardware_estop = on_hardware_estop

        self._active:          bool             = False
        self._current_type:    EmergencyType    = EmergencyType.NONE
        self._current_source:  EmergencySource  = EmergencySource.PLANNER
        self._events:          list             = []   # tüm olay geçmişi
        self._trigger_time:    float            = 0.0
        self._hardware_active: bool             = False  # donanımsal takip

    # ── Yazılımsal Acil Durum ─────────────────────────────────────────────────

    def trigger_software(self,
                         source: EmergencySource,
                         message: str,
                         etype: EmergencyType = None) -> None:
        """
        Yazılımsal acil durum tetikle.

        Args:
            source:  Nereden geldi?
            message: Log mesajı
            etype:   Hangi tip? (None ise source'dan otomatik belirlenir)
        """
        # Tip belirle
        if etype is None:
            _source_to_type = {
                EmergencySource.PLANNER:         EmergencyType.SOFTWARE_ESTOP,
                EmergencySource.PLANNING_STATUS: EmergencyType.PLANNING_EMERGENCY,
                EmergencySource.TRAJECTORY:      EmergencyType.TRAJECTORY_TIMEOUT,
                EmergencySource.TARGET_SPEED:    EmergencyType.TARGET_SPEED_TIMEOUT,
                EmergencySource.WATCHDOG:        EmergencyType.WATCHDOG_TIMEOUT,
            }
            etype = _source_to_type.get(source, EmergencyType.SOFTWARE_ESTOP)

        # Olay kaydet
        event = EmergencyEvent(
            emergency_type = etype,
            source         = source,
            timestamp      = time.monotonic(),
            message        = message,
        )
        self._events.append(event)

        # Zaten aktifse tekrar tetikleme
        if self._active:
            return

        # Aktifleştir
        self._active         = True
        self._current_type   = etype
        self._current_source = source
        self._trigger_time   = time.monotonic()

        # CAN'e dur komutu gönder
        print(f"[EMERGENCY] Yazılımsal ESTOP — {etype.name} | {source.name} | {message}")
        self._on_software_estop()

    def trigger_hardware_observed(self, message: str) -> None:
        """
        Donanımsal acil durum GÖZLEMLENDİ.
        Controller sadece loglar — tetiklemez!

        Yol Haritası v1.1:
        'AUTONOMOUS_EMERGENCY safety supervisor sorumluluğundadır.
         FSM bu sinyali yalnızca izleyebilir ve loglayabilir.'
        """
        self._hardware_active = True

        event = EmergencyEvent(
            emergency_type = EmergencyType.HARDWARE_ESTOP,
            source         = EmergencySource.HARDWARE,
            timestamp      = time.monotonic(),
            message        = f"DONANIMSAL ESTOP GÖZLEMLENDİ: {message}",
        )
        self._events.append(event)

        print(f"[EMERGENCY] Donanımsal ESTOP gözlemlendi — {message}")
        print("[EMERGENCY] Safety supervisor aracın gücünü kesmektedir.")
        print("[EMERGENCY] Controller bu sinyali tetiklemez, sadece loglar.")

        if self._on_hardware_estop:
            self._on_hardware_estop()

    # ── Reset ─────────────────────────────────────────────────────────────────

    def reset(self, reason: str = "Manuel reset") -> bool:
        """
        Yazılımsal acil durumu sıfırla.
        Donanımsal acil durumda çalışmaz — güvenlik kuralı.

        Returns:
            True  → reset başarılı
            False → donanımsal acil aktif, reset edilemez
        """
        if self._hardware_active:
            print("[EMERGENCY] Donanımsal ESTOP aktif — manuel reset gerekli!")
            return False

        if not self._active:
            return True  # Zaten aktif değil

        # Olayı çözüldü olarak işaretle
        for event in reversed(self._events):
            if not event.resolved:
                event.resolve()
                break

        self._active       = False
        self._current_type = EmergencyType.NONE
        print(f"[EMERGENCY] Reset — {reason}")
        return True

    def reset_hardware(self) -> None:
        """
        Donanımsal acil durumu sıfırla.
        Sadece fiziksel müdahale sonrası çağrılır.
        """
        self._hardware_active = False
        print("[EMERGENCY] Donanımsal ESTOP sıfırlandı.")

    # ── Durum Sorguları ───────────────────────────────────────────────────────

    @property
    def is_active(self) -> bool:
        """Herhangi bir acil durum aktif mi?"""
        return self._active or self._hardware_active

    @property
    def is_software_active(self) -> bool:
        """Yazılımsal acil durum aktif mi?"""
        return self._active

    @property
    def is_hardware_active(self) -> bool:
        """Donanımsal acil durum aktif mi?"""
        return self._hardware_active

    @property
    def current_type(self) -> EmergencyType:
        return self._current_type

    @property
    def duration_ms(self) -> float:
        """Acil durumun ne kadar sürdüğü (ms)."""
        if not self._active:
            return 0.0
        return (time.monotonic() - self._trigger_time) * 1000

    @property
    def event_count(self) -> int:
        """Toplam olay sayısı."""
        return len(self._events)

    def get_status(self) -> dict:
        """Debug için mevcut durum."""
        return {
            'active':          self._active,
            'hardware_active': self._hardware_active,
            'type':            self._current_type.name,
            'source':          self._current_source.name,
            'duration_ms':     round(self.duration_ms, 1),
            'event_count':     self.event_count,
            'last_event':      self._events[-1].to_dict() if self._events else None,
        }

    def get_event_log(self) -> list:
        """Tüm olay geçmişi."""
        return [e.to_dict() for e in self._events]


# ─── Test ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":

    print("EmergencyStopManager Testi")
    print("=" * 55)

    # Simüle: CAN emergency_stop çağrıldığında sadece yazdır
    def fake_can_stop():
        print("  [CAN] Byte2=0x81 gönderildi — araç durdu")

    def fake_hw_log():
        print("  [HW] Donanımsal ESTOP loglandı")

    mgr = EmergencyStopManager(
        on_software_estop = fake_can_stop,
        on_hardware_estop = fake_hw_log
    )

    # Test 1: Planner EMERGENCY_STOP
    print("\n[Test 1] Planner yazılımsal ESTOP")
    mgr.trigger_software(EmergencySource.PLANNER, "reason=8 geldi")
    print(f"  is_active: {mgr.is_active}")
    print(f"  type: {mgr.current_type.name}")
    print(f"  duration: {mgr.duration_ms:.1f}ms")

    # Test 2: Aktifken tekrar tetikleme (görmezden gelmeli)
    print("\n[Test 2] Aktifken tekrar tetikleme (görmezden gelmeli)")
    mgr.trigger_software(EmergencySource.TRAJECTORY, "1000ms gelmedi")
    print(f"  event_count: {mgr.event_count} (2 olmalı)")

    # Test 3: Reset
    print("\n[Test 3] Reset")
    result = mgr.reset("Test bitti")
    print(f"  reset başarılı: {result}")
    print(f"  is_active: {mgr.is_active}")

    # Test 4: Trajectory timeout
    print("\n[Test 4] Trajectory timeout ESTOP")
    mgr.trigger_software(
        EmergencySource.TRAJECTORY,
        "1050ms gelmedi",
        EmergencyType.TRAJECTORY_TIMEOUT
    )
    print(f"  type: {mgr.current_type.name}")
    mgr.reset("Trajectory geldi")

    # Test 5: Donanımsal ESTOP
    print("\n[Test 5] Donanımsal ESTOP gözlemi")
    mgr.trigger_hardware_observed("/emergency=True sinyali alındı")
    print(f"  hardware_active: {mgr.is_hardware_active}")

    # Donanımsal aktifken reset dene
    print("\n[Test 6] Donanımsal aktifken yazılım reset denemesi")
    result = mgr.reset("Deneme")
    print(f"  reset başarılı: {result} (False olmalı)")

    mgr.reset_hardware()
    print(f"  hardware reset sonrası: {mgr.is_hardware_active}")

    # Durum özeti
    print("\n[Durum Özeti]")
    status = mgr.get_status()
    for k, v in status.items():
        if k != 'last_event':
            print(f"  {k}: {v}")

    print(f"\nToplam olay: {mgr.event_count}")
    print("\nTüm testler tamamlandı!")
