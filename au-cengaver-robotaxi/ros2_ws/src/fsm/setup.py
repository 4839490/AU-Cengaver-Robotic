from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'fsm'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # ROS2'nin bu paketi tanıması için zorunlu
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Launch dosyaları
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Murat Üsame Üstün',
    maintainer_email='murat@cengaver',
    description='AU Cengaver FSM — durum makinesi node',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fsm_node = fsm.fsm_node:main',
        ],
    },
)
