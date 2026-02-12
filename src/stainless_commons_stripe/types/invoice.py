# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import application
from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .tax_rate import TaxRate
from .shared.source import Source
from .shared.address import Address
from .shared.shipping import Shipping
from .shared.tax_code import TaxCode
from .shared.deleted_tax_id import DeletedTaxID
from .shared.deleted_customer import DeletedCustomer
from .shared.deleted_application import DeletedApplication
from .shared.test_helpers_test_clock import TestHelpersTestClock
from .shared.invoice_setting_custom_field import InvoiceSettingCustomField
from .shipping_rate_delivery_estimate_bound import ShippingRateDeliveryEstimateBound

__all__ = [
    "Invoice",
    "Customer",
    "Discount",
    "Lines",
    "PaymentSettings",
    "PaymentSettingsPaymentMethodOptions",
    "PaymentSettingsPaymentMethodOptionsAcssDebit",
    "PaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions",
    "PaymentSettingsPaymentMethodOptionsBancontact",
    "PaymentSettingsPaymentMethodOptionsCard",
    "PaymentSettingsPaymentMethodOptionsCardInstallments",
    "PaymentSettingsPaymentMethodOptionsCustomerBalance",
    "PaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer",
    "PaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer",
    "PaymentSettingsPaymentMethodOptionsKonbini",
    "PaymentSettingsPaymentMethodOptionsPayto",
    "PaymentSettingsPaymentMethodOptionsPaytoMandateOptions",
    "PaymentSettingsPaymentMethodOptionsSepaDebit",
    "PaymentSettingsPaymentMethodOptionsUsBankAccount",
    "PaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections",
    "PaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters",
    "StatusTransitions",
    "AccountTaxID",
    "Application",
    "ConfirmationSecret",
    "CustomerTaxID",
    "DefaultPaymentMethod",
    "DefaultSource",
    "LatestRevision",
    "OnBehalfOf",
    "Payments",
    "Rendering",
    "RenderingPdf",
    "ShippingCost",
    "ShippingCostShippingRate",
    "ShippingCostShippingRateShippingRate",
    "ShippingCostShippingRateShippingRateDeliveryEstimate",
    "ShippingCostShippingRateShippingRateFixedAmount",
    "ShippingCostShippingRateShippingRateFixedAmountCurrencyOptions",
    "ShippingCostShippingRateShippingRateTaxCode",
    "ShippingCostTax",
    "TestClock",
    "ThresholdReason",
    "ThresholdReasonItemReason",
    "TotalTax",
    "TotalTaxTaxRateDetails",
]

if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer]

if TYPE_CHECKING or not PYDANTIC_V1:
    Discount = TypeAliasType("Discount", Union[str, "discount.Discount", "DeletedDiscount"])
else:
    Discount: TypeAlias = Union[str, "discount.Discount", "DeletedDiscount"]


class Lines(BaseModel):
    """The individual line items that make up the invoice.

    `lines` is sorted as follows: (1) pending invoice items (including prorations) in reverse chronological order, (2) subscription items in reverse chronological order, and (3) invoice items added after invoice creation in chronological order.
    """

    data: List["LineItem"]
    """Details about each object."""

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


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


class PaymentSettingsPaymentMethodOptionsCardInstallments(BaseModel):
    enabled: Optional[bool] = None
    """Whether Installments are enabled for this Invoice."""


class PaymentSettingsPaymentMethodOptionsCard(BaseModel):
    installments: Optional[PaymentSettingsPaymentMethodOptionsCardInstallments] = None

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


class PaymentSettingsPaymentMethodOptionsKonbini(BaseModel):
    pass


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


class PaymentSettingsPaymentMethodOptionsSepaDebit(BaseModel):
    pass


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

    konbini: Optional[PaymentSettingsPaymentMethodOptionsKonbini] = None

    payto: Optional[PaymentSettingsPaymentMethodOptionsPayto] = None

    sepa_debit: Optional[PaymentSettingsPaymentMethodOptionsSepaDebit] = None

    us_bank_account: Optional[PaymentSettingsPaymentMethodOptionsUsBankAccount] = None


