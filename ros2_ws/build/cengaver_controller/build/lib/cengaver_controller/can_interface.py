"""
CAN-Bus Haberleşme + Hız Yönetimi
===================================
Vehicle Interface ↔ Controller CAN Sözleşmesi v1.0

VEHICLECTRL Frame (0x560):
  Byte 0 → Kontak     (0x00=Kapalı,  0x01=Açık)
  Byte 1 → Direksiyon (0x00=TamSol,  0x81=Düz,  0xFF=TamSağ)
  Byte 2 → Hareket    (0x00=TamGeri, 0x81=Dur,   0xFF=TamİLeri)
  Byte 3 → El Freni   (0x00=İnik,    0xFF=Çekili)
  Byte 4 → Sinyal     (0=Kapalı,     1=Sol,       2=Sağ)
  Byte 5-7 → Rezerve  (0x00)
"""

import time
import math
from dataclasses import dataclass

try:
    import can
    CAN_AVAILABLE = True
except ImportError:
    CAN_AVAILABLE = False
    print("[UYARI] python-can bulunamadı. Simülasyon modunda çalışıyor.")

CAN_FRAME_ID  = 0x560
CAN_CHANNEL   = 'can0'
CAN_BITRATE   = 500_000
MAX_SPEED_MPS = 6.67

STEER_CENTER  = 0x81       # DÜZ — CAN dokümanı teyit etti (0x80 DEĞİL!)
STEER_MIN     = 0x00
STEER_MAX     = 0xFF

SPEED_STOP    = 0x81       # Hareketsiz
SPEED_PARK    = 0x91       # DÜZELTİLDİ: 0x8C → 0x91 (~0.83 m/s = 3 km/h)
                            # Hesap: 129 + (0.833/6.67)*126 ≈ 0x91
SPEED_CREEP   = 0x9B       # DÜZELTİLDİ: 0x99 → 0x9B (~1.39 m/s = 5 km/h)
                            # Hesap: 129 + (1.389/6.67)*126 ≈ 0x9B

RAMP_STEP     = 8


@dataclass
class SteeringCalibration:
    max_steer_angle_rad: float = 0.567
    toe_in_offset: int = 0


def steer_to_byte(delta_rad: float, cal: SteeringCalibration = None) -> int:
    if cal is None:
        cal = SteeringCalibration()
    norm = delta_rad / cal.max_steer_angle_rad
    norm = max(-1.0, min(1.0, norm))
    raw  = int(STEER_CENTER + norm * (STEER_MAX - STEER_CENTER))
    return max(STEER_MIN, min(STEER_MAX, raw + cal.toe_in_offset))


def speed_to_byte(speed_mps: float) -> int:
    speed_mps = max(-MAX_SPEED_MPS, min(MAX_SPEED_MPS, speed_mps))
    if abs(speed_mps) < 0.01:
        return SPEED_STOP
    norm = speed_mps / MAX_SPEED_MPS
    raw  = int(SPEED_STOP + norm * (STEER_MAX - SPEED_STOP))
    return max(0x00, min(0xFF, raw))


class SpeedRampManager:
    def __init__(self):
        self._current: int = SPEED_STOP

    def step(self, target_byte: int, emergency: bool = False) -> int:
        target_byte = max(0x00, min(0xFF, target_byte))
        if emergency:
            self._current = SPEED_STOP
            return self._current
        diff = target_byte - self._current
        if abs(diff) <= RAMP_STEP:
            self._current = target_byte
        elif diff > 0:
            self._current += RAMP_STEP
        else:
            self._current -= RAMP_STEP
        self._current = max(0x00, min(0xFF, self._current))
        return self._current

    def emergency_stop(self):
        self._current = SPEED_STOP

    @property
    def current(self) -> int:
        return self._current


class VehicleCtrlFrame:
    def build(self, steer_rad, speed_byte, kontak=True, el_freni=False, sinyal=0, cal=None):
        return bytes([
            0x01 if kontak else 0x00,
            steer_to_byte(steer_rad, cal),
            max(0x00, min(0xFF, speed_byte)),
            0xFF if el_freni else 0x00,
            sinyal & 0x03,
            0x00, 0x00, 0x00
        ])

    def build_stop(self, kontak=True):
        return bytes([0x01 if kontak else 0x00, STEER_CENTER, SPEED_STOP,
                      0x00, 0x00, 0x00, 0x00, 0x00])

    def build_park(self, kontak=True):
        return bytes([0x01 if kontak else 0x00, STEER_CENTER, SPEED_STOP,
                      0xFF, 0x00, 0x00, 0x00, 0x00])


