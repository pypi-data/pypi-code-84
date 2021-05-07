"""
Type annotations for lexv2-runtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/literals.html)

Usage::

    ```python
    from mypy_boto3_lexv2_runtime.literals import ConfirmationState

    data: ConfirmationState = "Confirmed"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ConfirmationState",
    "DialogActionType",
    "IntentState",
    "MessageContentType",
    "SentimentType",
)


ConfirmationState = Literal["Confirmed", "Denied", "None"]
DialogActionType = Literal["Close", "ConfirmIntent", "Delegate", "ElicitIntent", "ElicitSlot"]
IntentState = Literal["Failed", "Fulfilled", "InProgress", "ReadyForFulfillment", "Waiting"]
MessageContentType = Literal["CustomPayload", "ImageResponseCard", "PlainText", "SSML"]
SentimentType = Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]
