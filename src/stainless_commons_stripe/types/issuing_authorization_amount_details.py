# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IssuingAuthorizationAmountDetails"]


class IssuingAuthorizationAmountDetails(BaseModel):
    atm_fee: Optional[int] = None
    """The fee charged by the ATM for the cash withdrawal."""

    cashback_amount: Optional[int] = None
    """The amount of cash requested by the cardholder."""
