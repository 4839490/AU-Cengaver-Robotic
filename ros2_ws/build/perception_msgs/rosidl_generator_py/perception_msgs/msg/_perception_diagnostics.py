# generated from rosidl_generator_py/resource/_idl.py.em
# with input from perception_msgs:msg/PerceptionDiagnostics.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_PerceptionDiagnostics(type):
    """Metaclass of message 'PerceptionDiagnostics'."""

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
                'perception_msgs.msg.PerceptionDiagnostics')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__perception_diagnostics
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__perception_diagnostics
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__perception_diagnostics
            cls._TYPE_SUPPORT = module.type_support_msg__msg__perception_diagnostics
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__perception_diagnostics

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


class PerceptionDiagnostics(metaclass=Metaclass_PerceptionDiagnostics):
    """Message class 'PerceptionDiagnostics'."""

    __slots__ = [
        '_header',
        '_node_name',
        '_input_hz',
        '_output_hz',
        '_latency_ms',
        '_last_msg_age_ms',
        '_mean_confidence',
        '_num_outputs',
        '_gpu_utilization',
        '_warning_flags',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'node_name': 'string',
        'input_hz': 'float',
        'output_hz': 'float',
        'latency_ms': 'float',
        'last_msg_age_ms': 'uint32',
        'mean_confidence': 'float',
        'num_outputs': 'uint32',
        'gpu_utilization': 'float',
        'warning_flags': 'sequence<string>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.node_name = kwargs.get('node_name', str())
        self.input_hz = kwargs.get('input_hz', float())
        self.output_hz = kwargs.get('output_hz', float())
        self.latency_ms = kwargs.get('latency_ms', float())
        self.last_msg_age_ms = kwargs.get('last_msg_age_ms', int())
        self.mean_confidence = kwargs.get('mean_confidence', float())
        self.num_outputs = kwargs.get('num_outputs', int())
        self.gpu_utilization = kwargs.get('gpu_utilization', float())
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
        if self.node_name != other.node_name:
            return False
        if self.input_hz != other.input_hz:
            return False
        if self.output_hz != other.output_hz:
            return False
        if self.latency_ms != other.latency_ms:
            return False
        if self.last_msg_age_ms != other.last_msg_age_ms:
            return False
        if self.mean_confidence != other.mean_confidence:
            return False
        if self.num_outputs != other.num_outputs:
            return False
        if self.gpu_utilization != other.gpu_utilization:
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
    def node_name(self):
        """Message field 'node_name'."""
        return self._node_name

    @node_name.setter
    def node_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'node_name' field must be of type 'str'"
        self._node_name = value

    @property
    def input_hz(self):
        """Message field 'input_hz'."""
        return self._input_hz

    @input_hz.setter
    def input_hz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'input_hz' field must be of type 'float'"
        self._input_hz = value

    @property
    def output_hz(self):
        """Message field 'output_hz'."""
        return self._output_hz

    @output_hz.setter
    def output_hz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'output_hz' field must be of type 'float'"
        self._output_hz = value

    @property
    def latency_ms(self):
        """Message field 'latency_ms'."""
        return self._latency_ms

    @latency_ms.setter
    def latency_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'latency_ms' field must be of type 'float'"
        self._latency_ms = value

    @property
    def last_msg_age_ms(self):
        """Message field 'last_msg_age_ms'."""
        return self._last_msg_age_ms

    @last_msg_age_ms.setter
    def last_msg_age_ms(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'last_msg_age_ms' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'last_msg_age_ms' field must be an unsigned integer in [0, 4294967295]"
        self._last_msg_age_ms = value

    @property
    def mean_confidence(self):
        """Message field 'mean_confidence'."""
        return self._mean_confidence

    @mean_confidence.setter
    def mean_confidence(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'mean_confidence' field must be of type 'float'"
        self._mean_confidence = value

    @property
    def num_outputs(self):
        """Message field 'num_outputs'."""
        return self._num_outputs

    @num_outputs.setter
    def num_outputs(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'num_outputs' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'num_outputs' field must be an unsigned integer in [0, 4294967295]"
        self._num_outputs = value

    @property
    def gpu_utilization(self):
        """Message field 'gpu_utilization'."""
        return self._gpu_utilization

    @gpu_utilization.setter
    def gpu_utilization(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gpu_utilization' field must be of type 'float'"
        self._gpu_utilization = value

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
