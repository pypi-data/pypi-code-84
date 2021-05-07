"""
Type annotations for iotfleethub service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleethub/literals.html)

Usage::

    ```python
    from mypy_boto3_iotfleethub.literals import ApplicationState

    data: ApplicationState = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApplicationState", "ListApplicationsPaginatorName")


ApplicationState = Literal["ACTIVE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
ListApplicationsPaginatorName = Literal["list_applications"]
