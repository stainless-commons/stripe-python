# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "PaymentLinkCreateParams",
    "LineItem",
    "LineItemAdjustableQuantity",
    "LineItemPriceData",
    "LineItemPriceDataProductData",
    "LineItemPriceDataRecurring",
    "AfterCompletion",
    "AfterCompletionHostedConfirmation",
    "AfterCompletionRedirect",
    "AutomaticTax",
    "AutomaticTaxLiability",
    "ConsentCollection",
    "ConsentCollectionPaymentMethodReuseAgreement",
    "CustomField",
    "CustomFieldLabel",
    "CustomFieldDropdown",
    "CustomFieldDropdownOption",
    "CustomFieldNumeric",
    "CustomFieldText",
    "CustomText",
    "CustomTextAfterSubmit",
    "CustomTextAfterSubmitCustomTextPositionParam",
    "CustomTextShippingAddress",
    "CustomTextShippingAddressCustomTextPositionParam",
    "CustomTextSubmit",
    "CustomTextSubmitCustomTextPositionParam",
    "CustomTextTermsOfServiceAcceptance",
    "CustomTextTermsOfServiceAcceptanceCustomTextPositionParam",
    "InvoiceCreation",
    "InvoiceCreationInvoiceData",
    "InvoiceCreationInvoiceDataCustomFieldsCustomFieldsList",
    "InvoiceCreationInvoiceDataIssuer",
    "InvoiceCreationInvoiceDataRenderingOptions",
    "InvoiceCreationInvoiceDataRenderingOptionsCheckoutRenderingOptionsParam",
    "NameCollection",
    "NameCollectionBusiness",
    "NameCollectionIndividual",
    "OptionalItem",
    "OptionalItemAdjustableQuantity",
    "PaymentIntentData",
    "PhoneNumberCollection",
    "Restrictions",
    "RestrictionsCompletedSessions",
    "ShippingAddressCollection",
    "ShippingOption",
    "SubscriptionData",
    "SubscriptionDataInvoiceSettings",
    "SubscriptionDataInvoiceSettingsIssuer",
    "SubscriptionDataTrialSettings",
    "SubscriptionDataTrialSettingsEndBehavior",
    "TaxIDCollection",
    "TransferData",
]


