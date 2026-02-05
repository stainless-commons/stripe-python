# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "SubscriptionUpdateParams",
    "AddInvoiceItem",
    "AddInvoiceItemDiscount",
    "AddInvoiceItemPeriod",
    "AddInvoiceItemPeriodEnd",
    "AddInvoiceItemPeriodStart",
    "AddInvoiceItemPriceData",
    "AutomaticTax",
    "AutomaticTaxLiability",
    "BillingThresholds",
    "BillingThresholdsBillingThresholdsParam",
    "CancellationDetails",
    "DiscountsDiscountsList",
    "InvoiceSettings",
    "InvoiceSettingsIssuer",
    "Item",
    "ItemBillingThresholds",
    "ItemBillingThresholdsItemBillingThresholdsParam",
    "ItemDiscountsDiscountsList",
    "ItemPriceData",
    "ItemPriceDataRecurring",
    "PauseCollection",
    "PauseCollectionPauseCollectionParam",
    "PaymentSettings",
    "PaymentSettingsPaymentMethodOptions",
    "PaymentSettingsPaymentMethodOptionsAcssDebit",
    "PaymentSettingsPaymentMethodOptionsAcssDebitInvoicePaymentMethodOptionsParam",
    "PaymentSettingsPaymentMethodOptionsAcssDebitInvoicePaymentMethodOptionsParamMandateOptions",
    "PaymentSettingsPaymentMethodOptionsBancontact",
    "PaymentSettingsPaymentMethodOptionsBancontactInvoicePaymentMethodOptionsParam",
    "PaymentSettingsPaymentMethodOptionsCard",
    "PaymentSettingsPaymentMethodOptionsCardSubscriptionPaymentMethodOptionsParam",
    "PaymentSettingsPaymentMethodOptionsCardSubscriptionPaymentMethodOptionsParamMandateOptions",
    "PaymentSettingsPaymentMethodOptionsCustomerBalance",
    "PaymentSettingsPaymentMethodOptionsCustomerBalanceInvoicePaymentMethodOptionsParam",
    "PaymentSettingsPaymentMethodOptionsCustomerBalanceInvoicePaymentMethodOptionsParamBankTransfer",
    "PaymentSettingsPaymentMethodOptionsCustomerBalanceInvoicePaymentMethodOptionsParamBankTransferEuBankTransfer",
    "PaymentSettingsPaymentMethodOptionsPayto",
    "PaymentSettingsPaymentMethodOptionsPaytoInvoicePaymentMethodOptionsParam",
    "PaymentSettingsPaymentMethodOptionsPaytoInvoicePaymentMethodOptionsParamMandateOptions",
    "PaymentSettingsPaymentMethodOptionsUsBankAccount",
    "PaymentSettingsPaymentMethodOptionsUsBankAccountInvoicePaymentMethodOptionsParam",
    "PaymentSettingsPaymentMethodOptionsUsBankAccountInvoicePaymentMethodOptionsParamFinancialConnections",
    "PaymentSettingsPaymentMethodOptionsUsBankAccountInvoicePaymentMethodOptionsParamFinancialConnectionsFilters",
    "PendingInvoiceItemInterval",
    "PendingInvoiceItemIntervalPendingInvoiceItemIntervalParams",
    "TransferData",
    "TransferDataTransferDataSpecs",
    "TrialSettings",
    "TrialSettingsEndBehavior",
]


