"""
CAN-Bus Haberleşme + Hız Yönetimi
===================================
Vehicle Interface ↔ Controller CAN Sözleşmesi v1.0'a göre güncellenmiştir.

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


# ─── Sabitler ─────────────────────────────────────────────────────────────────

CAN_FRAME_ID  = 0x560      # VEHICLECTRL frame ID
CAN_CHANNEL   = 'can0'     # Linux CAN interface
CAN_BITRATE   = 500_000    # 500 kbps

MAX_SPEED_MPS = 6.67       # Tragger T-Car max: 24 km/h

# Direksiyon — CAN dokümanından ("81 Düz" olarak belgelenmiş)
STEER_CENTER  = 0x81       # DÜZ — 0x80 DEĞİL!
STEER_MIN     = 0x00       # Tam Sol
STEER_MAX     = 0xFF       # Tam Sağ

# Hız — CAN dokümanından
SPEED_STOP    = 0x81       # Hareketsiz
SPEED_PARK    = 0x8C       # ~0.83 m/s = 3 km/h
SPEED_CREEP   = 0x99       # ~1.39 m/s = 5 km/h

RAMP_STEP     = 8          # Max byte adımı / 50ms


# ─── Kalibrasyon ──────────────────────────────────────────────────────────────

@dataclass
class SteeringCalibration:
    """
    Direksiyon kalibrasyonu.
    Ağustos 2025'te araç gelince arazide ölçülecek.
    """
    max_steer_angle_rad: float = 0.567  # 32.5° — sözleşmeden, ölçülecek
    toe_in_offset: int = 0              # arazide belirlenecek


# ─── Dönüşüm Fonksiyonları ────────────────────────────────────────────────────

def steer_to_byte(delta_rad: float, cal: SteeringCalibration = None) -> int:
    """
    Ackermann açısı (radyan) → CAN Byte 1.
    Sol pozitif → 0x81'den büyük byte.
    Sağ negatif → 0x81'den küçük byte.
    """
    if cal is None:
        cal = SteeringCalibration()
    norm = delta_rad / cal.max_steer_angle_rad
    norm = max(-1.0, min(1.0, norm))
    raw  = int(STEER_CENTER + norm * (STEER_MAX - STEER_CENTER))
    return max(STEER_MIN, min(STEER_MAX, raw + cal.toe_in_offset))


def speed_to_byte(speed_mps: float) -> int:
    """
    Hız (m/s) → CAN Byte 2.
    Pozitif = ileri (0x82-0xFF)
    Sıfır   = dur   (0x81)
    Negatif = geri  (0x00-0x80)
    """
    speed_mps = max(-MAX_SPEED_MPS, min(MAX_SPEED_MPS, speed_mps))
    if abs(speed_mps) < 0.01:
        return SPEED_STOP
    norm = speed_mps / MAX_SPEED_MPS
    raw  = int(SPEED_STOP + norm * (STEER_MAX - SPEED_STOP))
    return max(0x00, min(0xFF, raw))


# ─── SpeedRamp ────────────────────────────────────────────────────────────────

class SpeedRampManager:
    """
    Jerk sınırlı hız geçişi.
    Her 50ms'de max RAMP_STEP byte değişir.
    Emergency=True ise anında SPEED_STOP (0x81).
    """

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


# ─── Frame Builder ────────────────────────────────────────────────────────────

class VehicleCtrlFrame:
    """
    VEHICLECTRL (0x560) 8-byte frame oluşturucu.

    Byte Düzeni (CAN protokol dokümanından — doğrulandı):
    B0=Kontak | B1=Direksiyon | B2=Hareket | B3=ElFreni | B4=Sinyal | B5-7=0x00
    """

    def build(self,
              steer_rad: float,
              speed_byte: int,
              kontak: bool = True,
              el_freni: bool = False,
              sinyal: int = 0,
              cal: SteeringCalibration = None) -> bytes:
        """
        8-byte VEHICLECTRL frame oluştur.

        Args:
            steer_rad:  Direksiyon açısı (radyan)
            speed_byte: Hız byte (0x00-0xFF) — SpeedRamp çıktısı
            kontak:     Araç kontağı açık mı?
            el_freni:   El freni çekili mi?
            sinyal:     0=Kapalı, 1=Sol, 2=Sağ
            cal:        Direksiyon kalibrasyonu
        """
        b0 = 0x01 if kontak   else 0x00
        b1 = steer_to_byte(steer_rad, cal)
        b2 = max(0x00, min(0xFF, speed_byte))
        b3 = 0xFF if el_freni else 0x00
        b4 = sinyal & 0x03
        return bytes([b0, b1, b2, b3, b4, 0x00, 0x00, 0x00])

    def build_stop(self, kontak: bool = True) -> bytes:
        """Yazılımsal durdurma frame'i."""
        return bytes([
            0x01 if kontak else 0x00,
            STEER_CENTER, SPEED_STOP,
            0x00, 0x00, 0x00, 0x00, 0x00
        ])

    def build_park(self, kontak: bool = True) -> bytes:
        """Park tamamlandı: hareketsiz + el freni çekili."""
        return bytes([
            0x01 if kontak else 0x00,
            STEER_CENTER, SPEED_STOP,
            0xFF, 0x00, 0x00, 0x00, 0x00
        ])


