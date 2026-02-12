# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.address import Address
from .shared.payment_method_details_card_present import PaymentMethodDetailsCardPresent
from .shared.payment_method_details_passthrough_card import PaymentMethodDetailsPassthroughCard
from .shared.payment_method_details_card_installments_plan import PaymentMethodDetailsCardInstallmentsPlan

__all__ = [
    "PaymentMethodDetails",
    "ACHCreditTransfer",
    "ACHDebit",
    "AcssDebit",
    "Affirm",
    "AfterpayClearpay",
    "Alipay",
    "Alma",
    "AlmaInstallments",
    "AmazonPay",
    "AmazonPayFunding",
    "AuBecsDebit",
    "BacsDebit",
    "Billie",
    "Blik",
    "Boleto",
    "Card",
    "CardChecks",
    "CardExtendedAuthorization",
    "CardIncrementalAuthorization",
    "CardInstallments",
    "CardMulticapture",
    "CardNetworkToken",
    "CardOvercapture",
    "CardThreeDSecure",
    "CardWallet",
    "CardWalletAmexExpressCheckout",
    "CardWalletApplePay",
    "CardWalletGooglePay",
    "CardWalletLink",
    "CardWalletMasterpass",
    "CardWalletSamsungPay",
    "CardWalletVisaCheckout",
    "Cashapp",
    "Crypto",
    "CustomerBalance",
    "Eps",
    "Fpx",
    "Giropay",
    "Grabpay",
    "InteracPresent",
    "InteracPresentReceipt",
    "KakaoPay",
    "Klarna",
    "KlarnaPayerDetails",
    "KlarnaPayerDetailsAddress",
    "Konbini",
    "KonbiniStore",
    "KrCard",
    "Link",
    "MBWay",
    "Mobilepay",
    "MobilepayCard",
    "Multibanco",
    "NaverPay",
    "NzBankAccount",
    "Oxxo",
    "P24",
    "PayByBank",
    "Payco",
    "Paynow",
    "Paypal",
    "PaypalSellerProtection",
    "Payto",
    "Pix",
    "Promptpay",
    "RevolutPay",
    "RevolutPayFunding",
    "SamsungPay",
    "Satispay",
    "SepaDebit",
    "StripeAccount",
    "Swish",
    "Twint",
    "Wechat",
    "WechatPay",
    "Zip",
]


class ACHCreditTransfer(BaseModel):
    account_number: Optional[str] = None
    """Account number to transfer funds to."""

    bank_name: Optional[str] = None
    """Name of the bank associated with the routing number."""

    routing_number: Optional[str] = None
    """Routing transit number for the bank account to transfer funds to."""

    swift_code: Optional[str] = None
    """SWIFT code of the bank associated with the routing number."""


class ACHDebit(BaseModel):
    account_holder_type: Optional[Literal["company", "individual"]] = None
    """Type of entity that holds the account.

    This can be either `individual` or `company`.
    """

    bank_name: Optional[str] = None
    """Name of the bank associated with the bank account."""

    country: Optional[str] = None
    """Two-letter ISO code representing the country the bank account is located in."""

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    last4: Optional[str] = None
    """Last four digits of the bank account number."""

    routing_number: Optional[str] = None
    """Routing transit number of the bank account."""


class AcssDebit(BaseModel):
    bank_name: Optional[str] = None
    """Name of the bank associated with the bank account."""

    expected_debit_date: Optional[str] = None
    """Estimated date to debit the customer's bank account.

    A date string in YYYY-MM-DD format.
    """

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    institution_number: Optional[str] = None
    """Institution number of the bank account"""

    last4: Optional[str] = None
    """Last four digits of the bank account number."""

    mandate: Optional[str] = None
    """ID of the mandate used to make this payment."""

    transit_number: Optional[str] = None
    """Transit number of the bank account."""


