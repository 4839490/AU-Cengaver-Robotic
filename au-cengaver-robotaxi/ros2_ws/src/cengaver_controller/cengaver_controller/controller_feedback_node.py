"""
Controller Feedback Node
========================
/controller/feedback topic'ini 20Hz'de yayınlar.
Sözleşme v1.2 Bölüm 12'ye göre.

Neden ayrı node?
  control_node.py CAN komutlarını hesaplar ve gönderir.
  Bu node ise araç durumunu planner'a geri bildirir.
  İkisini ayırarak sorumluluklar netleşir.

Publish:
  /controller/feedback  20Hz  ControllerFeedback.msg

Subscribe:
  /odometry             20Hz  Odometri (hız + pozisyon)
  /planning/trajectory  20Hz  CTE ve heading error için
  /can_status           10Hz  CAN bağlantı durumu (opsiyonel)

Veri kaynakları:
  actual_speed        → odometriden (encoder)
  actual_steering_deg → CAN'e gönderilen son komuttan
  cross_track_error   → Stanley/Pure Pursuit çıktısından
  heading_error       → Stanley/Pure Pursuit çıktısından
  brake_active        → speed_controller'dan
  full_brake_active   → emergency flag'inden
"""

import json
import math
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32, Bool
from geometry_msgs.msg import Twist


# Feedback geçerlilik süresi (sözleşme v1.2)
FEEDBACK_VALID_MS  = 200   # ms — aşılırsa planner EMERGENCY yayınlar
FEEDBACK_RATE_HZ   = 20    # Hz — her 50ms'de bir yayın