# ─── Ana CAN Arayüzü ──────────────────────────────────────────────────────────

class BEE1CANInterface:
    """
    BEE1 VEHICLECTRL CAN arayüzü.
    VehicleCtrlFrame + SpeedRamp birleşimi.

    Kullanım:
        can_if = BEE1CANInterface()
        can_if.connect()
        can_if.kontak_ac()
        can_if.send_command(steer_rad=0.1, speed_mps=1.5)
        can_if.disconnect()
    """

    def __init__(self, cal: SteeringCalibration = None):
        self.cal        = cal or SteeringCalibration()
        self.frame      = VehicleCtrlFrame()
        self.speed_ramp = SpeedRampManager()
        self._bus       = None
        self._connected = False
        self._kontak    = False

    # ── Bağlantı ──────────────────────────────────────────────────────────────

    def connect(self) -> bool:
        if not CAN_AVAILABLE:
            print("[SİMÜLASYON] CAN bağlantısı simüle ediliyor.")
            self._connected = True
            return True
        try:
            self._bus = can.interface.Bus(
                channel=CAN_CHANNEL,
                bustype='socketcan',
                bitrate=CAN_BITRATE
            )
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

    # ── Komutlar ──────────────────────────────────────────────────────────────

    def kontak_ac(self) -> bool:
        """Kontağı aç. Hareket komutlarından önce çağrılmalı."""
        self._kontak = True
        data = self.frame.build_stop(kontak=True)
        print("[CAN] Kontak AÇIK")
        return self._send_raw(data)

    def kontak_kapat(self) -> bool:
        """Kontağı kapat."""
        self.emergency_stop()
        self._kontak = False
        data = bytes([0x00, STEER_CENTER, SPEED_STOP, 0x00, 0x00, 0x00, 0x00, 0x00])
        print("[CAN] Kontak KAPALI")
        return self._send_raw(data)

    def send_command(self,
                     steer_rad:  float,
                     speed_mps:  float,
                     el_freni:   bool = False,
                     sinyal:     int  = 0,
                     emergency:  bool = False) -> bool:
        """
        Ana kontrol komutu — 20Hz döngüde çağrılır.

        Args:
            steer_rad:  Direksiyon açısı (radyan). Sol pozitif.
            speed_mps:  Hedef hız (m/s). Pozitif=ileri, Negatif=geri.
            el_freni:   El freni çekili mi?
            sinyal:     0=Kapalı, 1=Sol, 2=Sağ
            emergency:  True ise ramp bypass, anında 0x81

        Returns:
            True = gönderim başarılı
        """
        if not self._connected:
            print("[HATA] CAN bağlı değil.")
            return False

        speed_mps   = max(-MAX_SPEED_MPS, min(MAX_SPEED_MPS, speed_mps))
        target_byte = speed_to_byte(speed_mps)
        ramped_byte = self.speed_ramp.step(target_byte, emergency=emergency)

        data = self.frame.build(
            steer_rad  = steer_rad,
            speed_byte = ramped_byte,
            kontak     = self._kontak,
            el_freni   = el_freni,
            sinyal     = sinyal,
            cal        = self.cal
        )
        return self._send_raw(data)

    def emergency_stop(self) -> bool:
        """
        Yazılımsal acil durdurma.
        Ramp bypass — anında Byte2=0x81.
        Güç kesilmez (AUTONOMOUS_EMERGENCY farklıdır).
        """
        self.speed_ramp.emergency_stop()
        data = self.frame.build_stop(kontak=self._kontak)
        result = self._send_raw(data)
        print("[ACİL] Yazılımsal emergency stop — Byte2=0x81")
        return result

    def park_complete(self) -> bool:
        """Park tamamlandı: hareketsiz + el freni çekili (Byte3=0xFF)."""
        self.speed_ramp.emergency_stop()
        data = self.frame.build_park(kontak=self._kontak)
        result = self._send_raw(data)
        print("[PARK] El freni çekili — Byte3=0xFF")
        return result

    # ── İç Gönderici ─────────────────────────────────────────────────────────

    def _send_raw(self, data: bytes) -> bool:
        if not CAN_AVAILABLE or self._bus is None:
            hex_str = ' '.join(f'{b:02X}' for b in data)
            print(f"[SİM] CAN TX → 0x{CAN_FRAME_ID:03X} [{hex_str}]")
            return True
        try:
            msg = can.Message(
                arbitration_id=CAN_FRAME_ID,
                data=data,
                is_extended_id=False
            )
            self._bus.send(msg)
            return True
        except can.CanError as e:
            print(f"[HATA] CAN gönderimi başarısız: {e}")
            return False

    @property
    def debug_info(self) -> dict:
        return {
            'connected':  self._connected,
            'kontak':     self._kontak,
            'speed_byte': hex(self.speed_ramp.current),
        }


