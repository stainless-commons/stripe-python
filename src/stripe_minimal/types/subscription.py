# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import application
from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .tax_rate import TaxRate
from .shared.source import Source
from .shared.deleted_customer import DeletedCustomer
from .shared.deleted_application import DeletedApplication
from .shared.test_helpers_test_clock import TestHelpersTestClock
from .subscription_billing_thresholds import SubscriptionBillingThresholds

__all__ = [
    "Subscription",
    "BillingMode",
    "BillingModeFlexible",
    "Customer",
    "Discount",
    "Items",
    "Application",
    "BillingCycleAnchorConfig",
    "CancellationDetails",
    "DefaultPaymentMethod",
    "DefaultSource",
    "LatestInvoice",
    "OnBehalfOf",
    "PauseCollection",
    "PaymentSettings",
    "PaymentSettingsPaymentMethodOptions",
    "PaymentSettingsPaymentMethodOptionsAcssDebit",
    "PaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions",
    "PaymentSettingsPaymentMethodOptionsBancontact",
    "PaymentSettingsPaymentMethodOptionsCard",
    "PaymentSettingsPaymentMethodOptionsCardMandateOptions",
    "PaymentSettingsPaymentMethodOptionsCustomerBalance",
    "PaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer",
    "PaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer",
    "PaymentSettingsPaymentMethodOptionsPayto",
    "PaymentSettingsPaymentMethodOptionsPaytoMandateOptions",
    "PaymentSettingsPaymentMethodOptionsUsBankAccount",
    "PaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections",
    "PaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters",
    "PendingInvoiceItemInterval",
    "PendingSetupIntent",
    "Schedule",
    "TestClock",
    "TrialSettings",
    "TrialSettingsEndBehavior",
]


class BillingModeFlexible(BaseModel):
    proration_discounts: Optional[Literal["included", "itemized"]] = None
    """
    Controls how invoices and invoice items display proration amounts and discount
    amounts.
    """


class BillingMode(BaseModel):
    """The billing mode of the subscription."""

    type: Literal["classic", "flexible"]
    """
    Controls how prorations and invoices for subscriptions are calculated and
    orchestrated.
    """

    flexible: Optional[BillingModeFlexible] = None

    updated_at: Optional[int] = None
    """Details on when the current billing_mode was adopted."""


if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer]

if TYPE_CHECKING or not PYDANTIC_V1:
    Discount = TypeAliasType("Discount", Union[str, "discount.Discount"])
else:
    Discount: TypeAlias = Union[str, "discount.Discount"]


class Items(BaseModel):
    """List of subscription items, each with an attached price."""

    data: List["SubscriptionItem"]
    """Details about each object."""

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


Application: TypeAlias = Union[str, application.Application, DeletedApplication, None]


class BillingCycleAnchorConfig(BaseModel):
    day_of_month: int
    """The day of the month of the billing_cycle_anchor."""

    hour: Optional[int] = None
    """The hour of the day of the billing_cycle_anchor."""

    minute: Optional[int] = None
    """The minute of the hour of the billing_cycle_anchor."""

    month: Optional[int] = None
    """The month to start full cycle billing periods."""

    second: Optional[int] = None
    """The second of the minute of the billing_cycle_anchor."""


class CancellationDetails(BaseModel):
    comment: Optional[str] = None
    """
    Additional comments about why the user canceled the subscription, if the
    subscription was canceled explicitly by the user.
    """

    feedback: Optional[
        Literal[
            "customer_service",
            "low_quality",
            "missing_features",
            "other",
            "switched_service",
            "too_complex",
            "too_expensive",
            "unused",
        ]
    ] = None
    """
    The customer submitted reason for why they canceled, if the subscription was
    canceled explicitly by the user.
    """

    reason: Optional[Literal["cancellation_requested", "payment_disputed", "payment_failed"]] = None
    """Why this subscription was canceled."""


if TYPE_CHECKING or not PYDANTIC_V1:
    DefaultPaymentMethod = TypeAliasType("DefaultPaymentMethod", Union[str, "PaymentMethod", None])
