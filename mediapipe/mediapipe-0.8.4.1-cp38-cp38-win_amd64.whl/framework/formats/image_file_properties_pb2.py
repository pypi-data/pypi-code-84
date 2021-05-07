# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/formats/image_file_properties.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/formats/image_file_properties.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n7mediapipe/framework/formats/image_file_properties.proto\x12\tmediapipe\"\x91\x01\n\x13ImageFileProperties\x12\x13\n\x0bimage_width\x18\x01 \x01(\r\x12\x14\n\x0cimage_height\x18\x02 \x01(\r\x12\x17\n\x0f\x66ocal_length_mm\x18\x03 \x01(\x01\x12\x19\n\x11\x66ocal_length_35mm\x18\x04 \x01(\x01\x12\x1b\n\x13\x66ocal_length_pixels\x18\x05 \x01(\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IMAGEFILEPROPERTIES = _descriptor.Descriptor(
  name='ImageFileProperties',
  full_name='mediapipe.ImageFileProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_width', full_name='mediapipe.ImageFileProperties.image_width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_height', full_name='mediapipe.ImageFileProperties.image_height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='focal_length_mm', full_name='mediapipe.ImageFileProperties.focal_length_mm', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='focal_length_35mm', full_name='mediapipe.ImageFileProperties.focal_length_35mm', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='focal_length_pixels', full_name='mediapipe.ImageFileProperties.focal_length_pixels', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=216,
)

DESCRIPTOR.message_types_by_name['ImageFileProperties'] = _IMAGEFILEPROPERTIES

ImageFileProperties = _reflection.GeneratedProtocolMessageType('ImageFileProperties', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEFILEPROPERTIES,
  __module__ = 'mediapipe.framework.formats.image_file_properties_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ImageFileProperties)
  ))
_sym_db.RegisterMessage(ImageFileProperties)


# @@protoc_insertion_point(module_scope)
