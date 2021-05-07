# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetDomainResult',
    'AwaitableGetDomainResult',
    'get_domain',
]

@pulumi.output_type
class GetDomainResult:
    """
    A collection of values returned by getDomain.
    """
    def __init__(__self__, access_policies=None, advanced_options=None, advanced_security_options=None, arn=None, cluster_configs=None, cognito_options=None, created=None, deleted=None, domain_id=None, domain_name=None, ebs_options=None, elasticsearch_version=None, encryption_at_rests=None, endpoint=None, id=None, kibana_endpoint=None, log_publishing_options=None, node_to_node_encryptions=None, processing=None, snapshot_options=None, tags=None, vpc_options=None):
        if access_policies and not isinstance(access_policies, str):
            raise TypeError("Expected argument 'access_policies' to be a str")
        pulumi.set(__self__, "access_policies", access_policies)
        if advanced_options and not isinstance(advanced_options, dict):
            raise TypeError("Expected argument 'advanced_options' to be a dict")
        pulumi.set(__self__, "advanced_options", advanced_options)
        if advanced_security_options and not isinstance(advanced_security_options, list):
            raise TypeError("Expected argument 'advanced_security_options' to be a list")
        pulumi.set(__self__, "advanced_security_options", advanced_security_options)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if cluster_configs and not isinstance(cluster_configs, list):
            raise TypeError("Expected argument 'cluster_configs' to be a list")
        pulumi.set(__self__, "cluster_configs", cluster_configs)
        if cognito_options and not isinstance(cognito_options, list):
            raise TypeError("Expected argument 'cognito_options' to be a list")
        pulumi.set(__self__, "cognito_options", cognito_options)
        if created and not isinstance(created, bool):
            raise TypeError("Expected argument 'created' to be a bool")
        pulumi.set(__self__, "created", created)
        if deleted and not isinstance(deleted, bool):
            raise TypeError("Expected argument 'deleted' to be a bool")
        pulumi.set(__self__, "deleted", deleted)
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        pulumi.set(__self__, "domain_id", domain_id)
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if ebs_options and not isinstance(ebs_options, list):
            raise TypeError("Expected argument 'ebs_options' to be a list")
        pulumi.set(__self__, "ebs_options", ebs_options)
        if elasticsearch_version and not isinstance(elasticsearch_version, str):
            raise TypeError("Expected argument 'elasticsearch_version' to be a str")
        pulumi.set(__self__, "elasticsearch_version", elasticsearch_version)
        if encryption_at_rests and not isinstance(encryption_at_rests, list):
            raise TypeError("Expected argument 'encryption_at_rests' to be a list")
        pulumi.set(__self__, "encryption_at_rests", encryption_at_rests)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kibana_endpoint and not isinstance(kibana_endpoint, str):
            raise TypeError("Expected argument 'kibana_endpoint' to be a str")
        pulumi.set(__self__, "kibana_endpoint", kibana_endpoint)
        if log_publishing_options and not isinstance(log_publishing_options, list):
            raise TypeError("Expected argument 'log_publishing_options' to be a list")
        pulumi.set(__self__, "log_publishing_options", log_publishing_options)
        if node_to_node_encryptions and not isinstance(node_to_node_encryptions, list):
            raise TypeError("Expected argument 'node_to_node_encryptions' to be a list")
        pulumi.set(__self__, "node_to_node_encryptions", node_to_node_encryptions)
        if processing and not isinstance(processing, bool):
            raise TypeError("Expected argument 'processing' to be a bool")
        pulumi.set(__self__, "processing", processing)
        if snapshot_options and not isinstance(snapshot_options, list):
            raise TypeError("Expected argument 'snapshot_options' to be a list")
        pulumi.set(__self__, "snapshot_options", snapshot_options)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if vpc_options and not isinstance(vpc_options, list):
            raise TypeError("Expected argument 'vpc_options' to be a list")
        pulumi.set(__self__, "vpc_options", vpc_options)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> str:
        """
        The policy document attached to the domain.
        """
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="advancedOptions")
    def advanced_options(self) -> Mapping[str, str]:
        """
        Key-value string pairs to specify advanced configuration options.
        """
        return pulumi.get(self, "advanced_options")

    @property
    @pulumi.getter(name="advancedSecurityOptions")
    def advanced_security_options(self) -> Sequence['outputs.GetDomainAdvancedSecurityOptionResult']:
        """
        Status of the Elasticsearch domain's advanced security options. The block consists of the following attributes:
        """
        return pulumi.get(self, "advanced_security_options")

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the domain.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clusterConfigs")
    def cluster_configs(self) -> Sequence['outputs.GetDomainClusterConfigResult']:
        """
        Cluster configuration of the domain.
        """
        return pulumi.get(self, "cluster_configs")

    @property
    @pulumi.getter(name="cognitoOptions")
    def cognito_options(self) -> Sequence['outputs.GetDomainCognitoOptionResult']:
        """
        Domain Amazon Cognito Authentication options for Kibana.
        """
        return pulumi.get(self, "cognito_options")

    @property
    @pulumi.getter
    def created(self) -> bool:
        """
        Status of the creation of the domain.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def deleted(self) -> bool:
        """
        Status of the deletion of the domain.
        """
        return pulumi.get(self, "deleted")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> str:
        """
        Unique identifier for the domain.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> str:
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="ebsOptions")
    def ebs_options(self) -> Sequence['outputs.GetDomainEbsOptionResult']:
        """
        EBS Options for the instances in the domain.
        """
        return pulumi.get(self, "ebs_options")

    @property
    @pulumi.getter(name="elasticsearchVersion")
    def elasticsearch_version(self) -> str:
        """
        ElasticSearch version for the domain.
        """
        return pulumi.get(self, "elasticsearch_version")

    @property
    @pulumi.getter(name="encryptionAtRests")
    def encryption_at_rests(self) -> Sequence['outputs.GetDomainEncryptionAtRestResult']:
        """
        Domain encryption at rest related options.
        """
        return pulumi.get(self, "encryption_at_rests")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        Domain-specific endpoint used to submit index, search, and data upload requests.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kibanaEndpoint")
    def kibana_endpoint(self) -> str:
        """
        Domain-specific endpoint used to access the Kibana application.
        """
        return pulumi.get(self, "kibana_endpoint")

    @property
    @pulumi.getter(name="logPublishingOptions")
    def log_publishing_options(self) -> Sequence['outputs.GetDomainLogPublishingOptionResult']:
        """
        Domain log publishing related options.
        """
        return pulumi.get(self, "log_publishing_options")

    @property
    @pulumi.getter(name="nodeToNodeEncryptions")
    def node_to_node_encryptions(self) -> Sequence['outputs.GetDomainNodeToNodeEncryptionResult']:
        """
        Domain in transit encryption related options.
        """
        return pulumi.get(self, "node_to_node_encryptions")

    @property
    @pulumi.getter
    def processing(self) -> bool:
        """
        Status of a configuration change in the domain.
        * `snapshot_options` – Domain snapshot related options.
        """
        return pulumi.get(self, "processing")

    @property
    @pulumi.getter(name="snapshotOptions")
    def snapshot_options(self) -> Sequence['outputs.GetDomainSnapshotOptionResult']:
        return pulumi.get(self, "snapshot_options")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        The tags assigned to the domain.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcOptions")
    def vpc_options(self) -> Sequence['outputs.GetDomainVpcOptionResult']:
        """
        VPC Options for private Elasticsearch domains.
        """
        return pulumi.get(self, "vpc_options")