class PaymentSettings(BaseModel):
    default_mandate: Optional[str] = None
    """ID of the mandate to be used for this invoice.

    It must correspond to the payment method used to pay the invoice, including the
    invoice's default_payment_method or default_source, if set.
    """

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
    """The list of payment method types (e.g.

    card) to provide to the invoice’s PaymentIntent. If not set, Stripe attempts to
    automatically determine the types to use by looking at the invoice’s default
    payment method, the subscription’s default payment method, the customer’s
    default payment method, and your
    [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice).
    """


class StatusTransitions(BaseModel):
    finalized_at: Optional[int] = None
    """The time that the invoice draft was finalized."""

    marked_uncollectible_at: Optional[int] = None
    """The time that the invoice was marked uncollectible."""

    paid_at: Optional[int] = None
    """The time that the invoice was paid."""

    voided_at: Optional[int] = None
    """The time that the invoice was voided."""


if TYPE_CHECKING or not PYDANTIC_V1:
    AccountTaxID = TypeAliasType("AccountTaxID", Union[str, "TaxID", DeletedTaxID])
else:
    AccountTaxID: TypeAlias = Union[str, "TaxID", DeletedTaxID]

Application: TypeAlias = Union[str, application.Application, DeletedApplication, None]


class ConfirmationSecret(BaseModel):
    client_secret: str
    """
    The client_secret of the payment that Stripe creates for the invoice after
    finalization.
    """

    type: str
    """The type of client_secret.

    Currently this is always payment_intent, referencing the default payment_intent
    that Stripe creates during invoice finalization
    """


class CustomerTaxID(BaseModel):
    type: Literal[
        "ad_nrt",
        "ae_trn",
        "al_tin",
        "am_tin",
        "ao_tin",
        "ar_cuit",
        "au_abn",
        "au_arn",
        "aw_tin",
        "az_tin",
        "ba_tin",
        "bb_tin",
        "bd_bin",
        "bf_ifu",
        "bg_uic",
        "bh_vat",
        "bj_ifu",
        "bo_tin",
        "br_cnpj",
        "br_cpf",
        "bs_tin",
        "by_tin",
        "ca_bn",
        "ca_gst_hst",
        "ca_pst_bc",
        "ca_pst_mb",
        "ca_pst_sk",
        "ca_qst",
        "cd_nif",
        "ch_uid",
        "ch_vat",
        "cl_tin",
        "cm_niu",
        "cn_tin",
        "co_nit",
        "cr_tin",
        "cv_nif",
        "de_stn",
        "do_rcn",
        "ec_ruc",
        "eg_tin",
        "es_cif",
        "et_tin",
        "eu_oss_vat",
        "eu_vat",
        "gb_vat",
        "ge_vat",
        "gn_nif",
        "hk_br",
        "hr_oib",
        "hu_tin",
        "id_npwp",
        "il_vat",
        "in_gst",
        "is_vat",
        "jp_cn",
        "jp_rn",
        "jp_trn",
        "ke_pin",
        "kg_tin",
        "kh_tin",
        "kr_brn",
        "kz_bin",
        "la_tin",
        "li_uid",
        "li_vat",
        "ma_vat",
        "md_vat",
        "me_pib",
        "mk_vat",
        "mr_nif",
        "mx_rfc",
        "my_frp",
        "my_itn",
        "my_sst",
        "ng_tin",
        "no_vat",
        "no_voec",
        "np_pan",
        "nz_gst",
        "om_vat",
        "pe_ruc",
        "ph_tin",
        "pl_nip",
        "ro_tin",
        "rs_pib",
        "ru_inn",
        "ru_kpp",
        "sa_vat",
        "sg_gst",
        "sg_uen",
        "si_tin",
        "sn_ninea",
        "sr_fin",
        "sv_nit",
        "th_vat",
        "tj_tin",
        "tr_tin",
        "tw_vat",
        "tz_vat",
        "ua_vat",
        "ug_tin",
        "unknown",
        "us_ein",
        "uy_ruc",
        "uz_tin",
        "uz_vat",
        "ve_rif",
        "vn_tin",
        "za_vat",
        "zm_tin",
        "zw_tin",
    ]
    """
    The type of the tax ID, one of `ad_nrt`, `ar_cuit`, `eu_vat`, `bo_tin`,
    `br_cnpj`, `br_cpf`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`,
    `eu_oss_vat`, `hr_oib`, `pe_ruc`, `ro_tin`, `rs_pib`, `sv_nit`, `uy_ruc`,
    `ve_rif`, `vn_tin`, `gb_vat`, `nz_gst`, `au_abn`, `au_arn`, `in_gst`, `no_vat`,
    `no_voec`, `za_vat`, `ch_vat`, `mx_rfc`, `sg_uen`, `ru_inn`, `ru_kpp`, `ca_bn`,
    `hk_br`, `es_cif`, `pl_nip`, `tw_vat`, `th_vat`, `jp_cn`, `jp_rn`, `jp_trn`,
    `li_uid`, `li_vat`, `my_itn`, `us_ein`, `kr_brn`, `ca_qst`, `ca_gst_hst`,
    `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `my_sst`, `sg_gst`, `ae_trn`, `cl_tin`,
    `sa_vat`, `id_npwp`, `my_frp`, `il_vat`, `ge_vat`, `ua_vat`, `is_vat`, `bg_uic`,
    `hu_tin`, `si_tin`, `ke_pin`, `tr_tin`, `eg_tin`, `ph_tin`, `al_tin`, `bh_vat`,
    `kz_bin`, `ng_tin`, `om_vat`, `de_stn`, `ch_uid`, `tz_vat`, `uz_vat`, `uz_tin`,
    `md_vat`, `ma_vat`, `by_tin`, `ao_tin`, `bs_tin`, `bb_tin`, `cd_nif`, `mr_nif`,
    `me_pib`, `zw_tin`, `ba_tin`, `gn_nif`, `mk_vat`, `sr_fin`, `sn_ninea`,
    `am_tin`, `np_pan`, `tj_tin`, `ug_tin`, `zm_tin`, `kh_tin`, `aw_tin`, `az_tin`,
    `bd_bin`, `bj_ifu`, `et_tin`, `kg_tin`, `la_tin`, `cm_niu`, `cv_nif`, `bf_ifu`,
    or `unknown`
    """

    value: Optional[str] = None
    """The value of the tax ID."""


