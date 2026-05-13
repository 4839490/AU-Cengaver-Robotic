import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/usame/AU-Cengaver-Robotic/ros2_ws/install/localization'
