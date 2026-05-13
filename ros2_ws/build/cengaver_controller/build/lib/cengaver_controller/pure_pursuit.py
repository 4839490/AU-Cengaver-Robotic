"""
Pure Pursuit Kontrolcü
======================
Planner'dan gelen trajectory noktalarını takip eder.
Stanley'e alternatif veya tamamlayıcı olarak kullanılır.

Stanley vs Pure Pursuit:
  Stanley   → şerit merkezine geometrik yaklaşım, düşük hızda iyi
  Pure Pursuit → lookahead noktasına yay ile yaklaşım, yüksek hızda iyi

Bu kodda ikisi birlikte çalışabilir:
  Düşük hız (park, yaklaşım) → Stanley dominant
  Yüksek hız (lane follow)   → Pure Pursuit dominant

Pure Pursuit Formülü:
  delta = arctan(2 × L × sin(α) / ld)

  L  : dingil mesafesi (m)
  α  : araç ile hedef nokta arasındaki açı (rad)
  ld : lookahead mesafesi (m)
"""

import math
from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class PurePursuitParams:
    """Pure Pursuit parametreleri."""
    wheelbase:      float = 2.40   # Tragger T-Car dingil mesafesi (m)
    lookahead_min:  float = 2.0    # Min lookahead (m)
    lookahead_max:  float = 8.0    # Max lookahead (m)
    lookahead_k:    float = 0.6    # Adaptif lookahead katsayısı (hız × k)
    max_delta:      float = 0.567  # Max direksiyon açısı (rad) — 32.5°


@dataclass
class PurePursuitOutput:
    """Pure Pursuit çıktısı."""
    delta_rad:    float   # Direksiyon açısı (rad)
    lookahead:    float   # Kullanılan lookahead (m)
    target_x:     float   # Hedef nokta x (m)
    target_y:     float   # Hedef nokta y (m)
    alpha:        float   # Araç-hedef açısı (rad)
    valid:        bool    # Geçerli çıktı mı?


