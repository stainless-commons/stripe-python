# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .shared import application
from .._models import BaseModel
from .tax_rate import TaxRate
from .shared.tax_code import TaxCode
from .custom_text_position import CustomTextPosition
from .shared.deleted_tax_id import DeletedTaxID
from .shared.deleted_application import DeletedApplication
from .shared.invoice_setting_custom_field import InvoiceSettingCustomField
from .shipping_rate_delivery_estimate_bound import ShippingRateDeliveryEstimateBound

__all__ = [
    "PaymentLinkCreateResponse",
    "AfterCompletion",
    "AfterCompletionHostedConfirmation",
    "AfterCompletionRedirect",
    "AutomaticTax",
    "CustomField",
    "CustomFieldLabel",
    "CustomFieldDropdown",
    "CustomFieldDropdownOption",
    "CustomFieldNumeric",
    "CustomFieldText",
    "CustomText",
    "PhoneNumberCollection",
    "ShippingOption",
    "ShippingOptionShippingRate",
    "ShippingOptionShippingRateShippingRate",
    "ShippingOptionShippingRateShippingRateDeliveryEstimate",
    "ShippingOptionShippingRateShippingRateFixedAmount",
    "ShippingOptionShippingRateShippingRateFixedAmountCurrencyOptions",
    "ShippingOptionShippingRateShippingRateTaxCode",
    "TaxIDCollection",
    "Application",
    "ConsentCollection",
    "ConsentCollectionPaymentMethodReuseAgreement",
    "InvoiceCreation",
    "InvoiceCreationInvoiceData",
    "InvoiceCreationInvoiceDataAccountTaxID",
    "InvoiceCreationInvoiceDataRenderingOptions",
    "LineItems",
    "LineItemsData",
    "LineItemsDataAdjustableQuantity",
    "LineItemsDataDiscount",
    "LineItemsDataTax",
    "NameCollection",
    "NameCollectionBusiness",
    "NameCollectionIndividual",
    "OnBehalfOf",
    "OptionalItem",
    "OptionalItemAdjustableQuantity",
    "PaymentIntentData",
    "Restrictions",
    "RestrictionsCompletedSessions",
    "ShippingAddressCollection",
    "SubscriptionData",
    "SubscriptionDataInvoiceSettings",
    "SubscriptionDataTrialSettings",
    "SubscriptionDataTrialSettingsEndBehavior",
    "TransferData",
    "TransferDataDestination",
]


class AfterCompletionHostedConfirmation(BaseModel):
    custom_message: Optional[str] = None
    """
    The custom message that is displayed to the customer after the purchase is
    complete.
    """


class AfterCompletionRedirect(BaseModel):
    url: str
    """The URL the customer will be redirected to after the purchase is complete."""


class AfterCompletion(BaseModel):
    type: Literal["hosted_confirmation", "redirect"]
    """The specified behavior after the purchase is complete."""

    hosted_confirmation: Optional[AfterCompletionHostedConfirmation] = None

    redirect: Optional[AfterCompletionRedirect] = None


class AutomaticTax(BaseModel):
    enabled: bool
    """If `true`, tax will be calculated automatically using the customer's location."""

    liability: Optional["ConnectAccountReference"] = None


class CustomFieldLabel(BaseModel):
    type: Literal["custom"]
    """The type of the label."""

    custom: Optional[str] = None
    """Custom text for the label, displayed to the customer. Up to 50 characters."""


class CustomFieldDropdownOption(BaseModel):
    label: str
    """The label for the option, displayed to the customer. Up to 100 characters."""

    value: str
    """
    The value for this option, not displayed to the customer, used by your
    integration to reconcile the option selected by the customer. Must be unique to
    this option, alphanumeric, and up to 100 characters.
    """


class CustomFieldDropdown(BaseModel):
    options: List[CustomFieldDropdownOption]
    """The options available for the customer to select. Up to 200 options allowed."""

    default_value: Optional[str] = None
    """The value that will pre-fill on the payment page."""


