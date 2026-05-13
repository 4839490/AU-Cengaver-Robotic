# generated from rosidl_generator_py/resource/_idl.py.em
# with input from localization_msgs:msg/LocalizationDiagnostics.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_LocalizationDiagnostics(type):
    """Metaclass of message 'LocalizationDiagnostics'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
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
                'localization_msgs.msg.LocalizationDiagnostics')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__localization_diagnostics
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__localization_diagnostics
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__localization_diagnostics
            cls._TYPE_SUPPORT = module.type_support_msg__msg__localization_diagnostics
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__localization_diagnostics

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class LocalizationDiagnostics(metaclass=Metaclass_LocalizationDiagnostics):
    """Message class 'LocalizationDiagnostics'."""

    __slots__ = [
        '_header',
        '_age_ms',
        '_valid_until_ms',
        '_ekf_output_hz',
        '_gps_input_hz',
        '_imu_input_hz',
        '_ndt_output_hz',
        '_ekf_latency_ms',
        '_ndt_latency_ms',
        '_position_covariance',
        '_heading_covariance',
        '_ndt_quality',
        '_ekf_healthy',
        '_gps_healthy',
        '_imu_healthy',
        '_ndt_healthy',
        '_map_odom_stable',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'ekf_output_hz': 'double',
        'gps_input_hz': 'double',
        'imu_input_hz': 'double',
        'ndt_output_hz': 'double',
        'ekf_latency_ms': 'double',
        'ndt_latency_ms': 'double',
        'position_covariance': 'double',
        'heading_covariance': 'double',
        'ndt_quality': 'double',
        'ekf_healthy': 'boolean',
        'gps_healthy': 'boolean',
        'imu_healthy': 'boolean',
        'ndt_healthy': 'boolean',
        'map_odom_stable': 'boolean',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
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
        self.ekf_output_hz = kwargs.get('ekf_output_hz', float())
        self.gps_input_hz = kwargs.get('gps_input_hz', float())
        self.imu_input_hz = kwargs.get('imu_input_hz', float())
        self.ndt_output_hz = kwargs.get('ndt_output_hz', float())
        self.ekf_latency_ms = kwargs.get('ekf_latency_ms', float())
        self.ndt_latency_ms = kwargs.get('ndt_latency_ms', float())
        self.position_covariance = kwargs.get('position_covariance', float())
        self.heading_covariance = kwargs.get('heading_covariance', float())
        self.ndt_quality = kwargs.get('ndt_quality', float())
        self.ekf_healthy = kwargs.get('ekf_healthy', bool())
        self.gps_healthy = kwargs.get('gps_healthy', bool())
        self.imu_healthy = kwargs.get('imu_healthy', bool())
        self.ndt_healthy = kwargs.get('ndt_healthy', bool())
        self.map_odom_stable = kwargs.get('map_odom_stable', bool())
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
        if self.ekf_output_hz != other.ekf_output_hz:
            return False
        if self.gps_input_hz != other.gps_input_hz:
            return False
        if self.imu_input_hz != other.imu_input_hz:
            return False
        if self.ndt_output_hz != other.ndt_output_hz:
            return False
        if self.ekf_latency_ms != other.ekf_latency_ms:
            return False
        if self.ndt_latency_ms != other.ndt_latency_ms:
            return False
        if self.position_covariance != other.position_covariance:
            return False
        if self.heading_covariance != other.heading_covariance:
            return False
        if self.ndt_quality != other.ndt_quality:
            return False
        if self.ekf_healthy != other.ekf_healthy:
            return False
        if self.gps_healthy != other.gps_healthy:
            return False
        if self.imu_healthy != other.imu_healthy:
            return False
        if self.ndt_healthy != other.ndt_healthy:
            return False
        if self.map_odom_stable != other.map_odom_stable:
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
    def ekf_output_hz(self):
        """Message field 'ekf_output_hz'."""
        return self._ekf_output_hz

    @ekf_output_hz.setter
    def ekf_output_hz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ekf_output_hz' field must be of type 'float'"
        self._ekf_output_hz = value

    @property
    def gps_input_hz(self):
        """Message field 'gps_input_hz'."""
        return self._gps_input_hz

    @gps_input_hz.setter
    def gps_input_hz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gps_input_hz' field must be of type 'float'"
        self._gps_input_hz = value

    @property
    def imu_input_hz(self):
        """Message field 'imu_input_hz'."""
        return self._imu_input_hz

    @imu_input_hz.setter
    def imu_input_hz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'imu_input_hz' field must be of type 'float'"
        self._imu_input_hz = value

    @property
    def ndt_output_hz(self):
        """Message field 'ndt_output_hz'."""
        return self._ndt_output_hz

    @ndt_output_hz.setter
    def ndt_output_hz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ndt_output_hz' field must be of type 'float'"
        self._ndt_output_hz = value

    @property
    def ekf_latency_ms(self):
        """Message field 'ekf_latency_ms'."""
        return self._ekf_latency_ms

    @ekf_latency_ms.setter
    def ekf_latency_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ekf_latency_ms' field must be of type 'float'"
        self._ekf_latency_ms = value

    @property
    def ndt_latency_ms(self):
        """Message field 'ndt_latency_ms'."""
        return self._ndt_latency_ms

    @ndt_latency_ms.setter
    def ndt_latency_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ndt_latency_ms' field must be of type 'float'"
        self._ndt_latency_ms = value

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
    def ekf_healthy(self):
        """Message field 'ekf_healthy'."""
        return self._ekf_healthy

    @ekf_healthy.setter
    def ekf_healthy(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'ekf_healthy' field must be of type 'bool'"
        self._ekf_healthy = value

    @property
    def gps_healthy(self):
        """Message field 'gps_healthy'."""
        return self._gps_healthy

    @gps_healthy.setter
    def gps_healthy(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'gps_healthy' field must be of type 'bool'"
        self._gps_healthy = value

    @property
    def imu_healthy(self):
        """Message field 'imu_healthy'."""
        return self._imu_healthy

    @imu_healthy.setter
    def imu_healthy(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'imu_healthy' field must be of type 'bool'"
        self._imu_healthy = value

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
