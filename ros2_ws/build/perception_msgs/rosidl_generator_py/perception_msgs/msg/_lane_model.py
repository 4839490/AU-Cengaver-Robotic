# generated from rosidl_generator_py/resource/_idl.py.em
# with input from perception_msgs:msg/LaneModel.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_LaneModel(type):
    """Metaclass of message 'LaneModel'."""

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
            module = import_type_support('perception_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'perception_msgs.msg.LaneModel')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__lane_model
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__lane_model
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__lane_model
            cls._TYPE_SUPPORT = module.type_support_msg__msg__lane_model
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__lane_model

            from geometry_msgs.msg import Point
            if Point.__class__._TYPE_SUPPORT is None:
                Point.__class__.__import_type_support__()

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


class LaneModel(metaclass=Metaclass_LaneModel):
    """Message class 'LaneModel'."""

    __slots__ = [
        '_header',
        '_centerline',
        '_left_boundary',
        '_right_boundary',
        '_lane_confidence',
        '_lane_lost',
        '_curvature',
        '_lane_width_estimate',
        '_age_ms',
        '_valid_until_ms',
        '_source_sensor',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'centerline': 'sequence<geometry_msgs/Point>',
        'left_boundary': 'sequence<geometry_msgs/Point>',
        'right_boundary': 'sequence<geometry_msgs/Point>',
        'lane_confidence': 'float',
        'lane_lost': 'boolean',
        'curvature': 'float',
        'lane_width_estimate': 'float',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'source_sensor': 'string',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
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
        self.centerline = kwargs.get('centerline', [])
        self.left_boundary = kwargs.get('left_boundary', [])
        self.right_boundary = kwargs.get('right_boundary', [])
        self.lane_confidence = kwargs.get('lane_confidence', float())
        self.lane_lost = kwargs.get('lane_lost', bool())
        self.curvature = kwargs.get('curvature', float())
        self.lane_width_estimate = kwargs.get('lane_width_estimate', float())
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
        if self.centerline != other.centerline:
            return False
        if self.left_boundary != other.left_boundary:
            return False
        if self.right_boundary != other.right_boundary:
            return False
        if self.lane_confidence != other.lane_confidence:
            return False
        if self.lane_lost != other.lane_lost:
            return False
        if self.curvature != other.curvature:
            return False
        if self.lane_width_estimate != other.lane_width_estimate:
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
    def centerline(self):
        """Message field 'centerline'."""
        return self._centerline

    @centerline.setter
    def centerline(self, value):
        if __debug__:
            from geometry_msgs.msg import Point
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
                 all(isinstance(v, Point) for v in value) and
                 True), \
                "The 'centerline' field must be a set or sequence and each value of type 'Point'"
        self._centerline = value

    @property
    def left_boundary(self):
        """Message field 'left_boundary'."""
        return self._left_boundary

    @left_boundary.setter
    def left_boundary(self, value):
        if __debug__:
            from geometry_msgs.msg import Point
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
                 all(isinstance(v, Point) for v in value) and
                 True), \
                "The 'left_boundary' field must be a set or sequence and each value of type 'Point'"
        self._left_boundary = value

    @property
    def right_boundary(self):
        """Message field 'right_boundary'."""
        return self._right_boundary

    @right_boundary.setter
    def right_boundary(self, value):
        if __debug__:
            from geometry_msgs.msg import Point
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
                 all(isinstance(v, Point) for v in value) and
                 True), \
                "The 'right_boundary' field must be a set or sequence and each value of type 'Point'"
        self._right_boundary = value

    @property
    def lane_confidence(self):
        """Message field 'lane_confidence'."""
        return self._lane_confidence

    @lane_confidence.setter
    def lane_confidence(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lane_confidence' field must be of type 'float'"
        self._lane_confidence = value

    @property
    def lane_lost(self):
        """Message field 'lane_lost'."""
        return self._lane_lost

    @lane_lost.setter
    def lane_lost(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'lane_lost' field must be of type 'bool'"
        self._lane_lost = value

    @property
    def curvature(self):
        """Message field 'curvature'."""
        return self._curvature

    @curvature.setter
    def curvature(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'curvature' field must be of type 'float'"
        self._curvature = value

    @property
    def lane_width_estimate(self):
        """Message field 'lane_width_estimate'."""
        return self._lane_width_estimate

    @lane_width_estimate.setter
    def lane_width_estimate(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lane_width_estimate' field must be of type 'float'"
        self._lane_width_estimate = value

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
