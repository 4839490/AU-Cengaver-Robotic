from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'fake_publishers'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='AU Cengaver',
    maintainer_email='cengaver@example.com',
    description='AU Cengaver fake publishers',
    license='MIT',
    entry_points={
        'console_scripts': [
            'fake_localization = fake_publishers.fake_localization:main',
            'fake_perception = fake_publishers.fake_perception:main',
            'fake_controller_feedback = fake_publishers.fake_controller_feedback:main',
            'trajectory_to_cmdvel = fake_publishers.trajectory_to_cmdvel:main',
            'lane_follower = fake_publishers.lane_follower:main',
        ],
    },
)
