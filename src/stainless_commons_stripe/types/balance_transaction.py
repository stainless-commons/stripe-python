# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["BalanceTransaction", "FeeDetail", "Source", "SourceReserveTransaction", "SourceTaxDeductedAtSource"]


class FeeDetail(BaseModel):
    amount: int
    """Amount of the fee, in cents."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    type: str
    """
    Type of the fee, one of: `application_fee`, `payment_method_passthrough_fee`,
    `stripe_fee` or `tax`.
    """

    application: Optional[str] = None
    """ID of the Connect application that earned the fee."""

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """


class SourceReserveTransaction(BaseModel):
    id: str
    """Unique identifier for the object."""

    amount: int

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    object: Literal["reserve_transaction"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """


class SourceTaxDeductedAtSource(BaseModel):
    id: str
    """Unique identifier for the object."""

    object: Literal["tax_deducted_at_source"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    period_end: int
    """The end of the invoicing period.

    This TDS applies to Stripe fees collected during this invoicing period.
    """

    period_start: int
    """The start of the invoicing period.

    This TDS applies to Stripe fees collected during this invoicing period.
    """

    tax_deduction_account_number: str
    """The TAN that was supplied to Stripe when TDS was assessed"""


if TYPE_CHECKING or not PYDANTIC_V1:
    Source = TypeAliasType(
        "Source",
        Union[
            str,
            "ApplicationFee",
            "Charge",
            "ConnectCollectionTransfer",
            "CustomerCashBalanceTransaction",
            "Dispute",
            "FeeRefund",
            "IssuingAuthorization",
            "IssuingDispute",
            "IssuingTransaction",
            "Payout",
            "Refund",
            SourceReserveTransaction,
            SourceTaxDeductedAtSource,
            "Topup",
            "Transfer",
            "TransferReversal",
            None,
        ],
    )
else:
    Source: TypeAlias = Union[
        str,
        "ApplicationFee",
        "Charge",
        "ConnectCollectionTransfer",
        "CustomerCashBalanceTransaction",
        "Dispute",
        "FeeRefund",
        "IssuingAuthorization",
        "IssuingDispute",
        "IssuingTransaction",
        "Payout",
        "Refund",
        SourceReserveTransaction,
        SourceTaxDeductedAtSource,
        "Topup",
        "Transfer",
        "TransferReversal",
        None,
    ]


class BalanceTransaction(BaseModel):
    """
    Balance transactions represent funds moving through your Stripe account.
    Stripe creates them for every type of transaction that enters or leaves your Stripe account balance.

    Related guide: [Balance transaction types](https://docs.stripe.com/reports/balance-transaction-types)
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """Gross amount of this transaction (in cents (or local equivalent)).

    A positive value represents funds charged to another party, and a negative value
    represents funds sent to another party.
    """

    available_on: int
    """
    The date that the transaction's net funds become available in the Stripe
    balance.
    """

    balance_type: Literal["issuing", "payments", "refund_and_dispute_prefunding", "risk_reserved"]
    """The balance that this transaction impacts."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    fee: int
    """Fees (in cents (or local equivalent)) paid for this transaction.

    Represented as a positive integer when assessed.
    """

    fee_details: List[FeeDetail]
    """
    Detailed breakdown of fees (in cents (or local equivalent)) paid for this
    transaction.
    """

    net: int
    """Net impact to a Stripe balance (in cents (or local equivalent)).

    A positive value represents incrementing a Stripe balance, and a negative value
    decrementing a Stripe balance. You can calculate the net impact of a transaction
    on a balance by `amount` - `fee`
    """

    object: Literal["balance_transaction"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    reporting_category: str
    """
    Learn more about how
    [reporting categories](https://stripe.com/docs/reports/reporting-categories) can
    help you understand balance transactions from an accounting perspective.
    """

    status: str
    """
    The transaction's net funds status in the Stripe balance, which are either
    `available` or `pending`.
    """

    type: Literal[
        "adjustment",
        "advance",
        "advance_funding",
        "anticipation_repayment",
        "application_fee",
        "application_fee_refund",
        "charge",
        "climate_order_purchase",
        "climate_order_refund",
        "connect_collection_transfer",
        "contribution",
        "issuing_authorization_hold",
        "issuing_authorization_release",
        "issuing_dispute",
        "issuing_transaction",
        "obligation_outbound",
        "obligation_reversal_inbound",
        "payment",
        "payment_failure_refund",
        "payment_network_reserve_hold",
        "payment_network_reserve_release",
        "payment_refund",
        "payment_reversal",
        "payment_unreconciled",
        "payout",
        "payout_cancel",
        "payout_failure",
        "payout_minimum_balance_hold",
        "payout_minimum_balance_release",
        "refund",
        "refund_failure",
        "reserve_hold",
        "reserve_release",
        "reserve_transaction",
        "reserved_funds",
        "stripe_balance_payment_debit",
        "stripe_balance_payment_debit_reversal",
        "stripe_fee",
        "stripe_fx_fee",
        "tax_fee",
        "topup",
        "topup_reversal",
        "transfer",
        "transfer_cancel",
        "transfer_failure",
        "transfer_refund",
    ]
    """
    Transaction type: `adjustment`, `advance`, `advance_funding`,
    `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`,
    `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`,
    `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`,
    `issuing_dispute`, `issuing_transaction`, `obligation_outbound`,
    `obligation_reversal_inbound`, `payment`, `payment_failure_refund`,
    `payment_network_reserve_hold`, `payment_network_reserve_release`,
    `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`,
    `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`,
    `payout_minimum_balance_release`, `refund`, `refund_failure`,
    `reserve_transaction`, `reserved_funds`, `reserve_hold`, `reserve_release`,
    `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`,
    `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`,
    `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. Learn
    more about
    [balance transaction types and what they represent](https://stripe.com/docs/reports/balance-transaction-types).
    To classify transactions for accounting purposes, consider `reporting_category`
    instead.
    """

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    exchange_rate: Optional[float] = None
    """If applicable, this transaction uses an exchange rate.

    If money converts from currency A to currency B, then the `amount` in currency
    A, multipled by the `exchange_rate`, equals the `amount` in currency B. For
    example, if you charge a customer 10.00 EUR, the PaymentIntent's `amount` is
    `1000` and `currency` is `eur`. If this converts to 12.34 USD in your Stripe
    account, the BalanceTransaction's `amount` is `1234`, its `currency` is `usd`,
    and the `exchange_rate` is `1.234`.
    """

    source: Optional[Source] = None
    """This transaction relates to the Stripe object."""


from .topup import Topup
from .charge import Charge
from .payout import Payout
from .refund import Refund
from .dispute import Dispute
from .transfer import Transfer
from .fee_refund import FeeRefund
from .application_fee import ApplicationFee
from .issuing_dispute import IssuingDispute
from .transfer_reversal import TransferReversal
from .issuing_transaction import IssuingTransaction
from .issuing_authorization import IssuingAuthorization
from .connect_collection_transfer import ConnectCollectionTransfer
from .customer_cash_balance_transaction import CustomerCashBalanceTransaction
