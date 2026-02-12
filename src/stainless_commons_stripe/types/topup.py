# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.source import Source

__all__ = ["Topup", "BalanceTransaction"]

if TYPE_CHECKING or not PYDANTIC_V1:
    BalanceTransaction = TypeAliasType("BalanceTransaction", Union[str, "balance_transaction.BalanceTransaction", None])
else:
    BalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction", None]


class Topup(BaseModel):
    """To top up your Stripe balance, you create a top-up object.

    You can retrieve
    individual top-ups, as well as list all top-ups. Top-ups are identified by a
    unique, random ID.

    Related guide: [Topping up your platform account](https://docs.stripe.com/connect/top-ups)
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """Amount transferred."""

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

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    object: Literal["topup"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    status: Literal["canceled", "failed", "pending", "reversed", "succeeded"]
    """
    The status of the top-up is either `canceled`, `failed`, `pending`, `reversed`,
    or `succeeded`.
    """

    balance_transaction: Optional[BalanceTransaction] = None
    """
    ID of the balance transaction that describes the impact of this top-up on your
    account balance. May not be specified depending on status of top-up.
    """

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    expected_availability_date: Optional[int] = None
    """Date the funds are expected to arrive in your Stripe account for payouts.

    This factors in delays like weekends or bank holidays. May not be specified
    depending on status of top-up.
    """

    failure_code: Optional[str] = None
    """
    Error code explaining reason for top-up failure if available (see
    [the errors section](https://docs.stripe.com/api#errors) for a list of codes).
    """

    failure_message: Optional[str] = None
    """Message to user further explaining reason for top-up failure if available."""

    source: Optional[Source] = None
    """`Source` objects allow you to accept a variety of payment methods.

    They represent a customer's payment instrument, and can be used with the Stripe
    API just like a `Card` object: once chargeable, they can be charged, or can be
    attached to customers.

    Stripe doesn't recommend using the deprecated
    [Sources API](https://docs.stripe.com/api/sources). We recommend that you adopt
    the [PaymentMethods API](https://docs.stripe.com/api/payment_methods). This
    newer API provides access to our latest features and payment method types.

    Related guides: [Sources API](https://docs.stripe.com/sources) and
    [Sources & Customers](https://docs.stripe.com/sources/customers).
    """

    statement_descriptor: Optional[str] = None
    """Extra information about a top-up.

    This will appear on your source's bank statement. It must contain at least one
    letter.
    """

    transfer_group: Optional[str] = None
    """A string that identifies this top-up as part of a group."""


from . import balance_transaction
