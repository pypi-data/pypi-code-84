# Copyright 2020 StrongDM Inc
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
# 
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import nodes_pb2 as nodes__pb2


class NodesStub(object):
    """Nodes make up the strongDM network, and allow your users to connect securely to your resources. There are two types of nodes:
    - **Gateways** are the entry points into network. They listen for connection from the strongDM client, and provide access to databases and servers.
    - **Relays** are used to extend the strongDM network into segmented subnets. They provide access to databases and servers but do not listen for incoming connections.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/v1.Nodes/Create',
                request_serializer=nodes__pb2.NodeCreateRequest.SerializeToString,
                response_deserializer=nodes__pb2.NodeCreateResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/v1.Nodes/Get',
                request_serializer=nodes__pb2.NodeGetRequest.SerializeToString,
                response_deserializer=nodes__pb2.NodeGetResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/v1.Nodes/Update',
                request_serializer=nodes__pb2.NodeUpdateRequest.SerializeToString,
                response_deserializer=nodes__pb2.NodeUpdateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/v1.Nodes/Delete',
                request_serializer=nodes__pb2.NodeDeleteRequest.SerializeToString,
                response_deserializer=nodes__pb2.NodeDeleteResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/v1.Nodes/List',
                request_serializer=nodes__pb2.NodeListRequest.SerializeToString,
                response_deserializer=nodes__pb2.NodeListResponse.FromString,
                )


class NodesServicer(object):
    """Nodes make up the strongDM network, and allow your users to connect securely to your resources. There are two types of nodes:
    - **Gateways** are the entry points into network. They listen for connection from the strongDM client, and provide access to databases and servers.
    - **Relays** are used to extend the strongDM network into segmented subnets. They provide access to databases and servers but do not listen for incoming connections.
    """

    def Create(self, request, context):
        """Create registers a new Node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get reads one Node by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update patches a Node by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete removes a Node by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List gets a list of Nodes matching a given set of criteria.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=nodes__pb2.NodeCreateRequest.FromString,
                    response_serializer=nodes__pb2.NodeCreateResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=nodes__pb2.NodeGetRequest.FromString,
                    response_serializer=nodes__pb2.NodeGetResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=nodes__pb2.NodeUpdateRequest.FromString,
                    response_serializer=nodes__pb2.NodeUpdateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=nodes__pb2.NodeDeleteRequest.FromString,
                    response_serializer=nodes__pb2.NodeDeleteResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=nodes__pb2.NodeListRequest.FromString,
                    response_serializer=nodes__pb2.NodeListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.Nodes', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Nodes(object):
    """Nodes make up the strongDM network, and allow your users to connect securely to your resources. There are two types of nodes:
    - **Gateways** are the entry points into network. They listen for connection from the strongDM client, and provide access to databases and servers.
    - **Relays** are used to extend the strongDM network into segmented subnets. They provide access to databases and servers but do not listen for incoming connections.
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.Nodes/Create',
            nodes__pb2.NodeCreateRequest.SerializeToString,
            nodes__pb2.NodeCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.Nodes/Get',
            nodes__pb2.NodeGetRequest.SerializeToString,
            nodes__pb2.NodeGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.Nodes/Update',
            nodes__pb2.NodeUpdateRequest.SerializeToString,
            nodes__pb2.NodeUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.Nodes/Delete',
            nodes__pb2.NodeDeleteRequest.SerializeToString,
            nodes__pb2.NodeDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.Nodes/List',
            nodes__pb2.NodeListRequest.SerializeToString,
            nodes__pb2.NodeListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
