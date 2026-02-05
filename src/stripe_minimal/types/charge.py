# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import application
from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.address import Address
from .shared.shipping import Shipping
from .shared.deleted_customer import DeletedCustomer
from .shared.payment_flows_payment_intent_presentment_details import PaymentFlowsPaymentIntentPresentmentDetails

__all__ = [
    "Charge",
    "BillingDetails",
    "Application",
    "ApplicationFee",
    "BalanceTransaction",
    "Customer",
    "FailureBalanceTransaction",
    "FraudDetails",
    "OnBehalfOf",
    "Outcome",
    "OutcomeRule",
    "OutcomeRuleRule",
    "PaymentIntent",
    "RadarOptions",
    "Refunds",
    "Review",
    "SourceTransfer",
    "Transfer",
]


class BillingDetails(BaseModel):
    address: Optional[Address] = None

    email: Optional[str] = None
    """Email address."""

    name: Optional[str] = None
    """Full name."""

    phone: Optional[str] = None
    """Billing phone number (including extension)."""

    tax_id: Optional[str] = None
    """Taxpayer identification number.

    Used only for transactions between LATAM buyers and non-LATAM sellers.
    """


Application: TypeAlias = Union[str, application.Application, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    ApplicationFee = TypeAliasType("ApplicationFee", Union[str, "application_fee.ApplicationFee", None])
else:
    ApplicationFee: TypeAlias = Union[str, "application_fee.ApplicationFee", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    BalanceTransaction = TypeAliasType("BalanceTransaction", Union[str, "balance_transaction.BalanceTransaction", None])
else:
    BalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer, None])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    FailureBalanceTransaction = TypeAliasType(
        "FailureBalanceTransaction", Union[str, "balance_transaction.BalanceTransaction", None]
    )
else:
    FailureBalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction", None]


