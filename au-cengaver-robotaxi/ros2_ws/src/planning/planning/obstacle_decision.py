#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
obstacle_decision.py

Algoritma 10: Trajectory Sampling + Ağırlıklı Maliyet (Lokal Planlayıcı)
Algoritma 11: Mesafe Katmanlı Reaktif Engel Kaçınma

Algoritma Tablosu v2.0 §4:

  Algo 10:
    - Hız ve direksiyon alanını diskret örnekle (K örnek)
    - Her örnek için 0.5s ileri simülasyon
    - Maliyet: C = w_path·yol_sapması + w_obs·engel_maliyeti + w_head·heading_sapması
    - Karşı şerit bypass: maliyet = 1000
    - En düşük maliyetli yörüngeyi seç

  Algo 11:
    - in_path hesapla: planned_trajectory ile obstacle_track kesişiyor mu
    - in_path=true: TTC katmanına geç
      ttc > 3s → izle/hazırla
      2s < ttc ≤ 3s → hız düşür
      1s < ttc ≤ 2s → STOP_APPROACH / kaçınma
      ttc ≤ 1s VEYA distance < emergency_dist(v) → tam fren
    - PEDESTRIAN → TTC eşikleri ×2

Parametreler:
  K = 20–50 örnek
  w_path=1.0, w_obs=5.0, w_head=0.5
  TTC eşikleri: 3s / 2s / 1s
  emergency_dist = max(0.3, v·0.3 + 0.2)
  PEDESTRIAN çarpanı = 2×

Sözleşme: Perception ↔ Planner Contract v1.4
  - in_path alanı ObstacleTrack.msg'de YOKTUR — planner hesaplar
  - TTC = distance / max(closing_speed, ε)
  - ego_speed: active_route_context.ego_speed_mps'den gelir
"""

import math
from dataclasses import dataclass
from typing import List, Optional, Tuple


# ─── Sabitler ──────────────────────────────────────────────────────────────
# Algo 10 — Trajectory Sampling
K_SAMPLES          = 20       # örnek sayısı (gerçek zamanlı test ile ayarlanır)
SIM_TIME           = 0.5      # saniye — ileri simülasyon süresi
SIM_DT             = 0.05     # saniye — simülasyon adımı
W_PATH             = 1.0      # yol sapması ağırlığı
W_OBS              = 5.0      # engel maliyeti ağırlığı
W_HEAD             = 0.5      # heading sapması ağırlığı
OPPOSITE_LANE_COST = 1000.0   # karşı şerit cezası

# Algo 11 — Reaktif Engel Kaçınma
TTC_WATCH          = 3.0      # saniye — izle/hazırla
TTC_SLOW           = 2.0      # saniye — hız düşür
TTC_STOP           = 1.0      # saniye — STOP_APPROACH
REACTION_TIME      = 0.3      # saniye
BRAKING_MARGIN     = 0.2      # metre
PEDESTRIAN_MULT    = 2.0      # PEDESTRIAN TTC çarpanı
TTC_EPSILON        = 0.001    # sıfıra bölme koruması

# BEE1 Platform Sabitleri
WHEELBASE          = 1.86     # metre — Algo Tablosu v2.0 §2
MAX_STEER_DEG      = 32.5     # derece
V_MAX              = 6.67     # m/s


@dataclass
class ObstacleTrack:
    """Perception'dan gelen engel bilgisi."""
    track_id:    int
    class_label: str      # "car", "pedestrian", "cyclist", "unknown"
    position_x:  float    # base_link frame
    position_y:  float    # base_link frame
    distance:    float    # front_bumper'a mesafe
    ttc:         float    # perception'dan gelen TTC
    is_static:   bool
    velocity:    float = 0.0   # hareket hızı (m/s)


@dataclass
class ObstacleDecisionResult:
    """Engel kaçınma kararı."""
    action:          str     # 'CONTINUE', 'SLOW', 'STOP_APPROACH', 'EMERGENCY'
    speed_factor:    float   # 0.0–1.0 — hız çarpanı
    in_path:         bool    # Yolda engel var mı
    critical_track:  Optional[ObstacleTrack]
    warning_flags:   List[str]


