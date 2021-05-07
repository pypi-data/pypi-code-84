# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensor/tensors_to_classification_calculator.proto
"""Generated protocol buffer code."""
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
  name='mediapipe/calculators/tensor/tensors_to_classification_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nGmediapipe/calculators/tensor/tensors_to_classification_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xc8\x03\n(TensorsToClassificationCalculatorOptions\x12\x1b\n\x13min_score_threshold\x18\x01 \x01(\x02\x12\r\n\x05top_k\x18\x02 \x01(\x05\x12\x16\n\x0elabel_map_path\x18\x03 \x01(\t\x12O\n\tlabel_map\x18\x05 \x01(\x0b\x32<.mediapipe.TensorsToClassificationCalculatorOptions.LabelMap\x12\x1d\n\x15\x62inary_classification\x18\x04 \x01(\x08\x1a\x83\x01\n\x08LabelMap\x12S\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x42.mediapipe.TensorsToClassificationCalculatorOptions.LabelMap.Entry\x1a\"\n\x05\x45ntry\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05label\x18\x02 \x01(\t2b\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xae\x8d\x8c\xa0\x01 \x01(\x0b\x32\x33.mediapipe.TensorsToClassificationCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='mediapipe.TensorsToClassificationCalculatorOptions.LabelMap.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mediapipe.TensorsToClassificationCalculatorOptions.LabelMap.Entry.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='mediapipe.TensorsToClassificationCalculatorOptions.LabelMap.Entry.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=447,
  serialized_end=481,
)

_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP = _descriptor.Descriptor(
  name='LabelMap',
  full_name='mediapipe.TensorsToClassificationCalculatorOptions.LabelMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='mediapipe.TensorsToClassificationCalculatorOptions.LabelMap.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP_ENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=481,
)

_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TensorsToClassificationCalculatorOptions',
  full_name='mediapipe.TensorsToClassificationCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_score_threshold', full_name='mediapipe.TensorsToClassificationCalculatorOptions.min_score_threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='top_k', full_name='mediapipe.TensorsToClassificationCalculatorOptions.top_k', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label_map_path', full_name='mediapipe.TensorsToClassificationCalculatorOptions.label_map_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label_map', full_name='mediapipe.TensorsToClassificationCalculatorOptions.label_map', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='binary_classification', full_name='mediapipe.TensorsToClassificationCalculatorOptions.binary_classification', index=4,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TensorsToClassificationCalculatorOptions.ext', index=0,
      number=335742638, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=581,
)

_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP_ENTRY.containing_type = _TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP
_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP.fields_by_name['entries'].message_type = _TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP_ENTRY
_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP.containing_type = _TENSORSTOCLASSIFICATIONCALCULATOROPTIONS
_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS.fields_by_name['label_map'].message_type = _TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP
DESCRIPTOR.message_types_by_name['TensorsToClassificationCalculatorOptions'] = _TENSORSTOCLASSIFICATIONCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorsToClassificationCalculatorOptions = _reflection.GeneratedProtocolMessageType('TensorsToClassificationCalculatorOptions', (_message.Message,), {

  'LabelMap' : _reflection.GeneratedProtocolMessageType('LabelMap', (_message.Message,), {

    'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
      'DESCRIPTOR' : _TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP_ENTRY,
      '__module__' : 'mediapipe.calculators.tensor.tensors_to_classification_calculator_pb2'
      # @@protoc_insertion_point(class_scope:mediapipe.TensorsToClassificationCalculatorOptions.LabelMap.Entry)
      })
    ,
    'DESCRIPTOR' : _TENSORSTOCLASSIFICATIONCALCULATOROPTIONS_LABELMAP,
    '__module__' : 'mediapipe.calculators.tensor.tensors_to_classification_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.TensorsToClassificationCalculatorOptions.LabelMap)
    })
  ,
  'DESCRIPTOR' : _TENSORSTOCLASSIFICATIONCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.tensor.tensors_to_classification_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TensorsToClassificationCalculatorOptions)
  })
_sym_db.RegisterMessage(TensorsToClassificationCalculatorOptions)
_sym_db.RegisterMessage(TensorsToClassificationCalculatorOptions.LabelMap)
_sym_db.RegisterMessage(TensorsToClassificationCalculatorOptions.LabelMap.Entry)

_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TENSORSTOCLASSIFICATIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TENSORSTOCLASSIFICATIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
