# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.payment_flows_payment_intent_presentment_details import PaymentFlowsPaymentIntentPresentmentDetails

__all__ = [
    "Refund",
    "BalanceTransaction",
    "Charge",
    "DestinationDetails",
    "DestinationDetailsBlik",
    "DestinationDetailsBrBankTransfer",
    "DestinationDetailsCard",
    "DestinationDetailsCrypto",
    "DestinationDetailsEuBankTransfer",
    "DestinationDetailsGBBankTransfer",
    "DestinationDetailsJpBankTransfer",
    "DestinationDetailsMBWay",
    "DestinationDetailsMultibanco",
    "DestinationDetailsMxBankTransfer",
    "DestinationDetailsP24",
    "DestinationDetailsPaypal",
    "DestinationDetailsSwish",
    "DestinationDetailsThBankTransfer",
    "DestinationDetailsUsBankTransfer",
    "FailureBalanceTransaction",
    "NextAction",
    "NextActionDisplayDetails",
    "NextActionDisplayDetailsEmailSent",
    "PaymentIntent",
    "SourceTransferReversal",
    "TransferReversal",
]

if TYPE_CHECKING or not PYDANTIC_V1:
    BalanceTransaction = TypeAliasType("BalanceTransaction", Union[str, "balance_transaction.BalanceTransaction", None])
else:
    BalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Charge = TypeAliasType("Charge", Union[str, "charge.Charge", None])
else:
    Charge: TypeAlias = Union[str, "charge.Charge", None]


class DestinationDetailsBlik(BaseModel):
    network_decline_code: Optional[str] = None
    """
    For refunds declined by the network, a decline code provided by the network
    which indicates the reason the refund failed.
    """

    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsBrBankTransfer(BaseModel):
    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsCard(BaseModel):
    type: Literal["pending", "refund", "reversal"]
    """The type of refund. This can be `refund`, `reversal`, or `pending`."""

    reference: Optional[str] = None
    """Value of the reference number assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference number on the refund.

    This can be `pending`, `available` or `unavailable`.
    """

    reference_type: Optional[str] = None
    """Type of the reference number assigned to the refund."""


class DestinationDetailsCrypto(BaseModel):
    reference: Optional[str] = None
    """The transaction hash of the refund."""


class DestinationDetailsEuBankTransfer(BaseModel):
    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsGBBankTransfer(BaseModel):
    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsJpBankTransfer(BaseModel):
    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsMBWay(BaseModel):
    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsMultibanco(BaseModel):
    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsMxBankTransfer(BaseModel):
    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsP24(BaseModel):
    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsPaypal(BaseModel):
    network_decline_code: Optional[str] = None
    """
    For refunds declined by the network, a decline code provided by the network
    which indicates the reason the refund failed.
    """


class DestinationDetailsSwish(BaseModel):
    network_decline_code: Optional[str] = None
    """
    For refunds declined by the network, a decline code provided by the network
    which indicates the reason the refund failed.
    """

    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsThBankTransfer(BaseModel):
    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetailsUsBankTransfer(BaseModel):
    reference: Optional[str] = None
    """The reference assigned to the refund."""

    reference_status: Optional[str] = None
    """Status of the reference on the refund.

    This can be `pending`, `available` or `unavailable`.
    """


class DestinationDetails(BaseModel):
    type: str
    """
    The type of transaction-specific details of the payment method used in the
    refund (e.g., `card`). An additional hash is included on `destination_details`
    with a name matching this value. It contains information specific to the refund
    transaction.
    """

    affirm: Optional[object] = None

    afterpay_clearpay: Optional[object] = None

    alipay: Optional[object] = None

    alma: Optional[object] = None

    amazon_pay: Optional[object] = None

    au_bank_transfer: Optional[object] = None

    blik: Optional[DestinationDetailsBlik] = None

    br_bank_transfer: Optional[DestinationDetailsBrBankTransfer] = None

    card: Optional[DestinationDetailsCard] = None

    cashapp: Optional[object] = None

    crypto: Optional[DestinationDetailsCrypto] = None

    customer_cash_balance: Optional[object] = None

    eps: Optional[object] = None

    eu_bank_transfer: Optional[DestinationDetailsEuBankTransfer] = None

    gb_bank_transfer: Optional[DestinationDetailsGBBankTransfer] = None

    giropay: Optional[object] = None

    grabpay: Optional[object] = None

    jp_bank_transfer: Optional[DestinationDetailsJpBankTransfer] = None

    klarna: Optional[object] = None

    mb_way: Optional[DestinationDetailsMBWay] = None

    multibanco: Optional[DestinationDetailsMultibanco] = None

    mx_bank_transfer: Optional[DestinationDetailsMxBankTransfer] = None

    nz_bank_transfer: Optional[object] = None

    p24: Optional[DestinationDetailsP24] = None

    paynow: Optional[object] = None

    paypal: Optional[DestinationDetailsPaypal] = None

    pix: Optional[object] = None

    revolut: Optional[object] = None

    sofort: Optional[object] = None

    swish: Optional[DestinationDetailsSwish] = None

    th_bank_transfer: Optional[DestinationDetailsThBankTransfer] = None

    twint: Optional[object] = None

    us_bank_transfer: Optional[DestinationDetailsUsBankTransfer] = None

    wechat_pay: Optional[object] = None

    zip: Optional[object] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    FailureBalanceTransaction = TypeAliasType(
        "FailureBalanceTransaction", Union[str, "balance_transaction.BalanceTransaction"]
    )
