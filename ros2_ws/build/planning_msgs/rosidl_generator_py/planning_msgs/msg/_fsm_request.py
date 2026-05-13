# generated from rosidl_generator_py/resource/_idl.py.em
# with input from planning_msgs:msg/FSMRequest.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FSMRequest(type):
    """Metaclass of message 'FSMRequest'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'MODE_CHANGE': 0,
        'REPLANNING_NEEDED': 1,
        'GOAL_CONFIRMED': 2,
        'OBSTACLE_BLOCKED': 3,
        'LOCALIZATION_DEGRADED': 4,
        'PARK_READY': 5,
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
                'planning_msgs.msg.FSMRequest')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__fsm_request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__fsm_request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__fsm_request
            cls._TYPE_SUPPORT = module.type_support_msg__msg__fsm_request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__fsm_request

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'MODE_CHANGE': cls.__constants['MODE_CHANGE'],
            'REPLANNING_NEEDED': cls.__constants['REPLANNING_NEEDED'],
            'GOAL_CONFIRMED': cls.__constants['GOAL_CONFIRMED'],
            'OBSTACLE_BLOCKED': cls.__constants['OBSTACLE_BLOCKED'],
            'LOCALIZATION_DEGRADED': cls.__constants['LOCALIZATION_DEGRADED'],
            'PARK_READY': cls.__constants['PARK_READY'],
        }

    @property
    def MODE_CHANGE(self):
        """Message constant 'MODE_CHANGE'."""
        return Metaclass_FSMRequest.__constants['MODE_CHANGE']

    @property
    def REPLANNING_NEEDED(self):
        """Message constant 'REPLANNING_NEEDED'."""
        return Metaclass_FSMRequest.__constants['REPLANNING_NEEDED']

    @property
    def GOAL_CONFIRMED(self):
        """Message constant 'GOAL_CONFIRMED'."""
        return Metaclass_FSMRequest.__constants['GOAL_CONFIRMED']

    @property
    def OBSTACLE_BLOCKED(self):
        """Message constant 'OBSTACLE_BLOCKED'."""
        return Metaclass_FSMRequest.__constants['OBSTACLE_BLOCKED']

    @property
    def LOCALIZATION_DEGRADED(self):
        """Message constant 'LOCALIZATION_DEGRADED'."""
        return Metaclass_FSMRequest.__constants['LOCALIZATION_DEGRADED']

    @property
    def PARK_READY(self):
        """Message constant 'PARK_READY'."""
        return Metaclass_FSMRequest.__constants['PARK_READY']


class FSMRequest(metaclass=Metaclass_FSMRequest):
    """
    Message class 'FSMRequest'.

    Constants:
      MODE_CHANGE
      REPLANNING_NEEDED
      GOAL_CONFIRMED
      OBSTACLE_BLOCKED
      LOCALIZATION_DEGRADED
      PARK_READY
    """

    __slots__ = [
        '_header',
        '_request_type',
        '_requested_mode',
        '_waypoint_id',
        '_reason',
        '_age_ms',
        '_valid_until_ms',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'request_type': 'uint8',
        'requested_mode': 'uint8',
        'waypoint_id': 'uint32',
        'reason': 'string',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.request_type = kwargs.get('request_type', int())
        self.requested_mode = kwargs.get('requested_mode', int())
        self.waypoint_id = kwargs.get('waypoint_id', int())
        self.reason = kwargs.get('reason', str())
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
        if self.request_type != other.request_type:
            return False
        if self.requested_mode != other.requested_mode:
            return False
        if self.waypoint_id != other.waypoint_id:
            return False
        if self.reason != other.reason:
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
    def request_type(self):
        """Message field 'request_type'."""
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'request_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'request_type' field must be an unsigned integer in [0, 255]"
        self._request_type = value

    @property
    def requested_mode(self):
        """Message field 'requested_mode'."""
        return self._requested_mode

    @requested_mode.setter
    def requested_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'requested_mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'requested_mode' field must be an unsigned integer in [0, 255]"
        self._requested_mode = value

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