class CustomFieldNumeric(BaseModel):
    default_value: Optional[str] = None
    """The value that will pre-fill the field on the payment page."""

    maximum_length: Optional[int] = None
    """The maximum character length constraint for the customer's input."""

    minimum_length: Optional[int] = None
    """The minimum character length requirement for the customer's input."""


class CustomFieldText(BaseModel):
    default_value: Optional[str] = None
    """The value that will pre-fill the field on the payment page."""

    maximum_length: Optional[int] = None
    """The maximum character length constraint for the customer's input."""

    minimum_length: Optional[int] = None
    """The minimum character length requirement for the customer's input."""


class CustomField(BaseModel):
    key: str
    """String of your choice that your integration can use to reconcile this field.

    Must be unique to this field, alphanumeric, and up to 200 characters.
    """

    label: CustomFieldLabel

    optional: bool
    """
    Whether the customer is required to complete the field before completing the
    Checkout Session. Defaults to `false`.
    """

    type: Literal["dropdown", "numeric", "text"]
    """The type of the field."""

    dropdown: Optional[CustomFieldDropdown] = None

    numeric: Optional[CustomFieldNumeric] = None

    text: Optional[CustomFieldText] = None


class CustomText(BaseModel):
    after_submit: Optional[CustomTextPosition] = None

    shipping_address: Optional[CustomTextPosition] = None

    submit: Optional[CustomTextPosition] = None

    terms_of_service_acceptance: Optional[CustomTextPosition] = None


class PhoneNumberCollection(BaseModel):
    enabled: bool
    """If `true`, a phone number will be collected during checkout."""


class ShippingOptionShippingRateShippingRateDeliveryEstimate(BaseModel):
    maximum: Optional[ShippingRateDeliveryEstimateBound] = None

    minimum: Optional[ShippingRateDeliveryEstimateBound] = None


class ShippingOptionShippingRateShippingRateFixedAmountCurrencyOptions(BaseModel):
    amount: int
    """A non-negative integer in cents representing how much to charge."""

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of
    taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """


class ShippingOptionShippingRateShippingRateFixedAmount(BaseModel):
    amount: int
    """A non-negative integer in cents representing how much to charge."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    currency_options: Optional[Dict[str, ShippingOptionShippingRateShippingRateFixedAmountCurrencyOptions]] = None
    """Shipping rates defined in each available currency option.

    Each key must be a three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a
    [supported currency](https://stripe.com/docs/currencies).
    """


ShippingOptionShippingRateShippingRateTaxCode: TypeAlias = Union[str, TaxCode, None]


class ShippingOptionShippingRateShippingRate(BaseModel):
    """
    Shipping rates describe the price of shipping presented to your customers and
    applied to a purchase. For more information, see [Charge for shipping](https://docs.stripe.com/payments/during-payment/charge-shipping).
    """

    id: str
    """Unique identifier for the object."""

    active: bool
    """Whether the shipping rate can be used for new purchases. Defaults to `true`."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

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

    object: Literal["shipping_rate"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    type: Literal["fixed_amount"]
    """The type of calculation to use on the shipping rate."""

    delivery_estimate: Optional[ShippingOptionShippingRateShippingRateDeliveryEstimate] = None

    display_name: Optional[str] = None
    """The name of the shipping rate, meant to be displayable to the customer.

    This will appear on CheckoutSessions.
    """

    fixed_amount: Optional[ShippingOptionShippingRateShippingRateFixedAmount] = None

    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified"]] = None
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of
    taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """

    tax_code: Optional[ShippingOptionShippingRateShippingRateTaxCode] = None
    """A [tax code](https://docs.stripe.com/tax/tax-categories) ID.

    The Shipping tax code is `txcd_92010001`.
    """


ShippingOptionShippingRate: TypeAlias = Union[str, ShippingOptionShippingRateShippingRate]


