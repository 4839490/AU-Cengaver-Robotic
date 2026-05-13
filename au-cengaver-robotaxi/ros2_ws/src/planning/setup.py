from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'planning'

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
        (os.path.join('share', package_name, 'missions'),
            glob('missions/*.geojson')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ahmet Salih Uluşık',
    maintainer_email='cengaver@example.com',
    description='AU Cengaver Robotics — Planning paketi',
    license='MIT',
    entry_points={
        'console_scripts': [
            'planner_node = planning.planner_node:main',
        ],
    },
)