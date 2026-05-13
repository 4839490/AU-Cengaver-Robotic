# generated from rosidl_generator_py/resource/_idl.py.em
# with input from localization_msgs:msg/RawGps.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RawGps(type):
    """Metaclass of message 'RawGps'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'FIX_NONE': 0,
        'FIX_GPS': 1,
        'FIX_DGPS': 2,
        'FIX_RTK_FLOAT': 4,
        'FIX_RTK_FIXED': 5,
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
                'localization_msgs.msg.RawGps')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__raw_gps
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__raw_gps
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__raw_gps
            cls._TYPE_SUPPORT = module.type_support_msg__msg__raw_gps
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__raw_gps

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'FIX_NONE': cls.__constants['FIX_NONE'],
            'FIX_GPS': cls.__constants['FIX_GPS'],
            'FIX_DGPS': cls.__constants['FIX_DGPS'],
            'FIX_RTK_FLOAT': cls.__constants['FIX_RTK_FLOAT'],
            'FIX_RTK_FIXED': cls.__constants['FIX_RTK_FIXED'],
        }

    @property
    def FIX_NONE(self):
        """Message constant 'FIX_NONE'."""
        return Metaclass_RawGps.__constants['FIX_NONE']

    @property
    def FIX_GPS(self):
        """Message constant 'FIX_GPS'."""
        return Metaclass_RawGps.__constants['FIX_GPS']

    @property
    def FIX_DGPS(self):
        """Message constant 'FIX_DGPS'."""
        return Metaclass_RawGps.__constants['FIX_DGPS']

    @property
    def FIX_RTK_FLOAT(self):
        """Message constant 'FIX_RTK_FLOAT'."""
        return Metaclass_RawGps.__constants['FIX_RTK_FLOAT']

    @property
    def FIX_RTK_FIXED(self):
        """Message constant 'FIX_RTK_FIXED'."""
        return Metaclass_RawGps.__constants['FIX_RTK_FIXED']


class RawGps(metaclass=Metaclass_RawGps):
    """
    Message class 'RawGps'.

    Constants:
      FIX_NONE
      FIX_GPS
      FIX_DGPS
      FIX_RTK_FLOAT
      FIX_RTK_FIXED
    """

    __slots__ = [
        '_header',
        '_age_ms',
        '_valid_until_ms',
        '_latitude',
        '_longitude',
        '_altitude',
        '_speed',
        '_heading_deg',
        '_hdop',
        '_vdop',
        '_fix_type',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'age_ms': 'uint32',
        'valid_until_ms': 'uint32',
        'latitude': 'double',
        'longitude': 'double',
        'altitude': 'double',
        'speed': 'double',
        'heading_deg': 'double',
        'hdop': 'double',
        'vdop': 'double',
        'fix_type': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.age_ms = kwargs.get('age_ms', int())
        self.valid_until_ms = kwargs.get('valid_until_ms', int())
        self.latitude = kwargs.get('latitude', float())
        self.longitude = kwargs.get('longitude', float())
        self.altitude = kwargs.get('altitude', float())
        self.speed = kwargs.get('speed', float())
        self.heading_deg = kwargs.get('heading_deg', float())
        self.hdop = kwargs.get('hdop', float())
        self.vdop = kwargs.get('vdop', float())
        self.fix_type = kwargs.get('fix_type', int())

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
        if self.age_ms != other.age_ms:
            return False
        if self.valid_until_ms != other.valid_until_ms:
            return False
        if self.latitude != other.latitude:
            return False
        if self.longitude != other.longitude:
            return False
        if self.altitude != other.altitude:
            return False
        if self.speed != other.speed:
            return False
        if self.heading_deg != other.heading_deg:
            return False
        if self.hdop != other.hdop:
            return False
        if self.vdop != other.vdop:
            return False
        if self.fix_type != other.fix_type:
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
    def latitude(self):
        """Message field 'latitude'."""
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'latitude' field must be of type 'float'"
        self._latitude = value

    @property
    def longitude(self):
        """Message field 'longitude'."""
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'longitude' field must be of type 'float'"
        self._longitude = value

    @property
    def altitude(self):
        """Message field 'altitude'."""
        return self._altitude

    @altitude.setter
    def altitude(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'altitude' field must be of type 'float'"
        self._altitude = value

    @property
    def speed(self):
        """Message field 'speed'."""
        return self._speed

    @speed.setter
    def speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'speed' field must be of type 'float'"
        self._speed = value

    @property
    def heading_deg(self):
        """Message field 'heading_deg'."""
        return self._heading_deg

    @heading_deg.setter
    def heading_deg(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'heading_deg' field must be of type 'float'"
        self._heading_deg = value

    @property
    def hdop(self):
        """Message field 'hdop'."""
        return self._hdop

    @hdop.setter
    def hdop(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'hdop' field must be of type 'float'"
        self._hdop = value

    @property
    def vdop(self):
        """Message field 'vdop'."""
        return self._vdop

    @vdop.setter
    def vdop(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'vdop' field must be of type 'float'"
        self._vdop = value

    @property
    def fix_type(self):
        """Message field 'fix_type'."""
        return self._fix_type

    @fix_type.setter
    def fix_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'fix_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'fix_type' field must be an unsigned integer in [0, 255]"
        self._fix_type = value
