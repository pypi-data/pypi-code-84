# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/daml/ledger/api/v1/admin/party_management_service.proto

from google.protobuf import (
    descriptor as _descriptor,
    message as _message,
    reflection as _reflection,
    symbol_database as _symbol_database,
)

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="com/daml/ledger/api/v1/admin/party_management_service.proto",
    package="com.daml.ledger.api.v1.admin",
    syntax="proto3",
    serialized_options=b"\n\034com.daml.ledger.api.v1.adminB PartyManagementServiceOuterClass\252\002\034Com.Daml.Ledger.Api.V1.Admin",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n;com/daml/ledger/api/v1/admin/party_management_service.proto\x12\x1c\x63om.daml.ledger.api.v1.admin"\x19\n\x17GetParticipantIdRequest"2\n\x18GetParticipantIdResponse\x12\x16\n\x0eparticipant_id\x18\x01 \x01(\t"$\n\x11GetPartiesRequest\x12\x0f\n\x07parties\x18\x01 \x03(\t"W\n\x12GetPartiesResponse\x12\x41\n\rparty_details\x18\x01 \x03(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetails"\x19\n\x17ListKnownPartiesRequest"]\n\x18ListKnownPartiesResponse\x12\x41\n\rparty_details\x18\x01 \x03(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetails"C\n\x14\x41llocatePartyRequest\x12\x15\n\rparty_id_hint\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t"Z\n\x15\x41llocatePartyResponse\x12\x41\n\rparty_details\x18\x01 \x01(\x0b\x32*.com.daml.ledger.api.v1.admin.PartyDetails"E\n\x0cPartyDetails\x12\r\n\x05party\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x10\n\x08is_local\x18\x03 \x01(\x08\x32\x8b\x04\n\x16PartyManagementService\x12\x81\x01\n\x10GetParticipantId\x12\x35.com.daml.ledger.api.v1.admin.GetParticipantIdRequest\x1a\x36.com.daml.ledger.api.v1.admin.GetParticipantIdResponse\x12o\n\nGetParties\x12/.com.daml.ledger.api.v1.admin.GetPartiesRequest\x1a\x30.com.daml.ledger.api.v1.admin.GetPartiesResponse\x12\x81\x01\n\x10ListKnownParties\x12\x35.com.daml.ledger.api.v1.admin.ListKnownPartiesRequest\x1a\x36.com.daml.ledger.api.v1.admin.ListKnownPartiesResponse\x12x\n\rAllocateParty\x12\x32.com.daml.ledger.api.v1.admin.AllocatePartyRequest\x1a\x33.com.daml.ledger.api.v1.admin.AllocatePartyResponseB_\n\x1c\x63om.daml.ledger.api.v1.adminB PartyManagementServiceOuterClass\xaa\x02\x1c\x43om.Daml.Ledger.Api.V1.Adminb\x06proto3',
)


_GETPARTICIPANTIDREQUEST = _descriptor.Descriptor(
    name="GetParticipantIdRequest",
    full_name="com.daml.ledger.api.v1.admin.GetParticipantIdRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=93,
    serialized_end=118,
)


_GETPARTICIPANTIDRESPONSE = _descriptor.Descriptor(
    name="GetParticipantIdResponse",
    full_name="com.daml.ledger.api.v1.admin.GetParticipantIdResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="participant_id",
            full_name="com.daml.ledger.api.v1.admin.GetParticipantIdResponse.participant_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=120,
    serialized_end=170,
)


_GETPARTIESREQUEST = _descriptor.Descriptor(
    name="GetPartiesRequest",
    full_name="com.daml.ledger.api.v1.admin.GetPartiesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parties",
            full_name="com.daml.ledger.api.v1.admin.GetPartiesRequest.parties",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=172,
    serialized_end=208,
)


_GETPARTIESRESPONSE = _descriptor.Descriptor(
    name="GetPartiesResponse",
    full_name="com.daml.ledger.api.v1.admin.GetPartiesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="party_details",
            full_name="com.daml.ledger.api.v1.admin.GetPartiesResponse.party_details",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=210,
    serialized_end=297,
)


_LISTKNOWNPARTIESREQUEST = _descriptor.Descriptor(
    name="ListKnownPartiesRequest",
    full_name="com.daml.ledger.api.v1.admin.ListKnownPartiesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=299,
    serialized_end=324,
)


_LISTKNOWNPARTIESRESPONSE = _descriptor.Descriptor(
    name="ListKnownPartiesResponse",
    full_name="com.daml.ledger.api.v1.admin.ListKnownPartiesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="party_details",
            full_name="com.daml.ledger.api.v1.admin.ListKnownPartiesResponse.party_details",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=326,
    serialized_end=419,
)


_ALLOCATEPARTYREQUEST = _descriptor.Descriptor(
    name="AllocatePartyRequest",
    full_name="com.daml.ledger.api.v1.admin.AllocatePartyRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="party_id_hint",
            full_name="com.daml.ledger.api.v1.admin.AllocatePartyRequest.party_id_hint",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="com.daml.ledger.api.v1.admin.AllocatePartyRequest.display_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=421,
    serialized_end=488,
)


_ALLOCATEPARTYRESPONSE = _descriptor.Descriptor(
    name="AllocatePartyResponse",
    full_name="com.daml.ledger.api.v1.admin.AllocatePartyResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="party_details",
            full_name="com.daml.ledger.api.v1.admin.AllocatePartyResponse.party_details",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=490,
    serialized_end=580,
)


_PARTYDETAILS = _descriptor.Descriptor(
    name="PartyDetails",
    full_name="com.daml.ledger.api.v1.admin.PartyDetails",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="party",
            full_name="com.daml.ledger.api.v1.admin.PartyDetails.party",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="display_name",
            full_name="com.daml.ledger.api.v1.admin.PartyDetails.display_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="is_local",
            full_name="com.daml.ledger.api.v1.admin.PartyDetails.is_local",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=582,
    serialized_end=651,
)

_GETPARTIESRESPONSE.fields_by_name["party_details"].message_type = _PARTYDETAILS
_LISTKNOWNPARTIESRESPONSE.fields_by_name["party_details"].message_type = _PARTYDETAILS
_ALLOCATEPARTYRESPONSE.fields_by_name["party_details"].message_type = _PARTYDETAILS
DESCRIPTOR.message_types_by_name["GetParticipantIdRequest"] = _GETPARTICIPANTIDREQUEST
DESCRIPTOR.message_types_by_name["GetParticipantIdResponse"] = _GETPARTICIPANTIDRESPONSE
DESCRIPTOR.message_types_by_name["GetPartiesRequest"] = _GETPARTIESREQUEST
DESCRIPTOR.message_types_by_name["GetPartiesResponse"] = _GETPARTIESRESPONSE
DESCRIPTOR.message_types_by_name["ListKnownPartiesRequest"] = _LISTKNOWNPARTIESREQUEST
DESCRIPTOR.message_types_by_name["ListKnownPartiesResponse"] = _LISTKNOWNPARTIESRESPONSE
DESCRIPTOR.message_types_by_name["AllocatePartyRequest"] = _ALLOCATEPARTYREQUEST
DESCRIPTOR.message_types_by_name["AllocatePartyResponse"] = _ALLOCATEPARTYRESPONSE
DESCRIPTOR.message_types_by_name["PartyDetails"] = _PARTYDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetParticipantIdRequest = _reflection.GeneratedProtocolMessageType(
    "GetParticipantIdRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPARTICIPANTIDREQUEST,
        "__module__": "com.daml.ledger.api.v1.admin.party_management_service_pb2"
        # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GetParticipantIdRequest)
    },
)
_sym_db.RegisterMessage(GetParticipantIdRequest)

GetParticipantIdResponse = _reflection.GeneratedProtocolMessageType(
    "GetParticipantIdResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPARTICIPANTIDRESPONSE,
        "__module__": "com.daml.ledger.api.v1.admin.party_management_service_pb2"
        # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GetParticipantIdResponse)
    },
)
_sym_db.RegisterMessage(GetParticipantIdResponse)

