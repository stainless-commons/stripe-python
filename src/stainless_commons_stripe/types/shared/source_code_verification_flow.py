# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SourceCodeVerificationFlow"]


class SourceCodeVerificationFlow(BaseModel):
    attempts_remaining: int
    """
    The number of attempts remaining to authenticate the source object with a
    verification code.
    """

    status: str
    """
    The status of the code verification, either `pending` (awaiting verification,
    `attempts_remaining` should be greater than 0), `succeeded` (successful
    verification) or `failed` (failed verification, cannot be verified anymore as
    `attempts_remaining` should be 0).
    """
