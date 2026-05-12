# planning_msgs/TrajectoryPoint.msg
# =============================================================================
# Tek yörünge noktası — map frame
# Trajectory.msg ve ActiveRouteContext.msg içinde kullanılır
# =============================================================================

float64 x                    # Konum x (metre) — map frame
float64 y                    # Konum y (metre) — map frame
float64 yaw                  # Yön açısı (radyan)
float32 speed                # Referans hız (m/s)
float32 curvature            # Yol eğriliği (1/metre)
float32 distance_from_start  # Başlangıçtan mesafe (metre)