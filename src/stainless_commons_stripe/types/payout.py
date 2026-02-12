# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "Payout",
    "ApplicationFee",
    "BalanceTransaction",
    "Destination",
    "DestinationDeletedBankAccount",
    "DestinationDeletedCard",
    "FailureBalanceTransaction",
    "OriginalPayout",
    "ReversedBy",
    "TraceID",
]

if TYPE_CHECKING or not PYDANTIC_V1:
    ApplicationFee = TypeAliasType("ApplicationFee", Union[str, "application_fee.ApplicationFee", None])
else:
    ApplicationFee: TypeAlias = Union[str, "application_fee.ApplicationFee", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    BalanceTransaction = TypeAliasType("BalanceTransaction", Union[str, "balance_transaction.BalanceTransaction", None])
else:
    BalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction", None]


class DestinationDeletedBankAccount(BaseModel):
    id: str
    """Unique identifier for the object."""

    deleted: Literal[True]
    """Always true for a deleted object"""

    object: Literal["bank_account"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    currency: Optional[str] = None
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid
    out to the bank account.
    """


class DestinationDeletedCard(BaseModel):
    id: str
    """Unique identifier for the object."""

    deleted: Literal[True]
    """Always true for a deleted object"""

    object: Literal["card"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    currency: Optional[str] = None
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid
    out to the bank account.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    Destination = TypeAliasType(
        "Destination", Union[str, "BankAccount", "Card", DestinationDeletedBankAccount, DestinationDeletedCard, None]
    )
else:
    Destination: TypeAlias = Union[
        str, "BankAccount", "Card", DestinationDeletedBankAccount, DestinationDeletedCard, None
    ]

if TYPE_CHECKING or not PYDANTIC_V1:
    FailureBalanceTransaction = TypeAliasType(
        "FailureBalanceTransaction", Union[str, "balance_transaction.BalanceTransaction", None]
    )
else:
    FailureBalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    OriginalPayout = TypeAliasType("OriginalPayout", Union[str, "Payout", None])
else:
    OriginalPayout: TypeAlias = Union[str, "Payout", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    ReversedBy = TypeAliasType("ReversedBy", Union[str, "Payout", None])
else:
    ReversedBy: TypeAlias = Union[str, "Payout", None]


class TraceID(BaseModel):
    status: str
    """Possible values are `pending`, `supported`, and `unsupported`.

    When `payout.status` is `pending` or `in_transit`, this will be `pending`. When
    the payout transitions to `paid`, `failed`, or `canceled`, this status will
    become `supported` or `unsupported` shortly after in most cases. In some cases,
    this may appear as `pending` for up to 10 days after `arrival_date` until
    transitioning to `supported` or `unsupported`.
    """

    value: Optional[str] = None
    """The trace ID value if `trace_id.status` is `supported`, otherwise `nil`."""


class Payout(BaseModel):
    """
    A `Payout` object is created when you receive funds from Stripe, or when you
    initiate a payout to either a bank account or debit card of a [connected
    Stripe account](/docs/connect/bank-debit-card-payouts). You can retrieve individual payouts,
    and list all payouts. Payouts are made on [varying
    schedules](/docs/connect/manage-payout-schedule), depending on your country and
    industry.

    Related guide: [Receiving payouts](https://docs.stripe.com/payouts)
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """
    The amount (in cents (or local equivalent)) that transfers to your bank account
    or debit card.
    """

    arrival_date: int
    """Date that you can expect the payout to arrive in the bank.

    This factors in delays to account for weekends or bank holidays.
    """

    automatic: bool
    """
    Returns `true` if the payout is created by an
    [automated payout schedule](https://docs.stripe.com/payouts#payout-schedule) and
    `false` if it's
    [requested manually](https://stripe.com/docs/payouts#manual-payouts).
    """

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

    method: str
    """The method used to send this payout, which can be `standard` or `instant`.

    `instant` is supported for payouts to debit cards and bank accounts in certain
    countries. Learn more about
    [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks).
    """

    object: Literal["payout"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    reconciliation_status: Literal["completed", "in_progress", "not_applicable"]
    """
    If `completed`, you can use the
    [Balance Transactions API](https://docs.stripe.com/api/balance_transactions/list#balance_transaction_list-payout)
    to list all balance transactions that are paid out in this payout.
    """

    source_type: str
    """
    The source balance this payout came from, which can be one of the following:
    `card`, `fpx`, or `bank_account`.
    """

    status: str
    """
    Current status of the payout: `paid`, `pending`, `in_transit`, `canceled` or
    `failed`. A payout is `pending` until it's submitted to the bank, when it
    becomes `in_transit`. The status changes to `paid` if the transaction succeeds,
    or to `failed` or `canceled` (within 5 business days). Some payouts that fail
    might initially show as `paid`, then change to `failed`.
    """

    type: Literal["bank_account", "card"]
    """Can be `bank_account` or `card`."""

    application_fee: Optional[ApplicationFee] = None
    """The application fee (if any) for the payout.

    [See the Connect documentation](https://docs.stripe.com/connect/instant-payouts#monetization-and-fees)
    for details.
    """

    application_fee_amount: Optional[int] = None
    """The amount of the application fee (if any) requested for the payout.

    [See the Connect documentation](https://docs.stripe.com/connect/instant-payouts#monetization-and-fees)
    for details.
    """

    balance_transaction: Optional[BalanceTransaction] = None
    """
    ID of the balance transaction that describes the impact of this payout on your
    account balance.
    """

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    destination: Optional[Destination] = None
    """ID of the bank account or card the payout is sent to."""

    failure_balance_transaction: Optional[FailureBalanceTransaction] = None
    """
    If the payout fails or cancels, this is the ID of the balance transaction that
    reverses the initial balance transaction and returns the funds from the failed
    payout back in your balance.
    """

    failure_code: Optional[str] = None
    """Error code that provides a reason for a payout failure, if available.

    View our [list of failure codes](https://docs.stripe.com/api#payout_failures).
    """

    failure_message: Optional[str] = None
    """Message that provides the reason for a payout failure, if available."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    original_payout: Optional[OriginalPayout] = None
    """If the payout reverses another, this is the ID of the original payout."""

    payout_method: Optional[str] = None
    """ID of the v2 FinancialAccount the funds are sent to."""

    reversed_by: Optional[ReversedBy] = None
    """If the payout reverses, this is the ID of the payout that reverses this payout."""

    statement_descriptor: Optional[str] = None
    """Extra information about a payout that displays on the user's bank statement."""

    trace_id: Optional[TraceID] = None


from . import application_fee, balance_transaction
from .card import Card
from .bank_account import BankAccount
