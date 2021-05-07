# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import (
    participant_pruning_service_pb2 as com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_participant__pruning__service__pb2,
)


class ParticipantPruningServiceStub(object):
    """Status: experimental interface, will change before it is deemed production
    ready

    Prunes/truncates the "oldest" transactions from the participant (the participant Ledger Api Server plus any other
    participant-local state) by removing a portion of the ledger in such a way that the set of future, allowed
    commands are not affected.

    This enables:
    1. keeping the "inactive" portion of the ledger to a manageable size and
    2. removing inactive state to honor the right to be forgotten.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Prune = channel.unary_unary(
            "/com.daml.ledger.api.v1.admin.ParticipantPruningService/Prune",
            request_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_participant__pruning__service__pb2.PruneRequest.SerializeToString,
            response_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_participant__pruning__service__pb2.PruneResponse.FromString,
        )


class ParticipantPruningServiceServicer(object):
    """Status: experimental interface, will change before it is deemed production
    ready

    Prunes/truncates the "oldest" transactions from the participant (the participant Ledger Api Server plus any other
    participant-local state) by removing a portion of the ledger in such a way that the set of future, allowed
    commands are not affected.

    This enables:
    1. keeping the "inactive" portion of the ledger to a manageable size and
    2. removing inactive state to honor the right to be forgotten.
    """

    def Prune(self, request, context):
        """Prune the ledger specifying the offset before and at which ledger transactions should be removed. Only returns when
        the potentially long-running prune request ends successfully or with one of the following errors:
        - ``INVALID_ARGUMENT``: if the payload, particularly the offset is malformed or missing
        - ``UNIMPLEMENTED``: if the participant is based on a ledger that has not implemented pruning
        - ``INTERNAL``: if the participant has encountered a failure and has potentially applied pruning partially. Such cases
        warrant verifying the participant health before retrying the prune with the same (or a larger, valid) offset.
        Successful retries after such errors ensure that different components reach a consistent pruning state.

        Other GRPC errors can be returned depending on the type of condition preventing a prune:
        - ``OUT_OF_RANGE``: if the participant is not yet able to prune at the specified offset, but without user intervention
        the offset will eventually be usable for pruning.
        - ``FAILED_PRECONDITION`` if some sort of user intervention is required before pruning can proceed at the specified
        offset.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ParticipantPruningServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Prune": grpc.unary_unary_rpc_method_handler(
            servicer.Prune,
            request_deserializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_participant__pruning__service__pb2.PruneRequest.FromString,
            response_serializer=com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_participant__pruning__service__pb2.PruneResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "com.daml.ledger.api.v1.admin.ParticipantPruningService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ParticipantPruningService(object):
    """Status: experimental interface, will change before it is deemed production
    ready

    Prunes/truncates the "oldest" transactions from the participant (the participant Ledger Api Server plus any other
    participant-local state) by removing a portion of the ledger in such a way that the set of future, allowed
    commands are not affected.

    This enables:
    1. keeping the "inactive" portion of the ledger to a manageable size and
    2. removing inactive state to honor the right to be forgotten.
    """

    @staticmethod
    def Prune(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/com.daml.ledger.api.v1.admin.ParticipantPruningService/Prune",
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_participant__pruning__service__pb2.PruneRequest.SerializeToString,
            com_dot_daml_dot_ledger_dot_api_dot_v1_dot_admin_dot_participant__pruning__service__pb2.PruneResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
