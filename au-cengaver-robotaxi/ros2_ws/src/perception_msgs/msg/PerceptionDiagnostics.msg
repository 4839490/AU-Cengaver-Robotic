# perception_msgs/PerceptionDiagnostics.msg
# =============================================================================
# Perception → izleme/debug diagnostik bilgisi
# Topic: /perception/diagnostics — 10Hz
# =============================================================================

std_msgs/Header header
float64 lane_input_hz        # Kamera girdi frekansı
float64 lane_output_hz       # Şerit çıktı frekansı
float64 lane_latency_ms      # Şerit işleme gecikmesi
float64 lane_mean_confidence # Ortalama şerit güveni
float64 light_input_hz       # Trafik ışığı girdi frekansı
float64 light_output_hz      # Trafik ışığı çıktı frekansı
float64 light_latency_ms     # Trafik ışığı işleme gecikmesi
float64 obstacle_input_hz    # LiDAR girdi frekansı
float64 obstacle_output_hz   # Engel çıktı frekansı
float64 obstacle_latency_ms  # Engel işleme gecikmesi
bool lane_healthy            # Şerit node sağlıklı mı?
bool light_healthy           # Trafik ışığı node sağlıklı mı?
bool obstacle_healthy        # Engel node sağlıklı mı?
string[] warning_flags
