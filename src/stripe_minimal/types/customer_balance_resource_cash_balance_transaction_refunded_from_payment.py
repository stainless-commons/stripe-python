# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["CustomerBalanceResourceCashBalanceTransactionRefundedFromPayment", "Refund"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Refund = TypeAliasType("Refund", Union[str, "refund.Refund"])
else:
    Refund: TypeAlias = Union[str, "refund.Refund"]


class CustomerBalanceResourceCashBalanceTransactionRefundedFromPayment(BaseModel):
    refund: Refund
    """
    The [Refund](https://docs.stripe.com/api/refunds/object) that moved these funds
    into the customer's cash balance.
    """


from . import refund
