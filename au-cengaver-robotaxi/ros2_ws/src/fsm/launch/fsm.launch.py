"""
AU Cengaver Robotics — FSM Launch Dosyası
TEKNOFEST 2026

Kullanım:
  ros2 launch fsm fsm.launch.py
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        Node(
            package='fsm',
            executable='fsm_node',
            name='fsm_node',
            output='screen',
            parameters=[
                # İleride buraya YAML parametre dosyası eklenebilir
                # {'param_file': '/path/to/fsm_params.yaml'}
            ],
            remappings=[
                # Topic isimleri değişirse buradan düzenlenir
                # Şimdilik sözleşmedeki isimler kullanılıyor
            ]
        ),

    ])
