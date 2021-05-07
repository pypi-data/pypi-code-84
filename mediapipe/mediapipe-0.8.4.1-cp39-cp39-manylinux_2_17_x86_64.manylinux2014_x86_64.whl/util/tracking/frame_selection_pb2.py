# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/tracking/frame_selection.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.util.tracking import camera_motion_pb2 as mediapipe_dot_util_dot_tracking_dot_camera__motion__pb2
from mediapipe.util.tracking import frame_selection_solution_evaluator_pb2 as mediapipe_dot_util_dot_tracking_dot_frame__selection__solution__evaluator__pb2
from mediapipe.util.tracking import region_flow_pb2 as mediapipe_dot_util_dot_tracking_dot_region__flow__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/util/tracking/frame_selection.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n-mediapipe/util/tracking/frame_selection.proto\x12\tmediapipe\x1a+mediapipe/util/tracking/camera_motion.proto\x1a@mediapipe/util/tracking/frame_selection_solution_evaluator.proto\x1a)mediapipe/util/tracking/region_flow.proto\"e\n\x17\x46rameSelectionTimestamp\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x11\n\tframe_idx\x18\x02 \x01(\x05\x12$\n\x18processed_from_timestamp\x18\x03 \x01(\x03:\x02-1\"\xc6\x01\n\x14\x46rameSelectionResult\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x11\n\tframe_idx\x18\x02 \x01(\x05\x12.\n\rcamera_motion\x18\x03 \x01(\x0b\x32\x17.mediapipe.CameraMotion\x12\x32\n\x08\x66\x65\x61tures\x18\x04 \x01(\x0b\x32 .mediapipe.RegionFlowFeatureList\x12$\n\x18processed_from_timestamp\x18\x05 \x01(\x03:\x02-1\"\xdc\x01\n\x17\x46rameSelectionCriterion\x12\x18\n\rsampling_rate\x18\x01 \x01(\x05:\x01\x30\x12\x1c\n\x10\x62\x61ndwidth_frames\x18\x02 \x01(\x02:\x02\x35\x30\x12\x1f\n\x14search_radius_frames\x18\x03 \x01(\x05:\x01\x31\x12J\n\x12solution_evaluator\x18\x04 \x01(\x0b\x32..mediapipe.FrameSelectionSolutionEvaluatorType\x12\x1c\n\x11max_output_frames\x18\x05 \x01(\x05:\x01\x30\"g\n\x15\x46rameSelectionOptions\x12\x35\n\tcriterion\x18\x01 \x03(\x0b\x32\".mediapipe.FrameSelectionCriterion\x12\x17\n\nchunk_size\x18\x02 \x01(\x05:\x03\x31\x30\x30')
  ,
  dependencies=[mediapipe_dot_util_dot_tracking_dot_camera__motion__pb2.DESCRIPTOR,mediapipe_dot_util_dot_tracking_dot_frame__selection__solution__evaluator__pb2.DESCRIPTOR,mediapipe_dot_util_dot_tracking_dot_region__flow__pb2.DESCRIPTOR,])




_FRAMESELECTIONTIMESTAMP = _descriptor.Descriptor(
  name='FrameSelectionTimestamp',
  full_name='mediapipe.FrameSelectionTimestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='mediapipe.FrameSelectionTimestamp.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_idx', full_name='mediapipe.FrameSelectionTimestamp.frame_idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processed_from_timestamp', full_name='mediapipe.FrameSelectionTimestamp.processed_from_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=-1,
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
  serialized_start=214,
  serialized_end=315,
)


_FRAMESELECTIONRESULT = _descriptor.Descriptor(
  name='FrameSelectionResult',
  full_name='mediapipe.FrameSelectionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='mediapipe.FrameSelectionResult.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_idx', full_name='mediapipe.FrameSelectionResult.frame_idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='camera_motion', full_name='mediapipe.FrameSelectionResult.camera_motion', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='mediapipe.FrameSelectionResult.features', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processed_from_timestamp', full_name='mediapipe.FrameSelectionResult.processed_from_timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=-1,
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
  serialized_start=318,
  serialized_end=516,
)