class FraudDetails(BaseModel):
    stripe_report: Optional[str] = None
    """Assessments from Stripe. If set, the value is `fraudulent`."""

    user_report: Optional[str] = None
    """Assessments reported by you.

    If set, possible values of are `safe` and `fraudulent`.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    OnBehalfOf = TypeAliasType("OnBehalfOf", Union[str, "Account", None])
else:
    OnBehalfOf: TypeAlias = Union[str, "Account", None]


class OutcomeRuleRule(BaseModel):
    id: str
    """Unique identifier for the object."""

    action: str
    """The action taken on the payment."""

    predicate: str
    """The predicate to evaluate the payment against."""


OutcomeRule: TypeAlias = Union[str, OutcomeRuleRule]


class Outcome(BaseModel):
    type: str
    """
    Possible values are `authorized`, `manual_review`, `issuer_declined`, `blocked`,
    and `invalid`. See [understanding declines](https://docs.stripe.com/declines)
    and [Radar reviews](https://docs.stripe.com/radar/reviews) for details.
    """

    advice_code: Optional[Literal["confirm_card_data", "do_not_try_again", "try_again_later"]] = None
    """
    An enumerated value providing a more detailed explanation on
    [how to proceed with an error](https://docs.stripe.com/declines#retrying-issuer-declines).
    """

    network_advice_code: Optional[str] = None
    """
    For charges declined by the network, a 2 digit code which indicates the advice
    returned by the network on how to proceed with an error.
    """

    network_decline_code: Optional[str] = None
    """
    For charges declined by the network, an alphanumeric code which indicates the
    reason the charge failed.
    """

    network_status: Optional[str] = None
    """
    Possible values are `approved_by_network`, `declined_by_network`,
    `not_sent_to_network`, and `reversed_after_approval`. The value
    `reversed_after_approval` indicates the payment was
    [blocked by Stripe](https://docs.stripe.com/declines#blocked-payments) after
    bank authorization, and may temporarily appear as "pending" on a cardholder's
    statement.
    """

    reason: Optional[str] = None
    """
    An enumerated value providing a more detailed explanation of the outcome's
    `type`. Charges blocked by Radar's default block rule have the value
    `highest_risk_level`. Charges placed in review by Radar's default review rule
    have the value `elevated_risk_level`. Charges blocked because the payment is
    unlikely to be authorized have the value `low_probability_of_authorization`.
    Charges authorized, blocked, or placed in review by custom rules have the value
    `rule`. See [understanding declines](https://docs.stripe.com/declines) for more
    details.
    """

    risk_level: Optional[str] = None
    """Stripe Radar's evaluation of the riskiness of the payment.

    Possible values for evaluated payments are `normal`, `elevated`, `highest`. For
    non-card payments, and card-based payments predating the public assignment of
    risk levels, this field will have the value `not_assessed`. In the event of an
    error in the evaluation, this field will have the value `unknown`. This field is
    only available with Radar.
    """

    risk_score: Optional[int] = None
    """Stripe Radar's evaluation of the riskiness of the payment.

    Possible values for evaluated payments are between 0 and 100. For non-card
    payments, card-based payments predating the public assignment of risk scores, or
    in the event of an error during evaluation, this field will not be present. This
    field is only available with Radar for Fraud Teams.
    """

    rule: Optional[OutcomeRule] = None
    """The ID of the Radar rule that matched the payment, if applicable."""

    seller_message: Optional[str] = None
    """
    A human-readable description of the outcome type and reason, designed for you
    (the recipient of the payment), not your customer.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    PaymentIntent = TypeAliasType("PaymentIntent", Union[str, "payment_intent.PaymentIntent", None])
else:
    PaymentIntent: TypeAlias = Union[str, "payment_intent.PaymentIntent", None]


class RadarOptions(BaseModel):
    """Options to configure Radar.

    See [Radar Session](https://docs.stripe.com/radar/radar-session) for more information.
    """

    session: Optional[str] = None
    """
    A [Radar Session](https://docs.stripe.com/radar/radar-session) is a snapshot of
    the browser metadata and device details that help Radar make more accurate
    predictions on your payments.
    """


class Refunds(BaseModel):
    """A list of refunds that have been applied to the charge."""

    data: List["Refund"]
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
    Review = TypeAliasType("Review", Union[str, "review.Review", None])
else:
    Review: TypeAlias = Union[str, "review.Review", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    SourceTransfer = TypeAliasType("SourceTransfer", Union[str, "transfer.Transfer", None])
else:
    SourceTransfer: TypeAlias = Union[str, "transfer.Transfer", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Transfer = TypeAliasType("Transfer", Union[str, "transfer.Transfer"])
else:
    Transfer: TypeAlias = Union[str, "transfer.Transfer"]


class Charge(BaseModel):
    """
    The `Charge` object represents a single attempt to move money into your Stripe account.
    PaymentIntent confirmation is the most common way to create Charges, but [Account Debits](https://docs.stripe.com/connect/account-debits) may also create Charges.
    Some legacy payment flows create Charges directly, which is not recommended for new integrations.
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """Amount intended to be collected by this payment.

    A positive integer representing how much to charge in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal) (e.g.,
    100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The
    minimum amount is $0.50 US or
    [equivalent in charge currency](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts).
    The amount value supports up to eight digits (e.g., a value of 99999999 for a
    USD charge of $999,999.99).
    """

    amount_captured: int
    """
    Amount in cents (or local equivalent) captured (can be less than the amount
    attribute on the charge if a partial capture was made).
    """

    amount_refunded: int
    """
    Amount in cents (or local equivalent) refunded (can be less than the amount
    attribute on the charge if a partial refund was issued).
    """

    billing_details: BillingDetails

    captured: bool
    """
    If the charge was created without capturing, this Boolean represents whether it
    is still uncaptured or has since been captured.
    """

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    disputed: bool
    """Whether the charge has been disputed."""

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

    object: Literal["charge"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    paid: bool
    """
    `true` if the charge succeeded, or was successfully authorized for later
    capture.
    """

    refunded: bool
    """Whether the charge has been fully refunded.

    If the charge is only partially refunded, this attribute will still be false.
    """

    status: Literal["failed", "pending", "succeeded"]
    """The status of the payment is either `succeeded`, `pending`, or `failed`."""

    application: Optional[Application] = None
    """ID of the Connect application that created the charge."""

    application_fee: Optional[ApplicationFee] = None
    """The application fee (if any) for the charge.

    [See the Connect documentation](https://docs.stripe.com/connect/direct-charges#collect-fees)
    for details.
    """

    application_fee_amount: Optional[int] = None
    """The amount of the application fee (if any) requested for the charge.

    [See the Connect documentation](https://docs.stripe.com/connect/direct-charges#collect-fees)
    for details.
    """

    balance_transaction: Optional[BalanceTransaction] = None
    """
    ID of the balance transaction that describes the impact of this charge on your
    account balance (not including refunds or disputes).
    """

    calculated_statement_descriptor: Optional[str] = None
    """
    The full statement descriptor that is passed to card networks, and that is
    displayed on your customers' credit card and bank statements. Allows you to see
    what the statement descriptor looks like after the static and dynamic portions
    are combined. This value only exists for card payments.
    """

    customer: Optional[Customer] = None
    """ID of the customer this charge is for if one exists."""

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    failure_balance_transaction: Optional[FailureBalanceTransaction] = None
    """
    ID of the balance transaction that describes the reversal of the balance on your
    account due to payment failure.
    """

    failure_code: Optional[str] = None
    """
    Error code explaining reason for charge failure if available (see
    [the errors section](https://docs.stripe.com/error-codes) for a list of codes).
    """

    failure_message: Optional[str] = None
    """Message to user further explaining reason for charge failure if available."""

    fraud_details: Optional[FraudDetails] = None

    on_behalf_of: Optional[OnBehalfOf] = None
    """
    The account (if any) the charge was made on behalf of without triggering an
    automatic transfer. See the
    [Connect documentation](https://docs.stripe.com/connect/separate-charges-and-transfers)
    for details.
    """

    outcome: Optional[Outcome] = None

    payment_intent: Optional[PaymentIntent] = None
    """ID of the PaymentIntent associated with this charge, if one exists."""

    payment_method: Optional[str] = None
    """ID of the payment method used in this charge."""

    payment_method_details: Optional["PaymentMethodDetails"] = None

    presentment_details: Optional[PaymentFlowsPaymentIntentPresentmentDetails] = None

    radar_options: Optional[RadarOptions] = None
    """Options to configure Radar.

    See [Radar Session](https://docs.stripe.com/radar/radar-session) for more
    information.
    """

    receipt_email: Optional[str] = None
    """This is the email address that the receipt for this charge was sent to."""

    receipt_number: Optional[str] = None
    """
    This is the transaction number that appears on email receipts sent for this
    charge. This attribute will be `null` until a receipt has been sent.
    """

    receipt_url: Optional[str] = None
    """This is the URL to view the receipt for this charge.

    The receipt is kept up-to-date to the latest state of the charge, including any
    refunds. If the charge is for an Invoice, the receipt will be stylized as an
    Invoice receipt.
    """

    refunds: Optional[Refunds] = None
    """A list of refunds that have been applied to the charge."""

    review: Optional[Review] = None
    """ID of the review associated with this charge if one exists."""

    shipping: Optional[Shipping] = None

    source_transfer: Optional[SourceTransfer] = None
    """The transfer ID which created this charge.

    Only present if the charge came from another Stripe account.
    [See the Connect documentation](https://docs.stripe.com/connect/destination-charges)
    for details.
    """

    statement_descriptor: Optional[str] = None
    """
    For a non-card charge, text that appears on the customer's statement as the
    statement descriptor. This value overrides the account's default statement
    descriptor. For information about requirements, including the 22-character
    limit, see
    [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

    For a card charge, this value is ignored unless you don't specify a
    `statement_descriptor_suffix`, in which case this value is used as the suffix.
    """

    statement_descriptor_suffix: Optional[str] = None
    """Provides information about a card charge.

    Concatenated to the account's
    [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static)
    to form the complete statement descriptor that appears on the customer's
    statement. If the account has no prefix value, the suffix is concatenated to the
    account's statement descriptor.
    """

    transfer: Optional[Transfer] = None
    """
    ID of the transfer to the `destination` account (only applicable if the charge
    was created using the `destination` parameter).
    """

    transfer_data: Optional["ChargeTransferData"] = None

    transfer_group: Optional[str] = None
    """A string that identifies this transaction as part of a group.

    See the
    [Connect documentation](https://docs.stripe.com/connect/separate-charges-and-transfers#transfer-options)
    for details.
    """


from . import review, customer, transfer, payment_intent, application_fee, balance_transaction
from .refund import Refund
from .account import Account
from .charge_transfer_data import ChargeTransferData
from .payment_method_details import PaymentMethodDetails
