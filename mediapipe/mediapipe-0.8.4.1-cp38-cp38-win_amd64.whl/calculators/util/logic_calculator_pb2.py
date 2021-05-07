# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/logic_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/util/logic_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n1mediapipe/calculators/util/logic_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xef\x01\n\x16LogicCalculatorOptions\x12\x37\n\x02op\x18\x01 \x01(\x0e\x32+.mediapipe.LogicCalculatorOptions.Operation\x12\x0e\n\x06negate\x18\x02 \x01(\x08\x12\x13\n\x0binput_value\x18\x03 \x03(\x08\"%\n\tOperation\x12\x07\n\x03\x41ND\x10\x00\x12\x06\n\x02OR\x10\x01\x12\x07\n\x03XOR\x10\x02\x32P\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xee\xc1\xc2\xa1\x01 \x01(\x0b\x32!.mediapipe.LogicCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LOGICCALCULATOROPTIONS_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='mediapipe.LogicCalculatorOptions.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AND', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XOR', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=223,
  serialized_end=260,
)
_sym_db.RegisterEnumDescriptor(_LOGICCALCULATOROPTIONS_OPERATION)


_LOGICCALCULATOROPTIONS = _descriptor.Descriptor(
  name='LogicCalculatorOptions',
  full_name='mediapipe.LogicCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='mediapipe.LogicCalculatorOptions.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negate', full_name='mediapipe.LogicCalculatorOptions.negate', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_value', full_name='mediapipe.LogicCalculatorOptions.input_value', index=2,
      number=3, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.LogicCalculatorOptions.ext', index=0,
      number=338731246, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      options=None),
  ],
  nested_types=[],
  enum_types=[
    _LOGICCALCULATOROPTIONS_OPERATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=342,
)

_LOGICCALCULATOROPTIONS.fields_by_name['op'].enum_type = _LOGICCALCULATOROPTIONS_OPERATION
_LOGICCALCULATOROPTIONS_OPERATION.containing_type = _LOGICCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['LogicCalculatorOptions'] = _LOGICCALCULATOROPTIONS

LogicCalculatorOptions = _reflection.GeneratedProtocolMessageType('LogicCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _LOGICCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.util.logic_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.LogicCalculatorOptions)
  ))
_sym_db.RegisterMessage(LogicCalculatorOptions)

_LOGICCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _LOGICCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_LOGICCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
