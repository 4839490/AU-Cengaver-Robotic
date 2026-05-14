#!/usr/bin/env python3

import os

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    planning_share = get_package_share_directory('planning')
    mission_file = os.path.join(
        planning_share,
        'missions',
        'test_mission.geojson',
    )

    return LaunchDescription([

        Node(
            package='fake_publishers',
            executable='gazebo_odom_localization_bridge',
            name='gazebo_odom_localization_bridge',
            output='screen',
            parameters=[{
                'odom_topic': '/odom',
                'publish_map_origin': True,
                'lat_ref': 40.789949,
                'lon_ref': 29.508726,
                'alt_ref': 85.2,
                'yaw_ref': 0.0,
            }],
        ),

        Node(
            package='fake_publishers',
            executable='fake_perception',
            name='fake_perception',
            output='screen',
            parameters=[{
                'lane_width': 3.5,
                'light_state': 3,
            }],
        ),

        Node(
            package='fsm',
            executable='fsm_node',
            name='fsm_node',
            output='screen',
            parameters=[{
                'auto_start_mission': True,
                'sim_total_waypoints': 3,
            }],
        ),

        Node(
            package='planning',
            executable='planner_node',
            name='planner_node',
            output='screen',
            parameters=[{
                'mission_file': mission_file,
                'publish_hz': 20.0,
                'status_hz': 10.0,
                'context_hz': 10.0,
                'valid_until_ms': 500,
            }],
        ),

        Node(
            package='fake_publishers',
            executable='trajectory_to_cmdvel',
            name='trajectory_to_cmdvel',
            output='screen',
            parameters=[{
                'max_speed': 1.5,
                'max_angular_z': 1.0,
                'k_stanley': 0.8,
                'lookahead_points': 4,
                'stale_timeout_ms': 700,
            }],
        ),
    ])
