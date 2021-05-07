# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/tracking/tracked_detection_manager_config.proto

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
  name='mediapipe/util/tracking/tracked_detection_manager_config.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_pb=_b('\n>mediapipe/util/tracking/tracked_detection_manager_config.proto\x12\tmediapipe\"~\n\x1dTrackedDetectionManagerConfig\x12+\n is_same_detection_max_area_ratio\x18\x01 \x01(\x02:\x01\x33\x12\x30\n#is_same_detection_min_overlap_ratio\x18\x02 \x01(\x02:\x03\x30.5')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TRACKEDDETECTIONMANAGERCONFIG = _descriptor.Descriptor(
  name='TrackedDetectionManagerConfig',
  full_name='mediapipe.TrackedDetectionManagerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_same_detection_max_area_ratio', full_name='mediapipe.TrackedDetectionManagerConfig.is_same_detection_max_area_ratio', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(3),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_same_detection_min_overlap_ratio', full_name='mediapipe.TrackedDetectionManagerConfig.is_same_detection_min_overlap_ratio', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
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
  serialized_start=77,
  serialized_end=203,
)

DESCRIPTOR.message_types_by_name['TrackedDetectionManagerConfig'] = _TRACKEDDETECTIONMANAGERCONFIG

TrackedDetectionManagerConfig = _reflection.GeneratedProtocolMessageType('TrackedDetectionManagerConfig', (_message.Message,), dict(
  DESCRIPTOR = _TRACKEDDETECTIONMANAGERCONFIG,
  __module__ = 'mediapipe.util.tracking.tracked_detection_manager_config_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TrackedDetectionManagerConfig)
  ))
_sym_db.RegisterMessage(TrackedDetectionManagerConfig)


# @@protoc_insertion_point(module_scope)
