# generated from rosidl_generator_py/resource/_idl.py.em
# with input from localization_msgs:msg/LocalizationOdometry.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_LocalizationOdometry(type):
    """Metaclass of message 'LocalizationOdometry'."""

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
                'localization_msgs.msg.LocalizationOdometry')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__localization_odometry
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__localization_odometry
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__localization_odometry
            cls._TYPE_SUPPORT = module.type_support_msg__msg__localization_odometry
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__localization_odometry

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


class LocalizationOdometry(metaclass=Metaclass_LocalizationOdometry):
    """Message class 'LocalizationOdometry'."""

    __slots__ = [
        '_header',
        '_age_ms',
        '_valid_until_ms',
        '_x',
        '_y',
        '_yaw',
        '_linear_velocity',
        '_angular_velocity',
        '_position_covariance',
        '_heading_covariance',
        '_velocity_covariance',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'x': 'double',
        'y': 'double',
        'yaw': 'double',
        'linear_velocity': 'double',
        'angular_velocity': 'double',
        'position_covariance': 'double',
        'heading_covariance': 'double',
        'velocity_covariance': 'double',
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
        self.x = kwargs.get('x', float())
        self.y = kwargs.get('y', float())
        self.yaw = kwargs.get('yaw', float())
        self.linear_velocity = kwargs.get('linear_velocity', float())
        self.angular_velocity = kwargs.get('angular_velocity', float())
        self.position_covariance = kwargs.get('position_covariance', float())
        self.heading_covariance = kwargs.get('heading_covariance', float())
        self.velocity_covariance = kwargs.get('velocity_covariance', float())
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
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        if self.yaw != other.yaw:
            return False
        if self.linear_velocity != other.linear_velocity:
            return False
        if self.angular_velocity != other.angular_velocity:
            return False
        if self.position_covariance != other.position_covariance:
            return False
        if self.heading_covariance != other.heading_covariance:
            return False
        if self.velocity_covariance != other.velocity_covariance:
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
    def x(self):
        """Message field 'x'."""
        return self._x

    @x.setter
    def x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x' field must be of type 'float'"
        self._x = value

    @property
    def y(self):
        """Message field 'y'."""
        return self._y

    @y.setter
    def y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y' field must be of type 'float'"
        self._y = value

    @property
    def yaw(self):
        """Message field 'yaw'."""
        return self._yaw

    @yaw.setter
    def yaw(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw' field must be of type 'float'"
        self._yaw = value

    @property
    def linear_velocity(self):
        """Message field 'linear_velocity'."""
        return self._linear_velocity

    @linear_velocity.setter
    def linear_velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'linear_velocity' field must be of type 'float'"
        self._linear_velocity = value

    @property
    def angular_velocity(self):
        """Message field 'angular_velocity'."""
        return self._angular_velocity

    @angular_velocity.setter
    def angular_velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angular_velocity' field must be of type 'float'"
        self._angular_velocity = value

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
    def velocity_covariance(self):
        """Message field 'velocity_covariance'."""
        return self._velocity_covariance

    @velocity_covariance.setter
    def velocity_covariance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'velocity_covariance' field must be of type 'float'"
        self._velocity_covariance = value

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
