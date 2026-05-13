# generated from rosidl_generator_py/resource/_idl.py.em
# with input from perception_msgs:msg/TrafficSign.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TrafficSign(type):
    """Metaclass of message 'TrafficSign'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'UNKNOWN_SIGN': 0,
        'STOP': 1,
        'SPEED_LIMIT': 2,
        'NO_ENTRY': 3,
        'MANDATORY_LEFT': 4,
        'MANDATORY_RIGHT': 5,
        'MANDATORY_STRAIGHT': 6,
        'MANDATORY_LEFT_STRAIGHT': 7,
        'MANDATORY_RIGHT_STRAIGHT': 8,
        'ROUNDABOUT': 9,
        'PARKING': 10,
        'NO_PARKING': 11,
        'TUNNEL': 12,
        'PEDESTRIAN_CROSSING': 13,
        'NEW': 0,
        'TRACKED': 1,
        'ALREADY_HANDLED': 2,
        'STALE': 3,
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
                'perception_msgs.msg.TrafficSign')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__traffic_sign
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__traffic_sign
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__traffic_sign
            cls._TYPE_SUPPORT = module.type_support_msg__msg__traffic_sign
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__traffic_sign

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'UNKNOWN_SIGN': cls.__constants['UNKNOWN_SIGN'],
            'STOP': cls.__constants['STOP'],
            'SPEED_LIMIT': cls.__constants['SPEED_LIMIT'],
            'NO_ENTRY': cls.__constants['NO_ENTRY'],
            'MANDATORY_LEFT': cls.__constants['MANDATORY_LEFT'],
            'MANDATORY_RIGHT': cls.__constants['MANDATORY_RIGHT'],
            'MANDATORY_STRAIGHT': cls.__constants['MANDATORY_STRAIGHT'],
            'MANDATORY_LEFT_STRAIGHT': cls.__constants['MANDATORY_LEFT_STRAIGHT'],
            'MANDATORY_RIGHT_STRAIGHT': cls.__constants['MANDATORY_RIGHT_STRAIGHT'],
            'ROUNDABOUT': cls.__constants['ROUNDABOUT'],
            'PARKING': cls.__constants['PARKING'],
            'NO_PARKING': cls.__constants['NO_PARKING'],
            'TUNNEL': cls.__constants['TUNNEL'],
            'PEDESTRIAN_CROSSING': cls.__constants['PEDESTRIAN_CROSSING'],
            'NEW': cls.__constants['NEW'],
            'TRACKED': cls.__constants['TRACKED'],
            'ALREADY_HANDLED': cls.__constants['ALREADY_HANDLED'],
            'STALE': cls.__constants['STALE'],
        }

    @property
    def UNKNOWN_SIGN(self):
        """Message constant 'UNKNOWN_SIGN'."""
        return Metaclass_TrafficSign.__constants['UNKNOWN_SIGN']

    @property
    def STOP(self):
        """Message constant 'STOP'."""
        return Metaclass_TrafficSign.__constants['STOP']

    @property
    def SPEED_LIMIT(self):
        """Message constant 'SPEED_LIMIT'."""
        return Metaclass_TrafficSign.__constants['SPEED_LIMIT']

    @property
    def NO_ENTRY(self):
        """Message constant 'NO_ENTRY'."""
        return Metaclass_TrafficSign.__constants['NO_ENTRY']

    @property
    def MANDATORY_LEFT(self):
        """Message constant 'MANDATORY_LEFT'."""
        return Metaclass_TrafficSign.__constants['MANDATORY_LEFT']

    @property
    def MANDATORY_RIGHT(self):
        """Message constant 'MANDATORY_RIGHT'."""
        return Metaclass_TrafficSign.__constants['MANDATORY_RIGHT']

    @property
    def MANDATORY_STRAIGHT(self):
        """Message constant 'MANDATORY_STRAIGHT'."""
        return Metaclass_TrafficSign.__constants['MANDATORY_STRAIGHT']

    @property
    def MANDATORY_LEFT_STRAIGHT(self):
        """Message constant 'MANDATORY_LEFT_STRAIGHT'."""
        return Metaclass_TrafficSign.__constants['MANDATORY_LEFT_STRAIGHT']

    @property
    def MANDATORY_RIGHT_STRAIGHT(self):
        """Message constant 'MANDATORY_RIGHT_STRAIGHT'."""
        return Metaclass_TrafficSign.__constants['MANDATORY_RIGHT_STRAIGHT']

    @property
    def ROUNDABOUT(self):
        """Message constant 'ROUNDABOUT'."""
        return Metaclass_TrafficSign.__constants['ROUNDABOUT']

    @property
    def PARKING(self):
        """Message constant 'PARKING'."""
        return Metaclass_TrafficSign.__constants['PARKING']

    @property
    def NO_PARKING(self):
        """Message constant 'NO_PARKING'."""
        return Metaclass_TrafficSign.__constants['NO_PARKING']

    @property
    def TUNNEL(self):
        """Message constant 'TUNNEL'."""
        return Metaclass_TrafficSign.__constants['TUNNEL']

    @property
    def PEDESTRIAN_CROSSING(self):
        """Message constant 'PEDESTRIAN_CROSSING'."""
        return Metaclass_TrafficSign.__constants['PEDESTRIAN_CROSSING']

    @property
    def NEW(self):
        """Message constant 'NEW'."""
        return Metaclass_TrafficSign.__constants['NEW']

    @property
    def TRACKED(self):
        """Message constant 'TRACKED'."""
        return Metaclass_TrafficSign.__constants['TRACKED']

    @property
    def ALREADY_HANDLED(self):
        """Message constant 'ALREADY_HANDLED'."""
        return Metaclass_TrafficSign.__constants['ALREADY_HANDLED']

    @property
    def STALE(self):
        """Message constant 'STALE'."""
        return Metaclass_TrafficSign.__constants['STALE']


class TrafficSign(metaclass=Metaclass_TrafficSign):
    """
    Message class 'TrafficSign'.

    Constants:
      UNKNOWN_SIGN
      STOP
      SPEED_LIMIT
      NO_ENTRY
      MANDATORY_LEFT
      MANDATORY_RIGHT
      MANDATORY_STRAIGHT
      MANDATORY_LEFT_STRAIGHT
      MANDATORY_RIGHT_STRAIGHT
      ROUNDABOUT
      PARKING
      NO_PARKING
      TUNNEL
      PEDESTRIAN_CROSSING
      NEW
      TRACKED
      ALREADY_HANDLED
      STALE
    """

    __slots__ = [
        '_sign_id',
        '_type',
        '_confidence',
        '_relevant_to_route',
        '_distance',
        '_event_status',
        '_confirmed',
        '_bbox_x',
        '_bbox_y',
        '_bbox_w',
        '_bbox_h',
        '_age_ms',
        '_valid_until_ms',
        '_event_memory_ttl_ms',
        '_source_sensor',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'sign_id': 'uint32',
        'type': 'uint8',
        'confidence': 'float',
        'relevant_to_route': 'boolean',
        'distance': 'float',
        'event_status': 'uint8',
        'confirmed': 'boolean',
        'bbox_x': 'float',
        'bbox_y': 'float',
        'bbox_w': 'float',
        'bbox_h': 'float',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'event_memory_ttl_ms': 'uint32',
        'source_sensor': 'string',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.sign_id = kwargs.get('sign_id', int())
        self.type = kwargs.get('type', int())
        self.confidence = kwargs.get('confidence', float())
        self.relevant_to_route = kwargs.get('relevant_to_route', bool())
        self.distance = kwargs.get('distance', float())
        self.event_status = kwargs.get('event_status', int())
        self.confirmed = kwargs.get('confirmed', bool())
        self.bbox_x = kwargs.get('bbox_x', float())
        self.bbox_y = kwargs.get('bbox_y', float())
        self.bbox_w = kwargs.get('bbox_w', float())
        self.bbox_h = kwargs.get('bbox_h', float())
        self.age_ms = kwargs.get('age_ms', int())
        self.valid_until_ms = kwargs.get('valid_until_ms', int())
        self.event_memory_ttl_ms = kwargs.get('event_memory_ttl_ms', int())
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
        if self.sign_id != other.sign_id:
            return False
        if self.type != other.type:
            return False
        if self.confidence != other.confidence:
            return False
        if self.relevant_to_route != other.relevant_to_route:
            return False
        if self.distance != other.distance:
            return False
        if self.event_status != other.event_status:
            return False
        if self.confirmed != other.confirmed:
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
        if self.event_memory_ttl_ms != other.event_memory_ttl_ms:
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
    def sign_id(self):
        """Message field 'sign_id'."""
        return self._sign_id

    @sign_id.setter
    def sign_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'sign_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'sign_id' field must be an unsigned integer in [0, 4294967295]"
        self._sign_id = value

    @property  # noqa: A003
    def type(self):  # noqa: A003
        """Message field 'type'."""
        return self._type

    @type.setter  # noqa: A003
    def type(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'type' field must be an unsigned integer in [0, 255]"
        self._type = value

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
    def distance(self):
        """Message field 'distance'."""
        return self._distance

    @distance.setter
    def distance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance' field must be of type 'float'"
        self._distance = value

    @property
    def event_status(self):
        """Message field 'event_status'."""
        return self._event_status

    @event_status.setter
    def event_status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'event_status' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'event_status' field must be an unsigned integer in [0, 255]"
        self._event_status = value

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
    def event_memory_ttl_ms(self):
        """Message field 'event_memory_ttl_ms'."""
        return self._event_memory_ttl_ms

    @event_memory_ttl_ms.setter
    def event_memory_ttl_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'event_memory_ttl_ms' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'event_memory_ttl_ms' field must be an unsigned integer in [0, 4294967295]"
        self._event_memory_ttl_ms = value

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