class Affirm(BaseModel):
    location: Optional[str] = None
    """
    ID of the [location](https://docs.stripe.com/api/terminal/locations) that this
    transaction's reader is assigned to.
    """

    reader: Optional[str] = None
    """
    ID of the [reader](https://docs.stripe.com/api/terminal/readers) this
    transaction was made on.
    """

    transaction_id: Optional[str] = None
    """The Affirm transaction ID associated with this payment."""


class AfterpayClearpay(BaseModel):
    order_id: Optional[str] = None
    """The Afterpay order ID associated with this payment intent."""

    reference: Optional[str] = None
    """Order identifier shown to the merchant in Afterpay’s online portal."""


class Alipay(BaseModel):
    buyer_id: Optional[str] = None
    """Uniquely identifies this particular Alipay account.

    You can use this attribute to check whether two Alipay accounts are the same.
    """

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular Alipay account.

    You can use this attribute to check whether two Alipay accounts are the same.
    """

    transaction_id: Optional[str] = None
    """Transaction ID of this particular Alipay transaction."""


class AlmaInstallments(BaseModel):
    count: int
    """The number of installments."""


class Alma(BaseModel):
    installments: Optional[AlmaInstallments] = None

    transaction_id: Optional[str] = None
    """The Alma transaction ID associated with this payment."""


class AmazonPayFunding(BaseModel):
    card: Optional[PaymentMethodDetailsPassthroughCard] = None

    type: Optional[Literal["card"]] = None
    """funding type of the underlying payment method."""


class AmazonPay(BaseModel):
    funding: Optional[AmazonPayFunding] = None

    transaction_id: Optional[str] = None
    """The Amazon Pay transaction ID associated with this payment."""


class AuBecsDebit(BaseModel):
    bsb_number: Optional[str] = None
    """Bank-State-Branch number of the bank account."""

    expected_debit_date: Optional[str] = None
    """Estimated date to debit the customer's bank account.

    A date string in YYYY-MM-DD format.
    """

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    last4: Optional[str] = None
    """Last four digits of the bank account number."""

    mandate: Optional[str] = None
    """ID of the mandate used to make this payment."""


class BacsDebit(BaseModel):
    expected_debit_date: Optional[str] = None
    """Estimated date to debit the customer's bank account.

    A date string in YYYY-MM-DD format.
    """

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    last4: Optional[str] = None
    """Last four digits of the bank account number."""

    mandate: Optional[str] = None
    """ID of the mandate used to make this payment."""

    sort_code: Optional[str] = None
    """Sort code of the bank account. (e.g., `10-20-30`)"""


class Billie(BaseModel):
    transaction_id: Optional[str] = None
    """The Billie transaction ID associated with this payment."""


class Blik(BaseModel):
    buyer_id: Optional[str] = None
    """A unique and immutable identifier assigned by BLIK to every buyer."""


class Boleto(BaseModel):
    tax_id: str
    """
    The tax ID of the customer (CPF for individuals consumers or CNPJ for businesses
    consumers)
    """


class CardChecks(BaseModel):
    address_line1_check: Optional[str] = None
    """
    If a address line1 was provided, results of the check, one of `pass`, `fail`,
    `unavailable`, or `unchecked`.
    """

    address_postal_code_check: Optional[str] = None
    """
    If a address postal code was provided, results of the check, one of `pass`,
    `fail`, `unavailable`, or `unchecked`.
    """

    cvc_check: Optional[str] = None
    """
    If a CVC was provided, results of the check, one of `pass`, `fail`,
    `unavailable`, or `unchecked`.
    """


class CardExtendedAuthorization(BaseModel):
    status: Literal["disabled", "enabled"]
    """
    Indicates whether or not the capture window is extended beyond the standard
    authorization.
    """


class CardIncrementalAuthorization(BaseModel):
    status: Literal["available", "unavailable"]
    """Indicates whether or not the incremental authorization feature is supported."""


class CardInstallments(BaseModel):
    plan: Optional[PaymentMethodDetailsCardInstallmentsPlan] = None


class CardMulticapture(BaseModel):
    status: Literal["available", "unavailable"]
    """Indicates whether or not multiple captures are supported."""


class CardNetworkToken(BaseModel):
    used: bool
    """
    Indicates if Stripe used a network token, either user provided or Stripe managed
    when processing the transaction.
    """


class CardOvercapture(BaseModel):
    maximum_amount_capturable: int
    """The maximum amount that can be captured."""

    status: Literal["available", "unavailable"]
    """Indicates whether or not the authorized amount can be over-captured."""


class CardThreeDSecure(BaseModel):
    authentication_flow: Optional[Literal["challenge", "frictionless"]] = None
    """
    For authenticated transactions: how the customer was authenticated by the
    issuing bank.
    """

    electronic_commerce_indicator: Optional[Literal["01", "02", "05", "06", "07"]] = None
    """The Electronic Commerce Indicator (ECI).

    A protocol-level field indicating what degree of authentication was performed.
    """

    exemption_indicator: Optional[Literal["low_risk", "none"]] = None
    """
    The exemption requested via 3DS and accepted by the issuer at authentication
    time.
    """

    exemption_indicator_applied: Optional[bool] = None
    """Whether Stripe requested the value of `exemption_indicator` in the transaction.

    This will depend on the outcome of Stripe's internal risk assessment.
    """

    result: Optional[
        Literal["attempt_acknowledged", "authenticated", "exempted", "failed", "not_supported", "processing_error"]
    ] = None
    """Indicates the outcome of 3D Secure authentication."""

    result_reason: Optional[
        Literal[
            "abandoned",
            "bypassed",
            "canceled",
            "card_not_enrolled",
            "network_not_supported",
            "protocol_error",
            "rejected",
        ]
    ] = None
    """
    Additional information about why 3D Secure succeeded or failed based on the
    `result`.
    """

    transaction_id: Optional[str] = None
    """
    The 3D Secure 1 XID or 3D Secure 2 Directory Server Transaction ID (dsTransId)
    for this payment.
    """

    version: Optional[Literal["1.0.2", "2.1.0", "2.2.0", "2.3.0", "2.3.1"]] = None
    """The version of 3D Secure that was used."""


class CardWalletAmexExpressCheckout(BaseModel):
    pass


class CardWalletApplePay(BaseModel):
    pass


class CardWalletGooglePay(BaseModel):
    pass


class CardWalletLink(BaseModel):
    pass


class CardWalletMasterpass(BaseModel):
    billing_address: Optional[Address] = None

    email: Optional[str] = None
    """Owner's verified email.

    Values are verified or provided by the wallet directly (if supported) at the
    time of authorization or settlement. They cannot be set or mutated.
    """

    name: Optional[str] = None
    """Owner's verified full name.

    Values are verified or provided by the wallet directly (if supported) at the
    time of authorization or settlement. They cannot be set or mutated.
    """

    shipping_address: Optional[Address] = None


class CardWalletSamsungPay(BaseModel):
    pass


class CardWalletVisaCheckout(BaseModel):
    billing_address: Optional[Address] = None

    email: Optional[str] = None
    """Owner's verified email.

    Values are verified or provided by the wallet directly (if supported) at the
    time of authorization or settlement. They cannot be set or mutated.
    """

    name: Optional[str] = None
    """Owner's verified full name.

    Values are verified or provided by the wallet directly (if supported) at the
    time of authorization or settlement. They cannot be set or mutated.
    """

    shipping_address: Optional[Address] = None


class CardWallet(BaseModel):
    type: Literal[
        "amex_express_checkout", "apple_pay", "google_pay", "link", "masterpass", "samsung_pay", "visa_checkout"
    ]
    """
    The type of the card wallet, one of `amex_express_checkout`, `apple_pay`,
    `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An
    additional hash is included on the Wallet subhash with a name matching this
    value. It contains additional information specific to the card wallet type.
    """

    amex_express_checkout: Optional[CardWalletAmexExpressCheckout] = None

    apple_pay: Optional[CardWalletApplePay] = None

    dynamic_last4: Optional[str] = None
    """
    (For tokenized numbers only.) The last four digits of the device account number.
    """

    google_pay: Optional[CardWalletGooglePay] = None

    link: Optional[CardWalletLink] = None

    masterpass: Optional[CardWalletMasterpass] = None

    samsung_pay: Optional[CardWalletSamsungPay] = None

    visa_checkout: Optional[CardWalletVisaCheckout] = None


class Card(BaseModel):
    exp_month: int
    """Two-digit number representing the card's expiration month."""

    exp_year: int
    """Four-digit number representing the card's expiration year."""

    amount_authorized: Optional[int] = None
    """The authorized amount."""

    authorization_code: Optional[str] = None
    """Authorization code on the charge."""

    brand: Optional[str] = None
    """Card brand.

    Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`,
    `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
    """

    capture_before: Optional[int] = None
    """
    When using manual capture, a future timestamp at which the charge will be
    automatically refunded if uncaptured.
    """

    checks: Optional[CardChecks] = None

    country: Optional[str] = None
    """Two-letter ISO code representing the country of the card.

    You could use this attribute to get a sense of the international breakdown of
    cards you've collected.
    """

    extended_authorization: Optional[CardExtendedAuthorization] = None

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

    incremental_authorization: Optional[CardIncrementalAuthorization] = None

    installments: Optional[CardInstallments] = None

    last4: Optional[str] = None
    """The last four digits of the card."""

    mandate: Optional[str] = None
    """ID of the mandate used to make this payment or created by it."""

    multicapture: Optional[CardMulticapture] = None

    network: Optional[str] = None
    """Identifies which network this charge was processed on.

    Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`,
    `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """

    network_token: Optional[CardNetworkToken] = None

    network_transaction_id: Optional[str] = None
    """This is used by the financial networks to identify a transaction.

    Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and
    American Express calls this the Acquirer Reference Data. This value will be
    present if it is returned by the financial network in the authorization
    response, and null otherwise.
    """

    overcapture: Optional[CardOvercapture] = None

    regulated_status: Optional[Literal["regulated", "unregulated"]] = None
    """Status of a card based on the card issuer."""

    three_d_secure: Optional[CardThreeDSecure] = None

    wallet: Optional[CardWallet] = None


class Cashapp(BaseModel):
    buyer_id: Optional[str] = None
    """A unique and immutable identifier assigned by Cash App to every buyer."""

    cashtag: Optional[str] = None
    """A public identifier for buyers using Cash App."""

    transaction_id: Optional[str] = None
    """A unique and immutable identifier of payments assigned by Cash App"""


class Crypto(BaseModel):
    buyer_address: Optional[str] = None
    """The wallet address of the customer."""

    network: Optional[Literal["base", "ethereum", "polygon", "solana"]] = None
    """The blockchain network that the transaction was sent on."""

    token_currency: Optional[Literal["usdc", "usdg", "usdp"]] = None
    """The token currency that the transaction was sent with."""

    transaction_hash: Optional[str] = None
    """The blockchain transaction hash of the crypto payment."""


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

    verified_name: Optional[str] = None
    """Owner's verified full name.

    Values are verified or provided by EPS directly (if supported) at the time of
    authorization or settlement. They cannot be set or mutated. EPS rarely provides
    this information so the attribute is usually empty.
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
    """The customer's bank.

    Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`,
    `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`,
    `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`,
    `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`.
    """

    transaction_id: Optional[str] = None
    """Unique transaction id generated by FPX for every request from the merchant"""


class Giropay(BaseModel):
    bank_code: Optional[str] = None
    """Bank code of bank associated with the bank account."""

    bank_name: Optional[str] = None
    """Name of the bank associated with the bank account."""

    bic: Optional[str] = None
    """Bank Identifier Code of the bank associated with the bank account."""

    verified_name: Optional[str] = None
    """Owner's verified full name.

    Values are verified or provided by Giropay directly (if supported) at the time
    of authorization or settlement. They cannot be set or mutated. Giropay rarely
    provides this information so the attribute is usually empty.
    """


class Grabpay(BaseModel):
    transaction_id: Optional[str] = None
    """Unique transaction id generated by GrabPay"""


class InteracPresentReceipt(BaseModel):
    account_type: Optional[Literal["checking", "savings", "unknown"]] = None
    """The type of account being debited or credited"""

    application_cryptogram: Optional[str] = None
    """
    The Application Cryptogram, a unique value generated by the card to authenticate
    the transaction with issuers.
    """

    application_preferred_name: Optional[str] = None
    """
    The Application Identifier (AID) on the card used to determine which networks
    are eligible to process the transaction. Referenced from EMV tag 9F12, data
    encoded on the card's chip.
    """

    authorization_code: Optional[str] = None
    """Identifier for this transaction."""

    authorization_response_code: Optional[str] = None
    """EMV tag 8A. A code returned by the card issuer."""

    cardholder_verification_method: Optional[str] = None
    """Describes the method used by the cardholder to verify ownership of the card.

    One of the following: `approval`, `failure`, `none`, `offline_pin`,
    `offline_pin_and_signature`, `online_pin`, or `signature`.
    """

    dedicated_file_name: Optional[str] = None
    """
    Similar to the application_preferred_name, identifying the applications (AIDs)
    available on the card. Referenced from EMV tag 84.
    """

    terminal_verification_results: Optional[str] = None
    """
    A 5-byte string that records the checks and validations that occur between the
    card and the terminal. These checks determine how the terminal processes the
    transaction and what risk tolerance is acceptable. Referenced from EMV Tag 95.
    """

    transaction_status_information: Optional[str] = None
    """An indication of which steps were completed during the card read process.

    Referenced from EMV Tag 9B.
    """


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

    emv_auth_data: Optional[str] = None
    """Authorization response cryptogram."""

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

    generated_card: Optional[str] = None
    """
    ID of a card PaymentMethod generated from the card_present PaymentMethod that
    may be attached to a Customer for future transactions. Only present if it was
    possible to generate a card PaymentMethod.
    """

    issuer: Optional[str] = None
    """The name of the card's issuing bank."""

    last4: Optional[str] = None
    """The last four digits of the card."""

    network: Optional[str] = None
    """Identifies which network this charge was processed on.

    Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`,
    `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """

    network_transaction_id: Optional[str] = None
    """This is used by the financial networks to identify a transaction.

    Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and
    American Express calls this the Acquirer Reference Data. This value will be
    present if it is returned by the financial network in the authorization
    response, and null otherwise.
    """

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

    receipt: Optional[InteracPresentReceipt] = None