_FRAMESELECTIONCRITERION = _descriptor.Descriptor(
  name='FrameSelectionCriterion',
  full_name='mediapipe.FrameSelectionCriterion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sampling_rate', full_name='mediapipe.FrameSelectionCriterion.sampling_rate', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bandwidth_frames', full_name='mediapipe.FrameSelectionCriterion.bandwidth_frames', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(50),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_radius_frames', full_name='mediapipe.FrameSelectionCriterion.search_radius_frames', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solution_evaluator', full_name='mediapipe.FrameSelectionCriterion.solution_evaluator', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_output_frames', full_name='mediapipe.FrameSelectionCriterion.max_output_frames', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=519,
  serialized_end=739,
)


_FRAMESELECTIONOPTIONS = _descriptor.Descriptor(
  name='FrameSelectionOptions',
  full_name='mediapipe.FrameSelectionOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='criterion', full_name='mediapipe.FrameSelectionOptions.criterion', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chunk_size', full_name='mediapipe.FrameSelectionOptions.chunk_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
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
  serialized_start=741,
  serialized_end=844,
)

_FRAMESELECTIONRESULT.fields_by_name['camera_motion'].message_type = mediapipe_dot_util_dot_tracking_dot_camera__motion__pb2._CAMERAMOTION
_FRAMESELECTIONRESULT.fields_by_name['features'].message_type = mediapipe_dot_util_dot_tracking_dot_region__flow__pb2._REGIONFLOWFEATURELIST
_FRAMESELECTIONCRITERION.fields_by_name['solution_evaluator'].message_type = mediapipe_dot_util_dot_tracking_dot_frame__selection__solution__evaluator__pb2._FRAMESELECTIONSOLUTIONEVALUATORTYPE
_FRAMESELECTIONOPTIONS.fields_by_name['criterion'].message_type = _FRAMESELECTIONCRITERION
DESCRIPTOR.message_types_by_name['FrameSelectionTimestamp'] = _FRAMESELECTIONTIMESTAMP
DESCRIPTOR.message_types_by_name['FrameSelectionResult'] = _FRAMESELECTIONRESULT
DESCRIPTOR.message_types_by_name['FrameSelectionCriterion'] = _FRAMESELECTIONCRITERION
DESCRIPTOR.message_types_by_name['FrameSelectionOptions'] = _FRAMESELECTIONOPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrameSelectionTimestamp = _reflection.GeneratedProtocolMessageType('FrameSelectionTimestamp', (_message.Message,), dict(
  DESCRIPTOR = _FRAMESELECTIONTIMESTAMP,
  __module__ = 'mediapipe.util.tracking.frame_selection_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FrameSelectionTimestamp)
  ))
_sym_db.RegisterMessage(FrameSelectionTimestamp)

FrameSelectionResult = _reflection.GeneratedProtocolMessageType('FrameSelectionResult', (_message.Message,), dict(
  DESCRIPTOR = _FRAMESELECTIONRESULT,
  __module__ = 'mediapipe.util.tracking.frame_selection_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FrameSelectionResult)
  ))
_sym_db.RegisterMessage(FrameSelectionResult)

FrameSelectionCriterion = _reflection.GeneratedProtocolMessageType('FrameSelectionCriterion', (_message.Message,), dict(
  DESCRIPTOR = _FRAMESELECTIONCRITERION,
  __module__ = 'mediapipe.util.tracking.frame_selection_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FrameSelectionCriterion)
  ))
_sym_db.RegisterMessage(FrameSelectionCriterion)

FrameSelectionOptions = _reflection.GeneratedProtocolMessageType('FrameSelectionOptions', (_message.Message,), dict(
  DESCRIPTOR = _FRAMESELECTIONOPTIONS,
  __module__ = 'mediapipe.util.tracking.frame_selection_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FrameSelectionOptions)
  ))
_sym_db.RegisterMessage(FrameSelectionOptions)


# @@protoc_insertion_point(module_scope)
