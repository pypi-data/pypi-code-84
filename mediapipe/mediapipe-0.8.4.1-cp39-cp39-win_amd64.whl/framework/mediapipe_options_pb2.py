# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/mediapipe_options.proto

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
  name='mediapipe/framework/mediapipe_options.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n+mediapipe/framework/mediapipe_options.proto\x12\tmediapipe\"\x1e\n\x10MediaPipeOptions*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02\x42\x33\n\x1a\x63om.google.mediapipe.protoB\x15MediaPipeOptionsProto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MEDIAPIPEOPTIONS = _descriptor.Descriptor(
  name='MediaPipeOptions',
  full_name='mediapipe.MediaPipeOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(20000, 536870912), ],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['MediaPipeOptions'] = _MEDIAPIPEOPTIONS

MediaPipeOptions = _reflection.GeneratedProtocolMessageType('MediaPipeOptions', (_message.Message,), dict(
  DESCRIPTOR = _MEDIAPIPEOPTIONS,
  __module__ = 'mediapipe.framework.mediapipe_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.MediaPipeOptions)
  ))
_sym_db.RegisterMessage(MediaPipeOptions)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.google.mediapipe.protoB\025MediaPipeOptionsProto'))
# @@protoc_insertion_point(module_scope)
