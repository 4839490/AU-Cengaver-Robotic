"""
controller.launch.py
====================
AU Cengaver Robotics — TEKNOFEST 2026
"""

# DÜZELTİLDİ: ament_python → ament_index_python (launch çalışmıyordu)
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    pkg_name = 'cengaver_controller'

    vehicle_params_arg = DeclareLaunchArgument(
        name          = 'vehicle_params',
        default_value = PathJoinSubstitution([
            FindPackageShare(pkg_name), 'config', 'vehicle_params.yaml'
        ]),
        description   = 'vehicle_params.yaml dosyasının tam yolu'
    )
    log_level_arg = DeclareLaunchArgument(
        name='log_level', default_value='info',
        description='Log seviyesi: debug, info, warn, error'
    )
    simulation_arg = DeclareLaunchArgument(
        name='simulation', default_value='false',
        description='Simülasyon modu — true: CAN simüle edilir'
    )
    use_pure_pursuit_arg = DeclareLaunchArgument(
        name='use_pure_pursuit', default_value='false',
        description='true: Pure Pursuit, false: Stanley (varsayılan)'
    )
    namespace_arg = DeclareLaunchArgument(
        name='namespace', default_value='',
        description='Node namespace (opsiyonel)'
    )

    vehicle_params   = LaunchConfiguration('vehicle_params')
    log_level        = LaunchConfiguration('log_level')
    simulation       = LaunchConfiguration('simulation')
    use_pure_pursuit = LaunchConfiguration('use_pure_pursuit')
    namespace        = LaunchConfiguration('namespace')

    controller_node = Node(
        package     = pkg_name,
        executable  = 'controller_node',
        name        = 'controller_node',
        namespace   = namespace,
        output      = 'screen',
        emulate_tty = True,
        parameters  = [
            vehicle_params,
            {'simulation_mode': simulation, 'use_pure_pursuit': use_pure_pursuit}
        ],
        arguments = ['--ros-args', '--log-level', log_level],
    )

    feedback_node = Node(
        package     = pkg_name,
        executable  = 'controller_feedback_node',
        name        = 'controller_feedback_node',
        namespace   = namespace,
        output      = 'screen',
        emulate_tty = True,
        parameters  = [vehicle_params],
        arguments   = ['--ros-args', '--log-level', log_level],
    )

    start_log = LogInfo(msg=[
        '\n', '=' * 60, '\n',
        '  AU Cengaver Robotics — Controller Launch\n',
        '  Sözleşme: Planner↔Controller v1.2 | CAN v1.0\n',
        '  vehicle_params: ', vehicle_params, '\n',
        '  simulation: ', simulation, '\n',
        '  log_level: ', log_level, '\n',
        '=' * 60,
    ])

    return LaunchDescription([
        vehicle_params_arg, log_level_arg, simulation_arg,
        use_pure_pursuit_arg, namespace_arg,
        start_log,
        controller_node, feedback_node,
    ])
