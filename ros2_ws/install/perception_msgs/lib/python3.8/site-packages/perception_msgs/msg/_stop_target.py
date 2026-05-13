# generated from rosidl_generator_py/resource/_idl.py.em
# with input from perception_msgs:msg/StopTarget.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_StopTarget(type):
    """Metaclass of message 'StopTarget'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'TRAFFIC_LIGHT_STOP': 0,
        'STOP_SIGN': 1,
        'PICKUP': 2,
        'DROPOFF': 3,
        'LOW': 0,
        'NORMAL': 1,
        'HIGH': 2,
        'CRITICAL': 3,
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
                'perception_msgs.msg.StopTarget')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__stop_target
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__stop_target
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__stop_target
            cls._TYPE_SUPPORT = module.type_support_msg__msg__stop_target
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__stop_target

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'TRAFFIC_LIGHT_STOP': cls.__constants['TRAFFIC_LIGHT_STOP'],
            'STOP_SIGN': cls.__constants['STOP_SIGN'],
            'PICKUP': cls.__constants['PICKUP'],
            'DROPOFF': cls.__constants['DROPOFF'],
            'LOW': cls.__constants['LOW'],
            'NORMAL': cls.__constants['NORMAL'],
            'HIGH': cls.__constants['HIGH'],
            'CRITICAL': cls.__constants['CRITICAL'],
        }

    @property
    def TRAFFIC_LIGHT_STOP(self):
        """Message constant 'TRAFFIC_LIGHT_STOP'."""
        return Metaclass_StopTarget.__constants['TRAFFIC_LIGHT_STOP']

    @property
    def STOP_SIGN(self):
        """Message constant 'STOP_SIGN'."""
        return Metaclass_StopTarget.__constants['STOP_SIGN']

    @property
    def PICKUP(self):
        """Message constant 'PICKUP'."""
        return Metaclass_StopTarget.__constants['PICKUP']

    @property
    def DROPOFF(self):
        """Message constant 'DROPOFF'."""
        return Metaclass_StopTarget.__constants['DROPOFF']

    @property
    def LOW(self):
        """Message constant 'LOW'."""
        return Metaclass_StopTarget.__constants['LOW']

    @property
    def NORMAL(self):
        """Message constant 'NORMAL'."""
        return Metaclass_StopTarget.__constants['NORMAL']

    @property
    def HIGH(self):
        """Message constant 'HIGH'."""
        return Metaclass_StopTarget.__constants['HIGH']

    @property
    def CRITICAL(self):
        """Message constant 'CRITICAL'."""
        return Metaclass_StopTarget.__constants['CRITICAL']


class StopTarget(metaclass=Metaclass_StopTarget):
    """
    Message class 'StopTarget'.

    Constants:
      TRAFFIC_LIGHT_STOP
      STOP_SIGN
      PICKUP
      DROPOFF
      LOW
      NORMAL
      HIGH
      CRITICAL
    """

    __slots__ = [
        '_header',
        '_target_type',
        '_distance_from_front_bumper',
        '_target_x',
        '_target_y',
        '_confidence',
        '_source',
        '_age_ms',
        '_valid_until_ms',
        '_waypoint_id',
        '_heading_at_stop',
        '_priority',
        '_required_stop_duration_ms',
        '_stop_reason_id',
        '_source_topic',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'target_type': 'uint8',
        'distance_from_front_bumper': 'float',
        'target_x': 'float',
        'target_y': 'float',
        'confidence': 'float',
        'source': 'string',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'waypoint_id': 'int32',
        'heading_at_stop': 'float',
        'priority': 'uint8',
        'required_stop_duration_ms': 'uint32',
        'stop_reason_id': 'uint32',
        'source_topic': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.target_type = kwargs.get('target_type', int())
        self.distance_from_front_bumper = kwargs.get('distance_from_front_bumper', float())
        self.target_x = kwargs.get('target_x', float())
        self.target_y = kwargs.get('target_y', float())
        self.confidence = kwargs.get('confidence', float())
        self.source = kwargs.get('source', str())
        self.age_ms = kwargs.get('age_ms', int())
        self.valid_until_ms = kwargs.get('valid_until_ms', int())
        self.waypoint_id = kwargs.get('waypoint_id', int())
        self.heading_at_stop = kwargs.get('heading_at_stop', float())
        self.priority = kwargs.get('priority', int())
        self.required_stop_duration_ms = kwargs.get('required_stop_duration_ms', int())
        self.stop_reason_id = kwargs.get('stop_reason_id', int())
        self.source_topic = kwargs.get('source_topic', str())

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
        if self.target_type != other.target_type:
            return False
        if self.distance_from_front_bumper != other.distance_from_front_bumper:
            return False
        if self.target_x != other.target_x:
            return False
        if self.target_y != other.target_y:
            return False
        if self.confidence != other.confidence:
            return False
        if self.source != other.source:
            return False
        if self.age_ms != other.age_ms:
            return False
        if self.valid_until_ms != other.valid_until_ms:
            return False
        if self.waypoint_id != other.waypoint_id:
            return False
        if self.heading_at_stop != other.heading_at_stop:
            return False
        if self.priority != other.priority:
            return False
        if self.required_stop_duration_ms != other.required_stop_duration_ms:
            return False
        if self.stop_reason_id != other.stop_reason_id:
            return False
        if self.source_topic != other.source_topic:
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
    def target_type(self):
        """Message field 'target_type'."""
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'target_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'target_type' field must be an unsigned integer in [0, 255]"
        self._target_type = value

    @property
    def distance_from_front_bumper(self):
        """Message field 'distance_from_front_bumper'."""
        return self._distance_from_front_bumper

    @distance_from_front_bumper.setter
    def distance_from_front_bumper(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance_from_front_bumper' field must be of type 'float'"
        self._distance_from_front_bumper = value

    @property
    def target_x(self):
        """Message field 'target_x'."""
        return self._target_x

    @target_x.setter
    def target_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'target_x' field must be of type 'float'"
        self._target_x = value

    @property
    def target_y(self):
        """Message field 'target_y'."""
        return self._target_y

    @target_y.setter
    def target_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'target_y' field must be of type 'float'"
        self._target_y = value

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
    def source(self):
        """Message field 'source'."""
        return self._source

    @source.setter
    def source(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'source' field must be of type 'str'"
        self._source = value

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
    def waypoint_id(self):
        """Message field 'waypoint_id'."""
        return self._waypoint_id

    @waypoint_id.setter
    def waypoint_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'waypoint_id' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'waypoint_id' field must be an integer in [-2147483648, 2147483647]"
        self._waypoint_id = value

    @property
    def heading_at_stop(self):
        """Message field 'heading_at_stop'."""
        return self._heading_at_stop

    @heading_at_stop.setter
    def heading_at_stop(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'heading_at_stop' field must be of type 'float'"
        self._heading_at_stop = value

    @property
    def priority(self):
        """Message field 'priority'."""
        return self._priority

    @priority.setter
    def priority(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'priority' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'priority' field must be an unsigned integer in [0, 255]"
        self._priority = value

    @property
    def required_stop_duration_ms(self):
        """Message field 'required_stop_duration_ms'."""
        return self._required_stop_duration_ms

    @required_stop_duration_ms.setter
    def required_stop_duration_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'required_stop_duration_ms' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'required_stop_duration_ms' field must be an unsigned integer in [0, 4294967295]"
        self._required_stop_duration_ms = value

    @property
    def stop_reason_id(self):
        """Message field 'stop_reason_id'."""
        return self._stop_reason_id

    @stop_reason_id.setter
    def stop_reason_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'stop_reason_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'stop_reason_id' field must be an unsigned integer in [0, 4294967295]"
        self._stop_reason_id = value

    @property
    def source_topic(self):
        """Message field 'source_topic'."""
        return self._source_topic

    @source_topic.setter
    def source_topic(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'source_topic' field must be of type 'str'"
        self._source_topic = value
