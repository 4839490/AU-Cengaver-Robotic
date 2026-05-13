# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fsm_msgs:msg/MissionState.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MissionState(type):
    """Metaclass of message 'MissionState'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'PICKUP': 0,
        'DROPOFF': 1,
        'WAYPOINT': 2,
        'PARK_ENTRY': 3,
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
                'fsm_msgs.msg.MissionState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__mission_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__mission_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__mission_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__mission_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__mission_state

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'PICKUP': cls.__constants['PICKUP'],
            'DROPOFF': cls.__constants['DROPOFF'],
            'WAYPOINT': cls.__constants['WAYPOINT'],
            'PARK_ENTRY': cls.__constants['PARK_ENTRY'],
        }

    @property
    def PICKUP(self):
        """Message constant 'PICKUP'."""
        return Metaclass_MissionState.__constants['PICKUP']

    @property
    def DROPOFF(self):
        """Message constant 'DROPOFF'."""
        return Metaclass_MissionState.__constants['DROPOFF']

    @property
    def WAYPOINT(self):
        """Message constant 'WAYPOINT'."""
        return Metaclass_MissionState.__constants['WAYPOINT']

    @property
    def PARK_ENTRY(self):
        """Message constant 'PARK_ENTRY'."""
        return Metaclass_MissionState.__constants['PARK_ENTRY']


class MissionState(metaclass=Metaclass_MissionState):
    """
    Message class 'MissionState'.

    Constants:
      PICKUP
      DROPOFF
      WAYPOINT
      PARK_ENTRY
    """

    __slots__ = [
        '_header',
        '_mission_active',
        '_total_waypoints',
        '_completed_waypoints',
        '_current_waypoint_id',
        '_current_waypoint_type',
        '_next_waypoint_id',
        '_next_waypoint_type',
        '_pickup_complete',
        '_dropoff_complete',
        '_age_ms',
        '_valid_until_ms',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'mission_active': 'boolean',
        'total_waypoints': 'uint8',
        'completed_waypoints': 'uint8',
        'current_waypoint_id': 'uint32',
        'current_waypoint_type': 'uint8',
        'next_waypoint_id': 'uint32',
        'next_waypoint_type': 'uint8',
        'pickup_complete': 'boolean',
        'dropoff_complete': 'boolean',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
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
        self.mission_active = kwargs.get('mission_active', bool())
        self.total_waypoints = kwargs.get('total_waypoints', int())
        self.completed_waypoints = kwargs.get('completed_waypoints', int())
        self.current_waypoint_id = kwargs.get('current_waypoint_id', int())
        self.current_waypoint_type = kwargs.get('current_waypoint_type', int())
        self.next_waypoint_id = kwargs.get('next_waypoint_id', int())
        self.next_waypoint_type = kwargs.get('next_waypoint_type', int())
        self.pickup_complete = kwargs.get('pickup_complete', bool())
        self.dropoff_complete = kwargs.get('dropoff_complete', bool())
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
        if self.mission_active != other.mission_active:
            return False
        if self.total_waypoints != other.total_waypoints:
            return False
        if self.completed_waypoints != other.completed_waypoints:
            return False
        if self.current_waypoint_id != other.current_waypoint_id:
            return False
        if self.current_waypoint_type != other.current_waypoint_type:
            return False
        if self.next_waypoint_id != other.next_waypoint_id:
            return False
        if self.next_waypoint_type != other.next_waypoint_type:
            return False
        if self.pickup_complete != other.pickup_complete:
            return False
        if self.dropoff_complete != other.dropoff_complete:
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
    def mission_active(self):
        """Message field 'mission_active'."""
        return self._mission_active

    @mission_active.setter
    def mission_active(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'mission_active' field must be of type 'bool'"
        self._mission_active = value

    @property
    def total_waypoints(self):
        """Message field 'total_waypoints'."""
        return self._total_waypoints

    @total_waypoints.setter
    def total_waypoints(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'total_waypoints' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'total_waypoints' field must be an unsigned integer in [0, 255]"
        self._total_waypoints = value

    @property
    def completed_waypoints(self):
        """Message field 'completed_waypoints'."""
        return self._completed_waypoints

    @completed_waypoints.setter
    def completed_waypoints(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'completed_waypoints' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'completed_waypoints' field must be an unsigned integer in [0, 255]"
        self._completed_waypoints = value

    @property
    def current_waypoint_id(self):
        """Message field 'current_waypoint_id'."""
        return self._current_waypoint_id

    @current_waypoint_id.setter
    def current_waypoint_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'current_waypoint_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'current_waypoint_id' field must be an unsigned integer in [0, 4294967295]"
        self._current_waypoint_id = value

    @property
    def current_waypoint_type(self):
        """Message field 'current_waypoint_type'."""
        return self._current_waypoint_type

    @current_waypoint_type.setter
    def current_waypoint_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'current_waypoint_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'current_waypoint_type' field must be an unsigned integer in [0, 255]"
        self._current_waypoint_type = value

    @property
    def next_waypoint_id(self):
        """Message field 'next_waypoint_id'."""
        return self._next_waypoint_id

    @next_waypoint_id.setter
    def next_waypoint_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'next_waypoint_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'next_waypoint_id' field must be an unsigned integer in [0, 4294967295]"
        self._next_waypoint_id = value

    @property
    def next_waypoint_type(self):
        """Message field 'next_waypoint_type'."""
        return self._next_waypoint_type

    @next_waypoint_type.setter
    def next_waypoint_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'next_waypoint_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'next_waypoint_type' field must be an unsigned integer in [0, 255]"
        self._next_waypoint_type = value

    @property
    def pickup_complete(self):
        """Message field 'pickup_complete'."""
        return self._pickup_complete

    @pickup_complete.setter
    def pickup_complete(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'pickup_complete' field must be of type 'bool'"
        self._pickup_complete = value

    @property
    def dropoff_complete(self):
        """Message field 'dropoff_complete'."""
        return self._dropoff_complete

    @dropoff_complete.setter
    def dropoff_complete(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'dropoff_complete' field must be of type 'bool'"
        self._dropoff_complete = value

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
