# generated from rosidl_generator_py/resource/_idl.py.em
# with input from perception_msgs:msg/ObstacleTrack.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ObstacleTrack(type):
    """Metaclass of message 'ObstacleTrack'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'UNKNOWN_OBSTACLE': 0,
        'VEHICLE': 1,
        'PEDESTRIAN': 2,
        'CONE': 3,
        'BARRIER': 4,
        'SIGN_POLE': 5,
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
                'perception_msgs.msg.ObstacleTrack')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__obstacle_track
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__obstacle_track
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__obstacle_track
            cls._TYPE_SUPPORT = module.type_support_msg__msg__obstacle_track
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__obstacle_track

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'UNKNOWN_OBSTACLE': cls.__constants['UNKNOWN_OBSTACLE'],
            'VEHICLE': cls.__constants['VEHICLE'],
            'PEDESTRIAN': cls.__constants['PEDESTRIAN'],
            'CONE': cls.__constants['CONE'],
            'BARRIER': cls.__constants['BARRIER'],
            'SIGN_POLE': cls.__constants['SIGN_POLE'],
        }

    @property
    def UNKNOWN_OBSTACLE(self):
        """Message constant 'UNKNOWN_OBSTACLE'."""
        return Metaclass_ObstacleTrack.__constants['UNKNOWN_OBSTACLE']

    @property
    def VEHICLE(self):
        """Message constant 'VEHICLE'."""
        return Metaclass_ObstacleTrack.__constants['VEHICLE']

    @property
    def PEDESTRIAN(self):
        """Message constant 'PEDESTRIAN'."""
        return Metaclass_ObstacleTrack.__constants['PEDESTRIAN']

    @property
    def CONE(self):
        """Message constant 'CONE'."""
        return Metaclass_ObstacleTrack.__constants['CONE']

    @property
    def BARRIER(self):
        """Message constant 'BARRIER'."""
        return Metaclass_ObstacleTrack.__constants['BARRIER']

    @property
    def SIGN_POLE(self):
        """Message constant 'SIGN_POLE'."""
        return Metaclass_ObstacleTrack.__constants['SIGN_POLE']


class ObstacleTrack(metaclass=Metaclass_ObstacleTrack):
    """
    Message class 'ObstacleTrack'.

    Constants:
      UNKNOWN_OBSTACLE
      VEHICLE
      PEDESTRIAN
      CONE
      BARRIER
      SIGN_POLE
    """

    __slots__ = [
        '_track_id',
        '_class_label',
        '_confidence',
        '_position_x',
        '_position_y',
        '_distance',
        '_velocity_x',
        '_velocity_y',
        '_ttc',
        '_width',
        '_length',
        '_height',
        '_is_static',
        '_source_sensor',
        '_semantic_source',
        '_geometry_source',
        '_age_ms',
        '_valid_until_ms',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'track_id': 'uint32',
        'class_label': 'uint8',
        'confidence': 'float',
        'position_x': 'float',
        'position_y': 'float',
        'distance': 'float',
        'velocity_x': 'float',
        'velocity_y': 'float',
        'ttc': 'float',
        'width': 'float',
        'length': 'float',
        'height': 'float',
        'is_static': 'boolean',
        'source_sensor': 'string',
        'semantic_source': 'string',
        'geometry_source': 'string',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.track_id = kwargs.get('track_id', int())
        self.class_label = kwargs.get('class_label', int())
        self.confidence = kwargs.get('confidence', float())
        self.position_x = kwargs.get('position_x', float())
        self.position_y = kwargs.get('position_y', float())
        self.distance = kwargs.get('distance', float())
        self.velocity_x = kwargs.get('velocity_x', float())
        self.velocity_y = kwargs.get('velocity_y', float())
        self.ttc = kwargs.get('ttc', float())
        self.width = kwargs.get('width', float())
        self.length = kwargs.get('length', float())
        self.height = kwargs.get('height', float())
        self.is_static = kwargs.get('is_static', bool())
        self.source_sensor = kwargs.get('source_sensor', str())
        self.semantic_source = kwargs.get('semantic_source', str())
        self.geometry_source = kwargs.get('geometry_source', str())
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
        if self.track_id != other.track_id:
            return False
        if self.class_label != other.class_label:
            return False
        if self.confidence != other.confidence:
            return False
        if self.position_x != other.position_x:
            return False
        if self.position_y != other.position_y:
            return False
        if self.distance != other.distance:
            return False
        if self.velocity_x != other.velocity_x:
            return False
        if self.velocity_y != other.velocity_y:
            return False
        if self.ttc != other.ttc:
            return False
        if self.width != other.width:
            return False
        if self.length != other.length:
            return False
        if self.height != other.height:
            return False
        if self.is_static != other.is_static:
            return False
        if self.source_sensor != other.source_sensor:
            return False
        if self.semantic_source != other.semantic_source:
            return False
        if self.geometry_source != other.geometry_source:
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
    def track_id(self):
        """Message field 'track_id'."""
        return self._track_id

    @track_id.setter
    def track_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'track_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'track_id' field must be an unsigned integer in [0, 4294967295]"
        self._track_id = value

    @property
    def class_label(self):
        """Message field 'class_label'."""
        return self._class_label

    @class_label.setter
    def class_label(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'class_label' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'class_label' field must be an unsigned integer in [0, 255]"
        self._class_label = value

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
    def position_x(self):
        """Message field 'position_x'."""
        return self._position_x

    @position_x.setter
    def position_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position_x' field must be of type 'float'"
        self._position_x = value

    @property
    def position_y(self):
        """Message field 'position_y'."""
        return self._position_y

    @position_y.setter
    def position_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'position_y' field must be of type 'float'"
        self._position_y = value

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
    def velocity_x(self):
        """Message field 'velocity_x'."""
        return self._velocity_x

    @velocity_x.setter
    def velocity_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'velocity_x' field must be of type 'float'"
        self._velocity_x = value

    @property
    def velocity_y(self):
        """Message field 'velocity_y'."""
        return self._velocity_y

    @velocity_y.setter
    def velocity_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'velocity_y' field must be of type 'float'"
        self._velocity_y = value

    @property
    def ttc(self):
        """Message field 'ttc'."""
        return self._ttc

    @ttc.setter
    def ttc(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ttc' field must be of type 'float'"
        self._ttc = value

    @property
    def width(self):
        """Message field 'width'."""
        return self._width

    @width.setter
    def width(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'width' field must be of type 'float'"
        self._width = value

    @property
    def length(self):
        """Message field 'length'."""
        return self._length

    @length.setter
    def length(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'length' field must be of type 'float'"
        self._length = value

    @property
    def height(self):
        """Message field 'height'."""
        return self._height

    @height.setter
    def height(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'height' field must be of type 'float'"
        self._height = value

    @property
    def is_static(self):
        """Message field 'is_static'."""
        return self._is_static

    @is_static.setter
    def is_static(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'is_static' field must be of type 'bool'"
        self._is_static = value

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
    def semantic_source(self):
        """Message field 'semantic_source'."""
        return self._semantic_source

    @semantic_source.setter
    def semantic_source(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'semantic_source' field must be of type 'str'"
        self._semantic_source = value

    @property
    def geometry_source(self):
        """Message field 'geometry_source'."""
        return self._geometry_source

    @geometry_source.setter
    def geometry_source(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'geometry_source' field must be of type 'str'"
        self._geometry_source = value

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