class ControllerFeedbackNode(Node):
    """
    Controller geri bildirim node'u.

    control_node.py'den durum bilgisi alır,
    planner'ın anlayacağı formatta /controller/feedback yayınlar.

    Planner bu feedback'i şunlar için kullanır:
      cross_track_error > 0.3m  → trajectory yeniden hesapla
      cross_track_error > 0.5m  → şerit kaybı uyarısı
      heading_error > 0.2 rad   → yönelim düzeltme önceliklendir
      full_brake_active = True  → yeni trajectory üretme, bekle
      feedback gelmezse 200ms   → planner status=EMERGENCY
    """

    def __init__(self):
        super().__init__('controller_feedback_node')

        # ── Parametreler ───────────────────────────────────────────────────────
        self.declare_parameter('feedback_rate_hz',    FEEDBACK_RATE_HZ)
        self.declare_parameter('steer_center_byte',   0x81)   # CAN direksiyon merkezi
        self.declare_parameter('max_steer_angle_deg', 32.5)   # Sözleşmeden

        rate          = self.get_parameter('feedback_rate_hz').value
        self._steer_center    = self.get_parameter('steer_center_byte').value
        self._max_steer_deg   = self.get_parameter('max_steer_angle_deg').value

        # ── Durum değişkenleri ─────────────────────────────────────────────────
        self._actual_speed:      float = 0.0   # m/s — odometriden
        self._actual_steer_byte: int   = 0x81  # son CAN direksiyon komutu
        self._cte:               float = 0.0   # cross-track error (m)
        self._heading_error:     float = 0.0   # heading error (rad)
        self._brake_active:      bool  = False
        self._full_brake_active: bool  = False
        self._emergency:         bool  = False

        # ── Subscriptions ──────────────────────────────────────────────────────

        # Odometri — gerçek araç hızı
        # Gerçek araçta nav_msgs/Odometry olacak
        # Şimdilik std_msgs/Float32 ile simüle ediyoruz
        self.create_subscription(
            Float32, '/odometry/speed',
            self._odometry_cb, 10
        )

        # Stanley/PurePursuit çıktısı — CTE ve heading error
        # control_node bu bilgiyi buraya yayınlıyor
        self.create_subscription(
            Twist, '/controller/state',
            self._state_cb, 10
        )

        # CAN'e gönderilen son direksiyon komutu
        self.create_subscription(
            String, '/can_last_command',
            self._can_command_cb, 10
        )

        # Emergency flag
        self.create_subscription(
            Bool, '/emergency',
            self._emergency_cb, 10
        )

        # Fren durumu
        self.create_subscription(
            Bool, '/controller/brake_active',
            self._brake_cb, 10
        )

        # ── Publisher ─────────────────────────────────────────────────────────
        self._feedback_pub = self.create_publisher(
            String, '/controller/feedback', 10
        )

        # ── Timer ─────────────────────────────────────────────────────────────
        self.create_timer(1.0 / rate, self._publish_feedback)

        self.get_logger().info(
            f'Controller Feedback Node başladı — {rate}Hz'
        )

    # ── Callbacks ─────────────────────────────────────────────────────────────

    def _odometry_cb(self, msg: Float32):
        """Araç hızı — odometri encoder'dan."""
        self._actual_speed = float(msg.data)

    def _state_cb(self, msg: Twist):
        """
        Kontrol durumu — control_node'dan geliyor.
        Twist: linear.x=CTE, angular.z=heading_error
        """
        self._cte           = msg.linear.x
        self._heading_error = msg.angular.z

    def _can_command_cb(self, msg: String):
        """Son CAN komutundan direksiyon byte'ını al."""
        try:
            data = json.loads(msg.data)
            self._actual_steer_byte = data.get('steer_byte', 0x81)
        except (json.JSONDecodeError, KeyError):
            pass

    def _emergency_cb(self, msg: Bool):
        self._emergency       = msg.data
        self._full_brake_active = msg.data

    def _brake_cb(self, msg: Bool):
        self._brake_active = msg.data

    # ── Ana Publish Fonksiyonu ────────────────────────────────────────────────

    def _publish_feedback(self):
        """
        20Hz'de /controller/feedback yayınla.
        Sözleşme v1.2 Bölüm 12 — ControllerFeedback.msg
        """

        # Direksiyon byte'ını dereceye çevir
        # (0x81 merkez, 0xFF tam sol, 0x00 tam sağ)
        steer_deg = self._steer_byte_to_deg(self._actual_steer_byte)

        # CTE eşik kontrolü — planner'a bilgi ver
        if abs(self._cte) > 0.5:
            self.get_logger().warn(
                f'CTE yüksek: {self._cte:.3f}m > 0.5m — planner hız düşürecek'
            )
        elif abs(self._cte) > 0.3:
            self.get_logger().info(
                f'CTE uyarı: {self._cte:.3f}m > 0.3m — planner trajectory yenileyebilir'
            )

        # Feedback mesajı — ControllerFeedback.msg formatı
        feedback = {
            'stamp':               time.time(),
            'actual_speed':        round(self._actual_speed, 3),
            'actual_steering_deg': round(steer_deg, 2),
            'cross_track_error':   round(self._cte, 4),
            'heading_error':       round(self._heading_error, 4),
            'brake_active':        self._brake_active,
            'full_brake_active':   self._full_brake_active,
            'valid_until_ms':      FEEDBACK_VALID_MS,
        }

        self._feedback_pub.publish(String(data=json.dumps(feedback)))

    # ── Yardımcı Fonksiyonlar ─────────────────────────────────────────────────

    def _steer_byte_to_deg(self, steer_byte: int) -> float:
        """
        CAN direksiyon byte'ını dereceye çevir.
        0x81 merkez → 0°
        0xFF tam sol → +max_steer_deg
        0x00 tam sağ → -max_steer_deg
        """
        # Normalize: [0x00, 0xFF] → [-1, +1] (merkez=0x81)
        center = self._steer_center
        if steer_byte >= center:
            norm = (steer_byte - center) / (0xFF - center)
        else:
            norm = -(center - steer_byte) / center

        norm = max(-1.0, min(1.0, norm))
        return norm * self._max_steer_deg


# ─── Entry Point ──────────────────────────────────────────────────────────────
def main(args=None):
    rclpy.init(args=args)
    node = ControllerFeedbackNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
