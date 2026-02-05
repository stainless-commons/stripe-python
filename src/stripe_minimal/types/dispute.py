# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "Dispute",
    "Charge",
    "Evidence",
    "EvidenceEnhancedEvidence",
    "EvidenceEnhancedEvidenceVisaCompellingEvidence3",
    "EvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransaction",
    "EvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransactionShippingAddress",
    "EvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransaction",
    "EvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransactionShippingAddress",
    "EvidenceEnhancedEvidenceVisaCompliance",
    "EvidenceCancellationPolicy",
    "EvidenceCustomerCommunication",
    "EvidenceCustomerSignature",
    "EvidenceDuplicateChargeDocumentation",
    "EvidenceReceipt",
    "EvidenceRefundPolicy",
    "EvidenceServiceDocumentation",
    "EvidenceShippingDocumentation",
    "EvidenceUncategorizedFile",
    "EvidenceDetails",
    "EvidenceDetailsEnhancedEligibility",
    "EvidenceDetailsEnhancedEligibilityVisaCompellingEvidence3",
    "EvidenceDetailsEnhancedEligibilityVisaCompliance",
    "PaymentIntent",
    "PaymentMethodDetails",
    "PaymentMethodDetailsAmazonPay",
    "PaymentMethodDetailsCard",
    "PaymentMethodDetailsKlarna",
    "PaymentMethodDetailsPaypal",
]

if TYPE_CHECKING or not PYDANTIC_V1:
    Charge = TypeAliasType("Charge", Union[str, "charge.Charge"])
else:
    Charge: TypeAlias = Union[str, "charge.Charge"]


class EvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransactionShippingAddress(BaseModel):
    city: Optional[str] = None
    """City, district, suburb, town, or village."""

    country: Optional[str] = None
    """
    Two-letter country code
    ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """

    line1: Optional[str] = None
    """Address line 1, such as the street, PO Box, or company name."""

    line2: Optional[str] = None
    """Address line 2, such as the apartment, suite, unit, or building."""

    postal_code: Optional[str] = None
    """ZIP or postal code."""

    state: Optional[str] = None
    """
    State, county, province, or region
    ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class EvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransaction(BaseModel):
    charge: str
    """Stripe charge ID for the Visa Compelling Evidence 3.0 eligible prior charge."""

    customer_account_id: Optional[str] = None
    """User Account ID used to log into business platform.

    Must be recognizable by the user.
    """

    customer_device_fingerprint: Optional[str] = None
    """
    Unique identifier of the cardholder’s device derived from a combination of at
    least two hardware and software attributes. Must be at least 20 characters.
    """

    customer_device_id: Optional[str] = None
    """
    Unique identifier of the cardholder’s device such as a device serial number
    (e.g., International Mobile Equipment Identity [IMEI]). Must be at least 15
    characters.
    """

    customer_email_address: Optional[str] = None
    """The email address of the customer."""

    customer_purchase_ip: Optional[str] = None
    """The IP address that the customer used when making the purchase."""

    product_description: Optional[str] = None
    """A description of the product or service that was sold."""

    shipping_address: Optional[
        EvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransactionShippingAddress
    ] = None


class EvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransactionShippingAddress(BaseModel):
    city: Optional[str] = None
    """City, district, suburb, town, or village."""

    country: Optional[str] = None
    """
    Two-letter country code
    ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """

    line1: Optional[str] = None
    """Address line 1, such as the street, PO Box, or company name."""

    line2: Optional[str] = None
    """Address line 2, such as the apartment, suite, unit, or building."""

    postal_code: Optional[str] = None
    """ZIP or postal code."""

    state: Optional[str] = None
    """
    State, county, province, or region
    ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class EvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransaction(BaseModel):
    customer_account_id: Optional[str] = None
    """User Account ID used to log into business platform.

    Must be recognizable by the user.
    """

    customer_device_fingerprint: Optional[str] = None
    """
    Unique identifier of the cardholder’s device derived from a combination of at
    least two hardware and software attributes. Must be at least 20 characters.
    """

    customer_device_id: Optional[str] = None
    """
    Unique identifier of the cardholder’s device such as a device serial number
    (e.g., International Mobile Equipment Identity [IMEI]). Must be at least 15
    characters.
    """

    customer_email_address: Optional[str] = None
    """The email address of the customer."""

    customer_purchase_ip: Optional[str] = None
    """The IP address that the customer used when making the purchase."""

    merchandise_or_services: Optional[Literal["merchandise", "services"]] = None
    """Categorization of disputed payment."""

    product_description: Optional[str] = None
    """A description of the product or service that was sold."""

    shipping_address: Optional[EvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransactionShippingAddress] = None


