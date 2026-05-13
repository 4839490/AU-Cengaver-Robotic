from setuptools import setup

package_name = 'perception'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='AU Cengaver Robotics',
    maintainer_email='yusufaydinau@gmail.com',
    description=(
        'Perception runtime package for AU Cengaver Robotics TEKNOFEST 2026 Robotaksi: '
        'Sprint 1–3 MVP perception nodes, ROS-free helpers, and fake publishers. '
        'Publishes evidence only; no driving decisions or control topics.'
    ),
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Per-node skeletons (Gate B / Step 4 split).
            'lane_node = perception.lane_node:main',
            'traffic_light_node = perception.traffic_light_node:main',
            'traffic_sign_node = perception.traffic_sign_node:main',
            'lidar_obstacle_node = perception.lidar_obstacle_node:main',
            'stop_target_node = perception.stop_target_node:main',
            'perception_diagnostics_node = perception.perception_diagnostics_node:main',
            'junction_node = perception.junction_node:main',
            # Backward-compatibility wrapper that spins every per-node skeleton
            # in a single process (kept so existing tooling/bag scripts that
            # invoke `dummy_perception_publishers` still work).
            'dummy_perception_publishers = perception.dummy_publishers:main',
            # Sprint 1 / S1-2 — fake image publisher for testing without real ZED2.
            'fake_image_pub = perception.fake_image_pub:main',
            # Sprint 2 / S2-A2 — fake lane scene publisher for lane_node testing.
            'fake_lane_image_pub = perception.fake_lane_image_pub:main',
            # Sprint 2 / S2-B2 — fake VLP-16-style PointCloud2 publisher for lidar testing.
            'fake_pointcloud_pub = perception.fake_pointcloud_pub:main',
            # Sprint 3 / S3-S2 — fake TrafficLightState publisher for stop_target_node smoke.
            'fake_traffic_light_state_pub = perception.fake_traffic_light_state_pub:main',
            # Sprint 3 / S3-R1 — fake ActiveRouteContext publisher for Track R smoke.
            'fake_route_context_pub = perception.fake_route_context_pub:main',
        ],
    },
)
