"""
Stanley Kontrolcü
=================
Şerit merkezi eğrisinden cross-track error (CTE) ve heading error hesaplar.
UFLD v2'den gelen polinom şerit verisiyle çalışır.

Sözleşme:
  Girdi  : Araç pozisyonu + şerit merkezi polinomu
  Çıktı  : delta_rad → Ackermann modeline gider
           cte       → HybridPID'e gider
           heading_error → HybridPID'e gider

Stanley Formülü:
  delta = heading_error + arctan(k × cte / (v + ks))

  heading_error : araç yönü ile şerit yönü arasındaki fark (rad)
  cte           : araç ile şerit merkezi arası yanal mesafe (m)
  v             : araç hızı (m/s)
  k             : Stanley kazanımı (tune edilecek)
  ks            : softening sabiti (düşük hızda kararlılık için)
"""

import math
from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class StanleyParams:
    """Stanley kontrolcü parametreleri."""
    k:              float = 0.8    # Stanley kazanımı — arazide tune edilecek
    ks:             float = 0.1    # Softening sabiti — düşük hızda salınımı önler
    max_delta:      float = 0.567  # Max direksiyon açısı (rad) — 32.5°, sözleşmeden
    lookahead_min:  float = 1.5    # Minimum lookahead mesafesi (m)
    lookahead_max:  float = 6.0    # Maksimum lookahead mesafesi (m)
    lookahead_k:    float = 0.5    # Adaptif lookahead katsayısı


@dataclass
class StanleyOutput:
    """Stanley kontrolcü çıktısı."""
    delta_rad:          float   # Direksiyon açısı komutu (radyan)
    cte:                float   # Cross-track error (m) — sola pozitif
    cross_track_error:  float   # cte ile aynı — sözleşme uyumu için
    heading_error:      float   # Heading error (rad) — sola pozitif
    lookahead:          float   # Kullanılan lookahead mesafesi (m)
    valid:              bool    # Çıktı geçerli mi?


