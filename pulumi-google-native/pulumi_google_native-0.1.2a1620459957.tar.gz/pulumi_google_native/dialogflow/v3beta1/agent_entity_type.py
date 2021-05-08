# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AgentEntityTypeArgs', 'AgentEntityType']

@pulumi.input_type
class AgentEntityTypeArgs:
    def __init__(__self__, *,
                 agents_id: pulumi.Input[str],
                 entity_types_id: pulumi.Input[str],
                 locations_id: pulumi.Input[str],
                 projects_id: pulumi.Input[str],
                 auto_expansion_mode: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_fuzzy_extraction: Optional[pulumi.Input[bool]] = None,
                 entities: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EntityTypeEntityArgs']]]] = None,
                 excluded_phrases: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhraseArgs']]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 redact: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a AgentEntityType resource.
        :param pulumi.Input[str] auto_expansion_mode: Indicates whether the entity type can be automatically expanded.
        :param pulumi.Input[str] display_name: Required. The human-readable name of the entity type, unique within the agent.
        :param pulumi.Input[bool] enable_fuzzy_extraction: Enables fuzzy entity extraction during classification.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EntityTypeEntityArgs']]] entities: The collection of entity entries associated with the entity type.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhraseArgs']]] excluded_phrases: Collection of exceptional words and phrases that shouldn't be matched. For example, if you have a size entity type with entry `giant`(an adjective), you might consider adding `giants`(a noun) as an exclusion. If the kind of entity type is `KIND_MAP`, then the phrases specified by entities and excluded phrases should be mutually exclusive.
        :param pulumi.Input[str] kind: Required. Indicates the kind of entity type.
        :param pulumi.Input[str] name: The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType. Format: `projects//locations//agents//entityTypes/`.
        :param pulumi.Input[bool] redact: Indicates whether parameters of the entity type should be redacted in log. If redaction is enabled, page parameters and intent parameters referring to the entity type will be replaced by parameter name during logging.
        """
        pulumi.set(__self__, "agents_id", agents_id)
        pulumi.set(__self__, "entity_types_id", entity_types_id)
        pulumi.set(__self__, "locations_id", locations_id)
        pulumi.set(__self__, "projects_id", projects_id)
        if auto_expansion_mode is not None:
            pulumi.set(__self__, "auto_expansion_mode", auto_expansion_mode)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if enable_fuzzy_extraction is not None:
            pulumi.set(__self__, "enable_fuzzy_extraction", enable_fuzzy_extraction)
        if entities is not None:
            pulumi.set(__self__, "entities", entities)
        if excluded_phrases is not None:
            pulumi.set(__self__, "excluded_phrases", excluded_phrases)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if language_code is not None:
            pulumi.set(__self__, "language_code", language_code)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if redact is not None:
            pulumi.set(__self__, "redact", redact)

    @property
    @pulumi.getter(name="agentsId")
    def agents_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "agents_id")

    @agents_id.setter
    def agents_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "agents_id", value)

    @property
    @pulumi.getter(name="entityTypesId")
    def entity_types_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "entity_types_id")

    @entity_types_id.setter
    def entity_types_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "entity_types_id", value)

    @property
    @pulumi.getter(name="locationsId")
    def locations_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "locations_id")

    @locations_id.setter
    def locations_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "locations_id", value)

    @property
    @pulumi.getter(name="projectsId")
    def projects_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "projects_id")

    @projects_id.setter
    def projects_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "projects_id", value)

    @property
    @pulumi.getter(name="autoExpansionMode")
    def auto_expansion_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether the entity type can be automatically expanded.
        """
        return pulumi.get(self, "auto_expansion_mode")

    @auto_expansion_mode.setter
    def auto_expansion_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_expansion_mode", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Required. The human-readable name of the entity type, unique within the agent.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables fuzzy entity extraction during classification.
        """
        return pulumi.get(self, "enable_fuzzy_extraction")

    @enable_fuzzy_extraction.setter
    def enable_fuzzy_extraction(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_fuzzy_extraction", value)

    @property
    @pulumi.getter
    def entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EntityTypeEntityArgs']]]]:
        """
        The collection of entity entries associated with the entity type.
        """
        return pulumi.get(self, "entities")

    @entities.setter
    def entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EntityTypeEntityArgs']]]]):
        pulumi.set(self, "entities", value)

    @property
    @pulumi.getter(name="excludedPhrases")
    def excluded_phrases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhraseArgs']]]]:
        """
        Collection of exceptional words and phrases that shouldn't be matched. For example, if you have a size entity type with entry `giant`(an adjective), you might consider adding `giants`(a noun) as an exclusion. If the kind of entity type is `KIND_MAP`, then the phrases specified by entities and excluded phrases should be mutually exclusive.
        """
        return pulumi.get(self, "excluded_phrases")

    @excluded_phrases.setter
    def excluded_phrases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhraseArgs']]]]):
        pulumi.set(self, "excluded_phrases", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Required. Indicates the kind of entity type.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "language_code")

    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "language_code", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType. Format: `projects//locations//agents//entityTypes/`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def redact(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether parameters of the entity type should be redacted in log. If redaction is enabled, page parameters and intent parameters referring to the entity type will be replaced by parameter name during logging.
        """
        return pulumi.get(self, "redact")

    @redact.setter
    def redact(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "redact", value)


