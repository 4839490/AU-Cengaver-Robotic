# planning_msgs/TrajectoryPoint.msg
# =============================================================================
# Tek bir yörünge noktası — map frame'inde
# Planner → Controller (20Hz, Trajectory.msg içinde points[] listesi)
# =============================================================================

float64 x                    # Konum x (metre) — map frame
float64 y                    # Konum y (metre) — map frame
float64 yaw                  # Yön açısı (radyan) — map frame
float32 speed                # O noktadaki referans hız (m/s)
float32 curvature            # Yol eğriliği (1/metre) — 0.0=düz, +sola, -sağa
float32 distance_from_start  # Başlangıçtan bu noktaya mesafe (m)
