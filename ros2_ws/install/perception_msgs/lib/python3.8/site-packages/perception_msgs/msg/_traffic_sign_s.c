// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from perception_msgs:msg/TrafficSign.idl
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
#include "perception_msgs/msg/detail/traffic_sign__struct.h"
#include "perception_msgs/msg/detail/traffic_sign__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool perception_msgs__msg__traffic_sign__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[46];
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
    assert(strncmp("perception_msgs.msg._traffic_sign.TrafficSign", full_classname_dest, 45) == 0);
  }
  perception_msgs__msg__TrafficSign * ros_message = _ros_message;
  {  // sign_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "sign_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->sign_id = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // type
    PyObject * field = PyObject_GetAttrString(_pymsg, "type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->type = (uint8_t)PyLong_AsUnsignedLong(field);
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
  {  // relevant_to_route
    PyObject * field = PyObject_GetAttrString(_pymsg, "relevant_to_route");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->relevant_to_route = (Py_True == field);
    Py_DECREF(field);
  }
  {  // distance
    PyObject * field = PyObject_GetAttrString(_pymsg, "distance");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->distance = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // event_status
    PyObject * field = PyObject_GetAttrString(_pymsg, "event_status");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->event_status = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // confirmed
    PyObject * field = PyObject_GetAttrString(_pymsg, "confirmed");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->confirmed = (Py_True == field);
    Py_DECREF(field);
  }
  {  // bbox_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "bbox_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->bbox_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // bbox_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "bbox_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->bbox_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // bbox_w
    PyObject * field = PyObject_GetAttrString(_pymsg, "bbox_w");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->bbox_w = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // bbox_h
    PyObject * field = PyObject_GetAttrString(_pymsg, "bbox_h");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->bbox_h = (float)PyFloat_AS_DOUBLE(field);
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
  {  // event_memory_ttl_ms
    PyObject * field = PyObject_GetAttrString(_pymsg, "event_memory_ttl_ms");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->event_memory_ttl_ms = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // source_sensor
    PyObject * field = PyObject_GetAttrString(_pymsg, "source_sensor");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->source_sensor, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
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
PyObject * perception_msgs__msg__traffic_sign__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of TrafficSign */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("perception_msgs.msg._traffic_sign");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "TrafficSign");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  perception_msgs__msg__TrafficSign * ros_message = (perception_msgs__msg__TrafficSign *)raw_ros_message;
  {  // sign_id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->sign_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sign_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // type
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "type", field);
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
  {  // relevant_to_route
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->relevant_to_route ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "relevant_to_route", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // distance
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->distance);
    {
      int rc = PyObject_SetAttrString(_pymessage, "distance", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // event_status
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->event_status);
    {
      int rc = PyObject_SetAttrString(_pymessage, "event_status", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // confirmed
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->confirmed ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "confirmed", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // bbox_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->bbox_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "bbox_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // bbox_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->bbox_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "bbox_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // bbox_w
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->bbox_w);
    {
      int rc = PyObject_SetAttrString(_pymessage, "bbox_w", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // bbox_h
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->bbox_h);
    {
      int rc = PyObject_SetAttrString(_pymessage, "bbox_h", field);
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
  {  // event_memory_ttl_ms
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->event_memory_ttl_ms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "event_memory_ttl_ms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // source_sensor
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->source_sensor.data,
      strlen(ros_message->source_sensor.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "source_sensor", field);
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
