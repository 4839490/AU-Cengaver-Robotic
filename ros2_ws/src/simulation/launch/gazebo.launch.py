#!/usr/bin/env python3
import os
import xacro
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg_sim    = get_package_share_directory('simulation')
    xacro_file = os.path.join(pkg_sim, 'urdf', 'bee1.urdf.xacro')
    world_file = os.path.join(pkg_sim, 'worlds', 'simple_test.world')

    robot_desc = xacro.process_file(xacro_file).toxml()

    # Gazebo
    gazebo = ExecuteProcess(
        cmd=['gzserver', '--verbose', world_file,
             '-s', 'libgazebo_ros_init.so',
             '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    # Robot state publisher
    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    )

    # Spawn — 5 saniye bekle
    spawn = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='gazebo_ros',
                executable='spawn_entity.py',
                name='spawn_bee1',
                output='screen',
                arguments=[
                    '-topic', 'robot_description',
                    '-entity', 'bee1',
                    '-x', '0.0',
                    '-y', '0.0',
                    '-z', '0.3',
                ]
            )
        ]
    )

    return LaunchDescription([gazebo, rsp, spawn])
