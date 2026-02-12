# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["FeeRefund", "Fee", "BalanceTransaction"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Fee = TypeAliasType("Fee", Union[str, "ApplicationFee"])
else:
    Fee: TypeAlias = Union[str, "ApplicationFee"]

if TYPE_CHECKING or not PYDANTIC_V1:
    BalanceTransaction = TypeAliasType("BalanceTransaction", Union[str, "balance_transaction.BalanceTransaction", None])
else:
    BalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction", None]


class FeeRefund(BaseModel):
    """
    `Application Fee Refund` objects allow you to refund an application fee that
    has previously been created but not yet refunded. Funds will be refunded to
    the Stripe account from which the fee was originally collected.

    Related guide: [Refunding application fees](https://docs.stripe.com/connect/destination-charges#refunding-app-fee)
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """Amount, in cents (or local equivalent)."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    fee: Fee
    """ID of the application fee that was refunded."""

    object: Literal["fee_refund"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    balance_transaction: Optional[BalanceTransaction] = None
    """Balance transaction that describes the impact on your account balance."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """


from . import balance_transaction
from .application_fee import ApplicationFee
