# generated from rosidl_generator_py/resource/_idl.py.em
# with input from planning_msgs:msg/PlanningStatus.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_PlanningStatus(type):
    """Metaclass of message 'PlanningStatus'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'STATUS_ACTIVE': 0,
        'STATUS_WAITING_FSM': 1,
        'STATUS_OBSTACLE_BLOCKED': 2,
        'STATUS_LANE_LOST': 3,
        'STATUS_LOCALIZATION_DEGRADED': 4,
        'STATUS_EMERGENCY': 5,
        'STATUS_MISSION_COMPLETE': 6,
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
                'planning_msgs.msg.PlanningStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__planning_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__planning_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__planning_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__planning_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__planning_status

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'STATUS_ACTIVE': cls.__constants['STATUS_ACTIVE'],
            'STATUS_WAITING_FSM': cls.__constants['STATUS_WAITING_FSM'],
            'STATUS_OBSTACLE_BLOCKED': cls.__constants['STATUS_OBSTACLE_BLOCKED'],
            'STATUS_LANE_LOST': cls.__constants['STATUS_LANE_LOST'],
            'STATUS_LOCALIZATION_DEGRADED': cls.__constants['STATUS_LOCALIZATION_DEGRADED'],
            'STATUS_EMERGENCY': cls.__constants['STATUS_EMERGENCY'],
            'STATUS_MISSION_COMPLETE': cls.__constants['STATUS_MISSION_COMPLETE'],
        }

    @property
    def STATUS_ACTIVE(self):
        """Message constant 'STATUS_ACTIVE'."""
        return Metaclass_PlanningStatus.__constants['STATUS_ACTIVE']

    @property
    def STATUS_WAITING_FSM(self):
        """Message constant 'STATUS_WAITING_FSM'."""
        return Metaclass_PlanningStatus.__constants['STATUS_WAITING_FSM']

    @property
    def STATUS_OBSTACLE_BLOCKED(self):
        """Message constant 'STATUS_OBSTACLE_BLOCKED'."""
        return Metaclass_PlanningStatus.__constants['STATUS_OBSTACLE_BLOCKED']

    @property
    def STATUS_LANE_LOST(self):
        """Message constant 'STATUS_LANE_LOST'."""
        return Metaclass_PlanningStatus.__constants['STATUS_LANE_LOST']

    @property
    def STATUS_LOCALIZATION_DEGRADED(self):
        """Message constant 'STATUS_LOCALIZATION_DEGRADED'."""
        return Metaclass_PlanningStatus.__constants['STATUS_LOCALIZATION_DEGRADED']

    @property
    def STATUS_EMERGENCY(self):
        """Message constant 'STATUS_EMERGENCY'."""
        return Metaclass_PlanningStatus.__constants['STATUS_EMERGENCY']

    @property
    def STATUS_MISSION_COMPLETE(self):
        """Message constant 'STATUS_MISSION_COMPLETE'."""
        return Metaclass_PlanningStatus.__constants['STATUS_MISSION_COMPLETE']


class PlanningStatus(metaclass=Metaclass_PlanningStatus):
    """
    Message class 'PlanningStatus'.

    Constants:
      STATUS_ACTIVE
      STATUS_WAITING_FSM
      STATUS_OBSTACLE_BLOCKED
      STATUS_LANE_LOST
      STATUS_LOCALIZATION_DEGRADED
      STATUS_EMERGENCY
      STATUS_MISSION_COMPLETE
    """

    __slots__ = [
        '_header',
        '_status',
        '_trajectory_valid',
        '_goal_reached',
        '_parking_entry_reached',
        '_obstacle_blocking',
        '_lane_lost',
        '_localization_degraded',
        '_active_waypoint_id',
        '_distance_to_goal',
        '_planner_mode',
        '_age_ms',
        '_valid_until_ms',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'status': 'uint8',
        'trajectory_valid': 'boolean',
        'goal_reached': 'boolean',
        'parking_entry_reached': 'boolean',
        'obstacle_blocking': 'boolean',
        'lane_lost': 'boolean',
        'localization_degraded': 'boolean',
        'active_waypoint_id': 'uint32',
        'distance_to_goal': 'float',
        'planner_mode': 'uint8',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
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
        self.status = kwargs.get('status', int())
        self.trajectory_valid = kwargs.get('trajectory_valid', bool())
        self.goal_reached = kwargs.get('goal_reached', bool())
        self.parking_entry_reached = kwargs.get('parking_entry_reached', bool())
        self.obstacle_blocking = kwargs.get('obstacle_blocking', bool())
        self.lane_lost = kwargs.get('lane_lost', bool())
        self.localization_degraded = kwargs.get('localization_degraded', bool())
        self.active_waypoint_id = kwargs.get('active_waypoint_id', int())
        self.distance_to_goal = kwargs.get('distance_to_goal', float())
        self.planner_mode = kwargs.get('planner_mode', int())
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
        if self.status != other.status:
            return False
        if self.trajectory_valid != other.trajectory_valid:
            return False
        if self.goal_reached != other.goal_reached:
            return False
        if self.parking_entry_reached != other.parking_entry_reached:
            return False
        if self.obstacle_blocking != other.obstacle_blocking:
            return False
        if self.lane_lost != other.lane_lost:
            return False
        if self.localization_degraded != other.localization_degraded:
            return False
        if self.active_waypoint_id != other.active_waypoint_id:
            return False
        if self.distance_to_goal != other.distance_to_goal:
            return False
        if self.planner_mode != other.planner_mode:
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
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'status' field must be an unsigned integer in [0, 255]"
        self._status = value

    @property
    def trajectory_valid(self):
        """Message field 'trajectory_valid'."""
        return self._trajectory_valid

    @trajectory_valid.setter
    def trajectory_valid(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'trajectory_valid' field must be of type 'bool'"
        self._trajectory_valid = value

    @property
    def goal_reached(self):
        """Message field 'goal_reached'."""
        return self._goal_reached

    @goal_reached.setter
    def goal_reached(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'goal_reached' field must be of type 'bool'"
        self._goal_reached = value

    @property
    def parking_entry_reached(self):
        """Message field 'parking_entry_reached'."""
        return self._parking_entry_reached

    @parking_entry_reached.setter
    def parking_entry_reached(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'parking_entry_reached' field must be of type 'bool'"
        self._parking_entry_reached = value

    @property
    def obstacle_blocking(self):
        """Message field 'obstacle_blocking'."""
        return self._obstacle_blocking

    @obstacle_blocking.setter
    def obstacle_blocking(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'obstacle_blocking' field must be of type 'bool'"
        self._obstacle_blocking = value

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
    def localization_degraded(self):
        """Message field 'localization_degraded'."""
        return self._localization_degraded

    @localization_degraded.setter
    def localization_degraded(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'localization_degraded' field must be of type 'bool'"
        self._localization_degraded = value

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
    def distance_to_goal(self):
        """Message field 'distance_to_goal'."""
        return self._distance_to_goal

    @distance_to_goal.setter
    def distance_to_goal(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'distance_to_goal' field must be of type 'float'"
        self._distance_to_goal = value

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
