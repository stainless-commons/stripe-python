# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "CustomerCreateParams",
    "Address",
    "AddressOptionalFieldsCustomerAddress",
    "CashBalance",
    "CashBalanceSettings",
    "InvoiceSettings",
    "InvoiceSettingsCustomFieldsCustomFieldsList",
    "InvoiceSettingsRenderingOptions",
    "InvoiceSettingsRenderingOptionsCustomerRenderingOptionsParam",
    "Shipping",
    "ShippingCustomerShipping",
    "ShippingCustomerShippingAddress",
    "Tax",
    "TaxIDData",
]


class CustomerCreateParams(TypedDict, total=False):
    address: Address
    """The customer's address.

    Learn about
    [country-specific requirements for calculating tax](https://docs.stripe.com/invoicing/taxes?dashboard-or-api=dashboard#set-up-customer).
    """

    balance: int
    """
    An integer amount in cents (or local equivalent) that represents the customer's
    current balance, which affect the customer's future invoices. A negative amount
    represents a credit that decreases the amount due on an invoice; a positive
    amount increases the amount due on an invoice.
    """

    business_name: Union[str, Literal[""]]
    """The customer's business name. This may be up to _150 characters_."""

    cash_balance: CashBalance
    """Balance information and default balance settings for this customer."""

    description: str
    """An arbitrary string that you can attach to a customer object.

    It is displayed alongside the customer in the dashboard.
    """

    email: str
    """Customer's email address.

    It's displayed alongside the customer in your dashboard and can be useful for
    searching and tracking. This may be up to _512 characters_.
    """

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    individual_name: Union[str, Literal[""]]
    """The customer's full name. This may be up to _150 characters_."""

    invoice_prefix: str
    """The prefix for the customer used to generate unique invoice numbers.

    Must be 3–12 uppercase letters or numbers.
    """

    invoice_settings: InvoiceSettings
    """Default invoice settings for this customer."""

    metadata: Union[Dict[str, str], Literal[""]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Individual keys can be unset by posting an
    empty value to them. All keys can be unset by posting an empty value to
    `metadata`.
    """

    name: str
    """The customer's full name or business name."""

    next_invoice_sequence: int
    """The sequence to be used on the customer's next invoice. Defaults to 1."""

    payment_method: str

    phone: str
    """The customer's phone number."""

    preferred_locales: SequenceNotStr[str]
    """Customer's preferred languages, ordered by preference."""

    shipping: Shipping
    """The customer's shipping information.

    Appears on invoices emailed to this customer.
    """

    source: str

    tax: Tax
    """Tax details about the customer."""

    tax_exempt: Literal["", "exempt", "none", "reverse"]
    """The customer's tax exemption. One of `none`, `exempt`, or `reverse`."""

    tax_id_data: Iterable[TaxIDData]
    """The customer's tax IDs."""

    test_clock: str
    """ID of the test clock to attach to the customer."""


class AddressOptionalFieldsCustomerAddress(TypedDict, total=False):
    city: str

    country: str

    line1: str

    line2: str

    postal_code: str

    state: str


Address: TypeAlias = Union[AddressOptionalFieldsCustomerAddress, Literal[""]]


class CashBalanceSettings(TypedDict, total=False):
    reconciliation_mode: Literal["automatic", "manual", "merchant_default"]


class CashBalance(TypedDict, total=False):
    """Balance information and default balance settings for this customer."""

    settings: CashBalanceSettings


class InvoiceSettingsCustomFieldsCustomFieldsList(TypedDict, total=False):
    name: Required[str]

    value: Required[str]


class InvoiceSettingsRenderingOptionsCustomerRenderingOptionsParam(TypedDict, total=False):
    amount_tax_display: Literal["", "exclude_tax", "include_inclusive_tax"]

    template: str


InvoiceSettingsRenderingOptions: TypeAlias = Union[
    InvoiceSettingsRenderingOptionsCustomerRenderingOptionsParam, Literal[""]
]


class InvoiceSettings(TypedDict, total=False):
    """Default invoice settings for this customer."""

    custom_fields: Union[Iterable[InvoiceSettingsCustomFieldsCustomFieldsList], Literal[""]]

    default_payment_method: str

    footer: str

    rendering_options: InvoiceSettingsRenderingOptions


class ShippingCustomerShippingAddress(TypedDict, total=False):
    city: str

    country: str

    line1: str

    line2: str

    postal_code: str

    state: str


class ShippingCustomerShipping(TypedDict, total=False):
    address: Required[ShippingCustomerShippingAddress]

    name: Required[str]

    phone: str


Shipping: TypeAlias = Union[ShippingCustomerShipping, Literal[""]]


class Tax(TypedDict, total=False):
    """Tax details about the customer."""

    ip_address: Union[str, Literal[""]]

    validate_location: Literal["deferred", "immediately"]


class TaxIDData(TypedDict, total=False):
    type: Required[
        Literal[
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
    ]

    value: Required[str]