else:
    DefaultPaymentMethod: TypeAlias = Union[str, "PaymentMethod", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    DefaultSource = TypeAliasType("DefaultSource", Union[str, "BankAccount", "Card", Source, None])
else:
    DefaultSource: TypeAlias = Union[str, "BankAccount", "Card", Source, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    LatestInvoice = TypeAliasType("LatestInvoice", Union[str, "Invoice", None])
else:
    LatestInvoice: TypeAlias = Union[str, "Invoice", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    OnBehalfOf = TypeAliasType("OnBehalfOf", Union[str, "Account", None])
else:
    OnBehalfOf: TypeAlias = Union[str, "Account", None]


class PauseCollection(BaseModel):
    """
    The Pause Collection settings determine how we will pause collection for this subscription and for how long the subscription
    should be paused.
    """

    behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
    """The payment collection behavior for this subscription while paused.

    One of `keep_as_draft`, `mark_uncollectible`, or `void`.
    """

    resumes_at: Optional[int] = None
    """The time after which the subscription will resume collecting payments."""


class PaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(BaseModel):
    transaction_type: Optional[Literal["business", "personal"]] = None
    """Transaction type of the mandate."""


class PaymentSettingsPaymentMethodOptionsAcssDebit(BaseModel):
    mandate_options: Optional[PaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions] = None

    verification_method: Optional[Literal["automatic", "instant", "microdeposits"]] = None
    """Bank account verification method."""


class PaymentSettingsPaymentMethodOptionsBancontact(BaseModel):
    preferred_language: Literal["de", "en", "fr", "nl"]
    """
    Preferred language of the Bancontact authorization page that the customer is
    redirected to.
    """


class PaymentSettingsPaymentMethodOptionsCardMandateOptions(BaseModel):
    amount: Optional[int] = None
    """Amount to be charged for future payments."""

    amount_type: Optional[Literal["fixed", "maximum"]] = None
    """One of `fixed` or `maximum`.

    If `fixed`, the `amount` param refers to the exact amount to be charged in
    future payments. If `maximum`, the amount charged can be up to the value passed
    for the `amount` param.
    """

    description: Optional[str] = None
    """
    A description of the mandate or subscription that is meant to be displayed to
    the customer.
    """


class PaymentSettingsPaymentMethodOptionsCard(BaseModel):
    mandate_options: Optional[PaymentSettingsPaymentMethodOptionsCardMandateOptions] = None

    network: Optional[
        Literal[
            "amex",
            "cartes_bancaires",
            "diners",
            "discover",
            "eftpos_au",
            "girocard",
            "interac",
            "jcb",
            "link",
            "mastercard",
            "unionpay",
            "unknown",
            "visa",
        ]
    ] = None
    """Selected network to process this Subscription on.

    Depends on the available networks of the card attached to the Subscription. Can
    be only set confirm-time.
    """

    request_three_d_secure: Optional[Literal["any", "automatic", "challenge"]] = None
    """
    We strongly recommend that you rely on our SCA Engine to automatically prompt
    your customers for authentication based on risk level and
    [other requirements](https://docs.stripe.com/strong-customer-authentication).
    However, if you wish to request 3D Secure based on logic from your own fraud
    engine, provide this option. Read our guide on
    [manually requesting 3D Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds)
    for more information on how this configuration interacts with Radar and our SCA
    Engine.
    """


class PaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(BaseModel):
    country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]
    """The desired country code of the bank account information.

    Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
    """


class PaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(BaseModel):
    eu_bank_transfer: Optional[PaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer] = None

    type: Optional[str] = None
    """The bank transfer type that can be used for funding.

    Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`,
    `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
    """


class PaymentSettingsPaymentMethodOptionsCustomerBalance(BaseModel):
    bank_transfer: Optional[PaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer] = None

    funding_type: Optional[Literal["bank_transfer"]] = None
    """
    The funding method type to be used when there are not enough funds in the
    customer balance. Permitted values include: `bank_transfer`.
    """


class PaymentSettingsPaymentMethodOptionsPaytoMandateOptions(BaseModel):
    amount: Optional[int] = None
    """The maximum amount that can be collected in a single invoice.

    If you don't specify a maximum, then there is no limit.
    """

    amount_type: Optional[Literal["fixed", "maximum"]] = None
    """Only `maximum` is supported."""

    purpose: Optional[
        Literal[
            "dependant_support",
            "government",
            "loan",
            "mortgage",
            "other",
            "pension",
            "personal",
            "retail",
            "salary",
            "tax",
            "utility",
        ]
    ] = None
    """The purpose for which payments are made.

    Has a default value based on your merchant category code.
    """


class PaymentSettingsPaymentMethodOptionsPayto(BaseModel):
    mandate_options: Optional[PaymentSettingsPaymentMethodOptionsPaytoMandateOptions] = None


class PaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(BaseModel):
    account_subcategories: Optional[List[Literal["checking", "savings"]]] = None
    """The account subcategories to use to filter for possible accounts to link.

    Valid subcategories are `checking` and `savings`.
    """


class PaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(BaseModel):
    filters: Optional[PaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters] = None

    permissions: Optional[List[Literal["balances", "ownership", "payment_method", "transactions"]]] = None
    """The list of permissions to request.

    The `payment_method` permission must be included.
    """

    prefetch: Optional[List[Literal["balances", "ownership", "transactions"]]] = None
    """Data features requested to be retrieved upon account creation."""


class PaymentSettingsPaymentMethodOptionsUsBankAccount(BaseModel):
    financial_connections: Optional[PaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections] = None

    verification_method: Optional[Literal["automatic", "instant", "microdeposits"]] = None
    """Bank account verification method."""


class PaymentSettingsPaymentMethodOptions(BaseModel):
    acss_debit: Optional[PaymentSettingsPaymentMethodOptionsAcssDebit] = None

    bancontact: Optional[PaymentSettingsPaymentMethodOptionsBancontact] = None

    card: Optional[PaymentSettingsPaymentMethodOptionsCard] = None

    customer_balance: Optional[PaymentSettingsPaymentMethodOptionsCustomerBalance] = None

    konbini: Optional[object] = None

    payto: Optional[PaymentSettingsPaymentMethodOptionsPayto] = None

    sepa_debit: Optional[object] = None

    us_bank_account: Optional[PaymentSettingsPaymentMethodOptionsUsBankAccount] = None


class PaymentSettings(BaseModel):
    payment_method_options: Optional[PaymentSettingsPaymentMethodOptions] = None

    payment_method_types: Optional[
        List[
            Literal[
                "ach_credit_transfer",
                "ach_debit",
                "acss_debit",
                "affirm",
                "amazon_pay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "boleto",
                "card",
                "cashapp",
                "crypto",
                "custom",
                "customer_balance",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "jp_credit_transfer",
                "kakao_pay",
                "klarna",
                "konbini",
                "kr_card",
                "link",
                "multibanco",
                "naver_pay",
                "nz_bank_account",
                "p24",
                "payco",
                "paynow",
                "paypal",
                "payto",
                "promptpay",
                "revolut_pay",
                "sepa_credit_transfer",
                "sepa_debit",
                "sofort",
                "swish",
                "us_bank_account",
                "wechat_pay",
            ]
        ]
    ] = None
    """
    The list of payment method types to provide to every invoice created by the
    subscription. If not set, Stripe attempts to automatically determine the types
    to use by looking at the invoice’s default payment method, the subscription’s
    default payment method, the customer’s default payment method, and your
    [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice).
    """

    save_default_payment_method: Optional[Literal["off", "on_subscription"]] = None
    """
    Configure whether Stripe updates `subscription.default_payment_method` when
    payment succeeds. Defaults to `off`.
    """


class PendingInvoiceItemInterval(BaseModel):
    interval: Literal["day", "month", "week", "year"]
    """Specifies invoicing frequency. Either `day`, `week`, `month` or `year`."""

    interval_count: int
    """The number of intervals between invoices.

    For example, `interval=month` and `interval_count=3` bills every 3 months.
    Maximum of one year interval allowed (1 year, 12 months, or 52 weeks).
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    PendingSetupIntent = TypeAliasType("PendingSetupIntent", Union[str, "SetupIntent", None])
else:
    PendingSetupIntent: TypeAlias = Union[str, "SetupIntent", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Schedule = TypeAliasType("Schedule", Union[str, "schedule.Schedule", None])
else:
    Schedule: TypeAlias = Union[str, "schedule.Schedule", None]

TestClock: TypeAlias = Union[str, TestHelpersTestClock, None]


class TrialSettingsEndBehavior(BaseModel):
    """Defines how a subscription behaves when a free trial ends."""

    missing_payment_method: Literal["cancel", "create_invoice", "pause"]
    """
    Indicates how the subscription should change when the trial ends if the user did
    not provide a payment method.
    """


class TrialSettings(BaseModel):
    """Configures how this subscription behaves during the trial period."""

    end_behavior: TrialSettingsEndBehavior
    """Defines how a subscription behaves when a free trial ends."""


class Subscription(BaseModel):
    """Subscriptions allow you to charge a customer on a recurring basis.

    Related guide: [Creating subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
    """

    id: str
    """Unique identifier for the object."""

    automatic_tax: "AutomaticTaxSubscription"

    billing_cycle_anchor: int
    """
    The reference point that aligns future
    [billing cycle](https://docs.stripe.com/subscriptions/billing-cycle) dates. It
    sets the day of week for `week` intervals, the day of month for `month` and
    `year` intervals, and the month of year for `year` intervals. The timestamp is
    in UTC format.
    """

    billing_mode: BillingMode
    """The billing mode of the subscription."""

    cancel_at_period_end: bool
    """
    Whether this subscription will (if `status=active`) or did (if
    `status=canceled`) cancel at the end of the current billing period.
    """

    collection_method: Literal["charge_automatically", "send_invoice"]
    """Either `charge_automatically`, or `send_invoice`.

    When charging automatically, Stripe will attempt to pay this subscription at the
    end of the cycle using the default source attached to the customer. When sending
    an invoice, Stripe will email your customer an invoice with payment instructions
    and mark the subscription as `active`.
    """

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: Customer
    """ID of the customer who owns the subscription."""

    discounts: List[Discount]
    """The discounts applied to the subscription.

    Subscription item discounts are applied before subscription discounts. Use
    `expand[]=discounts` to expand each discount.
    """

    invoice_settings: "SubscriptionInvoiceSettings"

    items: Items
    """List of subscription items, each with an attached price."""

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

    object: Literal["subscription"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    start_date: int
    """Date when the subscription was first created.

    The date might differ from the `created` date due to backdating.
    """

    status: Literal[
        "active", "canceled", "incomplete", "incomplete_expired", "past_due", "paused", "trialing", "unpaid"
    ]
    """
    Possible values are `incomplete`, `incomplete_expired`, `trialing`, `active`,
    `past_due`, `canceled`, `unpaid`, or `paused`.

    For `collection_method=charge_automatically` a subscription moves into
    `incomplete` if the initial payment attempt fails. A subscription in this status
    can only have metadata and default_source updated. Once the first invoice is
    paid, the subscription moves into an `active` status. If the first invoice is
    not paid within 23 hours, the subscription transitions to `incomplete_expired`.
    This is a terminal status, the open invoice will be voided and no further
    invoices will be generated.

    A subscription that is currently in a trial period is `trialing` and moves to
    `active` when the trial period is over.

    A subscription can only enter a `paused` status
    [when a trial ends without a payment method](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment).
    A `paused` subscription doesn't generate invoices and can be resumed after your
    customer adds their payment method. The `paused` status is different from
    [pausing collection](https://docs.stripe.com/billing/subscriptions/pause-payment),
    which still generates invoices and leaves the subscription's status unchanged.

    If subscription `collection_method=charge_automatically`, it becomes `past_due`
    when payment is required but cannot be paid (due to failed payment or awaiting
    additional user actions). Once Stripe has exhausted all payment retry attempts,
    the subscription will become `canceled` or `unpaid` (depending on your
    subscriptions settings).

    If subscription `collection_method=send_invoice` it becomes `past_due` when its
    invoice is not paid by the due date, and `canceled` or `unpaid` if it is still
    not paid by an additional deadline after that. Note that when a subscription has
    a status of `unpaid`, no subsequent invoices will be attempted (invoices will be
    created, but then immediately automatically closed). After receiving updated
    payment information from a customer, you may choose to reopen and pay their
    closed invoices.
    """

    application: Optional[Application] = None
    """ID of the Connect Application that created the subscription."""

    application_fee_percent: Optional[float] = None
    """A non-negative decimal between 0 and 100, with at most two decimal places.

    This represents the percentage of the subscription invoice total that will be
    transferred to the application owner's Stripe account.
    """

    billing_cycle_anchor_config: Optional[BillingCycleAnchorConfig] = None

    billing_thresholds: Optional[SubscriptionBillingThresholds] = None

    cancel_at: Optional[int] = None
    """A date in the future at which the subscription will automatically get canceled"""

    canceled_at: Optional[int] = None
    """If the subscription has been canceled, the date of that cancellation.

    If the subscription was canceled with `cancel_at_period_end`, `canceled_at` will
    reflect the time of the most recent update request, not the end of the
    subscription period when the subscription is automatically moved to a canceled
    state.
    """

    cancellation_details: Optional[CancellationDetails] = None

    customer_account: Optional[str] = None
    """ID of the account representing the customer who owns the subscription."""

    days_until_due: Optional[int] = None
    """Number of days a customer has to pay invoices generated by this subscription.

    This value will be `null` for subscriptions where
    `collection_method=charge_automatically`.
    """

    default_payment_method: Optional[DefaultPaymentMethod] = None
    """ID of the default payment method for the subscription.

    It must belong to the customer associated with the subscription. This takes
    precedence over `default_source`. If neither are set, invoices will use the
    customer's
    [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
    or
    [default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source).
    """

    default_source: Optional[DefaultSource] = None
    """ID of the default payment source for the subscription.

    It must belong to the customer associated with the subscription and be in a
    chargeable state. If `default_payment_method` is also set,
    `default_payment_method` will take precedence. If neither are set, invoices will
    use the customer's
    [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
    or
    [default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source).
    """

    default_tax_rates: Optional[List[TaxRate]] = None
    """
    The tax rates that will apply to any subscription item that does not have
    `tax_rates` set. Invoices created will have their `default_tax_rates` populated
    from the subscription.
    """

    description: Optional[str] = None
    """The subscription's description, meant to be displayable to the customer.

    Use this field to optionally store an explanation of the subscription for
    rendering in Stripe surfaces and certain local payment methods UIs.
    """

    ended_at: Optional[int] = None
    """If the subscription has ended, the date the subscription ended."""

    latest_invoice: Optional[LatestInvoice] = None
    """
    The most recent invoice this subscription has generated over its lifecycle (for
    example, when it cycles or is updated).
    """

    next_pending_invoice_item_invoice: Optional[int] = None
    """
    Specifies the approximate timestamp on which any pending invoice items will be
    billed according to the schedule provided at `pending_invoice_item_interval`.
    """

    on_behalf_of: Optional[OnBehalfOf] = None
    """
    The account (if any) the charge was made on behalf of for charges associated
    with this subscription. See the
    [Connect documentation](https://docs.stripe.com/connect/subscriptions#on-behalf-of)
    for details.
    """

    pause_collection: Optional[PauseCollection] = None
    """
    The Pause Collection settings determine how we will pause collection for this
    subscription and for how long the subscription should be paused.
    """

    payment_settings: Optional[PaymentSettings] = None

    pending_invoice_item_interval: Optional[PendingInvoiceItemInterval] = None

    pending_setup_intent: Optional[PendingSetupIntent] = None
    """
    You can use this [SetupIntent](https://docs.stripe.com/api/setup_intents) to
    collect user authentication when creating a subscription without immediate
    payment or updating a subscription's payment method, allowing you to optimize
    for off-session payments. Learn more in the
    [SCA Migration Guide](https://docs.stripe.com/billing/migration/strong-customer-authentication#scenario-2).
    """

    pending_update: Optional["PendingUpdate"] = None
    """
    Pending Updates store the changes pending from a previous update that will be
    applied to the Subscription upon successful payment.
    """

    schedule: Optional[Schedule] = None
    """The schedule attached to the subscription"""

    test_clock: Optional[TestClock] = None
    """ID of the test clock this subscription belongs to."""

    transfer_data: Optional["SubscriptionTransferData"] = None

    trial_end: Optional[int] = None
    """If the subscription has a trial, the end of that trial."""

    trial_settings: Optional[TrialSettings] = None
    """Configures how this subscription behaves during the trial period."""

    trial_start: Optional[int] = None
    """If the subscription has a trial, the beginning of that trial."""


from . import customer, discount, schedule
from .card import Card
from .account import Account
from .invoice import Invoice
from .bank_account import BankAccount
from .setup_intent import SetupIntent
from .payment_method import PaymentMethod
from .pending_update import PendingUpdate
from .subscription_item import SubscriptionItem
from .automatic_tax_subscription import AutomaticTaxSubscription
from .subscription_transfer_data import SubscriptionTransferData
from .subscription_invoice_settings import SubscriptionInvoiceSettings
