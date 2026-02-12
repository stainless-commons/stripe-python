# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import application
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "ApplicationFee",
    "Account",
    "Application",
    "Charge",
    "Refunds",
    "BalanceTransaction",
    "FeeSource",
    "OriginatingTransaction",
]

if TYPE_CHECKING or not PYDANTIC_V1:
    Account = TypeAliasType("Account", Union[str, "account.Account"])
else:
    Account: TypeAlias = Union[str, "account.Account"]

Application: TypeAlias = Union[str, application.Application]

if TYPE_CHECKING or not PYDANTIC_V1:
    Charge = TypeAliasType("Charge", Union[str, "_charge.Charge"])
else:
    Charge: TypeAlias = Union[str, "_charge.Charge"]


class Refunds(BaseModel):
    """A list of refunds that have been applied to the fee."""

    data: List["FeeRefund"]
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


class FeeSource(BaseModel):
    type: Literal["charge", "payout"]
    """Type of object that created the application fee."""

    charge: Optional[str] = None
    """Charge ID that created this application fee."""

    payout: Optional[str] = None
    """Payout ID that created this application fee."""


if TYPE_CHECKING or not PYDANTIC_V1:
    OriginatingTransaction = TypeAliasType("OriginatingTransaction", Union[str, "_charge.Charge", None])
else:
    OriginatingTransaction: TypeAlias = Union[str, "_charge.Charge", None]


class ApplicationFee(BaseModel):
    id: str
    """Unique identifier for the object."""

    account: Account
    """ID of the Stripe account this fee was taken from."""

    amount: int
    """Amount earned, in cents (or local equivalent)."""

    amount_refunded: int
    """
    Amount in cents (or local equivalent) refunded (can be less than the amount
    attribute on the fee if a partial refund was issued)
    """

    application: Application
    """ID of the Connect application that earned the fee."""

    charge: Charge
    """ID of the charge that the application fee was taken from."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

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

    object: Literal["application_fee"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    refunded: bool
    """Whether the fee has been fully refunded.

    If the fee is only partially refunded, this attribute will still be false.
    """

    refunds: Refunds
    """A list of refunds that have been applied to the fee."""

    balance_transaction: Optional[BalanceTransaction] = None
    """
    Balance transaction that describes the impact of this collected application fee
    on your account balance (not including refunds).
    """

    fee_source: Optional[FeeSource] = None

    originating_transaction: Optional[OriginatingTransaction] = None
    """
    ID of the corresponding charge on the platform account, if this fee was the
    result of a charge using the `destination` parameter.
    """


from . import charge as _charge, account, balance_transaction
from .fee_refund import FeeRefund
