# generated from rosidl_generator_py/resource/_idl.py.em
# with input from geographic_msgs:msg/RouteNetwork.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RouteNetwork(type):
    """Metaclass of message 'RouteNetwork'."""

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
            module = import_type_support('geographic_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'geographic_msgs.msg.RouteNetwork')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__route_network
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__route_network
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__route_network
            cls._TYPE_SUPPORT = module.type_support_msg__msg__route_network
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__route_network

            from geographic_msgs.msg import BoundingBox
            if BoundingBox.__class__._TYPE_SUPPORT is None:
                BoundingBox.__class__.__import_type_support__()

            from geographic_msgs.msg import KeyValue
            if KeyValue.__class__._TYPE_SUPPORT is None:
                KeyValue.__class__.__import_type_support__()

            from geographic_msgs.msg import RouteSegment
            if RouteSegment.__class__._TYPE_SUPPORT is None:
                RouteSegment.__class__.__import_type_support__()

            from geographic_msgs.msg import WayPoint
            if WayPoint.__class__._TYPE_SUPPORT is None:
                WayPoint.__class__.__import_type_support__()

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RouteNetwork(metaclass=Metaclass_RouteNetwork):
    """Message class 'RouteNetwork'."""

    __slots__ = [
        '_header',
        '_id',
        '_bounds',
        '_points',
        '_segments',
        '_props',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'id': 'unique_identifier_msgs/UUID',
        'bounds': 'geographic_msgs/BoundingBox',
        'points': 'sequence<geographic_msgs/WayPoint>',
        'segments': 'sequence<geographic_msgs/RouteSegment>',
        'props': 'sequence<geographic_msgs/KeyValue>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geographic_msgs', 'msg'], 'BoundingBox'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geographic_msgs', 'msg'], 'WayPoint')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geographic_msgs', 'msg'], 'RouteSegment')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geographic_msgs', 'msg'], 'KeyValue')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        from unique_identifier_msgs.msg import UUID
        self.id = kwargs.get('id', UUID())
        from geographic_msgs.msg import BoundingBox
        self.bounds = kwargs.get('bounds', BoundingBox())
        self.points = kwargs.get('points', [])
        self.segments = kwargs.get('segments', [])
        self.props = kwargs.get('props', [])

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
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
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.id != other.id:
            return False
        if self.bounds != other.bounds:
            return False
        if self.points != other.points:
            return False
        if self.segments != other.segments:
            return False
        if self.props != other.props:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if self._check_fields:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property  # noqa: A003
    def id(self):  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value):  # noqa: A003
        if self._check_fields:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'id' field must be a sub message of type 'UUID'"
        self._id = value

    @builtins.property
    def bounds(self):
        """Message field 'bounds'."""
        return self._bounds

    @bounds.setter
    def bounds(self, value):
        if self._check_fields:
            from geographic_msgs.msg import BoundingBox
            assert \
                isinstance(value, BoundingBox), \
                "The 'bounds' field must be a sub message of type 'BoundingBox'"
        self._bounds = value

    @builtins.property
    def points(self):
        """Message field 'points'."""
        return self._points

    @points.setter
    def points(self, value):
        if self._check_fields:
            from geographic_msgs.msg import WayPoint
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
                 all(isinstance(v, WayPoint) for v in value) and
                 True), \
                "The 'points' field must be a set or sequence and each value of type 'WayPoint'"
        self._points = value

    @builtins.property
    def segments(self):
        """Message field 'segments'."""
        return self._segments

    @segments.setter
    def segments(self, value):
        if self._check_fields:
            from geographic_msgs.msg import RouteSegment
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
                 all(isinstance(v, RouteSegment) for v in value) and
                 True), \
                "The 'segments' field must be a set or sequence and each value of type 'RouteSegment'"
        self._segments = value

    @builtins.property
    def props(self):
        """Message field 'props'."""
        return self._props

    @props.setter
    def props(self, value):
        if self._check_fields:
            from geographic_msgs.msg import KeyValue
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
                 all(isinstance(v, KeyValue) for v in value) and
                 True), \
                "The 'props' field must be a set or sequence and each value of type 'KeyValue'"
        self._props = value