class KakaoPay(BaseModel):
    buyer_id: Optional[str] = None
    """A unique identifier for the buyer as determined by the local payment processor."""

    transaction_id: Optional[str] = None
    """The Kakao Pay transaction ID associated with this payment."""


class KlarnaPayerDetailsAddress(BaseModel):
    country: Optional[str] = None
    """The payer address country"""


class KlarnaPayerDetails(BaseModel):
    address: Optional[KlarnaPayerDetailsAddress] = None


class Klarna(BaseModel):
    payer_details: Optional[KlarnaPayerDetails] = None

    payment_method_category: Optional[str] = None
    """
    The Klarna payment method used for this transaction. Can be one of `pay_later`,
    `pay_now`, `pay_with_financing`, or `pay_in_installments`
    """

    preferred_locale: Optional[str] = None
    """
    Preferred language of the Klarna authorization page that the customer is
    redirected to. Can be one of `de-AT`, `en-AT`, `nl-BE`, `fr-BE`, `en-BE`,
    `de-DE`, `en-DE`, `da-DK`, `en-DK`, `es-ES`, `en-ES`, `fi-FI`, `sv-FI`, `en-FI`,
    `en-GB`, `en-IE`, `it-IT`, `en-IT`, `nl-NL`, `en-NL`, `nb-NO`, `en-NO`, `sv-SE`,
    `en-SE`, `en-US`, `es-US`, `fr-FR`, `en-FR`, `cs-CZ`, `en-CZ`, `ro-RO`, `en-RO`,
    `el-GR`, `en-GR`, `en-AU`, `en-NZ`, `en-CA`, `fr-CA`, `pl-PL`, `en-PL`, `pt-PT`,
    `en-PT`, `de-CH`, `fr-CH`, `it-CH`, or `en-CH`
    """