GetPartiesRequest = _reflection.GeneratedProtocolMessageType(
    "GetPartiesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPARTIESREQUEST,
        "__module__": "com.daml.ledger.api.v1.admin.party_management_service_pb2"
        # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GetPartiesRequest)
    },
)
_sym_db.RegisterMessage(GetPartiesRequest)

GetPartiesResponse = _reflection.GeneratedProtocolMessageType(
    "GetPartiesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPARTIESRESPONSE,
        "__module__": "com.daml.ledger.api.v1.admin.party_management_service_pb2"
        # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.GetPartiesResponse)
    },
)
_sym_db.RegisterMessage(GetPartiesResponse)

ListKnownPartiesRequest = _reflection.GeneratedProtocolMessageType(
    "ListKnownPartiesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTKNOWNPARTIESREQUEST,
        "__module__": "com.daml.ledger.api.v1.admin.party_management_service_pb2"
        # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.ListKnownPartiesRequest)
    },
)
_sym_db.RegisterMessage(ListKnownPartiesRequest)

ListKnownPartiesResponse = _reflection.GeneratedProtocolMessageType(
    "ListKnownPartiesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTKNOWNPARTIESRESPONSE,
        "__module__": "com.daml.ledger.api.v1.admin.party_management_service_pb2"
        # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.ListKnownPartiesResponse)
    },
)
_sym_db.RegisterMessage(ListKnownPartiesResponse)