class ShippingOption(BaseModel):
    shipping_amount: int
    """A non-negative integer in cents representing how much to charge."""

    shipping_rate: ShippingOptionShippingRate
    """The ID of the Shipping Rate to use for this shipping option."""


class TaxIDCollection(BaseModel):
    enabled: bool
    """Indicates whether tax ID collection is enabled for the session."""

    required: Literal["if_supported", "never"]


Application: TypeAlias = Union[str, application.Application, DeletedApplication, None]


class ConsentCollectionPaymentMethodReuseAgreement(BaseModel):
    position: Literal["auto", "hidden"]
    """
    Determines the position and visibility of the payment method reuse agreement in
    the UI. When set to `auto`, Stripe's defaults will be used.

    When set to `hidden`, the payment method reuse agreement text will always be
    hidden in the UI.
    """


class ConsentCollection(BaseModel):
    payment_method_reuse_agreement: Optional[ConsentCollectionPaymentMethodReuseAgreement] = None

    promotions: Optional[Literal["auto", "none"]] = None
    """
    If set to `auto`, enables the collection of customer consent for promotional
    communications.
    """

    terms_of_service: Optional[Literal["none", "required"]] = None
    """
    If set to `required`, it requires cutomers to accept the terms of service before
    being able to pay. If set to `none`, customers won't be shown a checkbox to
    accept the terms of service.
    """


InvoiceCreationInvoiceDataAccountTaxID: TypeAlias = Union[str, "TaxID", DeletedTaxID]


class InvoiceCreationInvoiceDataRenderingOptions(BaseModel):
    amount_tax_display: Optional[str] = None
    """
    How line-item prices and amounts will be displayed with respect to tax on
    invoice PDFs.
    """

    template: Optional[str] = None
    """ID of the invoice rendering template to be used for the generated invoice."""


class InvoiceCreationInvoiceData(BaseModel):
    account_tax_ids: Optional[List[InvoiceCreationInvoiceDataAccountTaxID]] = None
    """The account tax IDs associated with the invoice."""

    custom_fields: Optional[List[InvoiceSettingCustomField]] = None
    """A list of up to 4 custom fields to be displayed on the invoice."""

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    footer: Optional[str] = None
    """Footer to be displayed on the invoice."""

    issuer: Optional["ConnectAccountReference"] = None

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    rendering_options: Optional[InvoiceCreationInvoiceDataRenderingOptions] = None


class InvoiceCreation(BaseModel):
    enabled: bool
    """Enable creating an invoice on successful payment."""

    invoice_data: Optional[InvoiceCreationInvoiceData] = None


class LineItemsDataAdjustableQuantity(BaseModel):
    enabled: bool

    maximum: Optional[int] = None

    minimum: Optional[int] = None


class LineItemsDataDiscount(BaseModel):
    amount: int
    """The amount discounted."""

    discount: "Discount"
    """
    A discount represents the actual application of a
    [coupon](https://api.stripe.com#coupons) or
    [promotion code](https://api.stripe.com#promotion_codes). It contains
    information about when the discount began, when it will end, and what it is
    applied to.

    Related guide:
    [Applying discounts to subscriptions](https://docs.stripe.com/billing/subscriptions/discounts)
    """


class LineItemsDataTax(BaseModel):
    amount: int
    """Amount of tax applied for this rate."""

    rate: TaxRate
    """
    Tax rates can be applied to [invoices](/invoicing/taxes/tax-rates),
    [subscriptions](/billing/taxes/tax-rates) and
    [Checkout Sessions](/payments/checkout/use-manual-tax-rates) to collect tax.

    Related guide: [Tax rates](/billing/taxes/tax-rates)
    """

    taxability_reason: Optional[
        Literal[
            "customer_exempt",
            "not_collecting",
            "not_subject_to_tax",
            "not_supported",
            "portion_product_exempt",
            "portion_reduced_rated",
            "portion_standard_rated",
            "product_exempt",
            "product_exempt_holiday",
            "proportionally_rated",
            "reduced_rated",
            "reverse_charge",
            "standard_rated",
            "taxable_basis_reduced",
            "zero_rated",
        ]
    ] = None
    """The reasoning behind this tax, for example, if the product is tax exempt.

    The possible values for this field may be extended as new tax rules are
    supported.
    """

    taxable_amount: Optional[int] = None
    """The amount on which tax is calculated, in cents (or local equivalent)."""