class ObstacleDecision:
    """
    Algoritma 10 + 11 — Engel Kaçınma.

    Kullanım:
        od = ObstacleDecision()
        result = od.decide(
            tracks=obstacle_tracks,
            trajectory=planned_trajectory,
            ego_speed=2.5,
            loc_status=0
        )
    """

    def __init__(self):
        self._loc_status = 0

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API
    # ───────────────────────────────────────────────────────────────────────

    def decide(
        self,
        tracks:     List[ObstacleTrack],
        trajectory: List,    # List[TrajectoryPoint]
        ego_speed:  float,
        loc_status: int = 0,
    ) -> ObstacleDecisionResult:
        """
        Algoritma 11 — Mesafe Katmanlı Reaktif Engel Kaçınma.

        Args:
            tracks:     Perception'dan gelen engel listesi
            trajectory: Planlanan trajectory
            ego_speed:  Araç hızı (m/s) — active_route_context.ego_speed_mps
            loc_status: Lokalizasyon durumu

        Returns:
            ObstacleDecisionResult
        """
        self._loc_status = loc_status

        if not tracks:
            return ObstacleDecisionResult(
                action='CONTINUE',
                speed_factor=1.0,
                in_path=False,
                critical_track=None,
                warning_flags=[]
            )

        warnings        = []
        worst_action    = 'CONTINUE'
        worst_factor    = 1.0
        critical_track  = None
        any_in_path     = False

        for track in tracks:
            # in_path hesapla — Algo 11
            in_path = self._check_in_path(track, trajectory)

            if not in_path:
                continue

            any_in_path = True

            # PEDESTRIAN çarpanı
            is_pedestrian = (track.class_label.lower() == 'pedestrian')
            ttc_mult      = PEDESTRIAN_MULT if is_pedestrian else 1.0

            # Efektif TTC eşikleri
            ttc_watch = TTC_WATCH * ttc_mult
            ttc_slow  = TTC_SLOW  * ttc_mult
            ttc_stop  = TTC_STOP  * ttc_mult

            # TTC kullan (perception'dan gelir)
            ttc = track.ttc

            # Emergency mesafe kontrolü
            emerg_dist = self._emergency_distance(ego_speed)

            if ttc <= ttc_stop or track.distance < emerg_dist:
                action = 'EMERGENCY'
                factor = 0.0
                warnings.append(
                    f'EMERGENCY:track_{track.track_id}'
                    f':ttc={ttc:.1f}s:dist={track.distance:.1f}m'
                )

            elif ttc <= ttc_slow:
                action = 'STOP_APPROACH'
                factor = 0.0
                warnings.append(
                    f'STOP_APPROACH:track_{track.track_id}'
                    f':ttc={ttc:.1f}s'
                )

            elif ttc <= ttc_watch:
                action = 'SLOW'
                factor = max(0.3, ttc / ttc_watch)
                warnings.append(
                    f'SLOW:track_{track.track_id}'
                    f':ttc={ttc:.1f}s'
                )

            else:
                action = 'CONTINUE'
                factor = 1.0

            # En kötü durumu seç
            if self._action_severity(action) > \
               self._action_severity(worst_action):
                worst_action   = action
                worst_factor   = factor
                critical_track = track

        return ObstacleDecisionResult(
            action=worst_action,
            speed_factor=worst_factor,
            in_path=any_in_path,
            critical_track=critical_track,
            warning_flags=warnings
        )

    def sample_trajectories(
        self,
        tracks:       List[ObstacleTrack],
        ego_x:        float,
        ego_y:        float,
        ego_yaw:      float,
        ego_speed:    float,
        target_speed: float,
        loc_status:   int = 0,
    ) -> Optional[List]:
        """
        Algoritma 10 — Trajectory Sampling + Ağırlıklı Maliyet.

        K örnek üret, her biri için maliyet hesapla,
        en düşük maliyetli yörüngeyi döndür.

        DEGRADED modda K yarıya iner, zaman ufku kısalır.
        """
        k = K_SAMPLES // 2 if loc_status == 4 else K_SAMPLES
        sim_time = SIM_TIME / 2 if loc_status == 4 else SIM_TIME

        best_trajectory = None
        best_cost       = float('inf')

        # Direksiyon açısı örnekleri
        steer_samples = self._linspace(
            -math.radians(MAX_STEER_DEG),
             math.radians(MAX_STEER_DEG),
             k
        )

        for steer in steer_samples:
            # İleri simülasyon
            traj = self._simulate(
                ego_x, ego_y, ego_yaw, ego_speed,
                steer, sim_time
            )

            # Maliyet hesapla
            cost = self._compute_cost(
                traj, steer, ego_yaw, tracks, ego_speed
            )

            if cost < best_cost:
                best_cost       = cost
                best_trajectory = traj

        return best_trajectory

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE — Algoritma 11
    # ───────────────────────────────────────────────────────────────────────

    def _check_in_path(
        self,
        track:      ObstacleTrack,
        trajectory: List
    ) -> bool:
        """
        Engel planned_trajectory üzerinde mi?
        Perception ↔ Planner Contract v1.4:
          in_path alanı YOKTUR — planner hesaplar.

        Basit yaklaşım: engel konumu trajectory noktalarına
        yakın mı kontrol et (eşik: 1.5m yanal mesafe).
        """
        if not trajectory:
            # Trajectory yoksa base_link'te önde mi bak
            return (
                track.position_x > 0 and
                track.distance < 10.0 and
                abs(track.position_y) < 1.5
            )

        LATERAL_THRESHOLD = 1.5   # metre

        for pt in trajectory:
            # Trajectory noktasına olan mesafe
            dx   = track.position_x - pt.x
            dy   = track.position_y - pt.y
            dist = math.sqrt(dx**2 + dy**2)

            if dist < LATERAL_THRESHOLD:
                return True

        return False

    def _emergency_distance(self, speed: float) -> float:
        """
        Algoritma 11:
        emergency_dist = max(0.3, v·0.3 + 0.2)
        """
        return max(0.3, speed * REACTION_TIME + BRAKING_MARGIN)

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE — Algoritma 10
    # ───────────────────────────────────────────────────────────────────────

    def _simulate(
        self,
        x: float, y: float, yaw: float,
        speed: float, steer: float,
        sim_time: float
    ) -> List[Tuple[float, float, float]]:
        """
        Basit bisiklet modeli ile ileri simülasyon.
        Planner ↔ Controller Contract: BEE1 dingil = 1.86m
        """
        traj  = [(x, y, yaw)]
        steps = int(sim_time / SIM_DT)

        for _ in range(steps):
            # Bisiklet modeli
            beta = math.atan(
                0.5 * math.tan(steer)
            )
            x   += speed * math.cos(yaw + beta) * SIM_DT
            y   += speed * math.sin(yaw + beta) * SIM_DT
            yaw += (speed / WHEELBASE) * math.tan(steer) * SIM_DT
            yaw  = self._normalize_angle(yaw)
            traj.append((x, y, yaw))

        return traj

    def _compute_cost(
        self,
        trajectory:   List[Tuple[float, float, float]],
        steer:        float,
        target_yaw:   float,
        tracks:       List[ObstacleTrack],
        ego_speed:    float
    ) -> float:
        """
        Algoritma 10 — Maliyet fonksiyonu:
        C = w_path·yol_sapması + w_obs·engel_maliyeti + w_head·heading_sapması
        """
        # Yol sapması — direksiyon açısının büyüklüğü
        path_cost = abs(steer)

        # Heading sapması
        final_yaw  = trajectory[-1][2] if trajectory else 0.0
        head_cost  = abs(self._normalize_angle(final_yaw - target_yaw))

        # Engel maliyeti
        obs_cost = 0.0
        for pt in trajectory:
            for track in tracks:
                dx   = pt[0] - track.position_x
                dy   = pt[1] - track.position_y
                dist = math.sqrt(dx**2 + dy**2)

                if dist < 0.5:
                    obs_cost += OPPOSITE_LANE_COST
                elif dist < 2.0:
                    obs_cost += W_OBS / (dist + 0.1)

        total = (
            W_PATH * path_cost +
            W_OBS  * obs_cost  +
            W_HEAD * head_cost
        )

        return total

    # ───────────────────────────────────────────────────────────────────────
    # YARDIMCI
    # ───────────────────────────────────────────────────────────────────────

    @staticmethod
    def _action_severity(action: str) -> int:
        """Aksiyon şiddeti — karşılaştırma için."""
        severity = {
            'CONTINUE':      0,
            'SLOW':          1,
            'STOP_APPROACH': 2,
            'EMERGENCY':     3,
        }
        return severity.get(action, 0)

    @staticmethod
    def _linspace(start: float, stop: float, n: int) -> List[float]:
        """n adet eşit aralıklı değer üret."""
        if n <= 1:
            return [start]
        step = (stop - start) / (n - 1)
        return [start + i * step for i in range(n)]

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-π, π] aralığına normalize et."""
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle