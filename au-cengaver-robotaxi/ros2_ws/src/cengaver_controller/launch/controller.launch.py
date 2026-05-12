"""
controller.launch.py
====================
AU Cengaver Robotics — TEKNOFEST 2026
Yol Haritası v1.1 — Adım 9: Controller Temel

Bu launch dosyası controller paketindeki tüm node'ları başlatır:
  1. controller_node          → ana kontrol döngüsü
  2. controller_feedback_node → /controller/feedback yayıncısı

Tüm parametreler vehicle_params.yaml'dan okunur.
Hiçbir parametre bu dosyada sabit yazılmaz.

Kullanım:
  ros2 launch cengaver_controller controller.launch.py

  # Özel parametre dosyasıyla:
  ros2 launch cengaver_controller controller.launch.py \
    vehicle_params:=/path/to/custom_params.yaml

  # Debug modunda:
  ros2 launch cengaver_controller controller.launch.py \
    log_level:=debug

  # Simülasyon modunda (CAN gerçek değil):
  ros2 launch cengaver_controller controller.launch.py \
    simulation:=true
"""

import os
from ament_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    LogInfo,
    OpaqueFunction,
)
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import (
    LaunchConfiguration,
    PathJoinSubstitution,
    PythonExpression,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    """Launch dosyası ana fonksiyonu."""

    # ── Paket yolu ────────────────────────────────────────────────────────────
    pkg_name = 'cengaver_controller'

    # ── Launch argümanları ────────────────────────────────────────────────────
    # Her argüman komut satırından override edilebilir

    vehicle_params_arg = DeclareLaunchArgument(
        name        = 'vehicle_params',
        default_value = PathJoinSubstitution([
            FindPackageShare(pkg_name), 'config', 'vehicle_params.yaml'
        ]),
        description = 'vehicle_params.yaml dosyasının tam yolu'
    )

    log_level_arg = DeclareLaunchArgument(
        name          = 'log_level',
        default_value = 'info',
        description   = 'Log seviyesi: debug, info, warn, error'
    )

    simulation_arg = DeclareLaunchArgument(
        name          = 'simulation',
        default_value = 'false',
        description   = 'Simülasyon modu — true: CAN simüle edilir'
    )

    use_pure_pursuit_arg = DeclareLaunchArgument(
        name          = 'use_pure_pursuit',
        default_value = 'false',
        description   = 'true: Pure Pursuit, false: Stanley (varsayılan)'
    )

    namespace_arg = DeclareLaunchArgument(
        name          = 'namespace',
        default_value = '',
        description   = 'Node namespace (opsiyonel)'
    )

    # ── Launch configuration değişkenleri ─────────────────────────────────────
    vehicle_params  = LaunchConfiguration('vehicle_params')
    log_level       = LaunchConfiguration('log_level')
    simulation      = LaunchConfiguration('simulation')
    use_pure_pursuit = LaunchConfiguration('use_pure_pursuit')
    namespace       = LaunchConfiguration('namespace')

    # ── Controller Node ───────────────────────────────────────────────────────
    controller_node = Node(
        package    = pkg_name,
        executable = 'controller_node',
        name       = 'controller_node',
        namespace  = namespace,
        output     = 'screen',
        emulate_tty = True,

        # Parametreler vehicle_params.yaml'dan okunur
        parameters = [
            vehicle_params,
            {
                # Runtime override'lar — YAML'dan alınır ama
                # launch argümanıyla değiştirilebilir
                'simulation_mode': simulation,
                'use_pure_pursuit': use_pure_pursuit,
            }
        ],

        # Remapping — topic isimlerini özelleştirmek için
        remappings = [
            # Varsayılan topic isimleri — sözleşme v1.2
            # ('/planning/trajectory', '/planning/trajectory'),
            # ('/planning/target_speed', '/planning/target_speed'),
            # ('/planning/status', '/planning/status'),
            # ('/controller/feedback', '/controller/feedback'),
        ],

        # Log seviyesi
        arguments  = ['--ros-args', '--log-level', log_level],
    )

    # ── Controller Feedback Node ──────────────────────────────────────────────
    feedback_node = Node(
        package    = pkg_name,
        executable = 'controller_feedback_node',
        name       = 'controller_feedback_node',
        namespace  = namespace,
        output     = 'screen',
        emulate_tty = True,

        parameters = [
            vehicle_params,
        ],

        arguments  = ['--ros-args', '--log-level', log_level],
    )

    # ── Başlangıç Logu ────────────────────────────────────────────────────────
    start_log = LogInfo(
        msg = [
            '\n',
            '=' * 60, '\n',
            '  AU Cengaver Robotics — Controller Launch\n',
            '  Sözleşme: Planner↔Controller v1.2 | CAN v1.0\n',
            '  vehicle_params: ', vehicle_params, '\n',
            '  simulation: ', simulation, '\n',
            '  log_level: ', log_level, '\n',
            '=' * 60,
        ]
    )

    # ── LaunchDescription ─────────────────────────────────────────────────────
    return LaunchDescription([
        # Argümanlar
        vehicle_params_arg,
        log_level_arg,
        simulation_arg,
        use_pure_pursuit_arg,
        namespace_arg,

        # Başlangıç logu
        start_log,

        # Node'lar
        controller_node,
        feedback_node,
    ])
