# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IssuingCardholderUserTermsAcceptance"]


class IssuingCardholderUserTermsAcceptance(BaseModel):
    date: Optional[int] = None
    """
    The Unix timestamp marking when the cardholder accepted the Authorized User
    Terms.
    """

    ip: Optional[str] = None
    """The IP address from which the cardholder accepted the Authorized User Terms."""

    user_agent: Optional[str] = None
    """
    The user agent of the browser from which the cardholder accepted the Authorized
    User Terms.
    """