# ─── Test ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("VEHICLECTRL CAN Arayüzü Testi v1.0")
    print("=" * 55)

    print("\n[Direksiyon Byte Tablosu]")
    print(f"{'Açı (°)':>10} {'Byte (hex)':>12} {'Decimal':>10}")
    print("-" * 35)
    for deg in [-32, -15, 0, 15, 32]:
        b = steer_to_byte(math.radians(deg))
        print(f"{deg:>10}°  {hex(b):>10}  {b:>10}")

    print("\n[Hız Byte Tablosu]")
    print(f"{'Hız (m/s)':>12} {'Byte (hex)':>12} {'Decimal':>10}")
    print("-" * 37)
    for mps in [-6.67, -1.0, 0.0, 0.83, 1.39, 3.0, 6.67]:
        b = speed_to_byte(mps)
        print(f"{mps:>12.2f}  {hex(b):>10}  {b:>10}")

    print("\n[Senaryo Testleri]")
    iface = BEE1CANInterface()
    iface.connect()
    iface.kontak_ac()

    print("\n→ Düz ileri 2 m/s (SpeedRamp)")
    for _ in range(5):
        iface.send_command(steer_rad=0.0, speed_mps=2.0)
        time.sleep(0.05)

    print("\n→ 10° sola, 0.5 m/s")
    for _ in range(3):
        iface.send_command(steer_rad=math.radians(10), speed_mps=0.5)
        time.sleep(0.05)

    print("\n→ Acil durdurma")
    iface.emergency_stop()

    print("\n→ Park el freni")
    iface.park_complete()

    iface.disconnect()
