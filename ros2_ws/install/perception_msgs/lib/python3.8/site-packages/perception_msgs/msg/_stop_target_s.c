// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from perception_msgs:msg/StopTarget.idl
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
#include "perception_msgs/msg/detail/stop_target__struct.h"
#include "perception_msgs/msg/detail/stop_target__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool perception_msgs__msg__stop_target__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[44];
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
    assert(strncmp("perception_msgs.msg._stop_target.StopTarget", full_classname_dest, 43) == 0);
  }
  perception_msgs__msg__StopTarget * ros_message = _ros_message;
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
  {  // target_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "target_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->target_type = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // distance_from_front_bumper
    PyObject * field = PyObject_GetAttrString(_pymsg, "distance_from_front_bumper");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->distance_from_front_bumper = (float)PyFloat_AS_DOUBLE(field);
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
  {  // confidence
    PyObject * field = PyObject_GetAttrString(_pymsg, "confidence");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->confidence = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // source
    PyObject * field = PyObject_GetAttrString(_pymsg, "source");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->source, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
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
  {  // waypoint_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "waypoint_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->waypoint_id = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // heading_at_stop
    PyObject * field = PyObject_GetAttrString(_pymsg, "heading_at_stop");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->heading_at_stop = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // priority
    PyObject * field = PyObject_GetAttrString(_pymsg, "priority");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->priority = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // required_stop_duration_ms
    PyObject * field = PyObject_GetAttrString(_pymsg, "required_stop_duration_ms");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->required_stop_duration_ms = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // stop_reason_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "stop_reason_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->stop_reason_id = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // source_topic
    PyObject * field = PyObject_GetAttrString(_pymsg, "source_topic");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->source_topic, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * perception_msgs__msg__stop_target__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of StopTarget */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("perception_msgs.msg._stop_target");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "StopTarget");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  perception_msgs__msg__StopTarget * ros_message = (perception_msgs__msg__StopTarget *)raw_ros_message;
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
  {  // target_type
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->target_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "target_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // distance_from_front_bumper
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->distance_from_front_bumper);
    {
      int rc = PyObject_SetAttrString(_pymessage, "distance_from_front_bumper", field);
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
  {  // confidence
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->confidence);
    {
      int rc = PyObject_SetAttrString(_pymessage, "confidence", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // source
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->source.data,
      strlen(ros_message->source.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "source", field);
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
  {  // waypoint_id
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->waypoint_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "waypoint_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // heading_at_stop
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->heading_at_stop);
    {
      int rc = PyObject_SetAttrString(_pymessage, "heading_at_stop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // priority
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->priority);
    {
      int rc = PyObject_SetAttrString(_pymessage, "priority", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // required_stop_duration_ms
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->required_stop_duration_ms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "required_stop_duration_ms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // stop_reason_id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->stop_reason_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "stop_reason_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // source_topic
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->source_topic.data,
      strlen(ros_message->source_topic.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "source_topic", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
