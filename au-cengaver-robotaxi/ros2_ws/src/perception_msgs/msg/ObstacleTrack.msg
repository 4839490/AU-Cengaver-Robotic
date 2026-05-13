# perception_msgs/ObstacleTrack.msg
# =============================================================================
# Tek engel track — ObstacleTracks.msg içinde kullanılır
#
# ⚠️ in_path alanı YOKTUR — planner planned_trajectory ile hesaplar
# =============================================================================

uint32 track_id       # Kalman filtresi track ID
string class_label    # "car", "pedestrian", "cyclist", "unknown"
float64 position_x    # Engel konumu x (metre) — base_link frame
float64 position_y    # Engel konumu y (metre) — base_link frame
float64 distance      # Araca mesafe (metre)
float64 ttc           # Time-to-collision (saniye)
bool is_static        # Statik mi?
