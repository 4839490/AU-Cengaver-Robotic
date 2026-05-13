# generated from rosidl_generator_py/resource/_idl.py.em
# with input from planning_msgs:msg/ActiveRouteContext.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ActiveRouteContext(type):
    """Metaclass of message 'ActiveRouteContext'."""

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
                'planning_msgs.msg.ActiveRouteContext')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__active_route_context
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__active_route_context
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__active_route_context
            cls._TYPE_SUPPORT = module.type_support_msg__msg__active_route_context
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__active_route_context

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


class ActiveRouteContext(metaclass=Metaclass_ActiveRouteContext):
    """Message class 'ActiveRouteContext'."""

    __slots__ = [
        '_header',
        '_active_waypoint_id',
        '_target_x',
        '_target_y',
        '_target_heading',
        '_planner_mode',
        '_route_direction',
        '_planned_trajectory',
        '_lookahead_distance',
        '_in_stop_zone',
        '_distance_to_stop_zone',
        '_localization_confidence',
        '_ego_speed_mps',
        '_route_context_valid',
        '_age_ms',
        '_valid_until_ms',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'active_waypoint_id': 'uint32',
        'target_x': 'float',
        'target_y': 'float',
        'target_heading': 'float',
        'planner_mode': 'uint8',
        'route_direction': 'string',
        'planned_trajectory': 'sequence<geometry_msgs/Point>',
        'lookahead_distance': 'float',
        'in_stop_zone': 'boolean',
        'distance_to_stop_zone': 'float',
        'localization_confidence': 'float',
        'ego_speed_mps': 'float',
        'route_context_valid': 'boolean',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point')),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
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
        self.active_waypoint_id = kwargs.get('active_waypoint_id', int())
        self.target_x = kwargs.get('target_x', float())
        self.target_y = kwargs.get('target_y', float())
        self.target_heading = kwargs.get('target_heading', float())
        self.planner_mode = kwargs.get('planner_mode', int())
        self.route_direction = kwargs.get('route_direction', str())
        self.planned_trajectory = kwargs.get('planned_trajectory', [])
        self.lookahead_distance = kwargs.get('lookahead_distance', float())
        self.in_stop_zone = kwargs.get('in_stop_zone', bool())
        self.distance_to_stop_zone = kwargs.get('distance_to_stop_zone', float())
        self.localization_confidence = kwargs.get('localization_confidence', float())
        self.ego_speed_mps = kwargs.get('ego_speed_mps', float())
        self.route_context_valid = kwargs.get('route_context_valid', bool())
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
        if self.active_waypoint_id != other.active_waypoint_id:
            return False
        if self.target_x != other.target_x:
            return False
        if self.target_y != other.target_y:
            return False
        if self.target_heading != other.target_heading:
            return False
        if self.planner_mode != other.planner_mode:
            return False
        if self.route_direction != other.route_direction:
            return False
        if self.planned_trajectory != other.planned_trajectory:
            return False
        if self.lookahead_distance != other.lookahead_distance:
            return False
        if self.in_stop_zone != other.in_stop_zone:
            return False
        if self.distance_to_stop_zone != other.distance_to_stop_zone:
            return False
        if self.localization_confidence != other.localization_confidence:
            return False
        if self.ego_speed_mps != other.ego_speed_mps:
            return False
        if self.route_context_valid != other.route_context_valid:
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
    def active_waypoint_id(self):
        """Message field 'active_waypoint_id'."""
        return self._active_waypoint_id

    @active_waypoint_id.setter
    def active_waypoint_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'active_waypoint_id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'active_waypoint_id' field must be an unsigned integer in [0, 4294967295]"
        self._active_waypoint_id = value

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
    def target_heading(self):
        """Message field 'target_heading'."""
        return self._target_heading

    @target_heading.setter
    def target_heading(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'target_heading' field must be of type 'float'"
        self._target_heading = value

    @property
    def planner_mode(self):
        """Message field 'planner_mode'."""
        return self._planner_mode

    @planner_mode.setter
    def planner_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'planner_mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'planner_mode' field must be an unsigned integer in [0, 255]"
        self._planner_mode = value

    @property
    def route_direction(self):
        """Message field 'route_direction'."""
        return self._route_direction

    @route_direction.setter
    def route_direction(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'route_direction' field must be of type 'str'"
        self._route_direction = value

    @property
    def planned_trajectory(self):
        """Message field 'planned_trajectory'."""
        return self._planned_trajectory

    @planned_trajectory.setter
    def planned_trajectory(self, value):
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
                "The 'planned_trajectory' field must be a set or sequence and each value of type 'Point'"
        self._planned_trajectory = value

    @property
    def lookahead_distance(self):
        """Message field 'lookahead_distance'."""
        return self._lookahead_distance

    @lookahead_distance.setter
    def lookahead_distance(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lookahead_distance' field must be of type 'float'"
        self._lookahead_distance = value

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
    def distance_to_stop_zone(self):
        """Message field 'distance_to_stop_zone'."""
        return self._distance_to_stop_zone

    @distance_to_stop_zone.setter
    def distance_to_stop_zone(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance_to_stop_zone' field must be of type 'float'"
        self._distance_to_stop_zone = value

    @property
    def localization_confidence(self):
        """Message field 'localization_confidence'."""
        return self._localization_confidence

    @localization_confidence.setter
    def localization_confidence(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'localization_confidence' field must be of type 'float'"
        self._localization_confidence = value

    @property
    def ego_speed_mps(self):
        """Message field 'ego_speed_mps'."""
        return self._ego_speed_mps

    @ego_speed_mps.setter
    def ego_speed_mps(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ego_speed_mps' field must be of type 'float'"
        self._ego_speed_mps = value

    @property
    def route_context_valid(self):
        """Message field 'route_context_valid'."""
        return self._route_context_valid

    @route_context_valid.setter
    def route_context_valid(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'route_context_valid' field must be of type 'bool'"
        self._route_context_valid = value

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
