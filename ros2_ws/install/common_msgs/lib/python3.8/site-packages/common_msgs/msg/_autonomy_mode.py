# generated from rosidl_generator_py/resource/_idl.py.em
# with input from common_msgs:msg/AutonomyMode.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AutonomyMode(type):
    """Metaclass of message 'AutonomyMode'."""

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
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('common_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'common_msgs.msg.AutonomyMode')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__autonomy_mode
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__autonomy_mode
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__autonomy_mode
            cls._TYPE_SUPPORT = module.type_support_msg__msg__autonomy_mode
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__autonomy_mode

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
        }

    @property
    def LANE_FOLLOW(self):
        """Message constant 'LANE_FOLLOW'."""
        return Metaclass_AutonomyMode.__constants['LANE_FOLLOW']

    @property
    def STOP_APPROACH(self):
        """Message constant 'STOP_APPROACH'."""
        return Metaclass_AutonomyMode.__constants['STOP_APPROACH']

    @property
    def PICKUP_APPROACH(self):
        """Message constant 'PICKUP_APPROACH'."""
        return Metaclass_AutonomyMode.__constants['PICKUP_APPROACH']

    @property
    def DROPOFF_APPROACH(self):
        """Message constant 'DROPOFF_APPROACH'."""
        return Metaclass_AutonomyMode.__constants['DROPOFF_APPROACH']

    @property
    def OBSTACLE_AVOID(self):
        """Message constant 'OBSTACLE_AVOID'."""
        return Metaclass_AutonomyMode.__constants['OBSTACLE_AVOID']

    @property
    def PARK_APPROACH(self):
        """Message constant 'PARK_APPROACH'."""
        return Metaclass_AutonomyMode.__constants['PARK_APPROACH']

    @property
    def PARK_MANEUVER(self):
        """Message constant 'PARK_MANEUVER'."""
        return Metaclass_AutonomyMode.__constants['PARK_MANEUVER']

    @property
    def MISSION_COMPLETE(self):
        """Message constant 'MISSION_COMPLETE'."""
        return Metaclass_AutonomyMode.__constants['MISSION_COMPLETE']


class AutonomyMode(metaclass=Metaclass_AutonomyMode):
    """
    Message class 'AutonomyMode'.

    Constants:
      LANE_FOLLOW
      STOP_APPROACH
      PICKUP_APPROACH
      DROPOFF_APPROACH
      OBSTACLE_AVOID
      PARK_APPROACH
      PARK_MANEUVER
      MISSION_COMPLETE
    """

    __slots__ = [
        '_mode',
    ]

    _fields_and_field_types = {
        'mode': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.mode = kwargs.get('mode', int())

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
        if self.mode != other.mode:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

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
