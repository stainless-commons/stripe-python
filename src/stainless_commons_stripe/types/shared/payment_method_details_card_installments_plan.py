# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PaymentMethodDetailsCardInstallmentsPlan"]


class PaymentMethodDetailsCardInstallmentsPlan(BaseModel):
    type: Literal["bonus", "fixed_count", "revolving"]
    """Type of installment plan, one of `fixed_count`, `bonus`, or `revolving`."""

    count: Optional[int] = None
    """
    For `fixed_count` installment plans, this is the number of installment payments
    your customer will make to their credit card.
    """

    interval: Optional[Literal["month"]] = None
    """
    For `fixed_count` installment plans, this is the interval between installment
    payments your customer will make to their credit card. One of `month`.
    """
