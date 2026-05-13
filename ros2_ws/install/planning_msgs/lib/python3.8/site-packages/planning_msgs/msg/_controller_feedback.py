# generated from rosidl_generator_py/resource/_idl.py.em
# with input from planning_msgs:msg/ControllerFeedback.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ControllerFeedback(type):
    """Metaclass of message 'ControllerFeedback'."""

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
                'planning_msgs.msg.ControllerFeedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__controller_feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__controller_feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__controller_feedback
            cls._TYPE_SUPPORT = module.type_support_msg__msg__controller_feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__controller_feedback

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


class ControllerFeedback(metaclass=Metaclass_ControllerFeedback):
    """Message class 'ControllerFeedback'."""

    __slots__ = [
        '_header',
        '_actual_speed',
        '_actual_steering_deg',
        '_cross_track_error',
        '_heading_error',
        '_brake_active',
        '_full_brake_active',
        '_age_ms',
        '_valid_until_ms',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'actual_speed': 'float',
        'actual_steering_deg': 'float',
        'cross_track_error': 'float',
        'heading_error': 'float',
        'brake_active': 'boolean',
        'full_brake_active': 'boolean',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.actual_speed = kwargs.get('actual_speed', float())
        self.actual_steering_deg = kwargs.get('actual_steering_deg', float())
        self.cross_track_error = kwargs.get('cross_track_error', float())
        self.heading_error = kwargs.get('heading_error', float())
        self.brake_active = kwargs.get('brake_active', bool())
        self.full_brake_active = kwargs.get('full_brake_active', bool())
        self.age_ms = kwargs.get('age_ms', int())
        self.valid_until_ms = kwargs.get('valid_until_ms', int())

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
        if self.actual_speed != other.actual_speed:
            return False
        if self.actual_steering_deg != other.actual_steering_deg:
            return False
        if self.cross_track_error != other.cross_track_error:
            return False
        if self.heading_error != other.heading_error:
            return False
        if self.brake_active != other.brake_active:
            return False
        if self.full_brake_active != other.full_brake_active:
            return False
        if self.age_ms != other.age_ms:
            return False
        if self.valid_until_ms != other.valid_until_ms:
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
    def actual_speed(self):
        """Message field 'actual_speed'."""
        return self._actual_speed

    @actual_speed.setter
    def actual_speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'actual_speed' field must be of type 'float'"
        self._actual_speed = value

    @property
    def actual_steering_deg(self):
        """Message field 'actual_steering_deg'."""
        return self._actual_steering_deg

    @actual_steering_deg.setter
    def actual_steering_deg(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'actual_steering_deg' field must be of type 'float'"
        self._actual_steering_deg = value

    @property
    def cross_track_error(self):
        """Message field 'cross_track_error'."""
        return self._cross_track_error

    @cross_track_error.setter
    def cross_track_error(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'cross_track_error' field must be of type 'float'"
        self._cross_track_error = value

    @property
    def heading_error(self):
        """Message field 'heading_error'."""
        return self._heading_error

    @heading_error.setter
    def heading_error(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'heading_error' field must be of type 'float'"
        self._heading_error = value

    @property
    def brake_active(self):
        """Message field 'brake_active'."""
        return self._brake_active

    @brake_active.setter
    def brake_active(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'brake_active' field must be of type 'bool'"
        self._brake_active = value

    @property
    def full_brake_active(self):
        """Message field 'full_brake_active'."""
        return self._full_brake_active

    @full_brake_active.setter
    def full_brake_active(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'full_brake_active' field must be of type 'bool'"
        self._full_brake_active = value

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
