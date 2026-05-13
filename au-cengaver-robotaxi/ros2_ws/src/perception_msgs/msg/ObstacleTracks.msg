# perception_msgs/msg/ObstacleTracks.msg
# Topic: /perception/obstacle_tracks | 20 Hz | frame_id: base_link | valid_until_ms: 200

std_msgs/Header header
perception_msgs/ObstacleTrack[] tracks
