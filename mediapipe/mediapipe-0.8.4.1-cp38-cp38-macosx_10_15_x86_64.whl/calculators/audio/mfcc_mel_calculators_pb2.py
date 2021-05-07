# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/audio/mfcc_mel_calculators.proto
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
  name='mediapipe/calculators/audio/mfcc_mel_calculators.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6mediapipe/calculators/audio/mfcc_mel_calculators.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xd5\x01\n\x1cMelSpectrumCalculatorOptions\x12\x19\n\rchannel_count\x18\x01 \x01(\x05:\x02\x32\x30\x12 \n\x13min_frequency_hertz\x18\x02 \x01(\x02:\x03\x31\x32\x35\x12!\n\x13max_frequency_hertz\x18\x03 \x01(\x02:\x04\x33\x38\x30\x30\x32U\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xb4\xa0\xbc% \x01(\x0b\x32\'.mediapipe.MelSpectrumCalculatorOptions\"\xc5\x01\n\x15MfccCalculatorOptions\x12\x44\n\x13mel_spectrum_params\x18\x01 \x01(\x0b\x32\'.mediapipe.MelSpectrumCalculatorOptions\x12\x16\n\nmfcc_count\x18\x02 \x01(\r:\x02\x31\x33\x32N\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x89\x9e\xb4% \x01(\x0b\x32 .mediapipe.MfccCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_MELSPECTRUMCALCULATOROPTIONS = _descriptor.Descriptor(
  name='MelSpectrumCalculatorOptions',
  full_name='mediapipe.MelSpectrumCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_count', full_name='mediapipe.MelSpectrumCalculatorOptions.channel_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_frequency_hertz', full_name='mediapipe.MelSpectrumCalculatorOptions.min_frequency_hertz', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(125),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_frequency_hertz', full_name='mediapipe.MelSpectrumCalculatorOptions.max_frequency_hertz', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(3800),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.MelSpectrumCalculatorOptions.ext', index=0,
      number=78581812, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=108,
  serialized_end=321,
)


_MFCCCALCULATOROPTIONS = _descriptor.Descriptor(
  name='MfccCalculatorOptions',
  full_name='mediapipe.MfccCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mel_spectrum_params', full_name='mediapipe.MfccCalculatorOptions.mel_spectrum_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mfcc_count', full_name='mediapipe.MfccCalculatorOptions.mfcc_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=13,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.MfccCalculatorOptions.ext', index=0,
      number=78450441, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=324,
  serialized_end=521,
)

_MFCCCALCULATOROPTIONS.fields_by_name['mel_spectrum_params'].message_type = _MELSPECTRUMCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['MelSpectrumCalculatorOptions'] = _MELSPECTRUMCALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['MfccCalculatorOptions'] = _MFCCCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MelSpectrumCalculatorOptions = _reflection.GeneratedProtocolMessageType('MelSpectrumCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _MELSPECTRUMCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.audio.mfcc_mel_calculators_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.MelSpectrumCalculatorOptions)
  })
_sym_db.RegisterMessage(MelSpectrumCalculatorOptions)

MfccCalculatorOptions = _reflection.GeneratedProtocolMessageType('MfccCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _MFCCCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.audio.mfcc_mel_calculators_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.MfccCalculatorOptions)
  })
_sym_db.RegisterMessage(MfccCalculatorOptions)

_MELSPECTRUMCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _MELSPECTRUMCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_MELSPECTRUMCALCULATOROPTIONS.extensions_by_name['ext'])
_MFCCCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _MFCCCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_MFCCCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
