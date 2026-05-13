# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsm_msgs:msg/FSMEvent.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FSMEvent(type):
    """Metaclass of message 'FSMEvent'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'PICKUP_COMPLETE': 0,
        'DROPOFF_COMPLETE': 1,
        'OBSTACLE_CLEARED': 2,
        'REPLANNING_REQUEST': 3,
        'MISSION_ABORT': 4,
        'RESUME': 5,
        'PARK_SLOT_CHANGE': 6,
        'EMERGENCY_STOP_REQUEST': 7,
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
                'fsm_msgs.msg.FSMEvent')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__fsm_event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__fsm_event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__fsm_event
            cls._TYPE_SUPPORT = module.type_support_msg__msg__fsm_event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__fsm_event

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'PICKUP_COMPLETE': cls.__constants['PICKUP_COMPLETE'],
            'DROPOFF_COMPLETE': cls.__constants['DROPOFF_COMPLETE'],
            'OBSTACLE_CLEARED': cls.__constants['OBSTACLE_CLEARED'],
            'REPLANNING_REQUEST': cls.__constants['REPLANNING_REQUEST'],
            'MISSION_ABORT': cls.__constants['MISSION_ABORT'],
            'RESUME': cls.__constants['RESUME'],
            'PARK_SLOT_CHANGE': cls.__constants['PARK_SLOT_CHANGE'],
            'EMERGENCY_STOP_REQUEST': cls.__constants['EMERGENCY_STOP_REQUEST'],
        }

    @property
    def PICKUP_COMPLETE(self):
        """Message constant 'PICKUP_COMPLETE'."""
        return Metaclass_FSMEvent.__constants['PICKUP_COMPLETE']

    @property
    def DROPOFF_COMPLETE(self):
        """Message constant 'DROPOFF_COMPLETE'."""
        return Metaclass_FSMEvent.__constants['DROPOFF_COMPLETE']

    @property
    def OBSTACLE_CLEARED(self):
        """Message constant 'OBSTACLE_CLEARED'."""
        return Metaclass_FSMEvent.__constants['OBSTACLE_CLEARED']

    @property
    def REPLANNING_REQUEST(self):
        """Message constant 'REPLANNING_REQUEST'."""
        return Metaclass_FSMEvent.__constants['REPLANNING_REQUEST']

    @property
    def MISSION_ABORT(self):
        """Message constant 'MISSION_ABORT'."""
        return Metaclass_FSMEvent.__constants['MISSION_ABORT']

    @property
    def RESUME(self):
        """Message constant 'RESUME'."""
        return Metaclass_FSMEvent.__constants['RESUME']

    @property
    def PARK_SLOT_CHANGE(self):
        """Message constant 'PARK_SLOT_CHANGE'."""
        return Metaclass_FSMEvent.__constants['PARK_SLOT_CHANGE']

    @property
    def EMERGENCY_STOP_REQUEST(self):
        """Message constant 'EMERGENCY_STOP_REQUEST'."""
        return Metaclass_FSMEvent.__constants['EMERGENCY_STOP_REQUEST']


class FSMEvent(metaclass=Metaclass_FSMEvent):
    """
    Message class 'FSMEvent'.

    Constants:
      PICKUP_COMPLETE
      DROPOFF_COMPLETE
      OBSTACLE_CLEARED
      REPLANNING_REQUEST
      MISSION_ABORT
      RESUME
      PARK_SLOT_CHANGE
      EMERGENCY_STOP_REQUEST
    """

    __slots__ = [
        '_header',
        '_event_type',
        '_waypoint_id',
        '_data',
        '_age_ms',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'event_type': 'uint8',
        'waypoint_id': 'uint32',
        'data': 'string',
        'age_ms': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.event_type = kwargs.get('event_type', int())
        self.waypoint_id = kwargs.get('waypoint_id', int())
        self.data = kwargs.get('data', str())
        self.age_ms = kwargs.get('age_ms', int())

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
        if self.event_type != other.event_type:
            return False
        if self.waypoint_id != other.waypoint_id:
            return False
        if self.data != other.data:
            return False
        if self.age_ms != other.age_ms:
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
    def event_type(self):
        """Message field 'event_type'."""
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'event_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'event_type' field must be an unsigned integer in [0, 255]"
        self._event_type = value

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
    def data(self):
        """Message field 'data'."""
        return self._data

    @data.setter
    def data(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'data' field must be of type 'str'"
        self._data = value

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