class KonbiniStore(BaseModel):
    chain: Optional[Literal["familymart", "lawson", "ministop", "seicomart"]] = None
    """The name of the convenience store chain where the payment was completed."""


class Konbini(BaseModel):
    store: Optional[KonbiniStore] = None


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

    buyer_id: Optional[str] = None
    """A unique identifier for the buyer as determined by the local payment processor."""

    last4: Optional[str] = None
    """The last four digits of the card.

    This may not be present for American Express cards.
    """

    transaction_id: Optional[str] = None
    """The Korean Card transaction ID associated with this payment."""


class Link(BaseModel):
    country: Optional[str] = None
    """
    Two-letter ISO code representing the funding source country beneath the Link
    payment. You could use this attribute to get a sense of international fees.
    """


class MBWay(BaseModel):
    pass


class MobilepayCard(BaseModel):
    brand: Optional[str] = None
    """Brand of the card used in the transaction"""

    country: Optional[str] = None
    """Two-letter ISO code representing the country of the card"""

    exp_month: Optional[int] = None
    """Two digit number representing the card's expiration month"""

    exp_year: Optional[int] = None
    """Two digit number representing the card's expiration year"""

    last4: Optional[str] = None
    """The last 4 digits of the card"""


class Mobilepay(BaseModel):
    card: Optional[MobilepayCard] = None