class EvidenceEnhancedEvidenceVisaCompellingEvidence3(BaseModel):
    prior_undisputed_transactions: List[EvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransaction]
    """
    List of exactly two prior undisputed transaction objects for Visa Compelling
    Evidence 3.0 evidence submission.
    """

    disputed_transaction: Optional[EvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransaction] = None


class EvidenceEnhancedEvidenceVisaCompliance(BaseModel):
    fee_acknowledged: bool
    """A field acknowledging the fee incurred when countering a Visa compliance
    dispute.

    If this field is set to true, evidence can be submitted for the compliance
    dispute. Stripe collects a 500 USD (or local equivalent) amount to cover the
    network costs associated with resolving compliance disputes. Stripe refunds the
    500 USD network fee if you win the dispute.
    """


class EvidenceEnhancedEvidence(BaseModel):
    visa_compelling_evidence_3: Optional[EvidenceEnhancedEvidenceVisaCompellingEvidence3] = None

    visa_compliance: Optional[EvidenceEnhancedEvidenceVisaCompliance] = None


EvidenceCancellationPolicy: TypeAlias = Union[str, "File", None]

EvidenceCustomerCommunication: TypeAlias = Union[str, "File", None]

EvidenceCustomerSignature: TypeAlias = Union[str, "File", None]

EvidenceDuplicateChargeDocumentation: TypeAlias = Union[str, "File", None]

EvidenceReceipt: TypeAlias = Union[str, "File", None]

EvidenceRefundPolicy: TypeAlias = Union[str, "File", None]

EvidenceServiceDocumentation: TypeAlias = Union[str, "File", None]

EvidenceShippingDocumentation: TypeAlias = Union[str, "File", None]

EvidenceUncategorizedFile: TypeAlias = Union[str, "File", None]