if TYPE_CHECKING or not PYDANTIC_V1:
    DefaultPaymentMethod = TypeAliasType("DefaultPaymentMethod", Union[str, "PaymentMethod", None])
else:
    DefaultPaymentMethod: TypeAlias = Union[str, "PaymentMethod", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    DefaultSource = TypeAliasType("DefaultSource", Union[str, "BankAccount", "Card", Source, None])
else:
    DefaultSource: TypeAlias = Union[str, "BankAccount", "Card", Source, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    LatestRevision = TypeAliasType("LatestRevision", Union[str, "Invoice", None])
else:
    LatestRevision: TypeAlias = Union[str, "Invoice", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    OnBehalfOf = TypeAliasType("OnBehalfOf", Union[str, "Account", None])
else:
    OnBehalfOf: TypeAlias = Union[str, "Account", None]


class Payments(BaseModel):
    """Payments for this invoice"""

    data: List["InvoicePayment"]
    """Details about each object."""

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


class RenderingPdf(BaseModel):
    page_size: Optional[Literal["a4", "auto", "letter"]] = None
    """Page size of invoice pdf.

    Options include a4, letter, and auto. If set to auto, page size will be switched
    to a4 or letter based on customer locale.
    """


class Rendering(BaseModel):
    amount_tax_display: Optional[str] = None
    """
    How line-item prices and amounts will be displayed with respect to tax on
    invoice PDFs.
    """

    pdf: Optional[RenderingPdf] = None

    template: Optional[str] = None
    """ID of the rendering template that the invoice is formatted by."""

    template_version: Optional[int] = None
    """Version of the rendering template that the invoice is using."""


class ShippingCostShippingRateShippingRateDeliveryEstimate(BaseModel):
    maximum: Optional[ShippingRateDeliveryEstimateBound] = None

    minimum: Optional[ShippingRateDeliveryEstimateBound] = None


class ShippingCostShippingRateShippingRateFixedAmountCurrencyOptions(BaseModel):
    amount: int
    """A non-negative integer in cents representing how much to charge."""

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of
    taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """


class ShippingCostShippingRateShippingRateFixedAmount(BaseModel):
    amount: int
    """A non-negative integer in cents representing how much to charge."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    currency_options: Optional[Dict[str, ShippingCostShippingRateShippingRateFixedAmountCurrencyOptions]] = None
    """Shipping rates defined in each available currency option.

    Each key must be a three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a
    [supported currency](https://stripe.com/docs/currencies).
    """


ShippingCostShippingRateShippingRateTaxCode: TypeAlias = Union[str, TaxCode, None]


class ShippingCostShippingRateShippingRate(BaseModel):
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

    delivery_estimate: Optional[ShippingCostShippingRateShippingRateDeliveryEstimate] = None

    display_name: Optional[str] = None
    """The name of the shipping rate, meant to be displayable to the customer.

    This will appear on CheckoutSessions.
    """

    fixed_amount: Optional[ShippingCostShippingRateShippingRateFixedAmount] = None

    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified"]] = None
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of
    taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """

    tax_code: Optional[ShippingCostShippingRateShippingRateTaxCode] = None
    """A [tax code](https://docs.stripe.com/tax/tax-categories) ID.

    The Shipping tax code is `txcd_92010001`.
    """


ShippingCostShippingRate: TypeAlias = Union[str, ShippingCostShippingRateShippingRate, None]


class ShippingCostTax(BaseModel):
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


class ShippingCost(BaseModel):
    amount_subtotal: int
    """Total shipping cost before any taxes are applied."""

    amount_tax: int
    """Total tax amount applied due to shipping costs.

    If no tax was applied, defaults to 0.
    """

    amount_total: int
    """Total shipping cost after taxes are applied."""

    shipping_rate: Optional[ShippingCostShippingRate] = None
    """The ID of the ShippingRate for this invoice."""

    taxes: Optional[List[ShippingCostTax]] = None
    """The taxes applied to the shipping rate."""


TestClock: TypeAlias = Union[str, TestHelpersTestClock, None]


class ThresholdReasonItemReason(BaseModel):
    line_item_ids: List[str]
    """The IDs of the line items that triggered the threshold invoice."""

    usage_gte: int
    """The quantity threshold boundary that applied to the given line item."""


class ThresholdReason(BaseModel):
    item_reasons: List[ThresholdReasonItemReason]
    """Indicates which line items triggered a threshold invoice."""

    amount_gte: Optional[int] = None
    """
    The total invoice amount threshold boundary if it triggered the threshold
    invoice.
    """


class TotalTaxTaxRateDetails(BaseModel):
    tax_rate: str
    """ID of the tax rate"""


class TotalTax(BaseModel):
    amount: int
    """The amount of the tax, in cents (or local equivalent)."""

    tax_behavior: Literal["exclusive", "inclusive"]
    """Whether this tax is inclusive or exclusive."""

    taxability_reason: Literal[
        "customer_exempt",
        "not_available",
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
    """The reasoning behind this tax, for example, if the product is tax exempt.

    The possible values for this field may be extended as new tax rules are
    supported.
    """

    type: Literal["tax_rate_details"]
    """The type of tax information."""

    tax_rate_details: Optional[TotalTaxTaxRateDetails] = None

    taxable_amount: Optional[int] = None
    """The amount on which tax is calculated, in cents (or local equivalent)."""


class Invoice(BaseModel):
    """
    Invoices are statements of amounts owed by a customer, and are either
    generated one-off, or generated periodically from a subscription.

    They contain [invoice items](https://api.stripe.com#invoiceitems), and proration adjustments
    that may be caused by subscription upgrades/downgrades (if necessary).

    If your invoice is configured to be billed through automatic charges,
    Stripe automatically finalizes your invoice and attempts payment. Note
    that finalizing the invoice,
    [when automatic](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection), does
    not happen immediately as the invoice is created. Stripe waits
    until one hour after the last webhook was successfully sent (or the last
    webhook timed out after failing). If you (and the platforms you may have
    connected to) have no webhooks configured, Stripe waits one hour after
    creation to finalize the invoice.

    If your invoice is configured to be billed by sending an email, then based on your
    [email settings](https://dashboard.stripe.com/account/billing/automatic),
    Stripe will email the invoice to your customer and await payment. These
    emails can contain a link to a hosted page to pay the invoice.

    Stripe applies any customer credit on the account before determining the
    amount due for the invoice (i.e., the amount that will be actually
    charged). If the amount due for the invoice is less than Stripe's [minimum allowed charge
    per currency](/docs/currencies#minimum-and-maximum-charge-amounts), the
    invoice is automatically marked paid, and we add the amount due to the
    customer's credit balance which is applied to the next invoice.

    More details on the customer's credit balance are
    [here](https://docs.stripe.com/billing/customer/balance).

    Related guide: [Send invoices to customers](https://docs.stripe.com/billing/invoices/sending)
    """

    id: str
    """Unique identifier for the object.

    For preview invoices created using the
    [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint,
    this id will be prefixed with `upcoming_in`.
    """

    amount_due: int
    """Final amount due at this time for this invoice.

    If the invoice's total is smaller than the minimum charge amount, for example,
    or if there is account credit that can be applied to the invoice, the
    `amount_due` may be 0. If there is a positive `starting_balance` for the invoice
    (the customer owes money), the `amount_due` will also take that into account.
    The charge that gets generated for the invoice will be for the amount specified
    in `amount_due`.
    """

    amount_overpaid: int
    """Amount that was overpaid on the invoice.

    The amount overpaid is credited to the customer's credit balance.
    """

    amount_paid: int
    """The amount, in cents (or local equivalent), that was paid."""

    amount_remaining: int
    """
    The difference between amount_due and amount_paid, in cents (or local
    equivalent).
    """

    amount_shipping: int
    """This is the sum of all the shipping amounts."""

    attempt_count: int
    """
    Number of payment attempts made for this invoice, from the perspective of the
    payment retry schedule. Any payment attempt counts as the first attempt, and
    subsequently only automatic retries increment the attempt count. In other words,
    manual payment attempts after the first attempt do not affect the retry
    schedule. If a failure is returned with a non-retryable return code, the invoice
    can no longer be retried unless a new payment method is obtained. Retries will
    continue to be scheduled, and attempt_count will continue to increment, but
    retries will only be executed if a new payment method is obtained.
    """

    attempted: bool
    """Whether an attempt has been made to pay the invoice.

    An invoice is not attempted until 1 hour after the `invoice.created` webhook,
    for example, so you might not want to display that invoice as unpaid to your
    users.
    """

    auto_advance: bool
    """
    Controls whether Stripe performs
    [automatic collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
    of the invoice. If `false`, the invoice's state doesn't automatically advance
    without an explicit action.
    """

    automatic_tax: "AutomaticTaxInvoice"

    collection_method: Literal["charge_automatically", "send_invoice"]
    """Either `charge_automatically`, or `send_invoice`.

    When charging automatically, Stripe will attempt to pay this invoice using the
    default source attached to the customer. When sending an invoice, Stripe will
    email this invoice to the customer with payment instructions.
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
    """The ID of the customer to bill."""

    default_tax_rates: List[TaxRate]
    """The tax rates applied to this invoice, if any."""

    discounts: List[Discount]
    """The discounts applied to the invoice.

    Line item discounts are applied before invoice discounts. Use
    `expand[]=discounts` to expand each discount.
    """

    issuer: "ConnectAccountReference"

    lines: Lines
    """The individual line items that make up the invoice.

    `lines` is sorted as follows: (1) pending invoice items (including prorations)
    in reverse chronological order, (2) subscription items in reverse chronological
    order, and (3) invoice items added after invoice creation in chronological
    order.
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["invoice"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    payment_settings: PaymentSettings

    period_end: int
    """End of the usage period during which invoice items were added to this invoice.

    This looks back one period for a subscription invoice. Use the
    [line item period](/api/invoices/line_item#invoice_line_item_object-period) to
    get the service period for each price.
    """

    period_start: int
    """Start of the usage period during which invoice items were added to this invoice.

    This looks back one period for a subscription invoice. Use the
    [line item period](/api/invoices/line_item#invoice_line_item_object-period) to
    get the service period for each price.
    """

    post_payment_credit_notes_amount: int
    """Total amount of all post-payment credit notes issued for this invoice."""

    pre_payment_credit_notes_amount: int
    """Total amount of all pre-payment credit notes issued for this invoice."""

    starting_balance: int
    """Starting customer balance before the invoice is finalized.

    If the invoice has not been finalized yet, this will be the current customer
    balance. For revision invoices, this also includes any customer balance that was
    applied to the original invoice.
    """

    status_transitions: StatusTransitions

    subtotal: int
    """
    Total of all subscriptions, invoice items, and prorations on the invoice before
    any invoice level discount or exclusive tax is applied. Item discounts are
    already incorporated
    """

    total: int
    """Total after discounts and taxes."""

    account_country: Optional[str] = None
    """
    The country of the business associated with this invoice, most often the
    business creating the invoice.
    """

    account_name: Optional[str] = None
    """
    The public name of the business associated with this invoice, most often the
    business creating the invoice.
    """

    account_tax_ids: Optional[List[AccountTaxID]] = None
    """The account tax IDs associated with the invoice.

    Only editable when the invoice is a draft.
    """

    application: Optional[Application] = None
    """ID of the Connect Application that created the invoice."""

    automatically_finalizes_at: Optional[int] = None
    """The time when this invoice is currently scheduled to be automatically finalized.

    The field will be `null` if the invoice is not scheduled to finalize in the
    future. If the invoice is not in the draft state, this field will always be
    `null` - see `finalized_at` for the time when an already-finalized invoice was
    finalized.
    """

    billing_reason: Optional[
        Literal[
            "automatic_pending_invoice_item_invoice",
            "manual",
            "quote_accept",
            "subscription",
            "subscription_create",
            "subscription_cycle",
            "subscription_threshold",
            "subscription_update",
            "upcoming",
        ]
    ] = None
    """Indicates the reason why the invoice was created.

    - `manual`: Unrelated to a subscription, for example, created via the invoice
      editor.
    - `subscription`: No longer in use. Applies to subscriptions from before May
      2018 where no distinction was made between updates, cycles, and thresholds.
    - `subscription_create`: A new subscription was created.
    - `subscription_cycle`: A subscription advanced into a new period.
    - `subscription_threshold`: A subscription reached a billing threshold.
    - `subscription_update`: A subscription was updated.
    - `upcoming`: Reserved for upcoming invoices created through the Create Preview
      Invoice API or when an `invoice.upcoming` event is generated for an upcoming
      invoice on a subscription.
    """

    confirmation_secret: Optional[ConfirmationSecret] = None

    custom_fields: Optional[List[InvoiceSettingCustomField]] = None
    """Custom fields displayed on the invoice."""

    customer_account: Optional[str] = None
    """The ID of the account representing the customer to bill."""

    customer_address: Optional[Address] = None

    customer_email: Optional[str] = None
    """The customer's email.

    Until the invoice is finalized, this field will equal `customer.email`. Once the
    invoice is finalized, this field will no longer be updated.
    """

    customer_name: Optional[str] = None
    """The customer's name.

    Until the invoice is finalized, this field will equal `customer.name`. Once the
    invoice is finalized, this field will no longer be updated.
    """

    customer_phone: Optional[str] = None
    """The customer's phone number.

    Until the invoice is finalized, this field will equal `customer.phone`. Once the
    invoice is finalized, this field will no longer be updated.
    """

    customer_shipping: Optional[Shipping] = None

    customer_tax_exempt: Optional[Literal["exempt", "none", "reverse"]] = None
    """The customer's tax exempt status.

    Until the invoice is finalized, this field will equal `customer.tax_exempt`.
    Once the invoice is finalized, this field will no longer be updated.
    """

    customer_tax_ids: Optional[List[CustomerTaxID]] = None
    """The customer's tax IDs.

    Until the invoice is finalized, this field will contain the same tax IDs as
    `customer.tax_ids`. Once the invoice is finalized, this field will no longer be
    updated.
    """

    default_payment_method: Optional[DefaultPaymentMethod] = None
    """ID of the default payment method for the invoice.

    It must belong to the customer associated with the invoice. If not set, defaults
    to the subscription's default payment method, if any, or to the default payment
    method in the customer's invoice settings.
    """

    default_source: Optional[DefaultSource] = None
    """ID of the default payment source for the invoice.

    It must belong to the customer associated with the invoice and be in a
    chargeable state. If not set, defaults to the subscription's default source, if
    any, or to the customer's default source.
    """

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users. Referenced as 'memo' in the Dashboard.
    """

    due_date: Optional[int] = None
    """The date on which payment for this invoice is due.

    This value will be `null` for invoices where
    `collection_method=charge_automatically`.
    """

    effective_at: Optional[int] = None
    """The date when this invoice is in effect.

    Same as `finalized_at` unless overwritten. When defined, this value replaces the
    system-generated 'Date of issue' printed on the invoice PDF and receipt.
    """

    ending_balance: Optional[int] = None
    """Ending customer balance after the invoice is finalized.

    Invoices are finalized approximately an hour after successful webhook delivery
    or when payment collection is attempted for the invoice. If the invoice has not
    been finalized yet, this will be null.
    """

    footer: Optional[str] = None
    """Footer displayed on the invoice."""

    from_invoice: Optional["InvoicesResourceFromInvoice"] = None

    hosted_invoice_url: Optional[str] = None
    """
    The URL for the hosted invoice page, which allows customers to view and pay an
    invoice. If the invoice has not been finalized yet, this will be null.
    """

    invoice_pdf: Optional[str] = None
    """The link to download the PDF for the invoice.

    If the invoice has not been finalized yet, this will be null.
    """

    last_finalization_error: Optional["APIErrors"] = None

    latest_revision: Optional[LatestRevision] = None
    """The ID of the most recent non-draft revision of this invoice"""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    next_payment_attempt: Optional[int] = None
    """The time at which payment will next be attempted.

    This value will be `null` for invoices where `collection_method=send_invoice`.
    """

    number: Optional[str] = None
    """
    A unique, identifying string that appears on emails sent to the customer for
    this invoice. This starts with the customer's unique invoice_prefix if it is
    specified.
    """

    on_behalf_of: Optional[OnBehalfOf] = None
    """The account (if any) for which the funds of the invoice payment are intended.

    If set, the invoice will be presented with the branding and support information
    of the specified account. See the
    [Invoices with Connect](https://docs.stripe.com/billing/invoices/connect)
    documentation for details.
    """

    parent: Optional["BillingBillResourceInvoicingParentsInvoiceParent"] = None

    payments: Optional[Payments] = None
    """Payments for this invoice"""

    receipt_number: Optional[str] = None
    """
    This is the transaction number that appears on email receipts sent for this
    invoice.
    """

    rendering: Optional[Rendering] = None

    shipping_cost: Optional[ShippingCost] = None

    shipping_details: Optional[Shipping] = None

    statement_descriptor: Optional[str] = None
    """Extra information about an invoice for the customer's credit card statement."""

    status: Optional[Literal["draft", "open", "paid", "uncollectible", "void"]] = None
    """
    The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or
    `void`.
    [Learn more](https://docs.stripe.com/billing/invoices/workflow#workflow-overview)
    """

    subtotal_excluding_tax: Optional[int] = None
    """
    The integer amount in cents (or local equivalent) representing the subtotal of
    the invoice before any invoice level discount or tax is applied. Item discounts
    are already incorporated
    """

    test_clock: Optional[TestClock] = None
    """ID of the test clock this invoice belongs to."""

    threshold_reason: Optional[ThresholdReason] = None

    total_discount_amounts: Optional[List["DiscountsResourceDiscountAmount"]] = None
    """The aggregate amounts calculated per discount across all line items."""

    total_excluding_tax: Optional[int] = None
    """
    The integer amount in cents (or local equivalent) representing the total amount
    of the invoice including all discounts but excluding all tax.
    """

    total_pretax_credit_amounts: Optional[List["InvoicesResourcePretaxCreditAmount"]] = None
    """
    Contains pretax credit amounts (ex: discount, credit grants, etc) that apply to
    this invoice. This is a combined list of total_pretax_credit_amounts across all
    invoice line items.
    """

    total_taxes: Optional[List[TotalTax]] = None
    """The aggregate tax information of all line items."""

    webhooks_delivered_at: Optional[int] = None
    """
    Invoices are automatically paid or sent 1 hour after webhooks are delivered, or
    until all webhook delivery attempts have
    [been exhausted](https://docs.stripe.com/billing/webhooks#understand). This
    field tracks the time when webhooks for this invoice were successfully
    delivered. If the invoice had no webhooks to deliver, this will be set while the
    invoice is being created.
    """


from . import customer, discount
from .card import Card
from .tax_id import TaxID
from .account import Account
from .line_item import LineItem
from .api_errors import APIErrors
from .bank_account import BankAccount
from .payment_method import PaymentMethod
from .invoice_payment import InvoicePayment
from .deleted_discount import DeletedDiscount
from .automatic_tax_invoice import AutomaticTaxInvoice
from .connect_account_reference import ConnectAccountReference
from .invoices_resource_from_invoice import InvoicesResourceFromInvoice
from .discounts_resource_discount_amount import DiscountsResourceDiscountAmount
from .invoices_resource_pretax_credit_amount import InvoicesResourcePretaxCreditAmount
from .billing_bill_resource_invoicing_parents_invoice_parent import BillingBillResourceInvoicingParentsInvoiceParent
