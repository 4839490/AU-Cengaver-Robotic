#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
localization.launch.py

Tüm lokalizasyon node'larını başlatır.
Sözleşme: Localization ↔ Planner Contract v1.2
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    sim_arg = DeclareLaunchArgument(
        'sim',
        default_value='true',
        description='Simülasyon modu — true: sim, false: gerçek araç'
    )

    map_origin_source_arg = DeclareLaunchArgument(
        'map_origin_source',
        default_value='config_file',
        description='Map origin kaynağı: config_file veya gps_fix'
    )

    lat_arg = DeclareLaunchArgument(
        'lat_ref',
        default_value='40.789949',
        description='Map origin referans enlemi'
    )

    lon_arg = DeclareLaunchArgument(
        'lon_ref',
        default_value='29.508726',
        description='Map origin referans boylamı'
    )

    alt_arg = DeclareLaunchArgument(
        'alt_ref',
        default_value='85.2',
        description='Map origin referans yüksekliği'
    )

    yaw_arg = DeclareLaunchArgument(
        'yaw_ref',
        default_value='0.0',
        description='Map origin referans yaw değeri, rad'
    )

    imu_topic_arg = DeclareLaunchArgument(
        'imu_topic',
        default_value='/imu/data',
        description='IMU topic'
    )

    joint_states_topic_arg = DeclareLaunchArgument(
        'joint_states_topic',
        default_value='/joint_states',
        description='JointState / encoder topic'
    )

    gps_topic_arg = DeclareLaunchArgument(
        'gps_topic',
        default_value='/fix',
        description='GPS NavSatFix topic'
    )

    map_origin_node = Node(
        package='localization',
        executable='map_origin_node',
        name='map_origin_node',
        output='screen',
        parameters=[{
            'source': LaunchConfiguration('map_origin_source'),
            'lat_ref': ParameterValue(LaunchConfiguration('lat_ref'), value_type=float),
            'lon_ref': ParameterValue(LaunchConfiguration('lon_ref'), value_type=float),
            'alt_ref': ParameterValue(LaunchConfiguration('alt_ref'), value_type=float),
            'yaw_ref': ParameterValue(LaunchConfiguration('yaw_ref'), value_type=float),
            'publish_hz': 1.0,
            'gps_topic': LaunchConfiguration('gps_topic'),
        }]
    )

    raw_gps_node = Node(
        package='localization',
        executable='raw_gps_node',
        name='raw_gps_node',
        output='screen',
        parameters=[{
            'gps_topic': LaunchConfiguration('gps_topic'),
            'gps_frame': 'gps_frame',
            'valid_until_ms': 200,
        }]
    )

    local_ekf_node = Node(
        package='localization',
        executable='local_ekf_node',
        name='local_ekf_node',
        output='screen',
        parameters=[{
            'sim': ParameterValue(LaunchConfiguration('sim'), value_type=bool),
            'publish_hz': 50.0,
            'imu_topic': LaunchConfiguration('imu_topic'),
            'joint_states_topic': LaunchConfiguration('joint_states_topic'),
            'wheel_radius': 0.3,
            'wheelbase': 2.40,
            'valid_until_ms': 200,
        }]
    )

    global_localization_node = Node(
        package='localization',
        executable='global_localization_node',
        name='global_localization_node',
        output='screen',
        parameters=[{
            'sim': ParameterValue(LaunchConfiguration('sim'), value_type=bool),
            'publish_hz': 30.0,
            'gps_topic': LaunchConfiguration('gps_topic'),
            'valid_until_ms': 300,
            'ndt_healthy_threshold': 0.5,
            'confidence_degraded_threshold': 0.5,
        }]
    )

    localization_diagnostics_node = Node(
        package='localization',
        executable='localization_diagnostics_node',
        name='localization_diagnostics_node',
        output='screen',
        parameters=[{
            'publish_hz': 1.0,
            'valid_until_ms': 2000,
            'odom_timeout_s': 0.2,
            'status_timeout_s': 0.5,
            'ndt_required': False,
        }]
    )

    return LaunchDescription([
        sim_arg,
        map_origin_source_arg,
        lat_arg,
        lon_arg,
        alt_arg,
        yaw_arg,
        imu_topic_arg,
        joint_states_topic_arg,
        gps_topic_arg,

        map_origin_node,
        raw_gps_node,
        local_ekf_node,
        global_localization_node,
        localization_diagnostics_node,
    ])