class Multibanco(BaseModel):
    entity: Optional[str] = None
    """Entity number associated with this Multibanco payment."""

    reference: Optional[str] = None
    """Reference number associated with this Multibanco payment."""


class NaverPay(BaseModel):
    buyer_id: Optional[str] = None
    """A unique identifier for the buyer as determined by the local payment processor."""

    transaction_id: Optional[str] = None
    """The Naver Pay transaction ID associated with this payment."""


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

    expected_debit_date: Optional[str] = None
    """Estimated date to debit the customer's bank account.

    A date string in YYYY-MM-DD format.
    """

    suffix: Optional[str] = None
    """The suffix of the bank account number."""


class Oxxo(BaseModel):
    number: Optional[str] = None
    """OXXO reference number"""


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
    """The customer's bank.

    Can be one of `ing`, `citi_handlowy`, `tmobile_usbugi_bankowe`, `plus_bank`,
    `etransfer_pocztowy24`, `banki_spbdzielcze`, `bank_nowy_bfg_sa`, `getin_bank`,
    `velobank`, `blik`, `noble_pay`, `ideabank`, `envelobank`,
    `santander_przelew24`, `nest_przelew`, `mbank_mtransfer`, `inteligo`,
    `pbac_z_ipko`, `bnp_paribas`, `credit_agricole`, `toyota_bank`, `bank_pekao_sa`,
    `volkswagen_bank`, `bank_millennium`, `alior_bank`, or `boz`.
    """

    reference: Optional[str] = None
    """Unique reference for this Przelewy24 payment."""

    verified_name: Optional[str] = None
    """Owner's verified full name.

    Values are verified or provided by Przelewy24 directly (if supported) at the
    time of authorization or settlement. They cannot be set or mutated. Przelewy24
    rarely provides this information so the attribute is usually empty.
    """


