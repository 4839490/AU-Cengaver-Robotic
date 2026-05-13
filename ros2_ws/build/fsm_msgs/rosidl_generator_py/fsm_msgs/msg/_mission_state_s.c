// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from fsm_msgs:msg/MissionState.idl
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
#include "fsm_msgs/msg/detail/mission_state__struct.h"
#include "fsm_msgs/msg/detail/mission_state__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool fsm_msgs__msg__mission_state__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[41];
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
    assert(strncmp("fsm_msgs.msg._mission_state.MissionState", full_classname_dest, 40) == 0);
  }
  fsm_msgs__msg__MissionState * ros_message = _ros_message;
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
  {  // mission_active
    PyObject * field = PyObject_GetAttrString(_pymsg, "mission_active");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->mission_active = (Py_True == field);
    Py_DECREF(field);
  }
  {  // total_waypoints
    PyObject * field = PyObject_GetAttrString(_pymsg, "total_waypoints");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->total_waypoints = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // completed_waypoints
    PyObject * field = PyObject_GetAttrString(_pymsg, "completed_waypoints");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->completed_waypoints = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // current_waypoint_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "current_waypoint_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->current_waypoint_id = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // current_waypoint_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "current_waypoint_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->current_waypoint_type = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // next_waypoint_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "next_waypoint_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->next_waypoint_id = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // next_waypoint_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "next_waypoint_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->next_waypoint_type = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // pickup_complete
    PyObject * field = PyObject_GetAttrString(_pymsg, "pickup_complete");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->pickup_complete = (Py_True == field);
    Py_DECREF(field);
  }
  {  // dropoff_complete
    PyObject * field = PyObject_GetAttrString(_pymsg, "dropoff_complete");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->dropoff_complete = (Py_True == field);
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

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * fsm_msgs__msg__mission_state__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of MissionState */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("fsm_msgs.msg._mission_state");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "MissionState");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  fsm_msgs__msg__MissionState * ros_message = (fsm_msgs__msg__MissionState *)raw_ros_message;
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
  {  // mission_active
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->mission_active ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "mission_active", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // total_waypoints
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->total_waypoints);
    {
      int rc = PyObject_SetAttrString(_pymessage, "total_waypoints", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // completed_waypoints
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->completed_waypoints);
    {
      int rc = PyObject_SetAttrString(_pymessage, "completed_waypoints", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // current_waypoint_id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->current_waypoint_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "current_waypoint_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // current_waypoint_type
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->current_waypoint_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "current_waypoint_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // next_waypoint_id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->next_waypoint_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "next_waypoint_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // next_waypoint_type
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->next_waypoint_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "next_waypoint_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pickup_complete
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->pickup_complete ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pickup_complete", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // dropoff_complete
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->dropoff_complete ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "dropoff_complete", field);
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

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
