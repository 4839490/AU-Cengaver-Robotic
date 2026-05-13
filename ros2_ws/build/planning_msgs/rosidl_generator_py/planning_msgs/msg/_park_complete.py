# generated from rosidl_generator_py/resource/_idl.py.em
# with input from planning_msgs:msg/ParkComplete.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ParkComplete(type):
    """Metaclass of message 'ParkComplete'."""

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
            module = import_type_support('planning_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'planning_msgs.msg.ParkComplete')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__park_complete
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__park_complete
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__park_complete
            cls._TYPE_SUPPORT = module.type_support_msg__msg__park_complete
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__park_complete

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


class ParkComplete(metaclass=Metaclass_ParkComplete):
    """Message class 'ParkComplete'."""

    __slots__ = [
        '_header',
        '_success',
        '_final_cross_track_error',
        '_final_heading_error',
        '_iterations_used',
        '_waypoint_id',
        '_age_ms',
        '_valid_until_ms',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'success': 'boolean',
        'final_cross_track_error': 'float',
        'final_heading_error': 'float',
        'iterations_used': 'uint8',
        'waypoint_id': 'uint32',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
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
        self.success = kwargs.get('success', bool())
        self.final_cross_track_error = kwargs.get('final_cross_track_error', float())
        self.final_heading_error = kwargs.get('final_heading_error', float())
        self.iterations_used = kwargs.get('iterations_used', int())
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
        if self.success != other.success:
            return False
        if self.final_cross_track_error != other.final_cross_track_error:
            return False
        if self.final_heading_error != other.final_heading_error:
            return False
        if self.iterations_used != other.iterations_used:
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
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @property
    def final_cross_track_error(self):
        """Message field 'final_cross_track_error'."""
        return self._final_cross_track_error

    @final_cross_track_error.setter
    def final_cross_track_error(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'final_cross_track_error' field must be of type 'float'"
        self._final_cross_track_error = value

    @property
    def final_heading_error(self):
        """Message field 'final_heading_error'."""
        return self._final_heading_error

    @final_heading_error.setter
    def final_heading_error(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'final_heading_error' field must be of type 'float'"
        self._final_heading_error = value

    @property
    def iterations_used(self):
        """Message field 'iterations_used'."""
        return self._iterations_used

    @iterations_used.setter
    def iterations_used(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'iterations_used' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'iterations_used' field must be an unsigned integer in [0, 255]"
        self._iterations_used = value

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
