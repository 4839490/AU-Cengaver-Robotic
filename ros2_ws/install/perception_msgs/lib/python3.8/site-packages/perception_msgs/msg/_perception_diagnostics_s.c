// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from perception_msgs:msg/PerceptionDiagnostics.idl
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
#include "perception_msgs/msg/detail/perception_diagnostics__struct.h"
#include "perception_msgs/msg/detail/perception_diagnostics__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool perception_msgs__msg__perception_diagnostics__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[66];
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
    assert(strncmp("perception_msgs.msg._perception_diagnostics.PerceptionDiagnostics", full_classname_dest, 65) == 0);
  }
  perception_msgs__msg__PerceptionDiagnostics * ros_message = _ros_message;
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
  {  // node_name
    PyObject * field = PyObject_GetAttrString(_pymsg, "node_name");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->node_name, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // input_hz
    PyObject * field = PyObject_GetAttrString(_pymsg, "input_hz");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->input_hz = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // output_hz
    PyObject * field = PyObject_GetAttrString(_pymsg, "output_hz");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->output_hz = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // latency_ms
    PyObject * field = PyObject_GetAttrString(_pymsg, "latency_ms");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->latency_ms = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // last_msg_age_ms
    PyObject * field = PyObject_GetAttrString(_pymsg, "last_msg_age_ms");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->last_msg_age_ms = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // mean_confidence
    PyObject * field = PyObject_GetAttrString(_pymsg, "mean_confidence");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->mean_confidence = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // num_outputs
    PyObject * field = PyObject_GetAttrString(_pymsg, "num_outputs");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->num_outputs = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // gpu_utilization
    PyObject * field = PyObject_GetAttrString(_pymsg, "gpu_utilization");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->gpu_utilization = (float)PyFloat_AS_DOUBLE(field);
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
PyObject * perception_msgs__msg__perception_diagnostics__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of PerceptionDiagnostics */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("perception_msgs.msg._perception_diagnostics");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "PerceptionDiagnostics");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  perception_msgs__msg__PerceptionDiagnostics * ros_message = (perception_msgs__msg__PerceptionDiagnostics *)raw_ros_message;
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
  {  // node_name
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->node_name.data,
      strlen(ros_message->node_name.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "node_name", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // input_hz
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->input_hz);
    {
      int rc = PyObject_SetAttrString(_pymessage, "input_hz", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // output_hz
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->output_hz);
    {
      int rc = PyObject_SetAttrString(_pymessage, "output_hz", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // latency_ms
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->latency_ms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "latency_ms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // last_msg_age_ms
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->last_msg_age_ms);
    {
      int rc = PyObject_SetAttrString(_pymessage, "last_msg_age_ms", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // mean_confidence
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->mean_confidence);
    {
      int rc = PyObject_SetAttrString(_pymessage, "mean_confidence", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // num_outputs
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->num_outputs);
    {
      int rc = PyObject_SetAttrString(_pymessage, "num_outputs", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // gpu_utilization
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->gpu_utilization);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gpu_utilization", field);
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
