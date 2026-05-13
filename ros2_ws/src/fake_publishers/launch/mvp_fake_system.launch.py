#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
mvp_fake_system.launch.py

Tüm sistemi fake publisher'larla başlatır:
  fake_localization → /localization/*
  fake_perception   → /perception/*
  fake_controller_feedback → /controller/feedback
  fsm_node          → /fsm/*
  planner_node      → /planning/*
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        # ── Fake Localization ─────────────────────────────────
        Node(
            package='fake_publishers',
            executable='fake_localization',
            name='fake_localization',
            output='screen',
            parameters=[{
                'speed':    2.0,
                'lat_ref':  40.789949,
                'lon_ref':  29.508726,
            }]
        ),

        # ── Fake Perception ───────────────────────────────────
        Node(
            package='fake_publishers',
            executable='fake_perception',
            name='fake_perception',
            output='screen',
            parameters=[{
                'lane_width':  3.5,
                'light_state': 3,   # GREEN
            }]
        ),

        # ── Fake Controller Feedback ──────────────────────────
        Node(
            package='fake_publishers',
            executable='fake_controller_feedback',
            name='fake_controller_feedback',
            output='screen',
            parameters=[{
                'speed': 2.0,
            }]
        ),

        # ── FSM Node ──────────────────────────────────────────
        Node(
            package='fsm',
            executable='fsm_node',
            name='fsm_node',
            output='screen',
        ),

        # ── Planner Node ──────────────────────────────────────
        Node(
            package='planning',
            executable='planner_node',
            name='planner_node',
            output='screen',
            parameters=[{
                'mission_file': '/home/usame/AU-Cengaver-Robotic/ros2_ws/src/planning/missions/test_mission.geojson',
                'publish_hz':   20.0,
            }]
        ),

    ])
