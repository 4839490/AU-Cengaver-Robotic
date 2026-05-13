#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
planning.launch.py

Planner node'unu başlatır.
Sözleşme: Planner ↔ Controller Contract v1.3
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    # ─── Launch Argümanları ────────────────────────────────────────────────
    mission_file_arg = DeclareLaunchArgument(
        'mission_file',
        default_value='',
        description='GeoJSON mission dosyası yolu'
    )

    sim_arg = DeclareLaunchArgument(
        'sim',
        default_value='true',
        description='Simülasyon modu'
    )

    publish_hz_arg = DeclareLaunchArgument(
        'publish_hz',
        default_value='20.0',
        description='Trajectory yayın frekansı (Hz)'
    )

    # ─── Planner Node ──────────────────────────────────────────────────────
    planner_node = Node(
        package='planning',
        executable='planner_node',
        name='planner_node',
        output='screen',
        parameters=[{
            'mission_file':    LaunchConfiguration('mission_file'),
            'publish_hz':      LaunchConfiguration('publish_hz'),
            'status_hz':       10.0,
            'context_hz':      10.0,
            'valid_until_ms':  500,
        }]
    )

    return LaunchDescription([
        mission_file_arg,
        sim_arg,
        publish_hz_arg,
        planner_node,
    ])