class LineItemsData(BaseModel):
    """A line item."""

    id: str
    """Unique identifier for the object."""

    amount_discount: int
    """Total discount amount applied. If no discounts were applied, defaults to 0."""

    amount_subtotal: int
    """Total before any discounts or taxes are applied."""

    amount_tax: int
    """Total tax amount applied. If no tax was applied, defaults to 0."""

    amount_total: int
    """Total after discounts and taxes."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    object: Literal["item"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    adjustable_quantity: Optional[LineItemsDataAdjustableQuantity] = None

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users. Defaults to product name.
    """

    discounts: Optional[List[LineItemsDataDiscount]] = None
    """The discounts applied to the line item."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    price: Optional["Price"] = None
    """
    Prices define the unit cost, currency, and (optional) billing cycle for both
    recurring and one-time purchases of products.
    [Products](https://api.stripe.com#products) help you track inventory or
    provisioning, and prices help you track payment terms. Different physical goods
    or levels of service should be represented by products, and pricing options
    should be represented by prices. This approach lets you change prices without
    having to change your provisioning scheme.

    For example, you might have a single "gold" product that has prices for
    $10/month, $100/year, and €9 once.

    Related guides:
    [Set up a subscription](https://docs.stripe.com/billing/subscriptions/set-up-subscription),
    [create an invoice](https://docs.stripe.com/billing/invoices/create), and more
    about [products and prices](https://docs.stripe.com/products-prices/overview).
    """

    quantity: Optional[int] = None
    """The quantity of products being purchased."""

    taxes: Optional[List[LineItemsDataTax]] = None
    """The taxes applied to the line item."""


class LineItems(BaseModel):
    """The line items representing what is being sold."""

    data: List[LineItemsData]
    """Details about each object."""

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


class NameCollectionBusiness(BaseModel):
    enabled: bool
    """Indicates whether business name collection is enabled for the payment link."""

    optional: bool
    """Whether the customer is required to complete the field before checking out.

    Defaults to `false`.
    """


class NameCollectionIndividual(BaseModel):
    enabled: bool
    """Indicates whether individual name collection is enabled for the payment link."""

    optional: bool
    """Whether the customer is required to complete the field before checking out.

    Defaults to `false`.
    """


class NameCollection(BaseModel):
    business: Optional[NameCollectionBusiness] = None

    individual: Optional[NameCollectionIndividual] = None


OnBehalfOf: TypeAlias = Union[str, "Account", None]


class OptionalItemAdjustableQuantity(BaseModel):
    enabled: bool
    """Set to true if the quantity can be adjusted to any non-negative integer."""

    maximum: Optional[int] = None
    """The maximum quantity of this item the customer can purchase.

    By default this value is 99.
    """

    minimum: Optional[int] = None
    """
    The minimum quantity of this item the customer must purchase, if they choose to
    purchase it. Because this item is optional, the customer will always be able to
    remove it from their order, even if the `minimum` configured here is greater
    than 0. By default this value is 0.
    """


class OptionalItem(BaseModel):
    price: str

    quantity: int

    adjustable_quantity: Optional[OptionalItemAdjustableQuantity] = None


class PaymentIntentData(BaseModel):
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that will set
    metadata on [Payment Intents](https://docs.stripe.com/api/payment_intents)
    generated from this payment link.
    """

    capture_method: Optional[Literal["automatic", "automatic_async", "manual"]] = None
    """Indicates when the funds will be captured from the customer's account."""

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    setup_future_usage: Optional[Literal["off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with the payment method
    collected during checkout.
    """

    statement_descriptor: Optional[str] = None
    """
    For a non-card payment, information about the charge that appears on the
    customer's statement when this payment succeeds in creating a charge.
    """

    statement_descriptor_suffix: Optional[str] = None
    """
    For a card payment, information about the charge that appears on the customer's
    statement when this payment succeeds in creating a charge. Concatenated with the
    account's statement descriptor prefix to form the complete statement descriptor.
    """

    transfer_group: Optional[str] = None
    """A string that identifies the resulting payment as part of a group.

    See the PaymentIntents
    [use case for connected accounts](https://docs.stripe.com/connect/separate-charges-and-transfers)
    for details.
    """


class RestrictionsCompletedSessions(BaseModel):
    count: int
    """
    The current number of checkout sessions that have been completed on the payment
    link which count towards the `completed_sessions` restriction to be met.
    """

    limit: int
    """
    The maximum number of checkout sessions that can be completed for the
    `completed_sessions` restriction to be met.
    """


class Restrictions(BaseModel):
    completed_sessions: RestrictionsCompletedSessions


class ShippingAddressCollection(BaseModel):
    allowed_countries: List[
        Literal[
            "AC",
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AO",
            "AQ",
            "AR",
            "AT",
            "AU",
            "AW",
            "AX",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BQ",
            "BR",
            "BS",
            "BT",
            "BV",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CV",
            "CW",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "EH",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GF",
            "GG",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GP",
            "GQ",
            "GR",
            "GS",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IO",
            "IQ",
            "IS",
            "IT",
            "JE",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MQ",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PS",
            "PT",
            "PY",
            "QA",
            "RE",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SJ",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "SS",
            "ST",
            "SV",
            "SX",
            "SZ",
            "TA",
            "TC",
            "TD",
            "TF",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VN",
            "VU",
            "WF",
            "WS",
            "XK",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
            "ZZ",
        ]
    ]
    """
    An array of two-letter ISO country codes representing which countries Checkout
    should provide as options for shipping locations. Unsupported country codes:
    `AS, CX, CC, CU, HM, IR, KP, MH, FM, NF, MP, PW, SD, SY, UM, VI`.
    """


class SubscriptionDataInvoiceSettings(BaseModel):
    issuer: "ConnectAccountReference"


class SubscriptionDataTrialSettingsEndBehavior(BaseModel):
    """Defines how a subscription behaves when a free trial ends."""

    missing_payment_method: Literal["cancel", "create_invoice", "pause"]
    """
    Indicates how the subscription should change when the trial ends if the user did
    not provide a payment method.
    """


class SubscriptionDataTrialSettings(BaseModel):
    """Configures how this subscription behaves during the trial period."""

    end_behavior: SubscriptionDataTrialSettingsEndBehavior
    """Defines how a subscription behaves when a free trial ends."""


class SubscriptionData(BaseModel):
    invoice_settings: SubscriptionDataInvoiceSettings

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that will set
    metadata on [Subscriptions](https://docs.stripe.com/api/subscriptions) generated
    from this payment link.
    """

    description: Optional[str] = None
    """The subscription's description, meant to be displayable to the customer.

    Use this field to optionally store an explanation of the subscription for
    rendering in Stripe surfaces and certain local payment methods UIs.
    """

    trial_period_days: Optional[int] = None
    """
    Integer representing the number of trial period days before the customer is
    charged for the first time.
    """

    trial_settings: Optional[SubscriptionDataTrialSettings] = None
    """Configures how this subscription behaves during the trial period."""


TransferDataDestination: TypeAlias = Union[str, "Account"]


class TransferData(BaseModel):
    destination: TransferDataDestination
    """The connected account receiving the transfer."""

    amount: Optional[int] = None
    """
    The amount in cents (or local equivalent) that will be transferred to the
    destination account. By default, the entire amount is transferred to the
    destination.
    """


class PaymentLinkCreateResponse(BaseModel):
    """
    A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times.

    When a customer opens a payment link it will open a new [checkout session](https://docs.stripe.com/api/checkout/sessions) to render the payment page. You can use [checkout session events](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed) to track payments through payment links.

    Related guide: [Payment Links API](https://docs.stripe.com/payment-links)
    """

    id: str
    """Unique identifier for the object."""

    active: bool
    """Whether the payment link's `url` is active.

    If `false`, customers visiting the URL will be shown a page saying that the link
    has been deactivated.
    """

    after_completion: AfterCompletion

    allow_promotion_codes: bool
    """Whether user redeemable promotion codes are enabled."""

    automatic_tax: AutomaticTax

    billing_address_collection: Literal["auto", "required"]
    """Configuration for collecting the customer's billing address.

    Defaults to `auto`.
    """

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    custom_fields: List[CustomField]
    """Collect additional information from your customer using custom fields.

    Up to 3 fields are supported. You can't set this parameter if `ui_mode` is
    `custom`.
    """

    custom_text: CustomText

    customer_creation: Literal["always", "if_required"]
    """Configuration for Customer creation during checkout."""

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

    object: Literal["payment_link"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    payment_method_collection: Literal["always", "if_required"]
    """Configuration for collecting a payment method during checkout.

    Defaults to `always`.
    """

    phone_number_collection: PhoneNumberCollection

    shipping_options: List[ShippingOption]
    """The shipping rate options applied to the session."""

    submit_type: Literal["auto", "book", "donate", "pay", "subscribe"]
    """
    Indicates the type of transaction being performed which customizes relevant text
    on the page, such as the submit button.
    """

    tax_id_collection: TaxIDCollection

    url: str
    """The public URL that can be shared with customers."""

    application: Optional[Application] = None
    """The ID of the Connect application that created the Payment Link."""

    application_fee_amount: Optional[int] = None
    """
    The amount of the application fee (if any) that will be requested to be applied
    to the payment and transferred to the application owner's Stripe account.
    """

    application_fee_percent: Optional[float] = None
    """
    This represents the percentage of the subscription invoice total that will be
    transferred to the application owner's Stripe account.
    """

    consent_collection: Optional[ConsentCollection] = None

    inactive_message: Optional[str] = None
    """
    The custom message to be displayed to a customer when a payment link is no
    longer active.
    """

    invoice_creation: Optional[InvoiceCreation] = None

    line_items: Optional[LineItems] = None
    """The line items representing what is being sold."""

    name_collection: Optional[NameCollection] = None

    on_behalf_of: Optional[OnBehalfOf] = None
    """The account on behalf of which to charge.

    See the
    [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts)
    for details.
    """

    optional_items: Optional[List[OptionalItem]] = None
    """The optional items presented to the customer at checkout."""

    payment_intent_data: Optional[PaymentIntentData] = None

    payment_method_types: Optional[
        List[
            Literal[
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "billie",
                "blik",
                "boleto",
                "card",
                "cashapp",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "klarna",
                "konbini",
                "link",
                "mb_way",
                "mobilepay",
                "multibanco",
                "oxxo",
                "p24",
                "pay_by_bank",
                "paynow",
                "paypal",
                "payto",
                "pix",
                "promptpay",
                "satispay",
                "sepa_debit",
                "sofort",
                "swish",
                "twint",
                "us_bank_account",
                "wechat_pay",
                "zip",
            ]
        ]
    ] = None
    """The list of payment method types that customers can use.

    When `null`, Stripe will dynamically show relevant payment methods you've
    enabled in your
    [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
    """

    restrictions: Optional[Restrictions] = None

    shipping_address_collection: Optional[ShippingAddressCollection] = None

    subscription_data: Optional[SubscriptionData] = None

    transfer_data: Optional[TransferData] = None


from .price import Price
from .tax_id import TaxID
from .account import Account
from .discount import Discount
from .connect_account_reference import ConnectAccountReference
