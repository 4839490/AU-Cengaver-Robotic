#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
planning.launch.py

Planner node'unu başlatır.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    mission_file_arg = DeclareLaunchArgument(
        'mission_file',
        default_value='',
        description='GeoJSON mission dosyası yolu',
    )

    sim_arg = DeclareLaunchArgument(
        'sim',
        default_value='true',
        description='Simülasyon modu',
    )

    publish_hz_arg = DeclareLaunchArgument(
        'publish_hz',
        default_value='20.0',
        description='Trajectory yayın frekansı, Hz',
    )

    status_hz_arg = DeclareLaunchArgument(
        'status_hz',
        default_value='10.0',
        description='PlanningStatus yayın frekansı, Hz',
    )

    context_hz_arg = DeclareLaunchArgument(
        'context_hz',
        default_value='10.0',
        description='ActiveRouteContext yayın frekansı, Hz',
    )

    valid_until_ms_arg = DeclareLaunchArgument(
        'valid_until_ms',
        default_value='500',
        description='Planning mesajları geçerlilik süresi, ms',
    )

    planner_node = Node(
        package='planning',
        executable='planner_node',
        name='planner_node',
        output='screen',
        parameters=[{
            'mission_file': LaunchConfiguration('mission_file'),

            'sim': ParameterValue(
                LaunchConfiguration('sim'),
                value_type=bool,
            ),

            'publish_hz': ParameterValue(
                LaunchConfiguration('publish_hz'),
                value_type=float,
            ),

            'status_hz': ParameterValue(
                LaunchConfiguration('status_hz'),
                value_type=float,
            ),

            'context_hz': ParameterValue(
                LaunchConfiguration('context_hz'),
                value_type=float,
            ),

            'valid_until_ms': ParameterValue(
                LaunchConfiguration('valid_until_ms'),
                value_type=int,
            ),
        }],
    )

    return LaunchDescription([
        mission_file_arg,
        sim_arg,
        publish_hz_arg,
        status_hz_arg,
        context_hz_arg,
        valid_until_ms_arg,
        planner_node,
    ])
