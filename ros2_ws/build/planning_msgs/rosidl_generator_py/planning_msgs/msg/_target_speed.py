# generated from rosidl_generator_py/resource/_idl.py.em
# with input from planning_msgs:msg/TargetSpeed.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TargetSpeed(type):
    """Metaclass of message 'TargetSpeed'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'REASON_LANE_FOLLOW': 0,
        'REASON_APPROACH_STOP': 1,
        'REASON_PICKUP_DROPOFF': 2,
        'REASON_OBSTACLE_SLOW': 3,
        'REASON_JUNCTION': 4,
        'REASON_TUNNEL': 5,
        'REASON_PARK_APPROACH': 6,
        'REASON_PARK_MANEUVER': 7,
        'REASON_EMERGENCY_STOP': 8,
        'REASON_LOCALIZATION_DEGRADED': 9,
        'REASON_LANE_LOST': 10,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('planning_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'planning_msgs.msg.TargetSpeed')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__target_speed
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__target_speed
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__target_speed
            cls._TYPE_SUPPORT = module.type_support_msg__msg__target_speed
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__target_speed

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'REASON_LANE_FOLLOW': cls.__constants['REASON_LANE_FOLLOW'],
            'REASON_APPROACH_STOP': cls.__constants['REASON_APPROACH_STOP'],
            'REASON_PICKUP_DROPOFF': cls.__constants['REASON_PICKUP_DROPOFF'],
            'REASON_OBSTACLE_SLOW': cls.__constants['REASON_OBSTACLE_SLOW'],
            'REASON_JUNCTION': cls.__constants['REASON_JUNCTION'],
            'REASON_TUNNEL': cls.__constants['REASON_TUNNEL'],
            'REASON_PARK_APPROACH': cls.__constants['REASON_PARK_APPROACH'],
            'REASON_PARK_MANEUVER': cls.__constants['REASON_PARK_MANEUVER'],
            'REASON_EMERGENCY_STOP': cls.__constants['REASON_EMERGENCY_STOP'],
            'REASON_LOCALIZATION_DEGRADED': cls.__constants['REASON_LOCALIZATION_DEGRADED'],
            'REASON_LANE_LOST': cls.__constants['REASON_LANE_LOST'],
        }

    @property
    def REASON_LANE_FOLLOW(self):
        """Message constant 'REASON_LANE_FOLLOW'."""
        return Metaclass_TargetSpeed.__constants['REASON_LANE_FOLLOW']

    @property
    def REASON_APPROACH_STOP(self):
        """Message constant 'REASON_APPROACH_STOP'."""
        return Metaclass_TargetSpeed.__constants['REASON_APPROACH_STOP']

    @property
    def REASON_PICKUP_DROPOFF(self):
        """Message constant 'REASON_PICKUP_DROPOFF'."""
        return Metaclass_TargetSpeed.__constants['REASON_PICKUP_DROPOFF']

    @property
    def REASON_OBSTACLE_SLOW(self):
        """Message constant 'REASON_OBSTACLE_SLOW'."""
        return Metaclass_TargetSpeed.__constants['REASON_OBSTACLE_SLOW']

    @property
    def REASON_JUNCTION(self):
        """Message constant 'REASON_JUNCTION'."""
        return Metaclass_TargetSpeed.__constants['REASON_JUNCTION']

    @property
    def REASON_TUNNEL(self):
        """Message constant 'REASON_TUNNEL'."""
        return Metaclass_TargetSpeed.__constants['REASON_TUNNEL']

    @property
    def REASON_PARK_APPROACH(self):
        """Message constant 'REASON_PARK_APPROACH'."""
        return Metaclass_TargetSpeed.__constants['REASON_PARK_APPROACH']

    @property
    def REASON_PARK_MANEUVER(self):
        """Message constant 'REASON_PARK_MANEUVER'."""
        return Metaclass_TargetSpeed.__constants['REASON_PARK_MANEUVER']

    @property
    def REASON_EMERGENCY_STOP(self):
        """Message constant 'REASON_EMERGENCY_STOP'."""
        return Metaclass_TargetSpeed.__constants['REASON_EMERGENCY_STOP']

    @property
    def REASON_LOCALIZATION_DEGRADED(self):
        """Message constant 'REASON_LOCALIZATION_DEGRADED'."""
        return Metaclass_TargetSpeed.__constants['REASON_LOCALIZATION_DEGRADED']

    @property
    def REASON_LANE_LOST(self):
        """Message constant 'REASON_LANE_LOST'."""
        return Metaclass_TargetSpeed.__constants['REASON_LANE_LOST']


class TargetSpeed(metaclass=Metaclass_TargetSpeed):
    """
    Message class 'TargetSpeed'.

    Constants:
      REASON_LANE_FOLLOW
      REASON_APPROACH_STOP
      REASON_PICKUP_DROPOFF
      REASON_OBSTACLE_SLOW
      REASON_JUNCTION
      REASON_TUNNEL
      REASON_PARK_APPROACH
      REASON_PARK_MANEUVER
      REASON_EMERGENCY_STOP
      REASON_LOCALIZATION_DEGRADED
      REASON_LANE_LOST
    """

    __slots__ = [
        '_header',
        '_speed',
        '_jerk_limit',
        '_reason',
        '_valid_until_ms',
        '_age_ms',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'speed': 'float',
        'jerk_limit': 'float',
        'reason': 'uint8',
        'valid_until_ms': 'uint32',
        'age_ms': 'uint32',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.speed = kwargs.get('speed', float())
        self.jerk_limit = kwargs.get('jerk_limit', float())
        self.reason = kwargs.get('reason', int())
        self.valid_until_ms = kwargs.get('valid_until_ms', int())
        self.age_ms = kwargs.get('age_ms', int())
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
        if self.speed != other.speed:
            return False
        if self.jerk_limit != other.jerk_limit:
            return False
        if self.reason != other.reason:
            return False
        if self.valid_until_ms != other.valid_until_ms:
            return False
        if self.age_ms != other.age_ms:
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
    def speed(self):
        """Message field 'speed'."""
        return self._speed

    @speed.setter
    def speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'speed' field must be of type 'float'"
        self._speed = value

    @property
    def jerk_limit(self):
        """Message field 'jerk_limit'."""
        return self._jerk_limit

    @jerk_limit.setter
    def jerk_limit(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'jerk_limit' field must be of type 'float'"
        self._jerk_limit = value

    @property
    def reason(self):
        """Message field 'reason'."""
        return self._reason

    @reason.setter
    def reason(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'reason' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'reason' field must be an unsigned integer in [0, 255]"
        self._reason = value

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
