// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from localization_msgs:msg/MapOrigin.idl
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
#include "localization_msgs/msg/detail/map_origin__struct.h"
#include "localization_msgs/msg/detail/map_origin__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool localization_msgs__msg__map_origin__convert_from_py(PyObject * _pymsg, void * _ros_message)
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
    assert(strncmp("localization_msgs.msg._map_origin.MapOrigin", full_classname_dest, 43) == 0);
  }
  localization_msgs__msg__MapOrigin * ros_message = _ros_message;
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
  {  // lat_ref
    PyObject * field = PyObject_GetAttrString(_pymsg, "lat_ref");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lat_ref = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // lon_ref
    PyObject * field = PyObject_GetAttrString(_pymsg, "lon_ref");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->lon_ref = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // alt_ref
    PyObject * field = PyObject_GetAttrString(_pymsg, "alt_ref");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->alt_ref = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw_ref
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw_ref");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw_ref = PyFloat_AS_DOUBLE(field);
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
  {  // locked
    PyObject * field = PyObject_GetAttrString(_pymsg, "locked");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->locked = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * localization_msgs__msg__map_origin__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of MapOrigin */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("localization_msgs.msg._map_origin");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "MapOrigin");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  localization_msgs__msg__MapOrigin * ros_message = (localization_msgs__msg__MapOrigin *)raw_ros_message;
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
  {  // lat_ref
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lat_ref);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lat_ref", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // lon_ref
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->lon_ref);
    {
      int rc = PyObject_SetAttrString(_pymessage, "lon_ref", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // alt_ref
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->alt_ref);
    {
      int rc = PyObject_SetAttrString(_pymessage, "alt_ref", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw_ref
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw_ref);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw_ref", field);
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
  {  // locked
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->locked ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "locked", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