class PayByBank(BaseModel):
    pass


class Payco(BaseModel):
    buyer_id: Optional[str] = None
    """A unique identifier for the buyer as determined by the local payment processor."""

    transaction_id: Optional[str] = None
    """The Payco transaction ID associated with this payment."""


class Paynow(BaseModel):
    location: Optional[str] = None
    """
    ID of the [location](https://docs.stripe.com/api/terminal/locations) that this
    transaction's reader is assigned to.
    """

    reader: Optional[str] = None
    """
    ID of the [reader](https://docs.stripe.com/api/terminal/readers) this
    transaction was made on.
    """

    reference: Optional[str] = None
    """Reference number associated with this PayNow payment"""


class PaypalSellerProtection(BaseModel):
    status: Literal["eligible", "not_eligible", "partially_eligible"]
    """Indicates whether the transaction is eligible for PayPal's seller protection."""

    dispute_categories: Optional[List[Literal["fraudulent", "product_not_received"]]] = None
    """An array of conditions that are covered for the transaction, if applicable."""


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

    payer_name: Optional[str] = None
    """Owner's full name.

    Values provided by PayPal directly (if supported) at the time of authorization
    or settlement. They cannot be set or mutated.
    """

    seller_protection: Optional[PaypalSellerProtection] = None

    transaction_id: Optional[str] = None
    """A unique ID generated by PayPal for this transaction."""