class StanleyController:
    """
    Stanley kontrolcü.

    UFLD v2'den gelen şerit polinomu veya waypoint listesinden
    araç için direksiyon açısı hesaplar.

    Kullanım:
        stanley = StanleyController()

        # Polinom ile (UFLD v2 çıktısı)
        output = stanley.compute_from_poly(
            coeffs=[a, b, c],     # şerit merkezi polinomu
            vehicle_speed=2.0,    # m/s
            vehicle_yaw=0.1       # rad
        )

        # Waypoint ile (planner trajectory)
        output = stanley.compute_from_waypoints(
            waypoints=[(x1,y1), (x2,y2), ...],
            vehicle_x=0.0,
            vehicle_y=0.0,
            vehicle_yaw=0.1,
            vehicle_speed=2.0
        )
    """

    def __init__(self, params: StanleyParams = None):
        self.params = params or StanleyParams()

    # ── Polinom tabanlı (UFLD v2) ─────────────────────────────────────────────

    def compute_from_poly(self,
                          coeffs: List[float],
                          vehicle_speed: float,
                          vehicle_yaw: float = 0.0) -> StanleyOutput:
        """
        UFLD v2 şerit polinomundan Stanley hesabı.

        Args:
            coeffs: [a, b, c] — y = ax² + bx + c şeklinde şerit merkezi
                    x: araç önündeki mesafe (m)
                    y: yanal sapma (m)
            vehicle_speed: Araç hızı (m/s)
            vehicle_yaw: Araç yaw açısı (rad)

        Returns:
            StanleyOutput
        """
        if len(coeffs) < 2:
            return StanleyOutput(0.0, 0.0, 0.0, 0.0, False)

        p = self.params

        # Adaptif lookahead mesafesi
        lookahead = self._compute_lookahead(vehicle_speed)

        # Lookahead noktasında CTE hesapla
        # y = ax² + bx + c — lookahead noktasındaki yanal sapma
        if len(coeffs) == 3:
            a, b, c = coeffs
        elif len(coeffs) == 2:
            a, b, c = 0.0, coeffs[0], coeffs[1]
        else:
            a, b, c = coeffs[0], coeffs[1], coeffs[2]

        # CTE: araç konumundaki (x=0) polinom değeri
        cte = c  # x=0'da y = c

        # Heading error: şerit eğiminin arctanı
        # Şerit yönü: dy/dx = 2ax + b → x=0'da = b
        lane_yaw = math.atan2(b, 1.0)
        heading_error = lane_yaw - vehicle_yaw
        heading_error = self._normalize_angle(heading_error)

        # Stanley formülü
        delta = self._stanley_formula(
            heading_error, cte, vehicle_speed
        )

        return StanleyOutput(
            delta_rad           = delta,
            cte                 = cte,
            cross_track_error   = cte,
            heading_error       = heading_error,
            lookahead           = lookahead,
            valid               = True
        )

    # ── Waypoint tabanlı (Planner trajectory) ────────────────────────────────

    def compute_from_waypoints(self,
                               waypoints: List[Tuple[float, float]],
                               vehicle_x: float,
                               vehicle_y: float,
                               vehicle_yaw: float,
                               vehicle_speed: float) -> StanleyOutput:
        """
        Planner'dan gelen waypoint listesinden Stanley hesabı.

        Args:
            waypoints: [(x1,y1), (x2,y2), ...] — map frame'inde
            vehicle_x: Araç x konumu (m)
            vehicle_y: Araç y konumu (m)
            vehicle_yaw: Araç yaw açısı (rad)
            vehicle_speed: Araç hızı (m/s)

        Returns:
            StanleyOutput
        """
        if len(waypoints) < 2:
            return StanleyOutput(0.0, 0.0, 0.0, 0.0, False)

        p = self.params

        # Adaptif lookahead
        lookahead = self._compute_lookahead(vehicle_speed)

        # En yakın waypoint'i bul
        nearest_idx = self._find_nearest_waypoint(
            waypoints, vehicle_x, vehicle_y
        )

        # Lookahead noktasını bul
        target_idx = self._find_lookahead_waypoint(
            waypoints, vehicle_x, vehicle_y,
            nearest_idx, lookahead
        )

        # Hedef waypoint
        tx, ty = waypoints[target_idx]

        # Cross-track error
        dx = tx - vehicle_x
        dy = ty - vehicle_y
        target_angle = math.atan2(dy, dx)
        cte = math.sin(target_angle - vehicle_yaw) * math.sqrt(dx**2 + dy**2)

        # Heading error — iki ardışık waypoint arasındaki yön
        if target_idx < len(waypoints) - 1:
            nx, ny = waypoints[target_idx + 1]
            lane_yaw = math.atan2(ny - ty, nx - tx)
        else:
            px, py = waypoints[target_idx - 1]
            lane_yaw = math.atan2(ty - py, tx - px)

        heading_error = self._normalize_angle(lane_yaw - vehicle_yaw)

        # Stanley formülü
        delta = self._stanley_formula(
            heading_error, cte, vehicle_speed
        )

        return StanleyOutput(
            delta_rad           = delta,
            cte                 = cte,
            cross_track_error   = cte,
            heading_error       = heading_error,
            lookahead           = lookahead,
            valid               = True
        )

    # ── İç Fonksiyonlar ───────────────────────────────────────────────────────

    def _stanley_formula(self,
                         heading_error: float,
                         cte: float,
                         speed: float) -> float:
        """
        Stanley direksiyon açısı formülü.

        delta = heading_error + arctan(k × cte / (v + ks))
        """
        p = self.params
        speed = max(speed, 0.1)   # sıfıra bölünmeden koru

        cte_term = math.atan2(p.k * cte, speed + p.ks)
        delta = heading_error + cte_term

        # Sınırla
        return max(-p.max_delta, min(p.max_delta, delta))

    def _compute_lookahead(self, speed: float) -> float:
        """Adaptif lookahead mesafesi — hıza göre değişir."""
        p = self.params
        lookahead = p.lookahead_k * abs(speed)
        return max(p.lookahead_min, min(p.lookahead_max, lookahead))

    def _find_nearest_waypoint(self,
                                waypoints: List[Tuple[float, float]],
                                x: float, y: float) -> int:
        """En yakın waypoint indeksini bul."""
        min_dist = float('inf')
        nearest  = 0
        for i, (wx, wy) in enumerate(waypoints):
            dist = math.sqrt((wx - x)**2 + (wy - y)**2)
            if dist < min_dist:
                min_dist = dist
                nearest  = i
        return nearest

    def _find_lookahead_waypoint(self,
                                  waypoints: List[Tuple[float, float]],
                                  x: float, y: float,
                                  start_idx: int,
                                  lookahead: float) -> int:
        """Lookahead mesafesindeki waypoint indeksini bul."""
        for i in range(start_idx, len(waypoints)):
            wx, wy = waypoints[i]
            dist = math.sqrt((wx - x)**2 + (wy - y)**2)
            if dist >= lookahead:
                return i
        return len(waypoints) - 1   # son waypoint

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-π, +π] aralığına normalize et."""
        while angle >  math.pi:
            angle -= 2 * math.pi
        while angle < -math.pi:
            angle += 2 * math.pi
        return angle


# ─── Test ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import math
    stanley = StanleyController()

    print("Stanley Kontrolcü Testi")
    print("=" * 55)

    # Test 1: Düz yolda merkezdeyiz
    print("\n[Test 1] Düz yol, araç merkezde")
    out = stanley.compute_from_poly(
        coeffs=[0.0, 0.0, 0.0],   # düz şerit, sapma yok
        vehicle_speed=2.0,
        vehicle_yaw=0.0
    )
    print(f"  delta={math.degrees(out.delta_rad):.2f}°  "
          f"cte={out.cte:.3f}m  "
          f"heading={math.degrees(out.heading_error):.2f}°")

    # Test 2: Araç şeridin 0.1m sağında
    print("\n[Test 2] Araç 0.1m sağa saptı")
    out = stanley.compute_from_poly(
        coeffs=[0.0, 0.0, 0.1],   # c=0.1 → 0.1m sola şerit var
        vehicle_speed=2.0,
        vehicle_yaw=0.0
    )
    print(f"  delta={math.degrees(out.delta_rad):.2f}°  "
          f"cte={out.cte:.3f}m  "
          f"heading={math.degrees(out.heading_error):.2f}°")

    # Test 3: Waypoint tabanlı
    print("\n[Test 3] Waypoint tabanlı — düz yol")
    waypoints = [(i * 0.5, 0.0) for i in range(20)]
    out = stanley.compute_from_waypoints(
        waypoints     = waypoints,
        vehicle_x     = 0.0,
        vehicle_y     = 0.1,   # 0.1m sağa saptı
        vehicle_yaw   = 0.0,
        vehicle_speed = 2.0
    )
    print(f"  delta={math.degrees(out.delta_rad):.2f}°  "
          f"cte={out.cte:.3f}m  "
          f"lookahead={out.lookahead:.2f}m")

    # Test 4: Farklı hızlarda lookahead
    print("\n[Test 4] Adaptif lookahead")
    for v in [0.5, 1.0, 2.0, 4.0, 6.67]:
        lh = stanley._compute_lookahead(v)
        print(f"  v={v:.2f} m/s → lookahead={lh:.2f}m")