class AwaitableGetDomainResult(GetDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainResult(
            access_policies=self.access_policies,
            advanced_options=self.advanced_options,
            advanced_security_options=self.advanced_security_options,
            arn=self.arn,
            cluster_configs=self.cluster_configs,
            cognito_options=self.cognito_options,
            created=self.created,
            deleted=self.deleted,
            domain_id=self.domain_id,
            domain_name=self.domain_name,
            ebs_options=self.ebs_options,
            elasticsearch_version=self.elasticsearch_version,
            encryption_at_rests=self.encryption_at_rests,
            endpoint=self.endpoint,
            id=self.id,
            kibana_endpoint=self.kibana_endpoint,
            log_publishing_options=self.log_publishing_options,
            node_to_node_encryptions=self.node_to_node_encryptions,
            processing=self.processing,
            snapshot_options=self.snapshot_options,
            tags=self.tags,
            vpc_options=self.vpc_options)


def get_domain(domain_name: Optional[str] = None,
               tags: Optional[Mapping[str, str]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainResult:
    """
    Use this data source to get information about an Elasticsearch Domain

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    my_domain = aws.elasticsearch.get_domain(domain_name="my-domain-name")
    ```


    :param str domain_name: Name of the domain.
    :param Mapping[str, str] tags: The tags assigned to the domain.
    """
    __args__ = dict()
    __args__['domainName'] = domain_name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:elasticsearch/getDomain:getDomain', __args__, opts=opts, typ=GetDomainResult).value

    return AwaitableGetDomainResult(
        access_policies=__ret__.access_policies,
        advanced_options=__ret__.advanced_options,
        advanced_security_options=__ret__.advanced_security_options,
        arn=__ret__.arn,
        cluster_configs=__ret__.cluster_configs,
        cognito_options=__ret__.cognito_options,
        created=__ret__.created,
        deleted=__ret__.deleted,
        domain_id=__ret__.domain_id,
        domain_name=__ret__.domain_name,
        ebs_options=__ret__.ebs_options,
        elasticsearch_version=__ret__.elasticsearch_version,
        encryption_at_rests=__ret__.encryption_at_rests,
        endpoint=__ret__.endpoint,
        id=__ret__.id,
        kibana_endpoint=__ret__.kibana_endpoint,
        log_publishing_options=__ret__.log_publishing_options,
        node_to_node_encryptions=__ret__.node_to_node_encryptions,
        processing=__ret__.processing,
        snapshot_options=__ret__.snapshot_options,
        tags=__ret__.tags,
        vpc_options=__ret__.vpc_options)
