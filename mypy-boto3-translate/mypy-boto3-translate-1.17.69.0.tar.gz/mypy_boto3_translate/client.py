"""
Type annotations for translate service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_translate import TranslateClient

    client: TranslateClient = boto3.client("translate")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_translate.literals import TerminologyDataFormat
from mypy_boto3_translate.paginator import ListTerminologiesPaginator
from mypy_boto3_translate.type_defs import (
    CreateParallelDataResponseTypeDef,
    DeleteParallelDataResponseTypeDef,
    DescribeTextTranslationJobResponseTypeDef,
    EncryptionKeyTypeDef,
    GetParallelDataResponseTypeDef,
    GetTerminologyResponseTypeDef,
    ImportTerminologyResponseTypeDef,
    InputDataConfigTypeDef,
    ListParallelDataResponseTypeDef,
    ListTerminologiesResponseTypeDef,
    ListTextTranslationJobsResponseTypeDef,
    OutputDataConfigTypeDef,
    ParallelDataConfigTypeDef,
    StartTextTranslationJobResponseTypeDef,
    StopTextTranslationJobResponseTypeDef,
    TerminologyDataTypeDef,
    TextTranslationJobFilterTypeDef,
    TranslateTextResponseTypeDef,
    UpdateParallelDataResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TranslateClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DetectedLanguageLowConfidenceException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidFilterException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TextSizeLimitExceededException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnsupportedLanguagePairException: Type[BotocoreClientError]


class TranslateClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#can-paginate)
        """

    def create_parallel_data(
        self,
        Name: str,
        ParallelDataConfig: "ParallelDataConfigTypeDef",
        ClientToken: str,
        Description: str = None,
        EncryptionKey: "EncryptionKeyTypeDef" = None,
    ) -> CreateParallelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.create_parallel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#create-parallel-data)
        """

    def delete_parallel_data(self, Name: str) -> DeleteParallelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.delete_parallel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#delete-parallel-data)
        """

    def delete_terminology(self, Name: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.delete_terminology)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#delete-terminology)
        """

    def describe_text_translation_job(
        self, JobId: str
    ) -> DescribeTextTranslationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.describe_text_translation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#describe-text-translation-job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#generate-presigned-url)
        """

    def get_parallel_data(self, Name: str) -> GetParallelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.get_parallel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#get-parallel-data)
        """

    def get_terminology(
        self, Name: str, TerminologyDataFormat: TerminologyDataFormat
    ) -> GetTerminologyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.get_terminology)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#get-terminology)
        """

    def import_terminology(
        self,
        Name: str,
        MergeStrategy: Literal["OVERWRITE"],
        TerminologyData: TerminologyDataTypeDef,
        Description: str = None,
        EncryptionKey: "EncryptionKeyTypeDef" = None,
    ) -> ImportTerminologyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.import_terminology)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#import-terminology)
        """

    def list_parallel_data(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListParallelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.list_parallel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#list-parallel-data)
        """

    def list_terminologies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListTerminologiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.list_terminologies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#list-terminologies)
        """

    def list_text_translation_jobs(
        self,
        Filter: TextTranslationJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTextTranslationJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.list_text_translation_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#list-text-translation-jobs)
        """

    def start_text_translation_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        SourceLanguageCode: str,
        TargetLanguageCodes: List[str],
        ClientToken: str,
        JobName: str = None,
        TerminologyNames: List[str] = None,
        ParallelDataNames: List[str] = None,
    ) -> StartTextTranslationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.start_text_translation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#start-text-translation-job)
        """

    def stop_text_translation_job(self, JobId: str) -> StopTextTranslationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.stop_text_translation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#stop-text-translation-job)
        """

    def translate_text(
        self,
        Text: str,
        SourceLanguageCode: str,
        TargetLanguageCode: str,
        TerminologyNames: List[str] = None,
    ) -> TranslateTextResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.translate_text)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#translate-text)
        """

    def update_parallel_data(
        self,
        Name: str,
        ParallelDataConfig: "ParallelDataConfigTypeDef",
        ClientToken: str,
        Description: str = None,
    ) -> UpdateParallelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Client.update_parallel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/client.html#update-parallel-data)
        """

    def get_paginator(
        self, operation_name: Literal["list_terminologies"]
    ) -> ListTerminologiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.69/reference/services/translate.html#Translate.Paginator.ListTerminologies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/paginators.html#listterminologiespaginator)
        """