class SubscriptionUpdateParams(TypedDict, total=False):
    add_invoice_items: Iterable[AddInvoiceItem]
    """
    A list of prices and quantities that will generate invoice items appended to the
    next invoice for this subscription. You may pass up to 20 items.
    """

    application_fee_percent: Union[float, Literal[""]]
    """A non-negative decimal between 0 and 100, with at most two decimal places.

    This represents the percentage of the subscription invoice total that will be
    transferred to the application owner's Stripe account. The request must be made
    by a platform account on a connected account in order to set an application fee
    percentage. For more information, see the application fees
    [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
    """

    automatic_tax: AutomaticTax
    """Automatic tax settings for this subscription.

    We recommend you only include this parameter when the existing value is being
    changed.
    """

    billing_cycle_anchor: Literal["now", "unchanged"]
    """Either `now` or `unchanged`.

    Setting the value to `now` resets the subscription's billing cycle anchor to the
    current time (in UTC). For more information, see the billing cycle
    [documentation](https://docs.stripe.com/billing/subscriptions/billing-cycle).
    """

    billing_thresholds: BillingThresholds
    """
    Define thresholds at which an invoice will be sent, and the subscription
    advanced to a new billing period. When updating, pass an empty string to remove
    previously-defined thresholds.
    """

    cancel_at: Union[Literal["", "max_period_end", "min_period_end"], int]
    """A timestamp at which the subscription should cancel.

    If set to a date before the current period ends, this will cause a proration if
    prorations have been enabled using `proration_behavior`. If set during a future
    period, this will always cause a proration for that period.
    """

    cancel_at_period_end: bool
    """
    Indicate whether this subscription should cancel at the end of the current
    period (`current_period_end`). Defaults to `false`.
    """

    cancellation_details: CancellationDetails
    """Details about why this subscription was cancelled"""

    collection_method: Literal["charge_automatically", "send_invoice"]
    """Either `charge_automatically`, or `send_invoice`.

    When charging automatically, Stripe will attempt to pay this subscription at the
    end of the cycle using the default source attached to the customer. When sending
    an invoice, Stripe will email your customer an invoice with payment instructions
    and mark the subscription as `active`. Defaults to `charge_automatically`.
    """

    days_until_due: int
    """Number of days a customer has to pay invoices generated by this subscription.

    Valid only for subscriptions where `collection_method` is set to `send_invoice`.
    """

    default_payment_method: str
    """ID of the default payment method for the subscription.

    It must belong to the customer associated with the subscription. This takes
    precedence over `default_source`. If neither are set, invoices will use the
    customer's
    [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
    or
    [default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source).
    """

    default_source: Union[str, Literal[""]]
    """ID of the default payment source for the subscription.

    It must belong to the customer associated with the subscription and be in a
    chargeable state. If `default_payment_method` is also set,
    `default_payment_method` will take precedence. If neither are set, invoices will
    use the customer's
    [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
    or
    [default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source).
    """

    default_tax_rates: Union[SequenceNotStr[str], Literal[""]]
    """
    The tax rates that will apply to any subscription item that does not have
    `tax_rates` set. Invoices created will have their `default_tax_rates` populated
    from the subscription. Pass an empty string to remove previously-defined tax
    rates.
    """

    description: Union[str, Literal[""]]
    """The subscription's description, meant to be displayable to the customer.

    Use this field to optionally store an explanation of the subscription for
    rendering in Stripe surfaces and certain local payment methods UIs.
    """

    discounts: Union[Iterable[DiscountsDiscountsList], Literal[""]]
    """The coupons to redeem into discounts for the subscription.

    If not specified or empty, inherits the discount from the subscription's
    customer.
    """

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    invoice_settings: InvoiceSettings
    """All invoices will be billed using the specified settings."""

    items: Iterable[Item]
    """A list of up to 20 subscription items, each with an attached price."""

    metadata: Union[Dict[str, str], Literal[""]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Individual keys can be unset by posting an
    empty value to them. All keys can be unset by posting an empty value to
    `metadata`.
    """

    off_session: bool
    """
    Indicates if a customer is on or off-session while an invoice payment is
    attempted. Defaults to `false` (on-session).
    """

    on_behalf_of: Union[str, Literal[""]]
    """
    The account on behalf of which to charge, for each of the subscription's
    invoices.
    """

    pause_collection: PauseCollection
    """If specified, payment collection for this subscription will be paused.

    Note that the subscription status will be unchanged and will not be updated to
    `paused`. Learn more about
    [pausing collection](https://docs.stripe.com/billing/subscriptions/pause-payment).
    """

    payment_behavior: Literal["allow_incomplete", "default_incomplete", "error_if_incomplete", "pending_if_incomplete"]
    """
    Use `allow_incomplete` to transition the subscription to `status=past_due` if a
    payment is required but cannot be paid. This allows you to manage scenarios
    where additional user actions are needed to pay a subscription's invoice. For
    example, SCA regulation may require 3DS authentication to complete payment. See
    the
    [SCA Migration Guide](https://docs.stripe.com/billing/migration/strong-customer-authentication)
    for Billing to learn more. This is the default behavior.

    Use `default_incomplete` to transition the subscription to `status=past_due`
    when payment is required and await explicit confirmation of the invoice's
    payment intent. This allows simpler management of scenarios where additional
    user actions are needed to pay a subscription’s invoice. Such as failed
    payments,
    [SCA regulation](https://docs.stripe.com/billing/migration/strong-customer-authentication),
    or collecting a mandate for a bank debit payment method.

    Use `pending_if_incomplete` to update the subscription using
    [pending updates](https://docs.stripe.com/billing/subscriptions/pending-updates).
    When you use `pending_if_incomplete` you can only pass the parameters
    [supported by pending updates](https://docs.stripe.com/billing/pending-updates-reference#supported-attributes).

    Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code
    if a subscription's invoice cannot be paid. For example, if a payment method
    requires 3DS authentication due to SCA regulation and further user action is
    needed, this parameter does not update the subscription and returns an error
    instead. This was the default behavior for API versions prior to 2019-03-14. See
    the [changelog](https://docs.stripe.com/changelog/2019-03-14) to learn more.
    """

    payment_settings: PaymentSettings
    """Payment settings to pass to invoices created by the subscription."""

    pending_invoice_item_interval: PendingInvoiceItemInterval
    """Specifies an interval for how often to bill for any pending invoice items.

    It is analogous to calling
    [Create an invoice](https://docs.stripe.com/api#create_invoice) for the given
    subscription at the specified interval.
    """

    proration_behavior: Literal["always_invoice", "create_prorations", "none"]
    """
    Determines how to handle
    [prorations](https://docs.stripe.com/billing/subscriptions/prorations) when the
    billing cycle changes (e.g., when switching plans, resetting
    `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity`
    changes. The default value is `create_prorations`.
    """

    proration_date: int
    """
    If set, prorations will be calculated as though the subscription was updated at
    the given time. This can be used to apply exactly the same prorations that were
    previewed with the
    [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint.
    `proration_date` can also be used to implement custom proration logic, such as
    prorating by day instead of by second, by providing the time that you wish to
    use for proration calculations.
    """

    transfer_data: TransferData
    """
    If specified, the funds from the subscription's invoices will be transferred to
    the destination and the ID of the resulting transfers will be found on the
    resulting charges. This will be unset if you POST an empty value.
    """

    trial_end: Union[Literal["now"], int]
    """
    Unix timestamp representing the end of the trial period the customer will get
    before being charged for the first time. This will always overwrite any trials
    that might apply via a subscribed plan. If set, `trial_end` will override the
    default trial period of the plan the customer is being subscribed to. The
    `billing_cycle_anchor` will be updated to the `trial_end` value. The special
    value `now` can be provided to end the customer's trial immediately. Can be at
    most two years from `billing_cycle_anchor`.
    """

    trial_from_plan: bool
    """Indicates if a plan's `trial_period_days` should be applied to the subscription.

    Setting `trial_end` per subscription is preferred, and this defaults to `false`.
    Setting this flag to `true` together with `trial_end` is not allowed. See
    [Using trial periods on subscriptions](https://docs.stripe.com/billing/subscriptions/trials)
    to learn more.
    """

    trial_settings: TrialSettings
    """Settings related to subscription trials."""


class AddInvoiceItemDiscount(TypedDict, total=False):
    coupon: str

    discount: str

    promotion_code: str


class AddInvoiceItemPeriodEnd(TypedDict, total=False):
    type: Required[Literal["min_item_period_end", "timestamp"]]

    timestamp: int


class AddInvoiceItemPeriodStart(TypedDict, total=False):
    type: Required[Literal["max_item_period_start", "now", "timestamp"]]

    timestamp: int


class AddInvoiceItemPeriod(TypedDict, total=False):
    end: Required[AddInvoiceItemPeriodEnd]

    start: Required[AddInvoiceItemPeriodStart]


class AddInvoiceItemPriceData(TypedDict, total=False):
    currency: Required[str]

    product: Required[str]

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]

    unit_amount: int

    unit_amount_decimal: str


class AddInvoiceItem(TypedDict, total=False):
    discounts: Iterable[AddInvoiceItemDiscount]

    metadata: Dict[str, str]

    period: AddInvoiceItemPeriod

    price: str

    price_data: AddInvoiceItemPriceData

    quantity: int

    tax_rates: Union[SequenceNotStr[str], Literal[""]]


class AutomaticTaxLiability(TypedDict, total=False):
    type: Required[Literal["account", "self"]]

    account: str


class AutomaticTax(TypedDict, total=False):
    """Automatic tax settings for this subscription.

    We recommend you only include this parameter when the existing value is being changed.
    """

    enabled: Required[bool]

    liability: AutomaticTaxLiability


class BillingThresholdsBillingThresholdsParam(TypedDict, total=False):
    amount_gte: int

    reset_billing_cycle_anchor: bool


BillingThresholds: TypeAlias = Union[BillingThresholdsBillingThresholdsParam, Literal[""]]


class CancellationDetails(TypedDict, total=False):
    """Details about why this subscription was cancelled"""

    comment: Union[str, Literal[""]]

    feedback: Literal[
        "",
        "customer_service",
        "low_quality",
        "missing_features",
        "other",
        "switched_service",
        "too_complex",
        "too_expensive",
        "unused",
    ]


class DiscountsDiscountsList(TypedDict, total=False):
    coupon: str

    discount: str

    promotion_code: str


class InvoiceSettingsIssuer(TypedDict, total=False):
    type: Required[Literal["account", "self"]]

    account: str


class InvoiceSettings(TypedDict, total=False):
    """All invoices will be billed using the specified settings."""

    account_tax_ids: Union[SequenceNotStr[str], Literal[""]]

    issuer: InvoiceSettingsIssuer


class ItemBillingThresholdsItemBillingThresholdsParam(TypedDict, total=False):
    usage_gte: Required[int]


ItemBillingThresholds: TypeAlias = Union[ItemBillingThresholdsItemBillingThresholdsParam, Literal[""]]


class ItemDiscountsDiscountsList(TypedDict, total=False):
    coupon: str

    discount: str

    promotion_code: str


class ItemPriceDataRecurring(TypedDict, total=False):
    interval: Required[Literal["day", "month", "week", "year"]]

    interval_count: int


class ItemPriceData(TypedDict, total=False):
    currency: Required[str]

    product: Required[str]

    recurring: Required[ItemPriceDataRecurring]

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]

    unit_amount: int

    unit_amount_decimal: str


class Item(TypedDict, total=False):
    id: str

    billing_thresholds: ItemBillingThresholds

    clear_usage: bool

    deleted: bool

    discounts: Union[Iterable[ItemDiscountsDiscountsList], Literal[""]]

    metadata: Union[Dict[str, str], Literal[""]]

    price: str

    price_data: ItemPriceData

    quantity: int

    tax_rates: Union[SequenceNotStr[str], Literal[""]]


class PauseCollectionPauseCollectionParam(TypedDict, total=False):
    behavior: Required[Literal["keep_as_draft", "mark_uncollectible", "void"]]

    resumes_at: int


PauseCollection: TypeAlias = Union[PauseCollectionPauseCollectionParam, Literal[""]]


class PaymentSettingsPaymentMethodOptionsAcssDebitInvoicePaymentMethodOptionsParamMandateOptions(
    TypedDict, total=False
):
    transaction_type: Literal["business", "personal"]


class PaymentSettingsPaymentMethodOptionsAcssDebitInvoicePaymentMethodOptionsParam(TypedDict, total=False):
    mandate_options: PaymentSettingsPaymentMethodOptionsAcssDebitInvoicePaymentMethodOptionsParamMandateOptions

    verification_method: Literal["automatic", "instant", "microdeposits"]


PaymentSettingsPaymentMethodOptionsAcssDebit: TypeAlias = Union[
    PaymentSettingsPaymentMethodOptionsAcssDebitInvoicePaymentMethodOptionsParam, Literal[""]
]


class PaymentSettingsPaymentMethodOptionsBancontactInvoicePaymentMethodOptionsParam(TypedDict, total=False):
    preferred_language: Literal["de", "en", "fr", "nl"]


PaymentSettingsPaymentMethodOptionsBancontact: TypeAlias = Union[
    PaymentSettingsPaymentMethodOptionsBancontactInvoicePaymentMethodOptionsParam, Literal[""]
]


class PaymentSettingsPaymentMethodOptionsCardSubscriptionPaymentMethodOptionsParamMandateOptions(
    TypedDict, total=False
):
    amount: int

    amount_type: Literal["fixed", "maximum"]

    description: str


class PaymentSettingsPaymentMethodOptionsCardSubscriptionPaymentMethodOptionsParam(TypedDict, total=False):
    mandate_options: PaymentSettingsPaymentMethodOptionsCardSubscriptionPaymentMethodOptionsParamMandateOptions

    network: Literal[
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

    request_three_d_secure: Literal["any", "automatic", "challenge"]


PaymentSettingsPaymentMethodOptionsCard: TypeAlias = Union[
    PaymentSettingsPaymentMethodOptionsCardSubscriptionPaymentMethodOptionsParam, Literal[""]
]


class PaymentSettingsPaymentMethodOptionsCustomerBalanceInvoicePaymentMethodOptionsParamBankTransferEuBankTransfer(
    TypedDict, total=False
):
    country: Required[str]


class PaymentSettingsPaymentMethodOptionsCustomerBalanceInvoicePaymentMethodOptionsParamBankTransfer(
    TypedDict, total=False
):
    eu_bank_transfer: (
        PaymentSettingsPaymentMethodOptionsCustomerBalanceInvoicePaymentMethodOptionsParamBankTransferEuBankTransfer
    )

    type: str


class PaymentSettingsPaymentMethodOptionsCustomerBalanceInvoicePaymentMethodOptionsParam(TypedDict, total=False):
    bank_transfer: PaymentSettingsPaymentMethodOptionsCustomerBalanceInvoicePaymentMethodOptionsParamBankTransfer

    funding_type: str


PaymentSettingsPaymentMethodOptionsCustomerBalance: TypeAlias = Union[
    PaymentSettingsPaymentMethodOptionsCustomerBalanceInvoicePaymentMethodOptionsParam, Literal[""]
]


class PaymentSettingsPaymentMethodOptionsPaytoInvoicePaymentMethodOptionsParamMandateOptions(TypedDict, total=False):
    amount: int

    purpose: Literal[
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


class PaymentSettingsPaymentMethodOptionsPaytoInvoicePaymentMethodOptionsParam(TypedDict, total=False):
    mandate_options: PaymentSettingsPaymentMethodOptionsPaytoInvoicePaymentMethodOptionsParamMandateOptions


PaymentSettingsPaymentMethodOptionsPayto: TypeAlias = Union[
    PaymentSettingsPaymentMethodOptionsPaytoInvoicePaymentMethodOptionsParam, Literal[""]
]


class PaymentSettingsPaymentMethodOptionsUsBankAccountInvoicePaymentMethodOptionsParamFinancialConnectionsFilters(
    TypedDict, total=False
):
    account_subcategories: List[Literal["checking", "savings"]]


class PaymentSettingsPaymentMethodOptionsUsBankAccountInvoicePaymentMethodOptionsParamFinancialConnections(
    TypedDict, total=False
):
    filters: PaymentSettingsPaymentMethodOptionsUsBankAccountInvoicePaymentMethodOptionsParamFinancialConnectionsFilters

    permissions: List[Literal["balances", "ownership", "payment_method", "transactions"]]

    prefetch: List[Literal["balances", "ownership", "transactions"]]


class PaymentSettingsPaymentMethodOptionsUsBankAccountInvoicePaymentMethodOptionsParam(TypedDict, total=False):
    financial_connections: (
        PaymentSettingsPaymentMethodOptionsUsBankAccountInvoicePaymentMethodOptionsParamFinancialConnections
    )

    verification_method: Literal["automatic", "instant", "microdeposits"]


PaymentSettingsPaymentMethodOptionsUsBankAccount: TypeAlias = Union[
    PaymentSettingsPaymentMethodOptionsUsBankAccountInvoicePaymentMethodOptionsParam, Literal[""]
]


class PaymentSettingsPaymentMethodOptions(TypedDict, total=False):
    acss_debit: PaymentSettingsPaymentMethodOptionsAcssDebit

    bancontact: PaymentSettingsPaymentMethodOptionsBancontact

    card: PaymentSettingsPaymentMethodOptionsCard

    customer_balance: PaymentSettingsPaymentMethodOptionsCustomerBalance

    konbini: Union[Literal[""], object]

    payto: PaymentSettingsPaymentMethodOptionsPayto

    sepa_debit: Union[Literal[""], object]

    us_bank_account: PaymentSettingsPaymentMethodOptionsUsBankAccount


class PaymentSettings(TypedDict, total=False):
    """Payment settings to pass to invoices created by the subscription."""

    payment_method_options: PaymentSettingsPaymentMethodOptions

    payment_method_types: Union[
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
        ],
        Literal[""],
    ]

    save_default_payment_method: Literal["off", "on_subscription"]


class PendingInvoiceItemIntervalPendingInvoiceItemIntervalParams(TypedDict, total=False):
    interval: Required[Literal["day", "month", "week", "year"]]

    interval_count: int


PendingInvoiceItemInterval: TypeAlias = Union[PendingInvoiceItemIntervalPendingInvoiceItemIntervalParams, Literal[""]]


class TransferDataTransferDataSpecs(TypedDict, total=False):
    destination: Required[str]

    amount_percent: float


TransferData: TypeAlias = Union[TransferDataTransferDataSpecs, Literal[""]]


class TrialSettingsEndBehavior(TypedDict, total=False):
    missing_payment_method: Required[Literal["cancel", "create_invoice", "pause"]]


class TrialSettings(TypedDict, total=False):
    """Settings related to subscription trials."""

    end_behavior: Required[TrialSettingsEndBehavior]
