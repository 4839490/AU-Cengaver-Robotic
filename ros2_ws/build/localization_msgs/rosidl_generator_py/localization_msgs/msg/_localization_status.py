# generated from rosidl_generator_py/resource/_idl.py.em
# with input from localization_msgs:msg/LocalizationStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_LocalizationStatus(type):
    """Metaclass of message 'LocalizationStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'OK': 0,
        'GNSS_LOST': 1,
        'IMU_ONLY': 2,
        'LIDAR_ONLY': 3,
        'DEGRADED': 4,
        'RELOCALIZING': 5,
        'LOST': 6,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('localization_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'localization_msgs.msg.LocalizationStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__localization_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__localization_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__localization_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__localization_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__localization_status

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'OK': cls.__constants['OK'],
            'GNSS_LOST': cls.__constants['GNSS_LOST'],
            'IMU_ONLY': cls.__constants['IMU_ONLY'],
            'LIDAR_ONLY': cls.__constants['LIDAR_ONLY'],
            'DEGRADED': cls.__constants['DEGRADED'],
            'RELOCALIZING': cls.__constants['RELOCALIZING'],
            'LOST': cls.__constants['LOST'],
        }

    @property
    def OK(self):
        """Message constant 'OK'."""
        return Metaclass_LocalizationStatus.__constants['OK']

    @property
    def GNSS_LOST(self):
        """Message constant 'GNSS_LOST'."""
        return Metaclass_LocalizationStatus.__constants['GNSS_LOST']

    @property
    def IMU_ONLY(self):
        """Message constant 'IMU_ONLY'."""
        return Metaclass_LocalizationStatus.__constants['IMU_ONLY']

    @property
    def LIDAR_ONLY(self):
        """Message constant 'LIDAR_ONLY'."""
        return Metaclass_LocalizationStatus.__constants['LIDAR_ONLY']

    @property
    def DEGRADED(self):
        """Message constant 'DEGRADED'."""
        return Metaclass_LocalizationStatus.__constants['DEGRADED']

    @property
    def RELOCALIZING(self):
        """Message constant 'RELOCALIZING'."""
        return Metaclass_LocalizationStatus.__constants['RELOCALIZING']

    @property
    def LOST(self):
        """Message constant 'LOST'."""
        return Metaclass_LocalizationStatus.__constants['LOST']


class LocalizationStatus(metaclass=Metaclass_LocalizationStatus):
    """
    Message class 'LocalizationStatus'.

    Constants:
      OK
      GNSS_LOST
      IMU_ONLY
      LIDAR_ONLY
      DEGRADED
      RELOCALIZING
      LOST
    """

    __slots__ = [
        '_header',
        '_age_ms',
        '_valid_until_ms',
        '_status',
        '_localization_confidence',
        '_position_covariance',
        '_heading_covariance',
        '_ndt_healthy',
        '_ndt_quality',
        '_map_odom_stable',
        '_map_odom_drift',
        '_gps_available',
        '_imu_available',
        '_lidar_available',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'status': 'uint8',
        'localization_confidence': 'double',
        'position_covariance': 'double',
        'heading_covariance': 'double',
        'ndt_healthy': 'boolean',
        'ndt_quality': 'double',
        'map_odom_stable': 'boolean',
        'map_odom_drift': 'double',
        'gps_available': 'boolean',
        'imu_available': 'boolean',
        'lidar_available': 'boolean',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.age_ms = kwargs.get('age_ms', int())
        self.valid_until_ms = kwargs.get('valid_until_ms', int())
        self.status = kwargs.get('status', int())
        self.localization_confidence = kwargs.get('localization_confidence', float())
        self.position_covariance = kwargs.get('position_covariance', float())
        self.heading_covariance = kwargs.get('heading_covariance', float())
        self.ndt_healthy = kwargs.get('ndt_healthy', bool())
        self.ndt_quality = kwargs.get('ndt_quality', float())
        self.map_odom_stable = kwargs.get('map_odom_stable', bool())
        self.map_odom_drift = kwargs.get('map_odom_drift', float())
        self.gps_available = kwargs.get('gps_available', bool())
        self.imu_available = kwargs.get('imu_available', bool())
        self.lidar_available = kwargs.get('lidar_available', bool())
        self.warning_flags = kwargs.get('warning_flags', [])

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.age_ms != other.age_ms:
            return False
        if self.valid_until_ms != other.valid_until_ms:
            return False
        if self.status != other.status:
            return False
        if self.localization_confidence != other.localization_confidence:
            return False
        if self.position_covariance != other.position_covariance:
            return False
        if self.heading_covariance != other.heading_covariance:
            return False
        if self.ndt_healthy != other.ndt_healthy:
            return False
        if self.ndt_quality != other.ndt_quality:
            return False
        if self.map_odom_stable != other.map_odom_stable:
            return False
        if self.map_odom_drift != other.map_odom_drift:
            return False
        if self.gps_available != other.gps_available:
            return False
        if self.imu_available != other.imu_available:
            return False
        if self.lidar_available != other.lidar_available:
            return False
        if self.warning_flags != other.warning_flags:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @property
    def age_ms(self):
        """Message field 'age_ms'."""
        return self._age_ms

    @age_ms.setter
    def age_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'age_ms' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'age_ms' field must be an unsigned integer in [0, 4294967295]"
        self._age_ms = value

    @property
    def valid_until_ms(self):
        """Message field 'valid_until_ms'."""
        return self._valid_until_ms

    @valid_until_ms.setter
    def valid_until_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'valid_until_ms' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'valid_until_ms' field must be an unsigned integer in [0, 4294967295]"
        self._valid_until_ms = value

    @property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'status' field must be an unsigned integer in [0, 255]"
        self._status = value

    @property
    def localization_confidence(self):
        """Message field 'localization_confidence'."""
        return self._localization_confidence

    @localization_confidence.setter
    def localization_confidence(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'localization_confidence' field must be of type 'float'"
        self._localization_confidence = value

    @property
    def position_covariance(self):
        """Message field 'position_covariance'."""
        return self._position_covariance

    @position_covariance.setter
    def position_covariance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position_covariance' field must be of type 'float'"
        self._position_covariance = value

    @property
    def heading_covariance(self):
        """Message field 'heading_covariance'."""
        return self._heading_covariance

    @heading_covariance.setter
    def heading_covariance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'heading_covariance' field must be of type 'float'"
        self._heading_covariance = value

    @property
    def ndt_healthy(self):
        """Message field 'ndt_healthy'."""
        return self._ndt_healthy

    @ndt_healthy.setter
    def ndt_healthy(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'ndt_healthy' field must be of type 'bool'"
        self._ndt_healthy = value

    @property
    def ndt_quality(self):
        """Message field 'ndt_quality'."""
        return self._ndt_quality

    @ndt_quality.setter
    def ndt_quality(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ndt_quality' field must be of type 'float'"
        self._ndt_quality = value

    @property
    def map_odom_stable(self):
        """Message field 'map_odom_stable'."""
        return self._map_odom_stable

    @map_odom_stable.setter
    def map_odom_stable(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'map_odom_stable' field must be of type 'bool'"
        self._map_odom_stable = value

    @property
    def map_odom_drift(self):
        """Message field 'map_odom_drift'."""
        return self._map_odom_drift

    @map_odom_drift.setter
    def map_odom_drift(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'map_odom_drift' field must be of type 'float'"
        self._map_odom_drift = value

    @property
    def gps_available(self):
        """Message field 'gps_available'."""
        return self._gps_available

    @gps_available.setter
    def gps_available(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'gps_available' field must be of type 'bool'"
        self._gps_available = value

    @property
    def imu_available(self):
        """Message field 'imu_available'."""
        return self._imu_available

    @imu_available.setter
    def imu_available(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'imu_available' field must be of type 'bool'"
        self._imu_available = value

    @property
    def lidar_available(self):
        """Message field 'lidar_available'."""
        return self._lidar_available

    @lidar_available.setter
    def lidar_available(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'lidar_available' field must be of type 'bool'"
        self._lidar_available = value

    @property
    def warning_flags(self):
        """Message field 'warning_flags'."""
        return self._warning_flags

    @warning_flags.setter
    def warning_flags(self, value):
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, str) for v in value) and
                 True), \
                "The 'warning_flags' field must be a set or sequence and each value of type 'str'"
        self._warning_flags = value