class PaymentLinkCreateParams(TypedDict, total=False):
    line_items: Required[Iterable[LineItem]]
    """The line items representing what is being sold.

    Each line item represents an item being sold. Up to 20 line items are supported.
    """

    after_completion: AfterCompletion
    """Behavior after the purchase is complete."""

    allow_promotion_codes: bool
    """Enables user redeemable promotion codes."""

    application_fee_amount: int
    """
    The amount of the application fee (if any) that will be requested to be applied
    to the payment and transferred to the application owner's Stripe account. Can
    only be applied when there are no line items with recurring prices.
    """

    application_fee_percent: float
    """A non-negative decimal between 0 and 100, with at most two decimal places.

    This represents the percentage of the subscription invoice total that will be
    transferred to the application owner's Stripe account. There must be at least 1
    line item with a recurring price to use this field.
    """

    automatic_tax: AutomaticTax
    """Configuration for automatic tax collection."""

    billing_address_collection: Literal["auto", "required"]
    """Configuration for collecting the customer's billing address.

    Defaults to `auto`.
    """

    consent_collection: ConsentCollection
    """Configure fields to gather active consent from customers."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)
    and supported by each line item's price.
    """

    custom_fields: Iterable[CustomField]
    """Collect additional information from your customer using custom fields.

    Up to 3 fields are supported. You can't set this parameter if `ui_mode` is
    `custom`.
    """

    custom_text: CustomText
    """Display additional text for your customers using custom text.

    You can't set this parameter if `ui_mode` is `custom`.
    """

    customer_creation: Literal["always", "if_required"]
    """
    Configures whether
    [checkout sessions](https://docs.stripe.com/api/checkout/sessions) created by
    this payment link create a [Customer](https://docs.stripe.com/api/customers).
    """

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    inactive_message: str
    """
    The custom message to be displayed to a customer when a payment link is no
    longer active.
    """

    invoice_creation: InvoiceCreation
    """Generate a post-purchase Invoice for one-time payments."""

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Individual keys can be unset by posting an
    empty value to them. All keys can be unset by posting an empty value to
    `metadata`. Metadata associated with this Payment Link will automatically be
    copied to [checkout sessions](https://docs.stripe.com/api/checkout/sessions)
    created by this payment link.
    """

    name_collection: NameCollection
    """Controls settings applied for collecting the customer's name."""

    on_behalf_of: str
    """The account on behalf of which to charge."""

    optional_items: Iterable[OptionalItem]
    """A list of optional items the customer can add to their order at checkout.

    Use this parameter to pass one-time or recurring
    [Prices](https://docs.stripe.com/api/prices). There is a maximum of 10 optional
    items allowed on a payment link, and the existing limits on the number of line
    items allowed on a payment link apply to the combined number of line items and
    optional items. There is a maximum of 20 combined line items and optional items.
    """

    payment_intent_data: PaymentIntentData
    """
    A subset of parameters to be passed to PaymentIntent creation for Checkout
    Sessions in `payment` mode.
    """

    payment_method_collection: Literal["always", "if_required"]
    """Specify whether Checkout should collect a payment method.

    When set to `if_required`, Checkout will not collect a payment method when the
    total due for the session is 0.This may occur if the Checkout Session includes a
    free trial or a discount.

    Can only be set in `subscription` mode. Defaults to `always`.

    If you'd like information on how to collect a payment method outside of
    Checkout, read the guide on
    [configuring subscriptions with a free trial](https://docs.stripe.com/payments/checkout/free-trials).
    """

    payment_method_types: List[
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
    """The list of payment method types that customers can use.

    If no value is passed, Stripe will dynamically show relevant payment methods
    from your
    [payment method settings](https://dashboard.stripe.com/settings/payment_methods)
    (20+ payment methods
    [supported](https://docs.stripe.com/payments/payment-methods/integration-options#payment-method-product-support)).
    """

    phone_number_collection: PhoneNumberCollection
    """Controls phone number collection settings during checkout.

    We recommend that you review your privacy policy and check with your legal
    contacts.
    """

    restrictions: Restrictions
    """Settings that restrict the usage of a payment link."""

    shipping_address_collection: ShippingAddressCollection
    """Configuration for collecting the customer's shipping address."""

    shipping_options: Iterable[ShippingOption]
    """
    The shipping rate options to apply to
    [checkout sessions](https://docs.stripe.com/api/checkout/sessions) created by
    this payment link.
    """

    submit_type: Literal["auto", "book", "donate", "pay", "subscribe"]
    """
    Describes the type of transaction being performed in order to customize relevant
    text on the page, such as the submit button. Changing this value will also
    affect the hostname in the
    [url](https://docs.stripe.com/api/payment_links/payment_links/object#url)
    property (example: `donate.stripe.com`).
    """

    subscription_data: SubscriptionData
    """When creating a subscription, the specified configuration data will be used.

    There must be at least one line item with a recurring price to use
    `subscription_data`.
    """

    tax_id_collection: TaxIDCollection
    """Controls tax ID collection during checkout."""

    transfer_data: TransferData
    """
    The account (if any) the payments will be attributed to for tax reporting, and
    where funds from each payment will be transferred to.
    """


class LineItemAdjustableQuantity(TypedDict, total=False):
    enabled: Required[bool]

    maximum: int

    minimum: int


class LineItemPriceDataProductData(TypedDict, total=False):
    name: Required[str]

    description: str

    images: SequenceNotStr[str]

    metadata: Dict[str, str]

    tax_code: str

    unit_label: str


class LineItemPriceDataRecurring(TypedDict, total=False):
    interval: Required[Literal["day", "month", "week", "year"]]

    interval_count: int


class LineItemPriceData(TypedDict, total=False):
    currency: Required[str]

    product: str

    product_data: LineItemPriceDataProductData

    recurring: LineItemPriceDataRecurring

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]

    unit_amount: int

    unit_amount_decimal: str


class LineItem(TypedDict, total=False):
    quantity: Required[int]

    adjustable_quantity: LineItemAdjustableQuantity

    price: str

    price_data: LineItemPriceData


class AfterCompletionHostedConfirmation(TypedDict, total=False):
    custom_message: str


class AfterCompletionRedirect(TypedDict, total=False):
    url: Required[str]


class AfterCompletion(TypedDict, total=False):
    """Behavior after the purchase is complete."""

    type: Required[Literal["hosted_confirmation", "redirect"]]

    hosted_confirmation: AfterCompletionHostedConfirmation

    redirect: AfterCompletionRedirect


class AutomaticTaxLiability(TypedDict, total=False):
    type: Required[Literal["account", "self"]]

    account: str


class AutomaticTax(TypedDict, total=False):
    """Configuration for automatic tax collection."""

    enabled: Required[bool]

    liability: AutomaticTaxLiability


class ConsentCollectionPaymentMethodReuseAgreement(TypedDict, total=False):
    position: Required[Literal["auto", "hidden"]]


class ConsentCollection(TypedDict, total=False):
    """Configure fields to gather active consent from customers."""

    payment_method_reuse_agreement: ConsentCollectionPaymentMethodReuseAgreement

    promotions: Literal["auto", "none"]

    terms_of_service: Literal["none", "required"]


class CustomFieldLabel(TypedDict, total=False):
    custom: Required[str]

    type: Required[Literal["custom"]]


class CustomFieldDropdownOption(TypedDict, total=False):
    label: Required[str]

    value: Required[str]


class CustomFieldDropdown(TypedDict, total=False):
    options: Required[Iterable[CustomFieldDropdownOption]]

    default_value: str


class CustomFieldNumeric(TypedDict, total=False):
    default_value: str

    maximum_length: int

    minimum_length: int


class CustomFieldText(TypedDict, total=False):
    default_value: str

    maximum_length: int

    minimum_length: int


class CustomField(TypedDict, total=False):
    key: Required[str]

    label: Required[CustomFieldLabel]

    type: Required[Literal["dropdown", "numeric", "text"]]

    dropdown: CustomFieldDropdown

    numeric: CustomFieldNumeric

    optional: bool

    text: CustomFieldText


class CustomTextAfterSubmitCustomTextPositionParam(TypedDict, total=False):
    message: Required[str]


CustomTextAfterSubmit: TypeAlias = Union[CustomTextAfterSubmitCustomTextPositionParam, Literal[""]]


class CustomTextShippingAddressCustomTextPositionParam(TypedDict, total=False):
    message: Required[str]


CustomTextShippingAddress: TypeAlias = Union[CustomTextShippingAddressCustomTextPositionParam, Literal[""]]


class CustomTextSubmitCustomTextPositionParam(TypedDict, total=False):
    message: Required[str]


CustomTextSubmit: TypeAlias = Union[CustomTextSubmitCustomTextPositionParam, Literal[""]]


class CustomTextTermsOfServiceAcceptanceCustomTextPositionParam(TypedDict, total=False):
    message: Required[str]


CustomTextTermsOfServiceAcceptance: TypeAlias = Union[
    CustomTextTermsOfServiceAcceptanceCustomTextPositionParam, Literal[""]
]


class CustomText(TypedDict, total=False):
    """Display additional text for your customers using custom text.

    You can't set this parameter if `ui_mode` is `custom`.
    """

    after_submit: CustomTextAfterSubmit

    shipping_address: CustomTextShippingAddress

    submit: CustomTextSubmit

    terms_of_service_acceptance: CustomTextTermsOfServiceAcceptance


class InvoiceCreationInvoiceDataCustomFieldsCustomFieldsList(TypedDict, total=False):
    name: Required[str]

    value: Required[str]


class InvoiceCreationInvoiceDataIssuer(TypedDict, total=False):
    type: Required[Literal["account", "self"]]

    account: str


class InvoiceCreationInvoiceDataRenderingOptionsCheckoutRenderingOptionsParam(TypedDict, total=False):
    amount_tax_display: Literal["", "exclude_tax", "include_inclusive_tax"]

    template: str


InvoiceCreationInvoiceDataRenderingOptions: TypeAlias = Union[
    InvoiceCreationInvoiceDataRenderingOptionsCheckoutRenderingOptionsParam, Literal[""]
]


class InvoiceCreationInvoiceData(TypedDict, total=False):
    account_tax_ids: Union[SequenceNotStr[str], Literal[""]]

    custom_fields: Union[Iterable[InvoiceCreationInvoiceDataCustomFieldsCustomFieldsList], Literal[""]]

    description: str

    footer: str

    issuer: InvoiceCreationInvoiceDataIssuer

    metadata: Union[Dict[str, str], Literal[""]]

    rendering_options: InvoiceCreationInvoiceDataRenderingOptions


class InvoiceCreation(TypedDict, total=False):
    """Generate a post-purchase Invoice for one-time payments."""

    enabled: Required[bool]

    invoice_data: InvoiceCreationInvoiceData


class NameCollectionBusiness(TypedDict, total=False):
    enabled: Required[bool]

    optional: bool


class NameCollectionIndividual(TypedDict, total=False):
    enabled: Required[bool]

    optional: bool


class NameCollection(TypedDict, total=False):
    """Controls settings applied for collecting the customer's name."""

    business: NameCollectionBusiness

    individual: NameCollectionIndividual


class OptionalItemAdjustableQuantity(TypedDict, total=False):
    enabled: Required[bool]

    maximum: int

    minimum: int


class OptionalItem(TypedDict, total=False):
    price: Required[str]

    quantity: Required[int]

    adjustable_quantity: OptionalItemAdjustableQuantity


class PaymentIntentData(TypedDict, total=False):
    """
    A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
    """

    capture_method: Literal["automatic", "automatic_async", "manual"]

    description: str

    metadata: Dict[str, str]

    setup_future_usage: Literal["off_session", "on_session"]

    statement_descriptor: str

    statement_descriptor_suffix: str

    transfer_group: str


class PhoneNumberCollection(TypedDict, total=False):
    """Controls phone number collection settings during checkout.

    We recommend that you review your privacy policy and check with your legal contacts.
    """

    enabled: Required[bool]


class RestrictionsCompletedSessions(TypedDict, total=False):
    limit: Required[int]


class Restrictions(TypedDict, total=False):
    """Settings that restrict the usage of a payment link."""

    completed_sessions: Required[RestrictionsCompletedSessions]


class ShippingAddressCollection(TypedDict, total=False):
    """Configuration for collecting the customer's shipping address."""

    allowed_countries: Required[
        List[
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
    ]


class ShippingOption(TypedDict, total=False):
    shipping_rate: str


class SubscriptionDataInvoiceSettingsIssuer(TypedDict, total=False):
    type: Required[Literal["account", "self"]]

    account: str


class SubscriptionDataInvoiceSettings(TypedDict, total=False):
    issuer: SubscriptionDataInvoiceSettingsIssuer


class SubscriptionDataTrialSettingsEndBehavior(TypedDict, total=False):
    missing_payment_method: Required[Literal["cancel", "create_invoice", "pause"]]


class SubscriptionDataTrialSettings(TypedDict, total=False):
    end_behavior: Required[SubscriptionDataTrialSettingsEndBehavior]


class SubscriptionData(TypedDict, total=False):
    """When creating a subscription, the specified configuration data will be used.

    There must be at least one line item with a recurring price to use `subscription_data`.
    """

    description: str

    invoice_settings: SubscriptionDataInvoiceSettings

    metadata: Dict[str, str]

    trial_period_days: int

    trial_settings: SubscriptionDataTrialSettings


class TaxIDCollection(TypedDict, total=False):
    """Controls tax ID collection during checkout."""

    enabled: Required[bool]

    required: Literal["if_supported", "never"]


class TransferData(TypedDict, total=False):
    """
    The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to.
    """

    destination: Required[str]

    amount: int