else:
    FailureBalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction"]


class NextActionDisplayDetailsEmailSent(BaseModel):
    email_sent_at: int
    """The timestamp when the email was sent."""

    email_sent_to: str
    """The recipient's email address."""


class NextActionDisplayDetails(BaseModel):
    email_sent: NextActionDisplayDetailsEmailSent

    expires_at: int
    """The expiry timestamp."""


class NextAction(BaseModel):
    type: str
    """Type of the next action to perform."""

    display_details: Optional[NextActionDisplayDetails] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    PaymentIntent = TypeAliasType("PaymentIntent", Union[str, "payment_intent.PaymentIntent", None])
else:
    PaymentIntent: TypeAlias = Union[str, "payment_intent.PaymentIntent", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    SourceTransferReversal = TypeAliasType(
        "SourceTransferReversal", Union[str, "transfer_reversal.TransferReversal", None]
    )
else:
    SourceTransferReversal: TypeAlias = Union[str, "transfer_reversal.TransferReversal", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    TransferReversal = TypeAliasType("TransferReversal", Union[str, "transfer_reversal.TransferReversal", None])
else:
    TransferReversal: TypeAlias = Union[str, "transfer_reversal.TransferReversal", None]


class Refund(BaseModel):
    """
    Refund objects allow you to refund a previously created charge that isn't
    refunded yet. Funds are refunded to the credit or debit card that's
    initially charged.

    Related guide: [Refunds](https://docs.stripe.com/refunds)
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

    object: Literal["refund"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    balance_transaction: Optional[BalanceTransaction] = None
    """Balance transaction that describes the impact on your account balance."""

    charge: Optional[Charge] = None
    """ID of the charge that's refunded."""

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    You can use this for displaying to users (available on non-card refunds only).
    """

    destination_details: Optional[DestinationDetails] = None

    failure_balance_transaction: Optional[FailureBalanceTransaction] = None
    """
    After the refund fails, this balance transaction describes the adjustment made
    on your account balance that reverses the initial balance transaction.
    """

    failure_reason: Optional[str] = None
    """Provides the reason for the refund failure.

    Possible values are: `lost_or_stolen_card`, `expired_or_canceled_card`,
    `charge_for_pending_refund_disputed`, `insufficient_funds`, `declined`,
    `merchant_request`, or `unknown`.
    """

    instructions_email: Optional[str] = None
    """
    For payment methods without native refund support (for example, Konbini,
    PromptPay), provide an email address for the customer to receive refund
    instructions.
    """

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    next_action: Optional[NextAction] = None

    payment_intent: Optional[PaymentIntent] = None
    """ID of the PaymentIntent that's refunded."""

    pending_reason: Optional[Literal["charge_pending", "insufficient_funds", "processing"]] = None
    """Provides the reason for why the refund is pending.

    Possible values are: `processing`, `insufficient_funds`, or `charge_pending`.
    """

    presentment_details: Optional[PaymentFlowsPaymentIntentPresentmentDetails] = None

    reason: Optional[Literal["duplicate", "expired_uncaptured_charge", "fraudulent", "requested_by_customer"]] = None
    """
    Reason for the refund, which is either user-provided (`duplicate`, `fraudulent`,
    or `requested_by_customer`) or generated by Stripe internally
    (`expired_uncaptured_charge`).
    """

    receipt_number: Optional[str] = None
    """
    This is the transaction number that appears on email receipts sent for this
    refund.
    """

    source_transfer_reversal: Optional[SourceTransferReversal] = None
    """The transfer reversal that's associated with the refund.

    Only present if the charge came from another Stripe account.
    """

    status: Optional[str] = None
    """Status of the refund.

    This can be `pending`, `requires_action`, `succeeded`, `failed`, or `canceled`.
    Learn more about
    [failed refunds](https://docs.stripe.com/refunds#failed-refunds).
    """

    transfer_reversal: Optional[TransferReversal] = None
    """
    This refers to the transfer reversal object if the accompanying transfer
    reverses. This is only applicable if the charge was created using the
    destination parameter.
    """


from . import charge, payment_intent, transfer_reversal, balance_transaction
