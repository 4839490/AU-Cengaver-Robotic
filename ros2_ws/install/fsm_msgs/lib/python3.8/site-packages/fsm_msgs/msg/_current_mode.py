# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsm_msgs:msg/CurrentMode.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CurrentMode(type):
    """Metaclass of message 'CurrentMode'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'LANE_FOLLOW': 0,
        'STOP_APPROACH': 1,
        'PICKUP_APPROACH': 2,
        'DROPOFF_APPROACH': 3,
        'OBSTACLE_AVOID': 4,
        'PARK_APPROACH': 5,
        'PARK_MANEUVER': 6,
        'MISSION_COMPLETE': 7,
        'STOP_NONE': 0,
        'STOP_RED_LIGHT': 1,
        'STOP_STOP_SIGN': 2,
        'STOP_OBSTACLE_TTC': 3,
        'STOP_LOCALIZATION_LOST': 4,
        'STOP_STALE_SENSOR': 5,
        'STOP_MISSION_ABORT': 6,
        'STOP_PEDESTRIAN': 7,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('fsm_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fsm_msgs.msg.CurrentMode')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__current_mode
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__current_mode
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__current_mode
            cls._TYPE_SUPPORT = module.type_support_msg__msg__current_mode
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__current_mode

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'LANE_FOLLOW': cls.__constants['LANE_FOLLOW'],
            'STOP_APPROACH': cls.__constants['STOP_APPROACH'],
            'PICKUP_APPROACH': cls.__constants['PICKUP_APPROACH'],
            'DROPOFF_APPROACH': cls.__constants['DROPOFF_APPROACH'],
            'OBSTACLE_AVOID': cls.__constants['OBSTACLE_AVOID'],
            'PARK_APPROACH': cls.__constants['PARK_APPROACH'],
            'PARK_MANEUVER': cls.__constants['PARK_MANEUVER'],
            'MISSION_COMPLETE': cls.__constants['MISSION_COMPLETE'],
            'STOP_NONE': cls.__constants['STOP_NONE'],
            'STOP_RED_LIGHT': cls.__constants['STOP_RED_LIGHT'],
            'STOP_STOP_SIGN': cls.__constants['STOP_STOP_SIGN'],
            'STOP_OBSTACLE_TTC': cls.__constants['STOP_OBSTACLE_TTC'],
            'STOP_LOCALIZATION_LOST': cls.__constants['STOP_LOCALIZATION_LOST'],
            'STOP_STALE_SENSOR': cls.__constants['STOP_STALE_SENSOR'],
            'STOP_MISSION_ABORT': cls.__constants['STOP_MISSION_ABORT'],
            'STOP_PEDESTRIAN': cls.__constants['STOP_PEDESTRIAN'],
        }

    @property
    def LANE_FOLLOW(self):
        """Message constant 'LANE_FOLLOW'."""
        return Metaclass_CurrentMode.__constants['LANE_FOLLOW']

    @property
    def STOP_APPROACH(self):
        """Message constant 'STOP_APPROACH'."""
        return Metaclass_CurrentMode.__constants['STOP_APPROACH']

    @property
    def PICKUP_APPROACH(self):
        """Message constant 'PICKUP_APPROACH'."""
        return Metaclass_CurrentMode.__constants['PICKUP_APPROACH']

    @property
    def DROPOFF_APPROACH(self):
        """Message constant 'DROPOFF_APPROACH'."""
        return Metaclass_CurrentMode.__constants['DROPOFF_APPROACH']

    @property
    def OBSTACLE_AVOID(self):
        """Message constant 'OBSTACLE_AVOID'."""
        return Metaclass_CurrentMode.__constants['OBSTACLE_AVOID']

    @property
    def PARK_APPROACH(self):
        """Message constant 'PARK_APPROACH'."""
        return Metaclass_CurrentMode.__constants['PARK_APPROACH']

    @property
    def PARK_MANEUVER(self):
        """Message constant 'PARK_MANEUVER'."""
        return Metaclass_CurrentMode.__constants['PARK_MANEUVER']

    @property
    def MISSION_COMPLETE(self):
        """Message constant 'MISSION_COMPLETE'."""
        return Metaclass_CurrentMode.__constants['MISSION_COMPLETE']

    @property
    def STOP_NONE(self):
        """Message constant 'STOP_NONE'."""
        return Metaclass_CurrentMode.__constants['STOP_NONE']

    @property
    def STOP_RED_LIGHT(self):
        """Message constant 'STOP_RED_LIGHT'."""
        return Metaclass_CurrentMode.__constants['STOP_RED_LIGHT']

    @property
    def STOP_STOP_SIGN(self):
        """Message constant 'STOP_STOP_SIGN'."""
        return Metaclass_CurrentMode.__constants['STOP_STOP_SIGN']

    @property
    def STOP_OBSTACLE_TTC(self):
        """Message constant 'STOP_OBSTACLE_TTC'."""
        return Metaclass_CurrentMode.__constants['STOP_OBSTACLE_TTC']

    @property
    def STOP_LOCALIZATION_LOST(self):
        """Message constant 'STOP_LOCALIZATION_LOST'."""
        return Metaclass_CurrentMode.__constants['STOP_LOCALIZATION_LOST']

    @property
    def STOP_STALE_SENSOR(self):
        """Message constant 'STOP_STALE_SENSOR'."""
        return Metaclass_CurrentMode.__constants['STOP_STALE_SENSOR']

    @property
    def STOP_MISSION_ABORT(self):
        """Message constant 'STOP_MISSION_ABORT'."""
        return Metaclass_CurrentMode.__constants['STOP_MISSION_ABORT']

    @property
    def STOP_PEDESTRIAN(self):
        """Message constant 'STOP_PEDESTRIAN'."""
        return Metaclass_CurrentMode.__constants['STOP_PEDESTRIAN']


class CurrentMode(metaclass=Metaclass_CurrentMode):
    """
    Message class 'CurrentMode'.

    Constants:
      LANE_FOLLOW
      STOP_APPROACH
      PICKUP_APPROACH
      DROPOFF_APPROACH
      OBSTACLE_AVOID
      PARK_APPROACH
      PARK_MANEUVER
      MISSION_COMPLETE
      STOP_NONE
      STOP_RED_LIGHT
      STOP_STOP_SIGN
      STOP_OBSTACLE_TTC
      STOP_LOCALIZATION_LOST
      STOP_STALE_SENSOR
      STOP_MISSION_ABORT
      STOP_PEDESTRIAN
    """

    __slots__ = [
        '_header',
        '_mode',
        '_previous_mode',
        '_reason',
        '_stop_reason',
        '_waypoint_id',
        '_age_ms',
        '_valid_until_ms',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'mode': 'uint8',
        'previous_mode': 'uint8',
        'reason': 'string',
        'stop_reason': 'uint8',
        'waypoint_id': 'uint32',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
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
        self.mode = kwargs.get('mode', int())
        self.previous_mode = kwargs.get('previous_mode', int())
        self.reason = kwargs.get('reason', str())
        self.stop_reason = kwargs.get('stop_reason', int())
        self.waypoint_id = kwargs.get('waypoint_id', int())
        self.age_ms = kwargs.get('age_ms', int())
        self.valid_until_ms = kwargs.get('valid_until_ms', int())
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
        if self.mode != other.mode:
            return False
        if self.previous_mode != other.previous_mode:
            return False
        if self.reason != other.reason:
            return False
        if self.stop_reason != other.stop_reason:
            return False
        if self.waypoint_id != other.waypoint_id:
            return False
        if self.age_ms != other.age_ms:
            return False
        if self.valid_until_ms != other.valid_until_ms:
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
    def mode(self):
        """Message field 'mode'."""
        return self._mode

    @mode.setter
    def mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'mode' field must be an unsigned integer in [0, 255]"
        self._mode = value

    @property
    def previous_mode(self):
        """Message field 'previous_mode'."""
        return self._previous_mode

    @previous_mode.setter
    def previous_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'previous_mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'previous_mode' field must be an unsigned integer in [0, 255]"
        self._previous_mode = value

    @property
    def reason(self):
        """Message field 'reason'."""
        return self._reason

    @reason.setter
    def reason(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'reason' field must be of type 'str'"
        self._reason = value

    @property
    def stop_reason(self):
        """Message field 'stop_reason'."""
        return self._stop_reason

    @stop_reason.setter
    def stop_reason(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'stop_reason' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'stop_reason' field must be an unsigned integer in [0, 255]"
        self._stop_reason = value

    @property
    def waypoint_id(self):
        """Message field 'waypoint_id'."""
        return self._waypoint_id

    @waypoint_id.setter
    def waypoint_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'waypoint_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'waypoint_id' field must be an unsigned integer in [0, 4294967295]"
        self._waypoint_id = value

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
