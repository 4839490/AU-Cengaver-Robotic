from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'localization'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py'),
        ),
        (
            os.path.join('share', package_name, 'config'),
            glob('config/*.yaml'),
        ),
    ],
    install_requires=[
        'setuptools',
        'numpy',
    ],
    zip_safe=True,
    maintainer='Ahmet Salih Uluşık',
    maintainer_email='cengaver@example.com',
    description='AU Cengaver Robotics localization package',
    license='MIT',
    entry_points={
        'console_scripts': [
            'local_ekf_node = localization.local_ekf_node:main',
            'global_localization_node = localization.global_localization_node:main',
            'map_origin_node = localization.map_origin_node:main',
            'raw_gps_node = localization.raw_gps_node:main',
            'localization_diagnostics_node = localization.localization_diagnostics_node:main',
        ],
    },
)