AllocatePartyRequest = _reflection.GeneratedProtocolMessageType(
    "AllocatePartyRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _ALLOCATEPARTYREQUEST,
        "__module__": "com.daml.ledger.api.v1.admin.party_management_service_pb2"
        # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.AllocatePartyRequest)
    },
)
_sym_db.RegisterMessage(AllocatePartyRequest)

AllocatePartyResponse = _reflection.GeneratedProtocolMessageType(
    "AllocatePartyResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _ALLOCATEPARTYRESPONSE,
        "__module__": "com.daml.ledger.api.v1.admin.party_management_service_pb2"
        # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.AllocatePartyResponse)
    },
)
_sym_db.RegisterMessage(AllocatePartyResponse)

PartyDetails = _reflection.GeneratedProtocolMessageType(
    "PartyDetails",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARTYDETAILS,
        "__module__": "com.daml.ledger.api.v1.admin.party_management_service_pb2"
        # @@protoc_insertion_point(class_scope:com.daml.ledger.api.v1.admin.PartyDetails)
    },
)
_sym_db.RegisterMessage(PartyDetails)


DESCRIPTOR._options = None

_PARTYMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
    name="PartyManagementService",
    full_name="com.daml.ledger.api.v1.admin.PartyManagementService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=654,
    serialized_end=1177,
    methods=[
        _descriptor.MethodDescriptor(
            name="GetParticipantId",
            full_name="com.daml.ledger.api.v1.admin.PartyManagementService.GetParticipantId",
            index=0,
            containing_service=None,
            input_type=_GETPARTICIPANTIDREQUEST,
            output_type=_GETPARTICIPANTIDRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetParties",
            full_name="com.daml.ledger.api.v1.admin.PartyManagementService.GetParties",
            index=1,
            containing_service=None,
            input_type=_GETPARTIESREQUEST,
            output_type=_GETPARTIESRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ListKnownParties",
            full_name="com.daml.ledger.api.v1.admin.PartyManagementService.ListKnownParties",
            index=2,
            containing_service=None,
            input_type=_LISTKNOWNPARTIESREQUEST,
            output_type=_LISTKNOWNPARTIESRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="AllocateParty",
            full_name="com.daml.ledger.api.v1.admin.PartyManagementService.AllocateParty",
            index=3,
            containing_service=None,
            input_type=_ALLOCATEPARTYREQUEST,
            output_type=_ALLOCATEPARTYRESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_PARTYMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name["PartyManagementService"] = _PARTYMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)