class AgentEntityType(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agents_id: Optional[pulumi.Input[str]] = None,
                 auto_expansion_mode: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_fuzzy_extraction: Optional[pulumi.Input[bool]] = None,
                 entities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EntityTypeEntityArgs']]]]] = None,
                 entity_types_id: Optional[pulumi.Input[str]] = None,
                 excluded_phrases: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhraseArgs']]]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 redact: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Creates an entity type in the specified agent.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_expansion_mode: Indicates whether the entity type can be automatically expanded.
        :param pulumi.Input[str] display_name: Required. The human-readable name of the entity type, unique within the agent.
        :param pulumi.Input[bool] enable_fuzzy_extraction: Enables fuzzy entity extraction during classification.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EntityTypeEntityArgs']]]] entities: The collection of entity entries associated with the entity type.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhraseArgs']]]] excluded_phrases: Collection of exceptional words and phrases that shouldn't be matched. For example, if you have a size entity type with entry `giant`(an adjective), you might consider adding `giants`(a noun) as an exclusion. If the kind of entity type is `KIND_MAP`, then the phrases specified by entities and excluded phrases should be mutually exclusive.
        :param pulumi.Input[str] kind: Required. Indicates the kind of entity type.
        :param pulumi.Input[str] name: The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType. Format: `projects//locations//agents//entityTypes/`.
        :param pulumi.Input[bool] redact: Indicates whether parameters of the entity type should be redacted in log. If redaction is enabled, page parameters and intent parameters referring to the entity type will be replaced by parameter name during logging.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AgentEntityTypeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an entity type in the specified agent.

        :param str resource_name: The name of the resource.
        :param AgentEntityTypeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AgentEntityTypeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agents_id: Optional[pulumi.Input[str]] = None,
                 auto_expansion_mode: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_fuzzy_extraction: Optional[pulumi.Input[bool]] = None,
                 entities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EntityTypeEntityArgs']]]]] = None,
                 entity_types_id: Optional[pulumi.Input[str]] = None,
                 excluded_phrases: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhraseArgs']]]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 locations_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects_id: Optional[pulumi.Input[str]] = None,
                 redact: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AgentEntityTypeArgs.__new__(AgentEntityTypeArgs)

            if agents_id is None and not opts.urn:
                raise TypeError("Missing required property 'agents_id'")
            __props__.__dict__["agents_id"] = agents_id
            __props__.__dict__["auto_expansion_mode"] = auto_expansion_mode
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["enable_fuzzy_extraction"] = enable_fuzzy_extraction
            __props__.__dict__["entities"] = entities
            if entity_types_id is None and not opts.urn:
                raise TypeError("Missing required property 'entity_types_id'")
            __props__.__dict__["entity_types_id"] = entity_types_id
            __props__.__dict__["excluded_phrases"] = excluded_phrases
            __props__.__dict__["kind"] = kind
            __props__.__dict__["language_code"] = language_code
            if locations_id is None and not opts.urn:
                raise TypeError("Missing required property 'locations_id'")
            __props__.__dict__["locations_id"] = locations_id
            __props__.__dict__["name"] = name
            if projects_id is None and not opts.urn:
                raise TypeError("Missing required property 'projects_id'")
            __props__.__dict__["projects_id"] = projects_id
            __props__.__dict__["redact"] = redact
        super(AgentEntityType, __self__).__init__(
            'google-native:dialogflow/v3beta1:AgentEntityType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AgentEntityType':
        """
        Get an existing AgentEntityType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AgentEntityTypeArgs.__new__(AgentEntityTypeArgs)

        __props__.__dict__["auto_expansion_mode"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["enable_fuzzy_extraction"] = None
        __props__.__dict__["entities"] = None
        __props__.__dict__["excluded_phrases"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["redact"] = None
        return AgentEntityType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoExpansionMode")
    def auto_expansion_mode(self) -> pulumi.Output[str]:
        """
        Indicates whether the entity type can be automatically expanded.
        """
        return pulumi.get(self, "auto_expansion_mode")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Required. The human-readable name of the entity type, unique within the agent.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> pulumi.Output[bool]:
        """
        Enables fuzzy entity extraction during classification.
        """
        return pulumi.get(self, "enable_fuzzy_extraction")

    @property
    @pulumi.getter
    def entities(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowCxV3beta1EntityTypeEntityResponse']]:
        """
        The collection of entity entries associated with the entity type.
        """
        return pulumi.get(self, "entities")

    @property
    @pulumi.getter(name="excludedPhrases")
    def excluded_phrases(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowCxV3beta1EntityTypeExcludedPhraseResponse']]:
        """
        Collection of exceptional words and phrases that shouldn't be matched. For example, if you have a size entity type with entry `giant`(an adjective), you might consider adding `giants`(a noun) as an exclusion. If the kind of entity type is `KIND_MAP`, then the phrases specified by entities and excluded phrases should be mutually exclusive.
        """
        return pulumi.get(self, "excluded_phrases")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Required. Indicates the kind of entity type.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType. Format: `projects//locations//agents//entityTypes/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def redact(self) -> pulumi.Output[bool]:
        """
        Indicates whether parameters of the entity type should be redacted in log. If redaction is enabled, page parameters and intent parameters referring to the entity type will be replaced by parameter name during logging.
        """
        return pulumi.get(self, "redact")