class PurePursuitController:
    """
    Pure Pursuit kontrolcü.

    Planner'dan gelen trajectory waypoint'lerini takip eder.
    Lookahead noktasına bir yay çizerek delta açısı hesaplar.

    Kullanım:
        pp = PurePursuitController()
        output = pp.compute(
            waypoints=[(x1,y1,yaw1), (x2,y2,yaw2), ...],
            vehicle_x=0.0,
            vehicle_y=0.0,
            vehicle_yaw=0.0,
            vehicle_speed=2.0
        )
        delta = output.delta_rad  → Ackermann'a gider
    """

    def __init__(self, params: PurePursuitParams = None):
        self.params = params or PurePursuitParams()

    def compute(self,
                waypoints: List[Tuple[float, float, float]],
                vehicle_x: float,
                vehicle_y: float,
                vehicle_yaw: float,
                vehicle_speed: float) -> PurePursuitOutput:
        """
        Pure Pursuit direksiyon açısı hesapla.

        Args:
            waypoints: [(x, y, yaw), ...] — map frame, planner trajectory
            vehicle_x: Araç x konumu (m)
            vehicle_y: Araç y konumu (m)
            vehicle_yaw: Araç yaw açısı (rad)
            vehicle_speed: Araç hızı (m/s)

        Returns:
            PurePursuitOutput
        """
        if len(waypoints) < 2:
            return PurePursuitOutput(0.0, 0.0, 0.0, 0.0, 0.0, False)

        p = self.params

        # Adaptif lookahead
        lookahead = self._compute_lookahead(vehicle_speed)

        # Lookahead noktasını bul
        target = self._find_lookahead_point(
            waypoints, vehicle_x, vehicle_y, lookahead
        )

        if target is None:
            # Lookahead noktası bulunamadı — son waypoint'e git
            target = waypoints[-1]

        tx, ty = target[0], target[1]

        # Araç frame'ine dönüştür
        # (global → lokal koordinat dönüşümü)
        dx = tx - vehicle_x
        dy = ty - vehicle_y

        # Araç frame'inde hedef açısı
        local_x =  dx * math.cos(vehicle_yaw) + dy * math.sin(vehicle_yaw)
        local_y = -dx * math.sin(vehicle_yaw) + dy * math.cos(vehicle_yaw)

        # α: araç ile hedef arasındaki açı (araç frame'inde)
        alpha = math.atan2(local_y, local_x)

        # Gerçek lookahead mesafesi
        ld = math.sqrt(dx**2 + dy**2)
        ld = max(ld, 0.1)   # sıfıra bölünmeden koru

        # Pure Pursuit formülü: delta = arctan(2 × L × sin(α) / ld)
        delta = math.atan2(2.0 * p.wheelbase * math.sin(alpha), ld)

        # Sınırla
        delta = max(-p.max_delta, min(p.max_delta, delta))

        return PurePursuitOutput(
            delta_rad = delta,
            lookahead = lookahead,
            target_x  = tx,
            target_y  = ty,
            alpha     = alpha,
            valid     = True
        )

    def compute_from_trajectory_msg(self,
                                     points: list,
                                     vehicle_x: float,
                                     vehicle_y: float,
                                     vehicle_yaw: float,
                                     vehicle_speed: float) -> PurePursuitOutput:
        """
        ROS2 Trajectory.msg noktalarından Pure Pursuit hesabı.

        Args:
            points: TrajectoryPoint listesi (x, y, yaw, speed, curvature)
            vehicle_x, vehicle_y, vehicle_yaw, vehicle_speed: Araç durumu

        Returns:
            PurePursuitOutput
        """
        # (x, y, yaw) tuple listesine çevir
        waypoints = [(pt['x'], pt['y'], pt['yaw']) for pt in points]
        return self.compute(waypoints, vehicle_x, vehicle_y,
                            vehicle_yaw, vehicle_speed)

    # ── İç Fonksiyonlar ───────────────────────────────────────────────────────

    def _compute_lookahead(self, speed: float) -> float:
        """Adaptif lookahead: hız arttıkça lookahead uzar."""
        p = self.params
        ld = p.lookahead_k * abs(speed)
        return max(p.lookahead_min, min(p.lookahead_max, ld))

    def _find_lookahead_point(self,
                               waypoints: List[Tuple],
                               vehicle_x: float,
                               vehicle_y: float,
                               lookahead: float) -> Optional[Tuple]:
        """
        Araçtan lookahead mesafesindeki waypoint'i bul.
        Tam mesafe yoksa interpolasyon yapar.
        """
        # Önce en yakın noktayı bul
        nearest_idx = 0
        min_dist    = float('inf')
        for i, pt in enumerate(waypoints):
            dist = math.sqrt((pt[0] - vehicle_x)**2 + (pt[1] - vehicle_y)**2)
            if dist < min_dist:
                min_dist    = dist
                nearest_idx = i

        # En yakın noktadan başlayarak lookahead mesafesinde nokta ara
        for i in range(nearest_idx, len(waypoints)):
            pt   = waypoints[i]
            dist = math.sqrt((pt[0] - vehicle_x)**2 + (pt[1] - vehicle_y)**2)
            if dist >= lookahead:
                # Interpolasyon: tam lookahead mesafesinde nokta üret
                if i > 0:
                    return self._interpolate(
                        waypoints[i-1], waypoints[i],
                        vehicle_x, vehicle_y, lookahead
                    )
                return pt

        # Tüm noktalar lookahead'den yakın — son noktayı döndür
        return waypoints[-1] if waypoints else None

    def _interpolate(self,
                      p1: Tuple, p2: Tuple,
                      vx: float, vy: float,
                      lookahead: float) -> Tuple:
        """İki waypoint arasında lookahead mesafesinde nokta üret."""
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]

        # Doğru parametrik formu: P = P1 + t*(P2-P1)
        dx = x2 - x1
        dy = y2 - y1

        # Araçtan P1'e vektör
        fx = x1 - vx
        fy = y1 - vy

        a = dx**2 + dy**2
        b = 2 * (fx*dx + fy*dy)
        c = fx**2 + fy**2 - lookahead**2

        disc = b**2 - 4*a*c
        if disc < 0 or a < 1e-10:
            return p2

        t = (-b + math.sqrt(disc)) / (2*a)
        t = max(0.0, min(1.0, t))

        ix = x1 + t * dx
        iy = y1 + t * dy

        # Yaw interpolasyonu
        yaw1 = p1[2] if len(p1) > 2 else math.atan2(dy, dx)
        yaw2 = p2[2] if len(p2) > 2 else math.atan2(dy, dx)
        iyaw = yaw1 + t * (yaw2 - yaw1)

        return (ix, iy, iyaw)


# ─── Test ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    pp = PurePursuitController()

    print("Pure Pursuit Kontrolcü Testi")
    print("=" * 55)

    # Test 1: Düz yol, araç merkezde
    waypoints = [(i * 0.5, 0.0, 0.0) for i in range(30)]
    out = pp.compute(waypoints, 0.0, 0.0, 0.0, 2.0)
    print(f"\n[Test 1] Düz yol, merkezde")
    print(f"  delta={math.degrees(out.delta_rad):.2f}°  "
          f"lookahead={out.lookahead:.2f}m  "
          f"alpha={math.degrees(out.alpha):.2f}°")

    # Test 2: Araç 0.2m sağa saptı
    out = pp.compute(waypoints, 0.0, 0.2, 0.0, 2.0)
    print(f"\n[Test 2] Araç 0.2m sağa saptı")
    print(f"  delta={math.degrees(out.delta_rad):.2f}°  "
          f"alpha={math.degrees(out.alpha):.2f}°")

    # Test 3: Sola dönen yay
    R = 8.0  # dönüş yarıçapı
    arc_points = [
        (R * math.sin(i * 0.05), R * (1 - math.cos(i * 0.05)), i * 0.05)
        for i in range(40)
    ]
    out = pp.compute(arc_points, 0.0, 0.0, 0.0, 3.0)
    print(f"\n[Test 3] Sol viraj (R={R}m)")
    print(f"  delta={math.degrees(out.delta_rad):.2f}°  "
          f"target=({out.target_x:.2f}, {out.target_y:.2f})")

    # Test 4: Adaptif lookahead
    print(f"\n[Test 4] Adaptif lookahead")
    for v in [0.5, 1.0, 2.0, 4.0, 6.67]:
        lh = pp._compute_lookahead(v)
        print(f"  v={v:.2f} m/s → lookahead={lh:.2f}m")
