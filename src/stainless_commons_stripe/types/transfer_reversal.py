# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["TransferReversal", "Transfer", "BalanceTransaction", "DestinationPaymentRefund", "SourceRefund"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Transfer = TypeAliasType("Transfer", Union[str, "transfer.Transfer"])
else:
    Transfer: TypeAlias = Union[str, "transfer.Transfer"]

if TYPE_CHECKING or not PYDANTIC_V1:
    BalanceTransaction = TypeAliasType("BalanceTransaction", Union[str, "balance_transaction.BalanceTransaction", None])
else:
    BalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    DestinationPaymentRefund = TypeAliasType("DestinationPaymentRefund", Union[str, "Refund", None])
else:
    DestinationPaymentRefund: TypeAlias = Union[str, "Refund", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    SourceRefund = TypeAliasType("SourceRefund", Union[str, "Refund", None])
else:
    SourceRefund: TypeAlias = Union[str, "Refund", None]


class TransferReversal(BaseModel):
    """
    [Stripe Connect](https://docs.stripe.com/connect) platforms can reverse transfers made to a
    connected account, either entirely or partially, and can also specify whether
    to refund any related application fees. Transfer reversals add to the
    platform's balance and subtract from the destination account's balance.

    Reversing a transfer that was made for a [destination
    charge](/docs/connect/destination-charges) is allowed only up to the amount of
    the charge. It is possible to reverse a
    [transfer_group](https://docs.stripe.com/connect/separate-charges-and-transfers#transfer-options)
    transfer only if the destination account has enough balance to cover the
    reversal.

    Related guide: [Reverse transfers](https://docs.stripe.com/connect/separate-charges-and-transfers#reverse-transfers)
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

    object: Literal["transfer_reversal"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    transfer: Transfer
    """ID of the transfer that was reversed."""

    balance_transaction: Optional[BalanceTransaction] = None
    """Balance transaction that describes the impact on your account balance."""

    destination_payment_refund: Optional[DestinationPaymentRefund] = None
    """Linked payment refund for the transfer reversal."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    source_refund: Optional[SourceRefund] = None
    """ID of the refund responsible for the transfer reversal."""


from . import transfer, balance_transaction
from .refund import Refund
