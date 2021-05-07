# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/modules/objectron/calculators/belief_decoder_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/modules/objectron/calculators/belief_decoder_config.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nCmediapipe/modules/objectron/calculators/belief_decoder_config.proto\x12\tmediapipe\"\xc4\x01\n\x13\x42\x65liefDecoderConfig\x12\x1e\n\x11heatmap_threshold\x18\x01 \x01(\x02:\x03\x30.9\x12\x1e\n\x12local_max_distance\x18\x02 \x01(\x02:\x02\x31\x30\x12\"\n\x11offset_scale_coef\x18\x03 \x01(\x02:\x03\x30.5B\x02\x18\x01\x12\x15\n\rvoting_radius\x18\x04 \x01(\x05\x12\x18\n\x10voting_allowance\x18\x05 \x01(\x05\x12\x18\n\x10voting_threshold\x18\x06 \x01(\x02'
)




_BELIEFDECODERCONFIG = _descriptor.Descriptor(
  name='BeliefDecoderConfig',
  full_name='mediapipe.BeliefDecoderConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='heatmap_threshold', full_name='mediapipe.BeliefDecoderConfig.heatmap_threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.9),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='local_max_distance', full_name='mediapipe.BeliefDecoderConfig.local_max_distance', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(10),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset_scale_coef', full_name='mediapipe.BeliefDecoderConfig.offset_scale_coef', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voting_radius', full_name='mediapipe.BeliefDecoderConfig.voting_radius', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voting_allowance', full_name='mediapipe.BeliefDecoderConfig.voting_allowance', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voting_threshold', full_name='mediapipe.BeliefDecoderConfig.voting_threshold', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=83,
  serialized_end=279,
)

DESCRIPTOR.message_types_by_name['BeliefDecoderConfig'] = _BELIEFDECODERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BeliefDecoderConfig = _reflection.GeneratedProtocolMessageType('BeliefDecoderConfig', (_message.Message,), {
  'DESCRIPTOR' : _BELIEFDECODERCONFIG,
  '__module__' : 'mediapipe.modules.objectron.calculators.belief_decoder_config_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.BeliefDecoderConfig)
  })
_sym_db.RegisterMessage(BeliefDecoderConfig)


_BELIEFDECODERCONFIG.fields_by_name['offset_scale_coef']._options = None
# @@protoc_insertion_point(module_scope)
