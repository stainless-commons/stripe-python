# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.address import Address
from .shared.payment_method_details_card_present_offline import PaymentMethodDetailsCardPresentOffline
from .shared.payment_flows_private_payment_methods_card_present_common_wallet import (
    PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet,
)

__all__ = [
    "PaymentMethod",
    "BillingDetails",
    "AcssDebit",
    "Affirm",
    "AfterpayClearpay",
    "Alipay",
    "Alma",
    "AmazonPay",
    "AuBecsDebit",
    "BacsDebit",
    "Bancontact",
    "Billie",
    "Blik",
    "Boleto",
    "CardPresent",
    "CardPresentNetworks",
    "Cashapp",
    "Crypto",
    "Custom",
    "CustomLogo",
    "Customer",
    "CustomerBalance",
    "Eps",
    "Fpx",
    "Giropay",
    "Grabpay",
    "Ideal",
    "InteracPresent",
    "InteracPresentNetworks",
    "KakaoPay",
    "Klarna",
    "KlarnaDob",
    "Konbini",
    "KrCard",
    "Link",
    "MBWay",
    "Mobilepay",
    "Multibanco",
    "NaverPay",
    "NzBankAccount",
    "Oxxo",
    "P24",
    "PayByBank",
    "Payco",
    "Paynow",
    "Paypal",
    "Payto",
    "Pix",
    "Promptpay",
    "RadarOptions",
    "RevolutPay",
    "SamsungPay",
    "Satispay",
    "Sofort",
    "Swish",
    "Twint",
    "UsBankAccount",
    "UsBankAccountNetworks",
    "UsBankAccountStatusDetails",
    "UsBankAccountStatusDetailsBlocked",
    "WechatPay",
    "Zip",
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


class AcssDebit(BaseModel):
    bank_name: Optional[str] = None
    """Name of the bank associated with the bank account."""

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    institution_number: Optional[str] = None
    """Institution number of the bank account."""

    last4: Optional[str] = None
    """Last four digits of the bank account number."""

    transit_number: Optional[str] = None
    """Transit number of the bank account."""


class Affirm(BaseModel):
    pass


class AfterpayClearpay(BaseModel):
    pass


class Alipay(BaseModel):
    pass


class Alma(BaseModel):
    pass


class AmazonPay(BaseModel):
    pass


class AuBecsDebit(BaseModel):
    bsb_number: Optional[str] = None
    """Six-digit number identifying bank and branch associated with this bank account."""

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    last4: Optional[str] = None
    """Last four digits of the bank account number."""


class BacsDebit(BaseModel):
    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    last4: Optional[str] = None
    """Last four digits of the bank account number."""

    sort_code: Optional[str] = None
    """Sort code of the bank account. (e.g., `10-20-30`)"""


class Bancontact(BaseModel):
    pass


class Billie(BaseModel):
    pass


class Blik(BaseModel):
    pass


class Boleto(BaseModel):
    tax_id: str
    """Uniquely identifies the customer tax id (CNPJ or CPF)"""


class CardPresentNetworks(BaseModel):
    available: List[str]
    """
    All networks available for selection via
    [payment_method_options.card.network](/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-network).
    """

    preferred: Optional[str] = None
    """The preferred network for the card."""


class CardPresent(BaseModel):
    exp_month: int
    """Two-digit number representing the card's expiration month."""

    exp_year: int
    """Four-digit number representing the card's expiration year."""

    brand: Optional[str] = None
    """Card brand.

    Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`,
    `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
    """

    brand_product: Optional[str] = None
    """
    The [product code](https://stripe.com/docs/card-product-codes) that identifies
    the specific program or product associated with a card.
    """

    cardholder_name: Optional[str] = None
    """
    The cardholder name as read from the card, in
    [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include
    alphanumeric characters, special characters and first/last name separator (`/`).
    In some cases, the cardholder name may not be available depending on how the
    issuer has configured the card. Cardholder name is typically not available on
    swipe or contactless payments, such as those made with Apple Pay and Google Pay.
    """

    country: Optional[str] = None
    """Two-letter ISO code representing the country of the card.

    You could use this attribute to get a sense of the international breakdown of
    cards you've collected.
    """

    description: Optional[str] = None
    """A high-level description of the type of cards issued in this range."""

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular card number.

    You can use this attribute to check whether two customers who’ve signed up with
    you are using the same card number, for example. For payment methods that
    tokenize card information (Apple Pay, Google Pay), the tokenized number might be
    provided instead of the underlying card number.

    _As of May 1, 2021, card fingerprint in India for Connect changed to allow two
    fingerprints for the same card---one for India and one for the rest of the
    world._
    """

    funding: Optional[str] = None
    """Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`."""

    issuer: Optional[str] = None
    """The name of the card's issuing bank."""

    last4: Optional[str] = None
    """The last four digits of the card."""

    networks: Optional[CardPresentNetworks] = None

    offline: Optional[PaymentMethodDetailsCardPresentOffline] = None

    preferred_locales: Optional[List[str]] = None
    """
    The languages that the issuing bank recommends using for localizing any
    customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data
    encoded on the card's chip.
    """

    read_method: Optional[
        Literal[
            "contact_emv",
            "contactless_emv",
            "contactless_magstripe_mode",
            "magnetic_stripe_fallback",
            "magnetic_stripe_track2",
        ]
    ] = None
    """How card details were read in this transaction."""

    wallet: Optional[PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet] = None


class Cashapp(BaseModel):
    buyer_id: Optional[str] = None
    """A unique and immutable identifier assigned by Cash App to every buyer."""

    cashtag: Optional[str] = None
    """A public identifier for buyers using Cash App."""


class Crypto(BaseModel):
    pass


class CustomLogo(BaseModel):
    url: str
    """URL of the Dashboard-only CustomPaymentMethodType logo."""

    content_type: Optional[str] = None
    """Content type of the Dashboard-only CustomPaymentMethodType logo."""


class Custom(BaseModel):
    type: str
    """ID of the Dashboard-only CustomPaymentMethodType. Not expandable."""

    display_name: Optional[str] = None
    """Display name of the Dashboard-only CustomPaymentMethodType."""

    logo: Optional[CustomLogo] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", None])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", None]


class CustomerBalance(BaseModel):
    pass


class Eps(BaseModel):
    bank: Optional[
        Literal[
            "arzte_und_apotheker_bank",
            "austrian_anadi_bank_ag",
            "bank_austria",
            "bankhaus_carl_spangler",
            "bankhaus_schelhammer_und_schattera_ag",
            "bawag_psk_ag",
            "bks_bank_ag",
            "brull_kallmus_bank_ag",
            "btv_vier_lander_bank",
            "capital_bank_grawe_gruppe_ag",
            "deutsche_bank_ag",
            "dolomitenbank",
            "easybank_ag",
            "erste_bank_und_sparkassen",
            "hypo_alpeadriabank_international_ag",
            "hypo_bank_burgenland_aktiengesellschaft",
            "hypo_noe_lb_fur_niederosterreich_u_wien",
            "hypo_oberosterreich_salzburg_steiermark",
            "hypo_tirol_bank_ag",
            "hypo_vorarlberg_bank_ag",
            "marchfelder_bank",
            "oberbank_ag",
            "raiffeisen_bankengruppe_osterreich",
            "schoellerbank_ag",
            "sparda_bank_wien",
            "volksbank_gruppe",
            "volkskreditbank_ag",
            "vr_bank_braunau",
        ]
    ] = None
    """The customer's bank.

    Should be one of `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`,
    `bank_austria`, `bankhaus_carl_spangler`,
    `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`,
    `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`,
    `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`,
    `hypo_alpeadriabank_international_ag`,
    `hypo_noe_lb_fur_niederosterreich_u_wien`,
    `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`,
    `hypo_vorarlberg_bank_ag`, `hypo_bank_burgenland_aktiengesellschaft`,
    `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`,
    `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`,
    `volkskreditbank_ag`, or `vr_bank_braunau`.
    """


class Fpx(BaseModel):
    bank: Literal[
        "affin_bank",
        "agrobank",
        "alliance_bank",
        "ambank",
        "bank_islam",
        "bank_muamalat",
        "bank_of_china",
        "bank_rakyat",
        "bsn",
        "cimb",
        "deutsche_bank",
        "hong_leong_bank",
        "hsbc",
        "kfh",
        "maybank2e",
        "maybank2u",
        "ocbc",
        "pb_enterprise",
        "public_bank",
        "rhb",
        "standard_chartered",
        "uob",
    ]
    """The customer's bank, if provided.

    Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`,
    `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`,
    `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`,
    `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`.
    """


class Giropay(BaseModel):
    pass


class Grabpay(BaseModel):
    pass


class Ideal(BaseModel):
    bank: Optional[
        Literal[
            "abn_amro",
            "adyen",
            "asn_bank",
            "bunq",
            "buut",
            "finom",
            "handelsbanken",
            "ing",
            "knab",
            "mollie",
            "moneyou",
            "n26",
            "nn",
            "rabobank",
            "regiobank",
            "revolut",
            "sns_bank",
            "triodos_bank",
            "van_lanschot",
            "yoursafe",
        ]
    ] = None
    """The customer's bank, if provided.

    Can be one of `abn_amro`, `adyen`, `asn_bank`, `bunq`, `buut`, `finom`,
    `handelsbanken`, `ing`, `knab`, `mollie`, `moneyou`, `n26`, `nn`, `rabobank`,
    `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or
    `yoursafe`.
    """

    bic: Optional[
        Literal[
            "ABNANL2A",
            "ADYBNL2A",
            "ASNBNL21",
            "BITSNL2A",
            "BUNQNL2A",
            "BUUTNL2A",
            "FNOMNL22",
            "FVLBNL22",
            "HANDNL2A",
            "INGBNL2A",
            "KNABNL2H",
            "MLLENL2A",
            "MOYONL21",
            "NNBANL2G",
            "NTSBDEB1",
            "RABONL2U",
            "RBRBNL21",
            "REVOIE23",
            "REVOLT21",
            "SNSBNL2A",
            "TRIONL2U",
        ]
    ] = None
    """The Bank Identifier Code of the customer's bank, if the bank was provided."""


class InteracPresentNetworks(BaseModel):
    available: List[str]
    """
    All networks available for selection via
    [payment_method_options.card.network](/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-network).
    """

    preferred: Optional[str] = None
    """The preferred network for the card."""


class InteracPresent(BaseModel):
    exp_month: int
    """Two-digit number representing the card's expiration month."""

    exp_year: int
    """Four-digit number representing the card's expiration year."""

    brand: Optional[str] = None
    """Card brand. Can be `interac`, `mastercard` or `visa`."""

    cardholder_name: Optional[str] = None
    """
    The cardholder name as read from the card, in
    [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include
    alphanumeric characters, special characters and first/last name separator (`/`).
    In some cases, the cardholder name may not be available depending on how the
    issuer has configured the card. Cardholder name is typically not available on
    swipe or contactless payments, such as those made with Apple Pay and Google Pay.
    """

    country: Optional[str] = None
    """Two-letter ISO code representing the country of the card.

    You could use this attribute to get a sense of the international breakdown of
    cards you've collected.
    """

    description: Optional[str] = None
    """A high-level description of the type of cards issued in this range."""

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular card number.

    You can use this attribute to check whether two customers who’ve signed up with
    you are using the same card number, for example. For payment methods that
    tokenize card information (Apple Pay, Google Pay), the tokenized number might be
    provided instead of the underlying card number.

    _As of May 1, 2021, card fingerprint in India for Connect changed to allow two
    fingerprints for the same card---one for India and one for the rest of the
    world._
    """

    funding: Optional[str] = None
    """Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`."""

    issuer: Optional[str] = None
    """The name of the card's issuing bank."""

    last4: Optional[str] = None
    """The last four digits of the card."""

    networks: Optional[InteracPresentNetworks] = None

    preferred_locales: Optional[List[str]] = None
    """
    The languages that the issuing bank recommends using for localizing any
    customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data
    encoded on the card's chip.
    """

    read_method: Optional[
        Literal[
            "contact_emv",
            "contactless_emv",
            "contactless_magstripe_mode",
            "magnetic_stripe_fallback",
            "magnetic_stripe_track2",
        ]
    ] = None
    """How card details were read in this transaction."""


class KakaoPay(BaseModel):
    pass


class KlarnaDob(BaseModel):
    day: Optional[int] = None
    """The day of birth, between 1 and 31."""

    month: Optional[int] = None
    """The month of birth, between 1 and 12."""

    year: Optional[int] = None
    """The four-digit year of birth."""


class Klarna(BaseModel):
    dob: Optional[KlarnaDob] = None


class Konbini(BaseModel):
    pass


class KrCard(BaseModel):
    brand: Optional[
        Literal[
            "bc",
            "citi",
            "hana",
            "hyundai",
            "jeju",
            "jeonbuk",
            "kakaobank",
            "kbank",
            "kdbbank",
            "kookmin",
            "kwangju",
            "lotte",
            "mg",
            "nh",
            "post",
            "samsung",
            "savingsbank",
            "shinhan",
            "shinhyup",
            "suhyup",
            "tossbank",
            "woori",
        ]
    ] = None
    """The local credit or debit card brand."""

    last4: Optional[str] = None
    """The last four digits of the card.

    This may not be present for American Express cards.
    """


class Link(BaseModel):
    email: Optional[str] = None
    """Account owner's email address."""


class MBWay(BaseModel):
    pass


class Mobilepay(BaseModel):
    pass


class Multibanco(BaseModel):
    pass


class NaverPay(BaseModel):
    funding: Literal["card", "points"]
    """Whether to fund this transaction with Naver Pay points or a card."""

    buyer_id: Optional[str] = None
    """Uniquely identifies this particular Naver Pay account.

    You can use this attribute to check whether two Naver Pay accounts are the same.
    """


class NzBankAccount(BaseModel):
    bank_code: str
    """The numeric code for the bank account's bank."""

    bank_name: str
    """The name of the bank."""

    branch_code: str
    """The numeric code for the bank account's bank branch."""

    last4: str
    """Last four digits of the bank account number."""

    account_holder_name: Optional[str] = None
    """The name on the bank account.

    Only present if the account holder name is different from the name of the
    authorized signatory collected in the PaymentMethod’s billing details.
    """

    suffix: Optional[str] = None
    """The suffix of the bank account number."""


class Oxxo(BaseModel):
    pass


class P24(BaseModel):
    bank: Optional[
        Literal[
            "alior_bank",
            "bank_millennium",
            "bank_nowy_bfg_sa",
            "bank_pekao_sa",
            "banki_spbdzielcze",
            "blik",
            "bnp_paribas",
            "boz",
            "citi_handlowy",
            "credit_agricole",
            "envelobank",
            "etransfer_pocztowy24",
            "getin_bank",
            "ideabank",
            "ing",
            "inteligo",
            "mbank_mtransfer",
            "nest_przelew",
            "noble_pay",
            "pbac_z_ipko",
            "plus_bank",
            "santander_przelew24",
            "tmobile_usbugi_bankowe",
            "toyota_bank",
            "velobank",
            "volkswagen_bank",
        ]
    ] = None
    """The customer's bank, if provided."""


class PayByBank(BaseModel):
    pass


class Payco(BaseModel):
    pass


class Paynow(BaseModel):
    pass


class Paypal(BaseModel):
    country: Optional[str] = None
    """Two-letter ISO code representing the buyer's country.

    Values are provided by PayPal directly (if supported) at the time of
    authorization or settlement. They cannot be set or mutated.
    """

    payer_email: Optional[str] = None
    """Owner's email.

    Values are provided by PayPal directly (if supported) at the time of
    authorization or settlement. They cannot be set or mutated.
    """

    payer_id: Optional[str] = None
    """PayPal account PayerID.

    This identifier uniquely identifies the PayPal customer.
    """


class Payto(BaseModel):
    bsb_number: Optional[str] = None
    """Bank-State-Branch number of the bank account."""

    last4: Optional[str] = None
    """Last four digits of the bank account number."""

    pay_id: Optional[str] = None
    """The PayID alias for the bank account."""


class Pix(BaseModel):
    pass


class Promptpay(BaseModel):
    pass


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


class RevolutPay(BaseModel):
    pass


class SamsungPay(BaseModel):
    pass


class Satispay(BaseModel):
    pass


class Sofort(BaseModel):
    country: Optional[str] = None
    """Two-letter ISO code representing the country the bank account is located in."""


class Swish(BaseModel):
    pass


class Twint(BaseModel):
    pass


class UsBankAccountNetworks(BaseModel):
    supported: List[Literal["ach", "us_domestic_wire"]]
    """All supported networks."""

    preferred: Optional[str] = None
    """The preferred network."""


class UsBankAccountStatusDetailsBlocked(BaseModel):
    network_code: Optional[
        Literal["R02", "R03", "R04", "R05", "R07", "R08", "R10", "R11", "R16", "R20", "R29", "R31"]
    ] = None
    """The ACH network code that resulted in this block."""

    reason: Optional[
        Literal[
            "bank_account_closed",
            "bank_account_frozen",
            "bank_account_invalid_details",
            "bank_account_restricted",
            "bank_account_unusable",
            "debit_not_authorized",
            "tokenized_account_number_deactivated",
        ]
    ] = None
    """The reason why this PaymentMethod's fingerprint has been blocked"""


class UsBankAccountStatusDetails(BaseModel):
    blocked: Optional[UsBankAccountStatusDetailsBlocked] = None


class UsBankAccount(BaseModel):
    account_holder_type: Optional[Literal["company", "individual"]] = None
    """Account holder type: individual or company."""

    account_type: Optional[Literal["checking", "savings"]] = None
    """Account type: checkings or savings. Defaults to checking if omitted."""

    bank_name: Optional[str] = None
    """The name of the bank."""

    financial_connections_account: Optional[str] = None
    """The ID of the Financial Connections Account used to create the payment method."""

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    last4: Optional[str] = None
    """Last four digits of the bank account number."""

    networks: Optional[UsBankAccountNetworks] = None

    routing_number: Optional[str] = None
    """Routing number of the bank account."""

    status_details: Optional[UsBankAccountStatusDetails] = None


class WechatPay(BaseModel):
    pass


class Zip(BaseModel):
    pass


class PaymentMethod(BaseModel):
    """
    PaymentMethod objects represent your customer's payment instruments.
    You can use them with [PaymentIntents](https://docs.stripe.com/payments/payment-intents) to collect payments or save them to
    Customer objects to store instrument details for future payments.

    Related guides: [Payment Methods](https://docs.stripe.com/payments/payment-methods) and [More Payment Scenarios](https://docs.stripe.com/payments/more-payment-scenarios).
    """

    id: str
    """Unique identifier for the object."""

    billing_details: BillingDetails

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["payment_method"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    type: Literal[
        "acss_debit",
        "affirm",
        "afterpay_clearpay",
        "alipay",
        "alma",
        "amazon_pay",
        "au_becs_debit",
        "bacs_debit",
        "bancontact",
        "billie",
        "blik",
        "boleto",
        "card",
        "card_present",
        "cashapp",
        "crypto",
        "custom",
        "customer_balance",
        "eps",
        "fpx",
        "giropay",
        "grabpay",
        "ideal",
        "interac_present",
        "kakao_pay",
        "klarna",
        "konbini",
        "kr_card",
        "link",
        "mb_way",
        "mobilepay",
        "multibanco",
        "naver_pay",
        "nz_bank_account",
        "oxxo",
        "p24",
        "pay_by_bank",
        "payco",
        "paynow",
        "paypal",
        "payto",
        "pix",
        "promptpay",
        "revolut_pay",
        "samsung_pay",
        "satispay",
        "sepa_debit",
        "sofort",
        "swish",
        "twint",
        "us_bank_account",
        "wechat_pay",
        "zip",
    ]
    """The type of the PaymentMethod.

    An additional hash is included on the PaymentMethod with a name matching this
    value. It contains additional information specific to the PaymentMethod type.
    """

    acss_debit: Optional[AcssDebit] = None

    affirm: Optional[Affirm] = None

    afterpay_clearpay: Optional[AfterpayClearpay] = None

    alipay: Optional[Alipay] = None

    allow_redisplay: Optional[Literal["always", "limited", "unspecified"]] = None
    """
    This field indicates whether this payment method can be shown again to its
    customer in a checkout flow. Stripe products such as Checkout and Elements use
    this field to determine whether a payment method can be shown as a saved payment
    method in a checkout flow. The field defaults to “unspecified”.
    """

    alma: Optional[Alma] = None

    amazon_pay: Optional[AmazonPay] = None

    au_becs_debit: Optional[AuBecsDebit] = None

    bacs_debit: Optional[BacsDebit] = None

    bancontact: Optional[Bancontact] = None

    billie: Optional[Billie] = None

    blik: Optional[Blik] = None

    boleto: Optional[Boleto] = None

    card: Optional["PaymentMethodCard"] = None

    card_present: Optional[CardPresent] = None

    cashapp: Optional[Cashapp] = None

    crypto: Optional[Crypto] = None

    custom: Optional[Custom] = None

    customer: Optional[Customer] = None
    """The ID of the Customer to which this PaymentMethod is saved.

    This will not be set when the PaymentMethod has not been saved to a Customer.
    """

    customer_account: Optional[str] = None

    customer_balance: Optional[CustomerBalance] = None

    eps: Optional[Eps] = None

    fpx: Optional[Fpx] = None

    giropay: Optional[Giropay] = None

    grabpay: Optional[Grabpay] = None

    ideal: Optional[Ideal] = None

    interac_present: Optional[InteracPresent] = None

    kakao_pay: Optional[KakaoPay] = None

    klarna: Optional[Klarna] = None

    konbini: Optional[Konbini] = None

    kr_card: Optional[KrCard] = None

    link: Optional[Link] = None

    mb_way: Optional[MBWay] = None

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    mobilepay: Optional[Mobilepay] = None

    multibanco: Optional[Multibanco] = None

    naver_pay: Optional[NaverPay] = None

    nz_bank_account: Optional[NzBankAccount] = None

    oxxo: Optional[Oxxo] = None

    p24: Optional[P24] = None

    pay_by_bank: Optional[PayByBank] = None

    payco: Optional[Payco] = None

    paynow: Optional[Paynow] = None

    paypal: Optional[Paypal] = None

    payto: Optional[Payto] = None

    pix: Optional[Pix] = None

    promptpay: Optional[Promptpay] = None

    radar_options: Optional[RadarOptions] = None
    """Options to configure Radar.

    See [Radar Session](https://docs.stripe.com/radar/radar-session) for more
    information.
    """

    revolut_pay: Optional[RevolutPay] = None

    samsung_pay: Optional[SamsungPay] = None

    satispay: Optional[Satispay] = None

    sepa_debit: Optional["PaymentMethodSepaDebit"] = None

    sofort: Optional[Sofort] = None

    swish: Optional[Swish] = None

    twint: Optional[Twint] = None

    us_bank_account: Optional[UsBankAccount] = None

    wechat_pay: Optional[WechatPay] = None

    zip: Optional[Zip] = None


from . import customer
from .payment_method_card import PaymentMethodCard
from .payment_method_sepa_debit import PaymentMethodSepaDebit