class BEE1CANInterface:

    def __init__(self, cal: SteeringCalibration = None):
        self.cal        = cal or SteeringCalibration()
        self.frame      = VehicleCtrlFrame()
        self.speed_ramp = SpeedRampManager()
        self._bus       = None
        self._connected = False
        self._kontak    = False

    def connect(self) -> bool:
        if not CAN_AVAILABLE:
            print("[SİMÜLASYON] CAN bağlantısı simüle ediliyor.")
            self._connected = True
            return True
        try:
            self._bus = can.interface.Bus(
                channel=CAN_CHANNEL, bustype='socketcan', bitrate=CAN_BITRATE)
            self._connected = True
            print(f"[CAN] {CAN_CHANNEL} bağlantısı kuruldu.")
            return True
        except Exception as e:
            print(f"[HATA] CAN bağlantısı kurulamadı: {e}")
            return False

    def disconnect(self):
        self.emergency_stop()
        if self._bus:
            self._bus.shutdown()
        self._connected = False
        print("[CAN] Bağlantı kapatıldı.")

    def kontak_ac(self) -> bool:
        self._kontak = True
        print("[CAN] Kontak AÇIK")
        return self._send_raw(self.frame.build_stop(kontak=True))

    def kontak_kapat(self) -> bool:
        self.emergency_stop()
        self._kontak = False
        print("[CAN] Kontak KAPALI")
        return self._send_raw(
            bytes([0x00, STEER_CENTER, SPEED_STOP, 0x00, 0x00, 0x00, 0x00, 0x00]))

    def send_command(self, steer_rad, speed_mps, el_freni=False, sinyal=0, emergency=False):
        if not self._connected:
            print("[HATA] CAN bağlı değil.")
            return False
        speed_mps   = max(-MAX_SPEED_MPS, min(MAX_SPEED_MPS, speed_mps))
        target_byte = speed_to_byte(speed_mps)
        ramped_byte = self.speed_ramp.step(target_byte, emergency=emergency)
        data = self.frame.build(
            steer_rad=steer_rad, speed_byte=ramped_byte,
            kontak=self._kontak, el_freni=el_freni, sinyal=sinyal, cal=self.cal)
        return self._send_raw(data)

    def emergency_stop(self) -> bool:
        self.speed_ramp.emergency_stop()
        result = self._send_raw(self.frame.build_stop(kontak=self._kontak))
        print("[ACİL] Yazılımsal emergency stop — Byte2=0x81")
        return result

    def park_complete(self) -> bool:
        self.speed_ramp.emergency_stop()
        result = self._send_raw(self.frame.build_park(kontak=self._kontak))
        print("[PARK] El freni çekili — Byte3=0xFF")
        return result

    def _send_raw(self, data: bytes) -> bool:
        if not CAN_AVAILABLE or self._bus is None:
            print(f"[SİM] CAN TX → 0x{CAN_FRAME_ID:03X} [{' '.join(f'{b:02X}' for b in data)}]")
            return True
        try:
            self._bus.send(can.Message(
                arbitration_id=CAN_FRAME_ID, data=data, is_extended_id=False))
            return True
        except can.CanError as e:
            print(f"[HATA] CAN gönderimi başarısız: {e}")
            return False

    @property
    def debug_info(self) -> dict:
        return {'connected': self._connected, 'kontak': self._kontak,
                'speed_byte': hex(self.speed_ramp.current)}


if __name__ == "__main__":
    print("VEHICLECTRL CAN Arayüzü Testi")
    print(f"SPEED_STOP=0x{SPEED_STOP:02X}  SPEED_PARK=0x{SPEED_PARK:02X}  SPEED_CREEP=0x{SPEED_CREEP:02X}")

    for deg in [-32, -15, 0, 15, 32]:
        b = steer_to_byte(math.radians(deg))
        print(f"  {deg:>4}° → 0x{b:02X} ({b})")

    iface = BEE1CANInterface()
    iface.connect()
    iface.kontak_ac()
    for _ in range(3):
        iface.send_command(steer_rad=0.0, speed_mps=2.0)
        time.sleep(0.05)
    iface.emergency_stop()
    iface.park_complete()
    iface.disconnect()
