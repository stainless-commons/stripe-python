# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SetupAttemptPaymentMethodDetails", "Card", "CardChecks", "CardThreeDSecure", "CardWallet", "NaverPay"]


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


class CardWallet(BaseModel):
    type: Literal["apple_pay", "google_pay", "link"]
    """The type of the card wallet, one of `apple_pay`, `google_pay`, or `link`.

    An additional hash is included on the Wallet subhash with a name matching this
    value. It contains additional information specific to the card wallet type.
    """

    apple_pay: Optional[object] = None

    google_pay: Optional[object] = None


class Card(BaseModel):
    brand: Optional[str] = None
    """Card brand.

    Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`,
    `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
    """

    checks: Optional[CardChecks] = None

    country: Optional[str] = None
    """Two-letter ISO code representing the country of the card.

    You could use this attribute to get a sense of the international breakdown of
    cards you've collected.
    """

    exp_month: Optional[int] = None
    """Two-digit number representing the card's expiration month."""

    exp_year: Optional[int] = None
    """Four-digit number representing the card's expiration year."""

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

    last4: Optional[str] = None
    """The last four digits of the card."""

    network: Optional[str] = None
    """Identifies which network this charge was processed on.

    Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`,
    `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """

    three_d_secure: Optional[CardThreeDSecure] = None

    wallet: Optional[CardWallet] = None


class NaverPay(BaseModel):
    buyer_id: Optional[str] = None
    """Uniquely identifies this particular Naver Pay account.

    You can use this attribute to check whether two Naver Pay accounts are the same.
    """


class SetupAttemptPaymentMethodDetails(BaseModel):
    type: str
    """The type of the payment method used in the SetupIntent (e.g., `card`).

    An additional hash is included on `payment_method_details` with a name matching
    this value. It contains confirmation-specific information for the payment
    method.
    """

    acss_debit: Optional[object] = None

    amazon_pay: Optional[object] = None

    au_becs_debit: Optional[object] = None

    bacs_debit: Optional[object] = None

    bancontact: Optional["PaymentMethodDetailsBancontactSetupAttempt"] = None

    boleto: Optional[object] = None

    card: Optional[Card] = None

    card_present: Optional["SetupAttemptPaymentMethodDetailsCardPresent"] = None

    cashapp: Optional[object] = None

    ideal: Optional["PaymentMethodDetailsIdealSetupAttempt"] = None

    kakao_pay: Optional[object] = None

    klarna: Optional[object] = None

    kr_card: Optional[object] = None

    link: Optional[object] = None

    naver_pay: Optional[NaverPay] = None

    nz_bank_account: Optional[object] = None

    paypal: Optional[object] = None

    payto: Optional[object] = None

    revolut_pay: Optional[object] = None

    sepa_debit: Optional[object] = None

    sofort: Optional["PaymentMethodDetailsSofortSetupAttempt"] = None

    us_bank_account: Optional[object] = None


from .payment_method_details_ideal_setup_attempt import PaymentMethodDetailsIdealSetupAttempt
from .payment_method_details_sofort_setup_attempt import PaymentMethodDetailsSofortSetupAttempt
from .payment_method_details_bancontact_setup_attempt import PaymentMethodDetailsBancontactSetupAttempt
from .setup_attempt_payment_method_details_card_present import SetupAttemptPaymentMethodDetailsCardPresent
