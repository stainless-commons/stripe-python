# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "InvoiceCreateParams",
    "AutomaticTax",
    "AutomaticTaxLiability",
    "CustomFieldsCustomFieldsList",
    "DiscountsDiscountsList",
    "FromInvoice",
    "Issuer",
    "PaymentSettings",
    "PaymentSettingsPaymentMethodOptions",
    "PaymentSettingsPaymentMethodOptionsAcssDebit",
    "PaymentSettingsPaymentMethodOptionsAcssDebitInvoicePaymentMethodOptionsParam",
    "PaymentSettingsPaymentMethodOptionsAcssDebitInvoicePaymentMethodOptionsParamMandateOptions",
    "PaymentSettingsPaymentMethodOptionsBancontact",
    "PaymentSettingsPaymentMethodOptionsBancontactInvoicePaymentMethodOptionsParam",
    "PaymentSettingsPaymentMethodOptionsCard",
    "PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParam",
    "PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParamInstallments",
    "PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParamInstallmentsPlan",
    "PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParamInstallmentsPlanInstallmentPlan",
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
    "Rendering",
    "RenderingPdf",
    "ShippingCost",
    "ShippingCostShippingRateData",
    "ShippingCostShippingRateDataDeliveryEstimate",
    "ShippingCostShippingRateDataDeliveryEstimateMaximum",
    "ShippingCostShippingRateDataDeliveryEstimateMinimum",
    "ShippingCostShippingRateDataFixedAmount",
    "ShippingCostShippingRateDataFixedAmountCurrencyOptions",
    "ShippingDetails",
    "ShippingDetailsAddress",
    "TransferData",
]


