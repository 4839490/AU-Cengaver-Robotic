"""
Hibrit PID Denetleyici
======================
Cross-track error ve heading error'ü ayrı ayrı işleyip
ağırlıklı toplamla tek bir direksiyon komutu üretir.
"""

import time
import math
from dataclasses import dataclass, field


@dataclass
class PIDGains:
    """PID kazanç katsayıları."""
    kp: float  # Oransal (Proportional)
    ki: float  # İntegral
    kd: float  # Türev (Derivative)


@dataclass
class PIDConfig:
    """PID denetleyici konfigürasyonu."""

    # Cross-track error (şerit merkezinden yanal sapma) PID
    cte_gains: PIDGains = field(default_factory=lambda: PIDGains(
        kp=0.8,    # başlangıç değeri — arazi testinde tune et
        ki=0.01,
        kd=0.15
    ))

    # Heading error (yön sapması) PID
    heading_gains: PIDGains = field(default_factory=lambda: PIDGains(
        kp=1.2,    # heading genellikle daha agresif tune ister
        ki=0.005,
        kd=0.25
    ))

    # Çıktı birleştirme ağırlıkları
    cte_weight: float = 0.4       # cross-track'in ağırlığı
    heading_weight: float = 0.6   # heading'in ağırlığı (genellikle dominant)

    # Anti-windup: integralin birikmesini sınırla
    integral_clamp: float = 1.0   # maksimum integral değeri

    # Çıktı sınırları (radyan)
    output_min: float = -0.52     # ~-30 derece
    output_max: float = 0.52      # ~+30 derece


class PIDController:
    """Tek eksenli PID denetleyici."""

    def __init__(self, gains: PIDGains, integral_clamp: float = 1.0):
        self.gains = gains
        self.integral_clamp = integral_clamp
        self._integral = 0.0
        self._prev_error = 0.0
        self._prev_time = None

    def compute(self, error: float, timestamp: float = None) -> float:
        """
        Hata girdisinden kontrol çıktısı hesapla.

        Args:
            error: Anlık hata değeri
            timestamp: Zaman damgası (saniye). None ise sistem saati kullanılır.

        Returns:
            PID çıktısı (ham, sınırlanmamış)
        """
        now = timestamp if timestamp is not None else time.monotonic()

        if self._prev_time is None:
            dt = 0.05  # ilk çağrıda varsayılan dt
        else:
            dt = now - self._prev_time
            dt = max(dt, 1e-6)  # sıfıra bölünmeden koru

        # P — anlık hata
        p_term = self.gains.kp * error

        # I — birikmiş hata (anti-windup ile)
        self._integral += error * dt
        self._integral = max(-self.integral_clamp,
                             min(self.integral_clamp, self._integral))
        i_term = self.gains.ki * self._integral

        # D — hatanın değişim hızı
        derivative = (error - self._prev_error) / dt
        d_term = self.gains.kd * derivative

        self._prev_error = error
        self._prev_time = now

        return p_term + i_term + d_term

    def reset(self):
        """FSM mod değişiminde integrali ve geçmiş değerleri sıfırla."""
        self._integral = 0.0
        self._prev_error = 0.0
        self._prev_time = None


class HybridPIDController:
    """
    Cross-track error + heading error'ü birleştiren hibrit PID.

    Stanley çıktısını (cte, heading_error) alır,
    Ackermann modeline gidecek delta komutunu üretir.

    Kullanım:
        pid = HybridPIDController()
        delta = pid.compute(cte=0.05, heading_error=0.02)
    """

    def __init__(self, config: PIDConfig = None):
        self.config = config or PIDConfig()
        self._cte_pid = PIDController(
            self.config.cte_gains,
            self.config.integral_clamp
        )
        self._heading_pid = PIDController(
            self.config.heading_gains,
            self.config.integral_clamp
        )

    def compute(self,
                cte: float,
                heading_error: float,
                timestamp: float = None) -> float:
        """
        Direksiyon açısı komutunu hesapla.

        Args:
            cte: Cross-track error (metre). Sola sapma pozitif.
            heading_error: Heading error (radyan). Sola sapma pozitif.
            timestamp: Zaman damgası (opsiyonel).

        Returns:
            delta: Direksiyon açısı komutu (radyan).
        """
        cte_out = self._cte_pid.compute(cte, timestamp)
        heading_out = self._heading_pid.compute(heading_error, timestamp)

        # Ağırlıklı birleştirme
        raw_delta = (self.config.cte_weight * cte_out +
                     self.config.heading_weight * heading_out)

        # Çıktıyı sınırla
        delta = max(self.config.output_min,
                    min(self.config.output_max, raw_delta))

        return delta

    def reset(self):
        """Mod değişiminde her iki PID'i de sıfırla."""
        self._cte_pid.reset()
        self._heading_pid.reset()

    @property
    def debug_info(self) -> dict:
        """Debug için iç durum bilgisi."""
        return {
            'cte_integral': self._cte_pid._integral,
            'heading_integral': self._heading_pid._integral,
        }


# ─── Test ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    pid = HybridPIDController()

    print("Hibrit PID Simülasyonu")
    print("=" * 60)
    print(f"{'t(s)':>6} {'CTE(m)':>8} {'Hdg(°)':>8} {'δ(°)':>8} {'integral':>10}")
    print("-" * 60)

    # Senaryo: araç şeridin 0.15m sağında, 5° sola bakıyor
    # Adım adım düzelmeyi gözlemle
    t = 0.0
    cte = 0.15       # 15cm sağ sapma
    heading = math.radians(5)  # 5° sola bakış

    for step in range(20):
        delta = pid.compute(cte, heading, timestamp=t)

        print(f"{t:>6.2f} {cte:>8.3f} {math.degrees(heading):>8.2f} "
              f"{math.degrees(delta):>8.2f} {pid.debug_info['cte_integral']:>10.4f}")

        # Basit simülasyon: delta uygulanınca hata azalıyor (gerçek araç olmadığı için kaba)
        cte -= delta * 0.03
        heading -= delta * 0.05
        t += 0.05
