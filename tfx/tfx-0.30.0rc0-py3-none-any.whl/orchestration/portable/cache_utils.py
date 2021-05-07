# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Portable library for resolving cached outputs."""
import collections
import copy
import hashlib
from typing import Any, Dict, List, Mapping, Optional, Sequence, Text

from tfx import types
from tfx.dsl.io import fileio
from tfx.orchestration import metadata
from tfx.orchestration.portable.mlmd import context_lib
from tfx.orchestration.portable.mlmd import execution_lib
from tfx.proto.orchestration import pipeline_pb2
from tfx.types import artifact_utils

from google.protobuf import message
from ml_metadata.proto import metadata_store_pb2


def _get_outputs_of_execution(
    metadata_handler: metadata.Metadata,
    execution_id: int) -> Optional[Dict[Text, List[types.Artifact]]]:
  """Fetches outputs produced by a historical execution.

  Args:
    metadata_handler: A handler to access MLMD store.
    execution_id: The id of the execution that produced the outputs.

  Returns:
    A dict of key -> List[Artifact] as the result if qualified outputs found.
    Otherwise returns None.
  """
  result = collections.defaultdict(list)

  output_events = [
      event for event in metadata_handler.store.get_events_by_execution_ids(
          [execution_id]) if event.type == metadata_store_pb2.Event.OUTPUT
  ]
  cached_output_artifacts = metadata_handler.store.get_artifacts_by_id(
      [e.artifact_id for e in output_events])
  for artifact in cached_output_artifacts:
    # Non-live artifact means partial result, will not be used.
    if artifact.state != metadata_store_pb2.Artifact.LIVE:
      return None

  artifact_types = metadata_handler.store.get_artifact_types_by_id(
      [a.type_id for a in cached_output_artifacts])

  for event, mlmd_artifact, artifact_type in zip(output_events,
                                                 cached_output_artifacts,
                                                 artifact_types):
    key = event.path.steps[0].key
    tfx_artifact = artifact_utils.deserialize_artifact(artifact_type,
                                                       mlmd_artifact)
    result[key].append(tfx_artifact)

  return result


def get_cache_context(
    metadata_handler: metadata.Metadata,
    pipeline_node: pipeline_pb2.PipelineNode,
    pipeline_info: pipeline_pb2.PipelineInfo,
    executor_spec: Optional[message.Message] = None,
    input_artifacts: Optional[Mapping[Text, Sequence[types.Artifact]]] = None,
    output_artifacts: Optional[Mapping[Text, Sequence[types.Artifact]]] = None,
    parameters: Optional[Mapping[Text,
                                 Any]] = None) -> metadata_store_pb2.Context:
  """Gets cache context for a potential node execution.

  The cache key is generated by applying SHA-256 hashing function on:
  - Serialized pipeline info.
  - Serialized node_info of the PipelineNode.
  - Serialized executor spec
  - Serialized input artifacts if any.
  - Serialized output artifacts if any. The uri was removed during the process.
  - Serialized parameters if any.
  - Serialized module file content if module file is present in parameters.

  Args:
    metadata_handler: A handler to access MLMD store.
    pipeline_node: A pipeline_pb2.PipelineNode instance to represent the node.
    pipeline_info: Information of the pipeline.
    executor_spec: A proto message representing the executor specification.
    input_artifacts: Input artifacts of the potential execution. The order of
      the artifacts under a key matters when calculating the cache key.
    output_artifacts: Output artifacts skeleton of the potential execution. The
      order of the artifadts under a key matters when calculating the cache key.
    parameters: Parameters of the potential execution.

  Returns:
    A metadata_store_pb2.Context for the cache key.
  """
  h = hashlib.sha256()
  h.update(pipeline_info.SerializeToString(deterministic=True))
  h.update(pipeline_node.node_info.SerializeToString(deterministic=True))
  if executor_spec:
    h.update(executor_spec.SerializeToString(deterministic=True))
  for key in sorted(input_artifacts or {}):
    h.update(key.encode())
    for artifact in input_artifacts[key]:
      h.update(artifact.mlmd_artifact.SerializeToString(deterministic=True))
  for key in sorted(output_artifacts or {}):
    h.update(key.encode())
    for artifact in output_artifacts[key]:
      stateless_artifact = copy.deepcopy(artifact)
      # Output uri and name should not be taken into consideration as cache key.
      stateless_artifact.uri = ''
      stateless_artifact.name = ''
      h.update(
          stateless_artifact.mlmd_artifact.SerializeToString(
              deterministic=True))
  parameters = parameters or {}
  for key, value in sorted(parameters.items()):
    h.update(key.encode())
    h.update(str(value).encode())

  # Special treatment for module files as they will be used as part of the logic
  # for processing. Currently this pattern is employeed by Trainer and
  # Transform.
  if ('module_file' in parameters and parameters['module_file'] and
      fileio.exists(parameters['module_file'])):
    with fileio.open(parameters['module_file'], 'r') as f:
      h.update(f.read().encode())

  return context_lib.register_context_if_not_exists(
      metadata_handler=metadata_handler,
      context_type_name=context_lib.CONTEXT_TYPE_EXECUTION_CACHE,
      context_name=h.hexdigest())


def get_cached_outputs(
    metadata_handler: metadata.Metadata,
    cache_context: metadata_store_pb2.Context,
) -> Optional[Dict[Text, List[types.Artifact]]]:
  """Tries to get the cached output artifacts given a cache context.

  Args:
    metadata_handler: A handler to access MLMD store.
    cache_context: The context representing the cache key.

  Returns:
    The cached output artifacts in a dict format. None if no qualified cache
    result is found.
  """
  # Only success executions should be the producer of cached outputs.
  cached_executions = filter(
      execution_lib.is_execution_successful,
      metadata_handler.store.get_executions_by_context(cache_context.id))
  if not cached_executions:
    return None
  # Sorts the candidate executions from newer to older.
  cached_executions = sorted(
      cached_executions,
      key=lambda e: e.last_update_time_since_epoch,
      reverse=True)

  # Defensively traverses candidate executions and returns once we find an
  # execution with valid outputs.
  for execution in cached_executions:
    cached_output_artifacts = _get_outputs_of_execution(metadata_handler,
                                                        execution.id)
    if cached_output_artifacts is not None:
      return cached_output_artifacts

  return None
