// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from planning_msgs:msg/ControllerFeedback.idl
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
#include "planning_msgs/msg/detail/controller_feedback__struct.h"
#include "planning_msgs/msg/detail/controller_feedback__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool planning_msgs__msg__controller_feedback__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[58];
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
    assert(strncmp("planning_msgs.msg._controller_feedback.ControllerFeedback", full_classname_dest, 57) == 0);
  }
  planning_msgs__msg__ControllerFeedback * ros_message = _ros_message;
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
  {  // actual_speed
    PyObject * field = PyObject_GetAttrString(_pymsg, "actual_speed");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->actual_speed = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // actual_steering_deg
    PyObject * field = PyObject_GetAttrString(_pymsg, "actual_steering_deg");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->actual_steering_deg = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // cross_track_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "cross_track_error");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->cross_track_error = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // heading_error
    PyObject * field = PyObject_GetAttrString(_pymsg, "heading_error");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->heading_error = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // brake_active
    PyObject * field = PyObject_GetAttrString(_pymsg, "brake_active");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->brake_active = (Py_True == field);
    Py_DECREF(field);
  }
  {  // full_brake_active
    PyObject * field = PyObject_GetAttrString(_pymsg, "full_brake_active");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->full_brake_active = (Py_True == field);
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
PyObject * planning_msgs__msg__controller_feedback__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ControllerFeedback */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("planning_msgs.msg._controller_feedback");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ControllerFeedback");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  planning_msgs__msg__ControllerFeedback * ros_message = (planning_msgs__msg__ControllerFeedback *)raw_ros_message;
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
  {  // actual_speed
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->actual_speed);
    {
      int rc = PyObject_SetAttrString(_pymessage, "actual_speed", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // actual_steering_deg
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->actual_steering_deg);
    {
      int rc = PyObject_SetAttrString(_pymessage, "actual_steering_deg", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cross_track_error
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->cross_track_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cross_track_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // heading_error
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->heading_error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "heading_error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // brake_active
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->brake_active ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "brake_active", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // full_brake_active
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->full_brake_active ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "full_brake_active", field);
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
