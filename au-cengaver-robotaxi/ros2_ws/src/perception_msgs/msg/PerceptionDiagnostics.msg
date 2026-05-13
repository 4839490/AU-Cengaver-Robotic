# perception_msgs/msg/PerceptionDiagnostics.msg
# Topic: /perception/diagnostics | 1-2 Hz | frame_id: "" (no spatial frame)
# Each perception node publishes its own row under this single topic.

std_msgs/Header header
string  node_name
float32 input_hz
float32 output_hz
float32 latency_ms
uint32  last_msg_age_ms
float32 mean_confidence
uint32  num_outputs
float32 gpu_utilization
string[] warning_flags
