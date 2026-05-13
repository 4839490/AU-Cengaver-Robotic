# generated from rosidl_generator_py/resource/_idl.py.em
# with input from localization_msgs:msg/MapOrigin.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MapOrigin(type):
    """Metaclass of message 'MapOrigin'."""

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
            module = import_type_support('localization_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'localization_msgs.msg.MapOrigin')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__map_origin
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__map_origin
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__map_origin
            cls._TYPE_SUPPORT = module.type_support_msg__msg__map_origin
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__map_origin

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


class MapOrigin(metaclass=Metaclass_MapOrigin):
    """Message class 'MapOrigin'."""

    __slots__ = [
        '_header',
        '_lat_ref',
        '_lon_ref',
        '_alt_ref',
        '_yaw_ref',
        '_source',
        '_locked',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'lat_ref': 'double',
        'lon_ref': 'double',
        'alt_ref': 'double',
        'yaw_ref': 'double',
        'source': 'string',
        'locked': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.lat_ref = kwargs.get('lat_ref', float())
        self.lon_ref = kwargs.get('lon_ref', float())
        self.alt_ref = kwargs.get('alt_ref', float())
        self.yaw_ref = kwargs.get('yaw_ref', float())
        self.source = kwargs.get('source', str())
        self.locked = kwargs.get('locked', bool())

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
        if self.lat_ref != other.lat_ref:
            return False
        if self.lon_ref != other.lon_ref:
            return False
        if self.alt_ref != other.alt_ref:
            return False
        if self.yaw_ref != other.yaw_ref:
            return False
        if self.source != other.source:
            return False
        if self.locked != other.locked:
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
    def lat_ref(self):
        """Message field 'lat_ref'."""
        return self._lat_ref

    @lat_ref.setter
    def lat_ref(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lat_ref' field must be of type 'float'"
        self._lat_ref = value

    @property
    def lon_ref(self):
        """Message field 'lon_ref'."""
        return self._lon_ref

    @lon_ref.setter
    def lon_ref(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'lon_ref' field must be of type 'float'"
        self._lon_ref = value

    @property
    def alt_ref(self):
        """Message field 'alt_ref'."""
        return self._alt_ref

    @alt_ref.setter
    def alt_ref(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'alt_ref' field must be of type 'float'"
        self._alt_ref = value

    @property
    def yaw_ref(self):
        """Message field 'yaw_ref'."""
        return self._yaw_ref

    @yaw_ref.setter
    def yaw_ref(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'yaw_ref' field must be of type 'float'"
        self._yaw_ref = value

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
    def locked(self):
        """Message field 'locked'."""
        return self._locked

    @locked.setter
    def locked(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'locked' field must be of type 'bool'"
        self._locked = value
