// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from planning_msgs:msg/ActiveRouteContext.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "planning_msgs/msg/detail/active_route_context__struct.h"
#include "planning_msgs/msg/detail/active_route_context__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes
#include "geometry_msgs/msg/detail/point__functions.h"
// end nested array functions include
ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);
ROSIDL_GENERATOR_C_IMPORT
bool geometry_msgs__msg__point__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * geometry_msgs__msg__point__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool planning_msgs__msg__active_route_context__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[59];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("planning_msgs.msg._active_route_context.ActiveRouteContext", full_classname_dest, 58) == 0);
  }
  planning_msgs__msg__ActiveRouteContext * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // active_waypoint_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "active_waypoint_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->active_waypoint_id = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // target_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "target_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->target_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // target_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "target_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->target_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // target_heading
    PyObject * field = PyObject_GetAttrString(_pymsg, "target_heading");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->target_heading = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // planner_mode
    PyObject * field = PyObject_GetAttrString(_pymsg, "planner_mode");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->planner_mode = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // route_direction
    PyObject * field = PyObject_GetAttrString(_pymsg, "route_direction");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->route_direction, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // planned_trajectory
    PyObject * field = PyObject_GetAttrString(_pymsg, "planned_trajectory");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'planned_trajectory'");
    if (!seq_field) {
      Py_DECREF(field);
      return false;
    }
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    if (!geometry_msgs__msg__Point__Sequence__init(&(ros_message->planned_trajectory), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create geometry_msgs__msg__Point__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    geometry_msgs__msg__Point * dest = ros_message->planned_trajectory.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!geometry_msgs__msg__point__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }
  {  // lookahead_distance
    PyObject * field = PyObject_GetAttrString(_pymsg, "lookahead_distance");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lookahead_distance = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // in_stop_zone
    PyObject * field = PyObject_GetAttrString(_pymsg, "in_stop_zone");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->in_stop_zone = (Py_True == field);
    Py_DECREF(field);
  }
  {  // distance_to_stop_zone
    PyObject * field = PyObject_GetAttrString(_pymsg, "distance_to_stop_zone");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->distance_to_stop_zone = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // localization_confidence
    PyObject * field = PyObject_GetAttrString(_pymsg, "localization_confidence");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->localization_confidence = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ego_speed_mps
    PyObject * field = PyObject_GetAttrString(_pymsg, "ego_speed_mps");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ego_speed_mps = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // route_context_valid
    PyObject * field = PyObject_GetAttrString(_pymsg, "route_context_valid");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->route_context_valid = (Py_True == field);
    Py_DECREF(field);
  }
  {  // age_ms
    PyObject * field = PyObject_GetAttrString(_pymsg, "age_ms");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->age_ms = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // valid_until_ms
    PyObject * field = PyObject_GetAttrString(_pymsg, "valid_until_ms");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->valid_until_ms = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // warning_flags
    PyObject * field = PyObject_GetAttrString(_pymsg, "warning_flags");
    if (!field) {
      return false;
    }
    {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'warning_flags'");
      if (!seq_field) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = PySequence_Size(field);
      if (-1 == size) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      if (!rosidl_runtime_c__String__Sequence__init(&(ros_message->warning_flags), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create String__Sequence ros_message");
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      rosidl_runtime_c__String * dest = ros_message->warning_flags.data;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        assert(PyUnicode_Check(item));
        PyObject * encoded_item = PyUnicode_AsUTF8String(item);
        if (!encoded_item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        rosidl_runtime_c__String__assign(&dest[i], PyBytes_AS_STRING(encoded_item));
        Py_DECREF(encoded_item);
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * planning_msgs__msg__active_route_context__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ActiveRouteContext */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("planning_msgs.msg._active_route_context");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ActiveRouteContext");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  planning_msgs__msg__ActiveRouteContext * ros_message = (planning_msgs__msg__ActiveRouteContext *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // active_waypoint_id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->active_waypoint_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "active_waypoint_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // target_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->target_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "target_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // target_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->target_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "target_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // target_heading
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->target_heading);
    {
      int rc = PyObject_SetAttrString(_pymessage, "target_heading", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // planner_mode
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->planner_mode);
    {
      int rc = PyObject_SetAttrString(_pymessage, "planner_mode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // route_direction
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->route_direction.data,
      strlen(ros_message->route_direction.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "route_direction", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // planned_trajectory
    PyObject * field = NULL;
    size_t size = ros_message->planned_trajectory.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    geometry_msgs__msg__Point * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->planned_trajectory.data[i]);
      PyObject * pyitem = geometry_msgs__msg__point__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "planned_trajectory", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lookahead_distance
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lookahead_distance);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lookahead_distance", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // in_stop_zone
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->in_stop_zone ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "in_stop_zone", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // distance_to_stop_zone
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->distance_to_stop_zone);
    {
      int rc = PyObject_SetAttrString(_pymessage, "distance_to_stop_zone", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // localization_confidence
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->localization_confidence);
    {
      int rc = PyObject_SetAttrString(_pymessage, "localization_confidence", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ego_speed_mps
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ego_speed_mps);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ego_speed_mps", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // route_context_valid
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->route_context_valid ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "route_context_valid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // age_ms
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->age_ms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "age_ms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // valid_until_ms
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->valid_until_ms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "valid_until_ms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // warning_flags
    PyObject * field = NULL;
    size_t size = ros_message->warning_flags.size;
    rosidl_runtime_c__String * src = ros_message->warning_flags.data;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    for (size_t i = 0; i < size; ++i) {
      PyObject * decoded_item = PyUnicode_DecodeUTF8(src[i].data, strlen(src[i].data), "replace");
      if (!decoded_item) {
        return NULL;
      }
      int rc = PyList_SetItem(field, i, decoded_item);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "warning_flags", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
