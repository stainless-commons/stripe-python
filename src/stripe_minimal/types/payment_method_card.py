# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.address import Address

__all__ = [
    "PaymentMethodCard",
    "Checks",
    "Networks",
    "ThreeDSecureUsage",
    "Wallet",
    "WalletMasterpass",
    "WalletVisaCheckout",
]


class Checks(BaseModel):
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


class Networks(BaseModel):
    available: List[str]
    """
    All networks available for selection via
    [payment_method_options.card.network](/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-network).
    """

    preferred: Optional[str] = None
    """The preferred network for co-branded cards.

    Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if
    requested network is not valid for the card.
    """


class ThreeDSecureUsage(BaseModel):
    supported: bool
    """Whether 3D Secure is supported on this card."""


class WalletMasterpass(BaseModel):
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


class WalletVisaCheckout(BaseModel):
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


class Wallet(BaseModel):
    type: Literal[
        "amex_express_checkout", "apple_pay", "google_pay", "link", "masterpass", "samsung_pay", "visa_checkout"
    ]
    """
    The type of the card wallet, one of `amex_express_checkout`, `apple_pay`,
    `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An
    additional hash is included on the Wallet subhash with a name matching this
    value. It contains additional information specific to the card wallet type.
    """

    amex_express_checkout: Optional[object] = None

    apple_pay: Optional[object] = None

    dynamic_last4: Optional[str] = None
    """
    (For tokenized numbers only.) The last four digits of the device account number.
    """

    google_pay: Optional[object] = None

    link: Optional[object] = None

    masterpass: Optional[WalletMasterpass] = None

    samsung_pay: Optional[object] = None

    visa_checkout: Optional[WalletVisaCheckout] = None


class PaymentMethodCard(BaseModel):
    brand: str
    """Card brand.

    Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`,
    `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
    """

    exp_month: int
    """Two-digit number representing the card's expiration month."""

    exp_year: int
    """Four-digit number representing the card's expiration year."""

    funding: str
    """Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`."""

    last4: str
    """The last four digits of the card."""

    checks: Optional[Checks] = None

    country: Optional[str] = None
    """Two-letter ISO code representing the country of the card.

    You could use this attribute to get a sense of the international breakdown of
    cards you've collected.
    """

    display_brand: Optional[str] = None
    """
    The brand to use when displaying the card, this accounts for customer's brand
    choice on dual-branded cards. Can be `american_express`, `cartes_bancaires`,
    `diners_club`, `discover`, `eftpos_australia`, `interac`, `jcb`, `mastercard`,
    `union_pay`, `visa`, or `other` and may contain more values in the future.
    """

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

    generated_from: Optional["PaymentMethodCardGeneratedCard"] = None

    networks: Optional[Networks] = None

    regulated_status: Optional[Literal["regulated", "unregulated"]] = None
    """Status of a card based on the card issuer."""

    three_d_secure_usage: Optional[ThreeDSecureUsage] = None

    wallet: Optional[Wallet] = None


from .payment_method_card_generated_card import PaymentMethodCardGeneratedCard
