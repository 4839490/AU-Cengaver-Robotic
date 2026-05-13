"""
Controller Feedback Node
========================
/controller/feedback topic'ini 20Hz'de yayınlar.

Publish:
  /controller/feedback  20Hz  planning_msgs/ControllerFeedback

Subscribe:
  /odometry/speed           20Hz  std_msgs/Float32
  /controller/state         20Hz  geometry_msgs/Twist (linear.x=CTE, angular.z=heading_error)
  /can_last_command         10Hz  std_msgs/String
  /emergency                olay  std_msgs/Bool
  /controller/brake_active  olay  std_msgs/Bool

ControllerFeedback.msg alanları (planning_msgs):
  std_msgs/Header header
  float32 actual_speed
  float32 actual_steering_deg
  float32 cross_track_error
  float32 heading_error
  bool    brake_active
  bool    full_brake_active
  uint32  age_ms           ← DÜZELTİLDİ: eski kodda eksikti
  uint32  valid_until_ms
"""

import json
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32, Bool
from geometry_msgs.msg import Twist

from planning_msgs.msg import ControllerFeedback   # DÜZELTİLDİ: String yerine gerçek MSG

FEEDBACK_VALID_MS = 200
FEEDBACK_RATE_HZ  = 20


class ControllerFeedbackNode(Node):

    def __init__(self):
        super().__init__('controller_feedback_node')

        self.declare_parameter('feedback_rate_hz',    FEEDBACK_RATE_HZ)
        self.declare_parameter('steer_center_byte',   0x81)
        self.declare_parameter('max_steer_angle_deg', 32.5)

        rate                = self.get_parameter('feedback_rate_hz').value
        self._steer_center  = self.get_parameter('steer_center_byte').value
        self._max_steer_deg = self.get_parameter('max_steer_angle_deg').value

        self._actual_speed:      float = 0.0
        self._actual_steer_byte: int   = 0x81
        self._cte:               float = 0.0
        self._heading_error:     float = 0.0
        self._brake_active:      bool  = False
        self._full_brake_active: bool  = False

        self.create_subscription(Float32, '/odometry/speed',          self._odometry_cb,    10)
        self.create_subscription(Twist,   '/controller/state',        self._state_cb,       10)
        self.create_subscription(String,  '/can_last_command',        self._can_command_cb, 10)
        self.create_subscription(Bool,    '/emergency',               self._emergency_cb,   10)
        self.create_subscription(Bool,    '/controller/brake_active', self._brake_cb,       10)

        # DÜZELTİLDİ: String → ControllerFeedback
        self._feedback_pub = self.create_publisher(ControllerFeedback, '/controller/feedback', 10)

        self.create_timer(1.0 / rate, self._publish_feedback)
        self.get_logger().info(f'Controller Feedback Node başladı — {rate}Hz')

    def _odometry_cb(self, msg: Float32):
        self._actual_speed = float(msg.data)

    def _state_cb(self, msg: Twist):
        self._cte           = msg.linear.x
        self._heading_error = msg.angular.z

    def _can_command_cb(self, msg: String):
        try:
            data = json.loads(msg.data)
            self._actual_steer_byte = data.get('steer_byte', 0x81)
        except (json.JSONDecodeError, KeyError):
            pass

    def _emergency_cb(self, msg: Bool):
        self._full_brake_active = msg.data

    def _brake_cb(self, msg: Bool):
        self._brake_active = msg.data

    def _publish_feedback(self):
        steer_deg = self._steer_byte_to_deg(self._actual_steer_byte)

        if abs(self._cte) > 0.5:
            self.get_logger().warn(f'CTE yüksek: {self._cte:.3f}m > 0.5m')
        elif abs(self._cte) > 0.3:
            self.get_logger().info(f'CTE uyarı: {self._cte:.3f}m > 0.3m')

        msg = ControllerFeedback()
        msg.header.stamp        = self.get_clock().now().to_msg()
        msg.actual_speed        = float(self._actual_speed)
        msg.actual_steering_deg = float(steer_deg)
        msg.cross_track_error   = float(self._cte)
        msg.heading_error       = float(self._heading_error)
        msg.brake_active        = self._brake_active
        msg.full_brake_active   = self._full_brake_active
        msg.age_ms              = 0          # DÜZELTİLDİ: MSG'de var, eklendi
        msg.valid_until_ms      = FEEDBACK_VALID_MS

        self._feedback_pub.publish(msg)

    def _steer_byte_to_deg(self, steer_byte: int) -> float:
        """CAN byte → derece. 0x81=merkez=0°"""
        center = self._steer_center
        if steer_byte >= center:
            norm = (steer_byte - center) / (0xFF - center)
        else:
            norm = -(center - steer_byte) / center
        return max(-1.0, min(1.0, norm)) * self._max_steer_deg


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