class Evidence(BaseModel):
    enhanced_evidence: EvidenceEnhancedEvidence

    access_activity_log: Optional[str] = None
    """
    Any server or activity logs showing proof that the customer accessed or
    downloaded the purchased digital product. This information should include IP
    addresses, corresponding timestamps, and any detailed recorded activity.
    """

    billing_address: Optional[str] = None
    """The billing address provided by the customer."""

    cancellation_policy: Optional[EvidenceCancellationPolicy] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your
    subscription cancellation policy, as shown to the customer.
    """

    cancellation_policy_disclosure: Optional[str] = None
    """
    An explanation of how and when the customer was shown your refund policy prior
    to purchase.
    """

    cancellation_rebuttal: Optional[str] = None
    """A justification for why the customer's subscription was not canceled."""

    customer_communication: Optional[EvidenceCustomerCommunication] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any
    communication with the customer that you feel is relevant to your case. Examples
    include emails proving that the customer received the product or service, or
    demonstrating their use of or satisfaction with the product or service.
    """

    customer_email_address: Optional[str] = None
    """The email address of the customer."""

    customer_name: Optional[str] = None
    """The name of the customer."""

    customer_purchase_ip: Optional[str] = None
    """The IP address that the customer used when making the purchase."""

    customer_signature: Optional[EvidenceCustomerSignature] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A relevant
    document or contract showing the customer's signature.
    """

    duplicate_charge_documentation: Optional[EvidenceDuplicateChargeDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload))
    Documentation for the prior charge that can uniquely identify the charge, such
    as a receipt, shipping label, work order, etc. This document should be paired
    with a similar document from the disputed payment that proves the two payments
    are separate.
    """

    duplicate_charge_explanation: Optional[str] = None
    """
    An explanation of the difference between the disputed charge versus the prior
    charge that appears to be a duplicate.
    """

    duplicate_charge_id: Optional[str] = None
    """
    The Stripe ID for the prior charge which appears to be a duplicate of the
    disputed charge.
    """

    product_description: Optional[str] = None
    """A description of the product or service that was sold."""

    receipt: Optional[EvidenceReceipt] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any receipt
    or message sent to the customer notifying them of the charge.
    """

    refund_policy: Optional[EvidenceRefundPolicy] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your refund
    policy, as shown to the customer.
    """

    refund_policy_disclosure: Optional[str] = None
    """
    Documentation demonstrating that the customer was shown your refund policy prior
    to purchase.
    """

    refund_refusal_explanation: Optional[str] = None
    """A justification for why the customer is not entitled to a refund."""

    service_date: Optional[str] = None
    """
    The date on which the customer received or began receiving the purchased
    service, in a clear human-readable format.
    """

    service_documentation: Optional[EvidenceServiceDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload))
    Documentation showing proof that a service was provided to the customer. This
    could include a copy of a signed contract, work order, or other form of written
    agreement.
    """

    shipping_address: Optional[str] = None
    """The address to which a physical product was shipped.

    You should try to include as complete address information as possible.
    """

    shipping_carrier: Optional[str] = None
    """
    The delivery service that shipped a physical product, such as Fedex, UPS, USPS,
    etc. If multiple carriers were used for this purchase, please separate them with
    commas.
    """

    shipping_date: Optional[str] = None
    """
    The date on which a physical product began its route to the shipping address, in
    a clear human-readable format.
    """

    shipping_documentation: Optional[EvidenceShippingDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload))
    Documentation showing proof that a product was shipped to the customer at the
    same address the customer provided to you. This could include a copy of the
    shipment receipt, shipping label, etc. It should show the customer's full
    shipping address, if possible.
    """

    shipping_tracking_number: Optional[str] = None
    """The tracking number for a physical product, obtained from the delivery service.

    If multiple tracking numbers were generated for this purchase, please separate
    them with commas.
    """

    uncategorized_file: Optional[EvidenceUncategorizedFile] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any
    additional evidence or statements.
    """

    uncategorized_text: Optional[str] = None
    """Any additional evidence or statements."""


class EvidenceDetailsEnhancedEligibilityVisaCompellingEvidence3(BaseModel):
    required_actions: List[
        Literal[
            "missing_customer_identifiers",
            "missing_disputed_transaction_description",
            "missing_merchandise_or_services",
            "missing_prior_undisputed_transaction_description",
            "missing_prior_undisputed_transactions",
        ]
    ]
    """
    List of actions required to qualify dispute for Visa Compelling Evidence 3.0
    evidence submission.
    """

    status: Literal["not_qualified", "qualified", "requires_action"]
    """Visa Compelling Evidence 3.0 eligibility status."""


class EvidenceDetailsEnhancedEligibilityVisaCompliance(BaseModel):
    status: Literal["fee_acknowledged", "requires_fee_acknowledgement"]
    """Visa compliance eligibility status."""


class EvidenceDetailsEnhancedEligibility(BaseModel):
    visa_compelling_evidence_3: Optional[EvidenceDetailsEnhancedEligibilityVisaCompellingEvidence3] = None

    visa_compliance: Optional[EvidenceDetailsEnhancedEligibilityVisaCompliance] = None


