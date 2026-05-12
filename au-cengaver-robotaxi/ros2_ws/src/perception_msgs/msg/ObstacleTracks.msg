# perception_msgs/ObstacleTracks.msg
# =============================================================================
# Perception → Planner engel listesi
# Topic: /perception/obstacle_tracks — 20Hz
# =============================================================================

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms
ObstacleTrack[] tracks
string[] warning_flags
