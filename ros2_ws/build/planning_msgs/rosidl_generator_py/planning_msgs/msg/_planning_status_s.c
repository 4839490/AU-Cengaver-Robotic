// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from planning_msgs:msg/PlanningStatus.idl
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
#include "planning_msgs/msg/detail/planning_status__struct.h"
#include "planning_msgs/msg/detail/planning_status__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"
#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool planning_msgs__msg__planning_status__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[50];
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
    assert(strncmp("planning_msgs.msg._planning_status.PlanningStatus", full_classname_dest, 49) == 0);
  }
  planning_msgs__msg__PlanningStatus * ros_message = _ros_message;
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
  {  // status
    PyObject * field = PyObject_GetAttrString(_pymsg, "status");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->status = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // trajectory_valid
    PyObject * field = PyObject_GetAttrString(_pymsg, "trajectory_valid");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->trajectory_valid = (Py_True == field);
    Py_DECREF(field);
  }
  {  // goal_reached
    PyObject * field = PyObject_GetAttrString(_pymsg, "goal_reached");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->goal_reached = (Py_True == field);
    Py_DECREF(field);
  }
  {  // parking_entry_reached
    PyObject * field = PyObject_GetAttrString(_pymsg, "parking_entry_reached");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->parking_entry_reached = (Py_True == field);
    Py_DECREF(field);
  }
  {  // obstacle_blocking
    PyObject * field = PyObject_GetAttrString(_pymsg, "obstacle_blocking");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->obstacle_blocking = (Py_True == field);
    Py_DECREF(field);
  }
  {  // lane_lost
    PyObject * field = PyObject_GetAttrString(_pymsg, "lane_lost");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->lane_lost = (Py_True == field);
    Py_DECREF(field);
  }
  {  // localization_degraded
    PyObject * field = PyObject_GetAttrString(_pymsg, "localization_degraded");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->localization_degraded = (Py_True == field);
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
  {  // distance_to_goal
    PyObject * field = PyObject_GetAttrString(_pymsg, "distance_to_goal");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->distance_to_goal = (float)PyFloat_AS_DOUBLE(field);
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
PyObject * planning_msgs__msg__planning_status__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of PlanningStatus */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("planning_msgs.msg._planning_status");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "PlanningStatus");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  planning_msgs__msg__PlanningStatus * ros_message = (planning_msgs__msg__PlanningStatus *)raw_ros_message;
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
  {  // status
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->status);
    {
      int rc = PyObject_SetAttrString(_pymessage, "status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // trajectory_valid
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->trajectory_valid ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "trajectory_valid", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // goal_reached
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->goal_reached ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "goal_reached", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // parking_entry_reached
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->parking_entry_reached ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "parking_entry_reached", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // obstacle_blocking
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->obstacle_blocking ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "obstacle_blocking", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lane_lost
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->lane_lost ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lane_lost", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // localization_degraded
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->localization_degraded ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "localization_degraded", field);
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
  {  // distance_to_goal
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->distance_to_goal);
    {
      int rc = PyObject_SetAttrString(_pymessage, "distance_to_goal", field);
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
