# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/tensor_converter_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/tensor/tensor_converter_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n>mediapipe/calculators/tensor/tensor_converter_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\x85\x04\n TensorConverterCalculatorOptions\x12\x19\n\x0bzero_center\x18\x01 \x01(\x08:\x04true\x12\'\n\x18use_custom_normalization\x18\x06 \x01(\x08:\x05\x66\x61lse\x12\x16\n\ncustom_div\x18\x07 \x01(\x02:\x02-1\x12\x16\n\ncustom_sub\x18\x08 \x01(\x02:\x02-1\x12\x1e\n\x0f\x66lip_vertically\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x10max_num_channels\x18\x03 \x01(\x05:\x01\x33\x12\x1f\n\x10row_major_matrix\x18\x04 \x01(\x08:\x05\x66\x61lse\x12$\n\x15use_quantized_tensors\x18\x05 \x01(\x08:\x05\x66\x61lse\x12_\n\x19output_tensor_float_range\x18\t \x01(\x0b\x32<.mediapipe.TensorConverterCalculatorOptions.TensorFloatRange\x1a,\n\x10TensorFloatRange\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\x32Z\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xad\x8d\x8c\xa0\x01 \x01(\x0b\x32+.mediapipe.TensorConverterCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_TENSORCONVERTERCALCULATOROPTIONS_TENSORFLOATRANGE = _descriptor.Descriptor(
  name='TensorFloatRange',
  full_name='mediapipe.TensorConverterCalculatorOptions.TensorFloatRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='mediapipe.TensorConverterCalculatorOptions.TensorFloatRange.min', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='mediapipe.TensorConverterCalculatorOptions.TensorFloatRange.max', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=497,
  serialized_end=541,
)

_TENSORCONVERTERCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TensorConverterCalculatorOptions',
  full_name='mediapipe.TensorConverterCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zero_center', full_name='mediapipe.TensorConverterCalculatorOptions.zero_center', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_custom_normalization', full_name='mediapipe.TensorConverterCalculatorOptions.use_custom_normalization', index=1,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_div', full_name='mediapipe.TensorConverterCalculatorOptions.custom_div', index=2,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(-1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_sub', full_name='mediapipe.TensorConverterCalculatorOptions.custom_sub', index=3,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(-1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flip_vertically', full_name='mediapipe.TensorConverterCalculatorOptions.flip_vertically', index=4,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_num_channels', full_name='mediapipe.TensorConverterCalculatorOptions.max_num_channels', index=5,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_major_matrix', full_name='mediapipe.TensorConverterCalculatorOptions.row_major_matrix', index=6,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_quantized_tensors', full_name='mediapipe.TensorConverterCalculatorOptions.use_quantized_tensors', index=7,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_tensor_float_range', full_name='mediapipe.TensorConverterCalculatorOptions.output_tensor_float_range', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TensorConverterCalculatorOptions.ext', index=0,
      number=335742637, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[_TENSORCONVERTERCALCULATOROPTIONS_TENSORFLOATRANGE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=633,
)

_TENSORCONVERTERCALCULATOROPTIONS_TENSORFLOATRANGE.containing_type = _TENSORCONVERTERCALCULATOROPTIONS
_TENSORCONVERTERCALCULATOROPTIONS.fields_by_name['output_tensor_float_range'].message_type = _TENSORCONVERTERCALCULATOROPTIONS_TENSORFLOATRANGE
DESCRIPTOR.message_types_by_name['TensorConverterCalculatorOptions'] = _TENSORCONVERTERCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorConverterCalculatorOptions = _reflection.GeneratedProtocolMessageType('TensorConverterCalculatorOptions', (_message.Message,), dict(

  TensorFloatRange = _reflection.GeneratedProtocolMessageType('TensorFloatRange', (_message.Message,), dict(
    DESCRIPTOR = _TENSORCONVERTERCALCULATOROPTIONS_TENSORFLOATRANGE,
    __module__ = 'mediapipe.calculators.tensor.tensor_converter_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.TensorConverterCalculatorOptions.TensorFloatRange)
    ))
  ,
  DESCRIPTOR = _TENSORCONVERTERCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.tensor.tensor_converter_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TensorConverterCalculatorOptions)
  ))
_sym_db.RegisterMessage(TensorConverterCalculatorOptions)
_sym_db.RegisterMessage(TensorConverterCalculatorOptions.TensorFloatRange)

_TENSORCONVERTERCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TENSORCONVERTERCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TENSORCONVERTERCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
