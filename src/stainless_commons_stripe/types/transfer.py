# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["Transfer", "Reversals", "BalanceTransaction", "Destination", "DestinationPayment", "SourceTransaction"]


class Reversals(BaseModel):
    """A list of reversals that have been applied to the transfer."""

    data: List["TransferReversal"]
    """Details about each object."""

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


if TYPE_CHECKING or not PYDANTIC_V1:
    BalanceTransaction = TypeAliasType("BalanceTransaction", Union[str, "balance_transaction.BalanceTransaction", None])
else:
    BalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Destination = TypeAliasType("Destination", Union[str, "Account", None])
else:
    Destination: TypeAlias = Union[str, "Account", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    DestinationPayment = TypeAliasType("DestinationPayment", Union[str, "Charge"])
else:
    DestinationPayment: TypeAlias = Union[str, "Charge"]

if TYPE_CHECKING or not PYDANTIC_V1:
    SourceTransaction = TypeAliasType("SourceTransaction", Union[str, "Charge", None])
else:
    SourceTransaction: TypeAlias = Union[str, "Charge", None]


class Transfer(BaseModel):
    """
    A `Transfer` object is created when you move funds between Stripe accounts as
    part of Connect.

    Before April 6, 2017, transfers also represented movement of funds from a
    Stripe account to a card or bank account. This behavior has since been split
    out into a [Payout](https://api.stripe.com#payout_object) object, with corresponding payout endpoints. For more
    information, read about the
    [transfer/payout split](https://docs.stripe.com/transfer-payout-split).

    Related guide: [Creating separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """Amount in cents (or local equivalent) to be transferred."""

    amount_reversed: int
    """
    Amount in cents (or local equivalent) reversed (can be less than the amount
    attribute on the transfer if a partial reversal was issued).
    """

    created: int
    """Time that this record of the transfer was first created."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    object: Literal["transfer"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    reversals: Reversals
    """A list of reversals that have been applied to the transfer."""

    reversed: bool
    """Whether the transfer has been fully reversed.

    If the transfer is only partially reversed, this attribute will still be false.
    """

    balance_transaction: Optional[BalanceTransaction] = None
    """
    Balance transaction that describes the impact of this transfer on your account
    balance.
    """

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    destination: Optional[Destination] = None
    """ID of the Stripe account the transfer was sent to."""

    destination_payment: Optional[DestinationPayment] = None
    """
    If the destination is a Stripe account, this will be the ID of the payment that
    the destination account received for the transfer.
    """

    source_transaction: Optional[SourceTransaction] = None
    """ID of the charge that was used to fund the transfer.

    If null, the transfer was funded from the available balance.
    """

    source_type: Optional[str] = None
    """The source balance this transfer came from.

    One of `card`, `fpx`, or `bank_account`.
    """

    transfer_group: Optional[str] = None
    """A string that identifies this transaction as part of a group.

    See the
    [Connect documentation](https://docs.stripe.com/connect/separate-charges-and-transfers#transfer-options)
    for details.
    """


from . import balance_transaction
from .charge import Charge
from .account import Account
from .transfer_reversal import TransferReversal
