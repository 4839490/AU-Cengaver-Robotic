# generated from rosidl_generator_py/resource/_idl.py.em
# with input from perception_msgs:msg/TrafficLightState.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TrafficLightState(type):
    """Metaclass of message 'TrafficLightState'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'UNKNOWN': 0,
        'RED': 1,
        'YELLOW': 2,
        'GREEN': 3,
        'STALE': 4,
        'CONFLICT': 5,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('perception_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'perception_msgs.msg.TrafficLightState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__traffic_light_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__traffic_light_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__traffic_light_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__traffic_light_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__traffic_light_state

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'UNKNOWN': cls.__constants['UNKNOWN'],
            'RED': cls.__constants['RED'],
            'YELLOW': cls.__constants['YELLOW'],
            'GREEN': cls.__constants['GREEN'],
            'STALE': cls.__constants['STALE'],
            'CONFLICT': cls.__constants['CONFLICT'],
        }

    @property
    def UNKNOWN(self):
        """Message constant 'UNKNOWN'."""
        return Metaclass_TrafficLightState.__constants['UNKNOWN']

    @property
    def RED(self):
        """Message constant 'RED'."""
        return Metaclass_TrafficLightState.__constants['RED']

    @property
    def YELLOW(self):
        """Message constant 'YELLOW'."""
        return Metaclass_TrafficLightState.__constants['YELLOW']

    @property
    def GREEN(self):
        """Message constant 'GREEN'."""
        return Metaclass_TrafficLightState.__constants['GREEN']

    @property
    def STALE(self):
        """Message constant 'STALE'."""
        return Metaclass_TrafficLightState.__constants['STALE']

    @property
    def CONFLICT(self):
        """Message constant 'CONFLICT'."""
        return Metaclass_TrafficLightState.__constants['CONFLICT']


class TrafficLightState(metaclass=Metaclass_TrafficLightState):
    """
    Message class 'TrafficLightState'.

    Constants:
      UNKNOWN
      RED
      YELLOW
      GREEN
      STALE
      CONFLICT
    """

    __slots__ = [
        '_header',
        '_state',
        '_confidence',
        '_relevant_to_route',
        '_distance_to_stop',
        '_confirmed',
        '_in_stop_zone',
        '_bbox_x',
        '_bbox_y',
        '_bbox_w',
        '_bbox_h',
        '_age_ms',
        '_valid_until_ms',
        '_source_sensor',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'state': 'uint8',
        'confidence': 'float',
        'relevant_to_route': 'boolean',
        'distance_to_stop': 'float',
        'confirmed': 'boolean',
        'in_stop_zone': 'boolean',
        'bbox_x': 'float',
        'bbox_y': 'float',
        'bbox_w': 'float',
        'bbox_h': 'float',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'source_sensor': 'string',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.state = kwargs.get('state', int())
        self.confidence = kwargs.get('confidence', float())
        self.relevant_to_route = kwargs.get('relevant_to_route', bool())
        self.distance_to_stop = kwargs.get('distance_to_stop', float())
        self.confirmed = kwargs.get('confirmed', bool())
        self.in_stop_zone = kwargs.get('in_stop_zone', bool())
        self.bbox_x = kwargs.get('bbox_x', float())
        self.bbox_y = kwargs.get('bbox_y', float())
        self.bbox_w = kwargs.get('bbox_w', float())
        self.bbox_h = kwargs.get('bbox_h', float())
        self.age_ms = kwargs.get('age_ms', int())
        self.valid_until_ms = kwargs.get('valid_until_ms', int())
        self.source_sensor = kwargs.get('source_sensor', str())
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
        if self.state != other.state:
            return False
        if self.confidence != other.confidence:
            return False
        if self.relevant_to_route != other.relevant_to_route:
            return False
        if self.distance_to_stop != other.distance_to_stop:
            return False
        if self.confirmed != other.confirmed:
            return False
        if self.in_stop_zone != other.in_stop_zone:
            return False
        if self.bbox_x != other.bbox_x:
            return False
        if self.bbox_y != other.bbox_y:
            return False
        if self.bbox_w != other.bbox_w:
            return False
        if self.bbox_h != other.bbox_h:
            return False
        if self.age_ms != other.age_ms:
            return False
        if self.valid_until_ms != other.valid_until_ms:
            return False
        if self.source_sensor != other.source_sensor:
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
    def state(self):
        """Message field 'state'."""
        return self._state

    @state.setter
    def state(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'state' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'state' field must be an unsigned integer in [0, 255]"
        self._state = value

    @property
    def confidence(self):
        """Message field 'confidence'."""
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'confidence' field must be of type 'float'"
        self._confidence = value

    @property
    def relevant_to_route(self):
        """Message field 'relevant_to_route'."""
        return self._relevant_to_route

    @relevant_to_route.setter
    def relevant_to_route(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'relevant_to_route' field must be of type 'bool'"
        self._relevant_to_route = value

    @property
    def distance_to_stop(self):
        """Message field 'distance_to_stop'."""
        return self._distance_to_stop

    @distance_to_stop.setter
    def distance_to_stop(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance_to_stop' field must be of type 'float'"
        self._distance_to_stop = value

    @property
    def confirmed(self):
        """Message field 'confirmed'."""
        return self._confirmed

    @confirmed.setter
    def confirmed(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'confirmed' field must be of type 'bool'"
        self._confirmed = value

    @property
    def in_stop_zone(self):
        """Message field 'in_stop_zone'."""
        return self._in_stop_zone

    @in_stop_zone.setter
    def in_stop_zone(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'in_stop_zone' field must be of type 'bool'"
        self._in_stop_zone = value

    @property
    def bbox_x(self):
        """Message field 'bbox_x'."""
        return self._bbox_x

    @bbox_x.setter
    def bbox_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'bbox_x' field must be of type 'float'"
        self._bbox_x = value

    @property
    def bbox_y(self):
        """Message field 'bbox_y'."""
        return self._bbox_y

    @bbox_y.setter
    def bbox_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'bbox_y' field must be of type 'float'"
        self._bbox_y = value

    @property
    def bbox_w(self):
        """Message field 'bbox_w'."""
        return self._bbox_w

    @bbox_w.setter
    def bbox_w(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'bbox_w' field must be of type 'float'"
        self._bbox_w = value

    @property
    def bbox_h(self):
        """Message field 'bbox_h'."""
        return self._bbox_h

    @bbox_h.setter
    def bbox_h(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'bbox_h' field must be of type 'float'"
        self._bbox_h = value

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
    def source_sensor(self):
        """Message field 'source_sensor'."""
        return self._source_sensor

    @source_sensor.setter
    def source_sensor(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'source_sensor' field must be of type 'str'"
        self._source_sensor = value

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
