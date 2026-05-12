from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'cengaver_controller'

setup(
    name    = package_name,
    version = '1.0.0',

    # Paket içindeki tüm Python modüllerini bul
    packages = find_packages(exclude=['test']),

    # Veri dosyaları — config ve launch klasörleri
    data_files = [
        # ROS2 ament index kaydı
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        # package.xml
        ('share/' + package_name, ['package.xml']),

        # Launch dosyaları
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),

        # Config dosyaları (vehicle_params.yaml)
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')),
    ],

    # Python bağımlılıkları
    install_requires = [
        'setuptools',
        'pyyaml',        # vehicle_params.yaml okumak için
    ],

    # python-can opsiyonel — gerçek araca bağlanınca gerekli
    extras_require = {
        'can': ['python-can'],
    },

    zip_safe = True,

    # Paket meta bilgileri
    maintainer       = 'Muhammed Durmaz',
    maintainer_email = 'muhammed.durmaz@ankara.edu.tr',
    description      = 'AU Cengaver Robotics Controller Paketi — TEKNOFEST 2026',
    license          = 'MIT',

    # Test
    tests_require = ['pytest'],

    # ROS2 entry points — node'ları çalıştırmak için
    # ros2 run cengaver_controller controller_node
    entry_points = {
        'console_scripts': [
            # Ana kontrol node'u
            'controller_node = cengaver_controller.controller_node:main',

            # Feedback node'u
            'controller_feedback_node = cengaver_controller.controller_feedback_node:main',
        ],
    },
)
