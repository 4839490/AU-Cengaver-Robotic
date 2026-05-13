// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from perception_msgs:msg/ObstacleTrack.idl
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
#include "perception_msgs/msg/detail/obstacle_track__struct.h"
#include "perception_msgs/msg/detail/obstacle_track__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool perception_msgs__msg__obstacle_track__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("perception_msgs.msg._obstacle_track.ObstacleTrack", full_classname_dest, 49) == 0);
  }
  perception_msgs__msg__ObstacleTrack * ros_message = _ros_message;
  {  // track_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "track_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->track_id = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // class_label
    PyObject * field = PyObject_GetAttrString(_pymsg, "class_label");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->class_label = (uint8_t)PyLong_AsUnsignedLong(field);
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
  {  // position_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "position_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // position_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "position_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->position_y = (float)PyFloat_AS_DOUBLE(field);
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
  {  // velocity_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->velocity_x = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // velocity_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->velocity_y = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ttc
    PyObject * field = PyObject_GetAttrString(_pymsg, "ttc");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ttc = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // width
    PyObject * field = PyObject_GetAttrString(_pymsg, "width");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->width = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // length
    PyObject * field = PyObject_GetAttrString(_pymsg, "length");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->length = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // height
    PyObject * field = PyObject_GetAttrString(_pymsg, "height");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->height = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // is_static
    PyObject * field = PyObject_GetAttrString(_pymsg, "is_static");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->is_static = (Py_True == field);
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
  {  // semantic_source
    PyObject * field = PyObject_GetAttrString(_pymsg, "semantic_source");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->semantic_source, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // geometry_source
    PyObject * field = PyObject_GetAttrString(_pymsg, "geometry_source");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->geometry_source, PyBytes_AS_STRING(encoded_field));
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
PyObject * perception_msgs__msg__obstacle_track__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ObstacleTrack */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("perception_msgs.msg._obstacle_track");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ObstacleTrack");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  perception_msgs__msg__ObstacleTrack * ros_message = (perception_msgs__msg__ObstacleTrack *)raw_ros_message;
  {  // track_id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->track_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "track_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // class_label
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->class_label);
    {
      int rc = PyObject_SetAttrString(_pymessage, "class_label", field);
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
  {  // position_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // position_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->position_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "position_y", field);
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
  {  // velocity_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->velocity_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "velocity_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // velocity_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->velocity_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "velocity_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ttc
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ttc);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ttc", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // width
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->width);
    {
      int rc = PyObject_SetAttrString(_pymessage, "width", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // length
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->length);
    {
      int rc = PyObject_SetAttrString(_pymessage, "length", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // height
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->height);
    {
      int rc = PyObject_SetAttrString(_pymessage, "height", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // is_static
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->is_static ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "is_static", field);
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
  {  // semantic_source
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->semantic_source.data,
      strlen(ros_message->semantic_source.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "semantic_source", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // geometry_source
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->geometry_source.data,
      strlen(ros_message->geometry_source.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "geometry_source", field);
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
