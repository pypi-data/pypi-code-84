# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/packet_factory.proto

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
  name='mediapipe/framework/packet_factory.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n(mediapipe/framework/packet_factory.proto\x12\tmediapipe\"\"\n\x14PacketFactoryOptions*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02\"\x95\x01\n\x13PacketFactoryConfig\x12\x16\n\x0epacket_factory\x18\x01 \x01(\t\x12\x1a\n\x12output_side_packet\x18\x02 \x01(\t\x12\x18\n\x0f\x65xternal_output\x18\xea\x07 \x01(\t\x12\x30\n\x07options\x18\x03 \x01(\x0b\x32\x1f.mediapipe.PacketFactoryOptions\"E\n\x13PacketManagerConfig\x12.\n\x06packet\x18\x01 \x03(\x0b\x32\x1e.mediapipe.PacketFactoryConfig')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PACKETFACTORYOPTIONS = _descriptor.Descriptor(
  name='PacketFactoryOptions',
  full_name='mediapipe.PacketFactoryOptions',
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
  serialized_start=55,
  serialized_end=89,
)


_PACKETFACTORYCONFIG = _descriptor.Descriptor(
  name='PacketFactoryConfig',
  full_name='mediapipe.PacketFactoryConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packet_factory', full_name='mediapipe.PacketFactoryConfig.packet_factory', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_side_packet', full_name='mediapipe.PacketFactoryConfig.output_side_packet', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='external_output', full_name='mediapipe.PacketFactoryConfig.external_output', index=2,
      number=1002, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='options', full_name='mediapipe.PacketFactoryConfig.options', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=92,
  serialized_end=241,
)


_PACKETMANAGERCONFIG = _descriptor.Descriptor(
  name='PacketManagerConfig',
  full_name='mediapipe.PacketManagerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packet', full_name='mediapipe.PacketManagerConfig.packet', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=243,
  serialized_end=312,
)

_PACKETFACTORYCONFIG.fields_by_name['options'].message_type = _PACKETFACTORYOPTIONS
_PACKETMANAGERCONFIG.fields_by_name['packet'].message_type = _PACKETFACTORYCONFIG
DESCRIPTOR.message_types_by_name['PacketFactoryOptions'] = _PACKETFACTORYOPTIONS
DESCRIPTOR.message_types_by_name['PacketFactoryConfig'] = _PACKETFACTORYCONFIG
DESCRIPTOR.message_types_by_name['PacketManagerConfig'] = _PACKETMANAGERCONFIG

PacketFactoryOptions = _reflection.GeneratedProtocolMessageType('PacketFactoryOptions', (_message.Message,), dict(
  DESCRIPTOR = _PACKETFACTORYOPTIONS,
  __module__ = 'mediapipe.framework.packet_factory_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.PacketFactoryOptions)
  ))
_sym_db.RegisterMessage(PacketFactoryOptions)

PacketFactoryConfig = _reflection.GeneratedProtocolMessageType('PacketFactoryConfig', (_message.Message,), dict(
  DESCRIPTOR = _PACKETFACTORYCONFIG,
  __module__ = 'mediapipe.framework.packet_factory_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.PacketFactoryConfig)
  ))
_sym_db.RegisterMessage(PacketFactoryConfig)

PacketManagerConfig = _reflection.GeneratedProtocolMessageType('PacketManagerConfig', (_message.Message,), dict(
  DESCRIPTOR = _PACKETMANAGERCONFIG,
  __module__ = 'mediapipe.framework.packet_factory_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.PacketManagerConfig)
  ))
_sym_db.RegisterMessage(PacketManagerConfig)


# @@protoc_insertion_point(module_scope)