class InvoiceCreateParams(TypedDict, total=False):
    account_tax_ids: Union[SequenceNotStr[str], Literal[""]]
    """The account tax IDs associated with the invoice.

    Only editable when the invoice is a draft.
    """

    application_fee_amount: int
    """
    A fee in cents (or local equivalent) that will be applied to the invoice and
    transferred to the application owner's Stripe account. The request must be made
    with an OAuth key or the Stripe-Account header in order to take an application
    fee. For more information, see the application fees
    [documentation](https://docs.stripe.com/billing/invoices/connect#collecting-fees).
    """

    auto_advance: bool
    """
    Controls whether Stripe performs
    [automatic collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
    of the invoice. If `false`, the invoice's state doesn't automatically advance
    without an explicit action. Defaults to false.
    """

    automatic_tax: AutomaticTax
    """Settings for automatic tax lookup for this invoice."""

    automatically_finalizes_at: int
    """
    The time when this invoice should be scheduled to finalize (up to 5 years in the
    future). The invoice is finalized at this time if it's still in draft state.
    """

    collection_method: Literal["charge_automatically", "send_invoice"]
    """Either `charge_automatically`, or `send_invoice`.

    When charging automatically, Stripe will attempt to pay this invoice using the
    default source attached to the customer. When sending an invoice, Stripe will
    email this invoice to the customer with payment instructions. Defaults to
    `charge_automatically`.
    """

    currency: str
    """The currency to create this invoice in.

    Defaults to that of `customer` if not specified.
    """

    custom_fields: Union[Iterable[CustomFieldsCustomFieldsList], Literal[""]]
    """A list of up to 4 custom fields to be displayed on the invoice."""

    customer: str
    """The ID of the customer to bill."""

    customer_account: str
    """The ID of the account to bill."""

    days_until_due: int
    """The number of days from when the invoice is created until it is due.

    Valid only for invoices where `collection_method=send_invoice`.
    """

    default_payment_method: str
    """ID of the default payment method for the invoice.

    It must belong to the customer associated with the invoice. If not set, defaults
    to the subscription's default payment method, if any, or to the default payment
    method in the customer's invoice settings.
    """

    default_source: str
    """ID of the default payment source for the invoice.

    It must belong to the customer associated with the invoice and be in a
    chargeable state. If not set, defaults to the subscription's default source, if
    any, or to the customer's default source.
    """

    default_tax_rates: SequenceNotStr[str]
    """
    The tax rates that will apply to any line item that does not have `tax_rates`
    set.
    """

    description: str
    """An arbitrary string attached to the object.

    Often useful for displaying to users. Referenced as 'memo' in the Dashboard.
    """

    discounts: Union[Iterable[DiscountsDiscountsList], Literal[""]]
    """The coupons and promotion codes to redeem into discounts for the invoice.

    If not specified, inherits the discount from the invoice's customer. Pass an
    empty string to avoid inheriting any discounts.
    """

    due_date: int
    """The date on which payment for this invoice is due.

    Valid only for invoices where `collection_method=send_invoice`.
    """

    effective_at: int
    """The date when this invoice is in effect.

    Same as `finalized_at` unless overwritten. When defined, this value replaces the
    system-generated 'Date of issue' printed on the invoice PDF and receipt.
    """

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    footer: str
    """Footer to be displayed on the invoice."""

    from_invoice: FromInvoice
    """Revise an existing invoice.

    The new invoice will be created in `status=draft`. See the
    [revision documentation](https://docs.stripe.com/invoicing/invoice-revisions)
    for more details.
    """

    issuer: Issuer
    """The connected account that issues the invoice.

    The invoice is presented with the branding and support information of the
    specified account.
    """

    metadata: Union[Dict[str, str], Literal[""]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Individual keys can be unset by posting an
    empty value to them. All keys can be unset by posting an empty value to
    `metadata`.
    """

    number: str
    """Set the number for this invoice.

    If no number is present then a number will be assigned automatically when the
    invoice is finalized. In many markets, regulations require invoices to be
    unique, sequential and / or gapless. You are responsible for ensuring this is
    true across all your different invoicing systems in the event that you edit the
    invoice number using our API. If you use only Stripe for your invoices and do
    not change invoice numbers, Stripe handles this aspect of compliance for you
    automatically.
    """

    on_behalf_of: str
    """The account (if any) for which the funds of the invoice payment are intended.

    If set, the invoice will be presented with the branding and support information
    of the specified account. See the
    [Invoices with Connect](https://docs.stripe.com/billing/invoices/connect)
    documentation for details.
    """

    payment_settings: PaymentSettings
    """
    Configuration settings for the PaymentIntent that is generated when the invoice
    is finalized.
    """

    pending_invoice_items_behavior: Literal["exclude", "include"]
    """How to handle pending invoice items on invoice creation.

    Defaults to `exclude` if the parameter is omitted.
    """

    rendering: Rendering
    """
    The rendering-related settings that control how the invoice is displayed on
    customer-facing surfaces such as PDF and Hosted Invoice Page.
    """

    shipping_cost: ShippingCost
    """Settings for the cost of shipping for this invoice."""

    shipping_details: ShippingDetails
    """Shipping details for the invoice.

    The Invoice PDF will use the `shipping_details` value if it is set, otherwise
    the PDF will render the shipping address from the customer.
    """

    statement_descriptor: str
    """Extra information about a charge for the customer's credit card statement.

    It must contain at least one letter. If not specified and this invoice is part
    of a subscription, the default `statement_descriptor` will be set to the first
    subscription item's product's `statement_descriptor`.
    """

    subscription: str
    """The ID of the subscription to invoice, if any.

    If set, the created invoice will only include pending invoice items for that
    subscription. The subscription's billing cycle and regular subscription events
    won't be affected.
    """

    transfer_data: TransferData
    """
    If specified, the funds from the invoice will be transferred to the destination
    and the ID of the resulting transfer will be found on the invoice's charge.
    """


class AutomaticTaxLiability(TypedDict, total=False):
    type: Required[Literal["account", "self"]]

    account: str


class AutomaticTax(TypedDict, total=False):
    """Settings for automatic tax lookup for this invoice."""

    enabled: Required[bool]

    liability: AutomaticTaxLiability


class CustomFieldsCustomFieldsList(TypedDict, total=False):
    name: Required[str]

    value: Required[str]


class DiscountsDiscountsList(TypedDict, total=False):
    coupon: str

    discount: str

    promotion_code: str


class FromInvoice(TypedDict, total=False):
    """Revise an existing invoice.

    The new invoice will be created in `status=draft`. See the [revision documentation](https://docs.stripe.com/invoicing/invoice-revisions) for more details.
    """

    action: Required[Literal["revision"]]

    invoice: Required[str]


class Issuer(TypedDict, total=False):
    """The connected account that issues the invoice.

    The invoice is presented with the branding and support information of the specified account.
    """

    type: Required[Literal["account", "self"]]

    account: str


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


class PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParamInstallmentsPlanInstallmentPlan(
    TypedDict, total=False
):
    type: Required[Literal["bonus", "fixed_count", "revolving"]]

    count: int

    interval: Literal["month"]


PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParamInstallmentsPlan: TypeAlias = Union[
    PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParamInstallmentsPlanInstallmentPlan, Literal[""]
]


class PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParamInstallments(TypedDict, total=False):
    enabled: bool

    plan: PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParamInstallmentsPlan


class PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParam(TypedDict, total=False):
    installments: PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParamInstallments

    request_three_d_secure: Literal["any", "automatic", "challenge"]


PaymentSettingsPaymentMethodOptionsCard: TypeAlias = Union[
    PaymentSettingsPaymentMethodOptionsCardInvoicePaymentMethodOptionsParam, Literal[""]
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
    """
    Configuration settings for the PaymentIntent that is generated when the invoice is finalized.
    """

    default_mandate: Union[str, Literal[""]]

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


class RenderingPdf(TypedDict, total=False):
    page_size: Literal["a4", "auto", "letter"]


class Rendering(TypedDict, total=False):
    """
    The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page.
    """

    amount_tax_display: Literal["", "exclude_tax", "include_inclusive_tax"]

    pdf: RenderingPdf

    template: str

    template_version: Union[int, Literal[""]]


class ShippingCostShippingRateDataDeliveryEstimateMaximum(TypedDict, total=False):
    unit: Required[Literal["business_day", "day", "hour", "month", "week"]]

    value: Required[int]


class ShippingCostShippingRateDataDeliveryEstimateMinimum(TypedDict, total=False):
    unit: Required[Literal["business_day", "day", "hour", "month", "week"]]

    value: Required[int]


class ShippingCostShippingRateDataDeliveryEstimate(TypedDict, total=False):
    maximum: ShippingCostShippingRateDataDeliveryEstimateMaximum

    minimum: ShippingCostShippingRateDataDeliveryEstimateMinimum


class ShippingCostShippingRateDataFixedAmountCurrencyOptions(TypedDict, total=False):
    amount: Required[int]

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]


class ShippingCostShippingRateDataFixedAmount(TypedDict, total=False):
    amount: Required[int]

    currency: Required[str]

    currency_options: Dict[str, ShippingCostShippingRateDataFixedAmountCurrencyOptions]


class ShippingCostShippingRateData(TypedDict, total=False):
    display_name: Required[str]

    delivery_estimate: ShippingCostShippingRateDataDeliveryEstimate

    fixed_amount: ShippingCostShippingRateDataFixedAmount

    metadata: Dict[str, str]

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]

    tax_code: str

    type: Literal["fixed_amount"]


class ShippingCost(TypedDict, total=False):
    """Settings for the cost of shipping for this invoice."""

    shipping_rate: str

    shipping_rate_data: ShippingCostShippingRateData


class ShippingDetailsAddress(TypedDict, total=False):
    city: str

    country: str

    line1: str

    line2: str

    postal_code: str

    state: str


class ShippingDetails(TypedDict, total=False):
    """Shipping details for the invoice.

    The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer.
    """

    address: Required[ShippingDetailsAddress]

    name: Required[str]

    phone: Union[str, Literal[""]]


class TransferData(TypedDict, total=False):
    """
    If specified, the funds from the invoice will be transferred to the destination and the ID of the resulting transfer will be found on the invoice's charge.
    """

    destination: Required[str]

    amount: int
