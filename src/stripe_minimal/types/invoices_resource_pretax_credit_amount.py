# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["InvoicesResourcePretaxCreditAmount", "CreditBalanceTransaction", "Discount"]

if TYPE_CHECKING or not PYDANTIC_V1:
    CreditBalanceTransaction = TypeAliasType(
        "CreditBalanceTransaction", Union[str, "BillingCreditBalanceTransaction", None]
    )
else:
    CreditBalanceTransaction: TypeAlias = Union[str, "BillingCreditBalanceTransaction", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Discount = TypeAliasType("Discount", Union[str, "discount.Discount", "DeletedDiscount"])
else:
    Discount: TypeAlias = Union[str, "discount.Discount", "DeletedDiscount"]


class InvoicesResourcePretaxCreditAmount(BaseModel):
    amount: int
    """The amount, in cents (or local equivalent), of the pretax credit amount."""

    type: Literal["credit_balance_transaction", "discount"]
    """Type of the pretax credit amount referenced."""

    credit_balance_transaction: Optional[CreditBalanceTransaction] = None
    """
    The credit balance transaction that was applied to get this pretax credit
    amount.
    """

    discount: Optional[Discount] = None
    """The discount that was applied to get this pretax credit amount."""


from . import discount
from .deleted_discount import DeletedDiscount
from .billing_credit_balance_transaction import BillingCreditBalanceTransaction