class Payto(BaseModel):
    bsb_number: Optional[str] = None
    """Bank-State-Branch number of the bank account."""

    last4: Optional[str] = None
    """Last four digits of the bank account number."""

    mandate: Optional[str] = None
    """ID of the mandate used to make this payment."""

    pay_id: Optional[str] = None
    """The PayID alias for the bank account."""


class Pix(BaseModel):
    bank_transaction_id: Optional[str] = None
    """Unique transaction id generated by BCB"""


class Promptpay(BaseModel):
    reference: Optional[str] = None
    """Bill reference generated by PromptPay"""


class RevolutPayFunding(BaseModel):
    card: Optional[PaymentMethodDetailsPassthroughCard] = None

    type: Optional[Literal["card"]] = None
    """funding type of the underlying payment method."""


class RevolutPay(BaseModel):
    funding: Optional[RevolutPayFunding] = None

    transaction_id: Optional[str] = None
    """The Revolut Pay transaction ID associated with this payment."""


class SamsungPay(BaseModel):
    buyer_id: Optional[str] = None
    """A unique identifier for the buyer as determined by the local payment processor."""

    transaction_id: Optional[str] = None
    """The Samsung Pay transaction ID associated with this payment."""


class Satispay(BaseModel):
    transaction_id: Optional[str] = None
    """The Satispay transaction ID associated with this payment."""


class SepaDebit(BaseModel):
    bank_code: Optional[str] = None
    """Bank code of bank associated with the bank account."""

    branch_code: Optional[str] = None
    """Branch code of bank associated with the bank account."""

    country: Optional[str] = None
    """Two-letter ISO code representing the country the bank account is located in."""

    expected_debit_date: Optional[str] = None
    """Estimated date to debit the customer's bank account.

    A date string in YYYY-MM-DD format.
    """

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    last4: Optional[str] = None
    """Last four characters of the IBAN."""

    mandate: Optional[str] = None
    """
    Find the ID of the mandate used for this payment under the
    [payment_method_details.sepa_debit.mandate](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-sepa_debit-mandate)
    property on the Charge. Use this mandate ID to
    [retrieve the Mandate](https://docs.stripe.com/api/mandates/retrieve).
    """


class StripeAccount(BaseModel):
    pass