class EvidenceDetails(BaseModel):
    enhanced_eligibility: EvidenceDetailsEnhancedEligibility

    has_evidence: bool
    """Whether evidence has been staged for this dispute."""

    past_due: bool
    """Whether the last evidence submission was submitted past the due date.

    Defaults to `false` if no evidence submissions have occurred. If `true`, then
    delivery of the latest evidence is _not_ guaranteed.
    """

    submission_count: int
    """The number of times evidence has been submitted.

    Typically, you may only submit evidence once.
    """

    due_by: Optional[int] = None
    """
    Date by which evidence must be submitted in order to successfully challenge
    dispute. Will be 0 if the customer's bank or credit card company doesn't allow a
    response for this particular dispute.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    PaymentIntent = TypeAliasType("PaymentIntent", Union[str, "payment_intent.PaymentIntent", None])
else:
    PaymentIntent: TypeAlias = Union[str, "payment_intent.PaymentIntent", None]


class PaymentMethodDetailsAmazonPay(BaseModel):
    dispute_type: Optional[Literal["chargeback", "claim"]] = None
    """The AmazonPay dispute type, chargeback or claim"""


class PaymentMethodDetailsCard(BaseModel):
    brand: str
    """Card brand.

    Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`,
    `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
    """

    case_type: Literal["block", "chargeback", "compliance", "inquiry", "resolution"]
    """The type of dispute opened.

    Different case types may have varying fees and financial impact.
    """

    network_reason_code: Optional[str] = None
    """
    The card network's specific dispute reason code, which maps to one of Stripe's
    primary dispute categories to simplify response guidance. The
    [Network code map](https://stripe.com/docs/disputes/categories#network-code-map)
    lists all available dispute reason codes by network.
    """


class PaymentMethodDetailsKlarna(BaseModel):
    chargeback_loss_reason_code: Optional[str] = None
    """Chargeback loss reason mapped by Stripe from Klarna's chargeback loss reason"""

    reason_code: Optional[str] = None
    """The reason for the dispute as defined by Klarna"""


class PaymentMethodDetailsPaypal(BaseModel):
    case_id: Optional[str] = None
    """The ID of the dispute in PayPal."""

    reason_code: Optional[str] = None
    """The reason for the dispute as defined by PayPal"""


class PaymentMethodDetails(BaseModel):
    type: Literal["amazon_pay", "card", "klarna", "paypal"]
    """Payment method type."""

    amazon_pay: Optional[PaymentMethodDetailsAmazonPay] = None

    card: Optional[PaymentMethodDetailsCard] = None

    klarna: Optional[PaymentMethodDetailsKlarna] = None

    paypal: Optional[PaymentMethodDetailsPaypal] = None


class Dispute(BaseModel):
    """
    A dispute occurs when a customer questions your charge with their card issuer.
    When this happens, you have the opportunity to respond to the dispute with
    evidence that shows that the charge is legitimate.

    Related guide: [Disputes and fraud](https://docs.stripe.com/disputes)
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """Disputed amount.

    Usually the amount of the charge, but it can differ (usually because of currency
    fluctuation or because only part of the order is disputed).
    """

    balance_transactions: List["BalanceTransaction"]
    """
    List of zero, one, or two balance transactions that show funds withdrawn and
    reinstated to your Stripe account as a result of this dispute.
    """

    charge: Charge
    """ID of the charge that's disputed."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    enhanced_eligibility_types: List[Literal["visa_compelling_evidence_3", "visa_compliance"]]
    """List of eligibility types that are included in `enhanced_evidence`."""

    evidence: Evidence

    evidence_details: EvidenceDetails

    is_charge_refundable: bool
    """If true, it's still possible to refund the disputed payment.

    After the payment has been fully refunded, no further funds are withdrawn from
    your Stripe account as a result of this dispute.
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

    object: Literal["dispute"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    reason: str
    """Reason given by cardholder for dispute.

    Possible values are `bank_cannot_process`, `check_returned`,
    `credit_not_processed`, `customer_initiated`, `debit_not_authorized`,
    `duplicate`, `fraudulent`, `general`, `incorrect_account_details`,
    `insufficient_funds`, `noncompliant`, `product_not_received`,
    `product_unacceptable`, `subscription_canceled`, or `unrecognized`. Learn more
    about [dispute reasons](https://docs.stripe.com/disputes/categories).
    """

    status: Literal[
        "lost",
        "needs_response",
        "prevented",
        "under_review",
        "warning_closed",
        "warning_needs_response",
        "warning_under_review",
        "won",
    ]
    """The current status of a dispute.

    Possible values include:`warning_needs_response`, `warning_under_review`,
    `warning_closed`, `needs_response`, `under_review`, `won`, `lost`, or
    `prevented`.
    """

    payment_intent: Optional[PaymentIntent] = None
    """ID of the PaymentIntent that's disputed."""

    payment_method_details: Optional[PaymentMethodDetails] = None


from . import charge, payment_intent
from .file import File
from .balance_transaction import BalanceTransaction
