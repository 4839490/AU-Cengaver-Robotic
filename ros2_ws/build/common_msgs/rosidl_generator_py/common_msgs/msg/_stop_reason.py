# generated from rosidl_generator_py/resource/_idl.py.em
# with input from common_msgs:msg/StopReason.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_StopReason(type):
    """Metaclass of message 'StopReason'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
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
            module = import_type_support('common_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'common_msgs.msg.StopReason')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__stop_reason
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__stop_reason
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__stop_reason
            cls._TYPE_SUPPORT = module.type_support_msg__msg__stop_reason
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__stop_reason

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
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
    def STOP_NONE(self):
        """Message constant 'STOP_NONE'."""
        return Metaclass_StopReason.__constants['STOP_NONE']

    @property
    def STOP_RED_LIGHT(self):
        """Message constant 'STOP_RED_LIGHT'."""
        return Metaclass_StopReason.__constants['STOP_RED_LIGHT']

    @property
    def STOP_STOP_SIGN(self):
        """Message constant 'STOP_STOP_SIGN'."""
        return Metaclass_StopReason.__constants['STOP_STOP_SIGN']

    @property
    def STOP_OBSTACLE_TTC(self):
        """Message constant 'STOP_OBSTACLE_TTC'."""
        return Metaclass_StopReason.__constants['STOP_OBSTACLE_TTC']

    @property
    def STOP_LOCALIZATION_LOST(self):
        """Message constant 'STOP_LOCALIZATION_LOST'."""
        return Metaclass_StopReason.__constants['STOP_LOCALIZATION_LOST']

    @property
    def STOP_STALE_SENSOR(self):
        """Message constant 'STOP_STALE_SENSOR'."""
        return Metaclass_StopReason.__constants['STOP_STALE_SENSOR']

    @property
    def STOP_MISSION_ABORT(self):
        """Message constant 'STOP_MISSION_ABORT'."""
        return Metaclass_StopReason.__constants['STOP_MISSION_ABORT']

    @property
    def STOP_PEDESTRIAN(self):
        """Message constant 'STOP_PEDESTRIAN'."""
        return Metaclass_StopReason.__constants['STOP_PEDESTRIAN']


class StopReason(metaclass=Metaclass_StopReason):
    """
    Message class 'StopReason'.

    Constants:
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
        '_reason',
    ]

    _fields_and_field_types = {
        'reason': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.reason = kwargs.get('reason', int())

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
        if self.reason != other.reason:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

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