class Swish(BaseModel):
    fingerprint: Optional[str] = None
    """Uniquely identifies the payer's Swish account.

    You can use this attribute to check whether two Swish transactions were paid for
    by the same payer
    """

    payment_reference: Optional[str] = None
    """Payer bank reference number for the payment"""

    verified_phone_last4: Optional[str] = None
    """The last four digits of the Swish account phone number"""


class Twint(BaseModel):
    pass


class Wechat(BaseModel):
    pass


class WechatPay(BaseModel):
    fingerprint: Optional[str] = None
    """Uniquely identifies this particular WeChat Pay account.

    You can use this attribute to check whether two WeChat accounts are the same.
    """

    location: Optional[str] = None
    """
    ID of the [location](https://docs.stripe.com/api/terminal/locations) that this
    transaction's reader is assigned to.
    """

    reader: Optional[str] = None
    """
    ID of the [reader](https://docs.stripe.com/api/terminal/readers) this
    transaction was made on.
    """

    transaction_id: Optional[str] = None
    """Transaction ID of this particular WeChat Pay transaction."""


class Zip(BaseModel):
    pass


class PaymentMethodDetails(BaseModel):
    type: str
    """
    The type of transaction-specific details of the payment method used in the
    payment. See
    [PaymentMethod.type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
    for the full list of possible types. An additional hash is included on
    `payment_method_details` with a name matching this value. It contains
    information specific to the payment method.
    """

    ach_credit_transfer: Optional[ACHCreditTransfer] = None

    ach_debit: Optional[ACHDebit] = None

    acss_debit: Optional[AcssDebit] = None

    affirm: Optional[Affirm] = None

    afterpay_clearpay: Optional[AfterpayClearpay] = None

    alipay: Optional[Alipay] = None

    alma: Optional[Alma] = None

    amazon_pay: Optional[AmazonPay] = None

    au_becs_debit: Optional[AuBecsDebit] = None

    bacs_debit: Optional[BacsDebit] = None

    bancontact: Optional["PaymentMethodDetailsBancontactDispute"] = None

    billie: Optional[Billie] = None

    blik: Optional[Blik] = None

    boleto: Optional[Boleto] = None

    card: Optional[Card] = None

    card_present: Optional[PaymentMethodDetailsCardPresent] = None

    cashapp: Optional[Cashapp] = None

    crypto: Optional[Crypto] = None

    customer_balance: Optional[CustomerBalance] = None

    eps: Optional[Eps] = None

    fpx: Optional[Fpx] = None

    giropay: Optional[Giropay] = None

    grabpay: Optional[Grabpay] = None

    ideal: Optional["PaymentMethodDetailsIdealDispute"] = None

    interac_present: Optional[InteracPresent] = None

    kakao_pay: Optional[KakaoPay] = None

    klarna: Optional[Klarna] = None

    konbini: Optional[Konbini] = None

    kr_card: Optional[KrCard] = None

    link: Optional[Link] = None

    mb_way: Optional[MBWay] = None

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

    revolut_pay: Optional[RevolutPay] = None

    samsung_pay: Optional[SamsungPay] = None

    satispay: Optional[Satispay] = None

    sepa_debit: Optional[SepaDebit] = None

    sofort: Optional["PaymentMethodDetailsSofortDispute"] = None

    stripe_account: Optional[StripeAccount] = None

    swish: Optional[Swish] = None

    twint: Optional[Twint] = None

    us_bank_account: Optional["PaymentMethodDetailsUsBankAccount"] = None

    wechat: Optional[Wechat] = None

    wechat_pay: Optional[WechatPay] = None

    zip: Optional[Zip] = None


from .payment_method_details_ideal_dispute import PaymentMethodDetailsIdealDispute
from .payment_method_details_sofort_dispute import PaymentMethodDetailsSofortDispute
from .payment_method_details_us_bank_account import PaymentMethodDetailsUsBankAccount
from .payment_method_details_bancontact_dispute import PaymentMethodDetailsBancontactDispute
