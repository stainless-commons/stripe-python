# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .payment_method_details_card_present_offline import PaymentMethodDetailsCardPresentOffline
from .payment_method_details_card_present_receipt import PaymentMethodDetailsCardPresentReceipt
from .payment_flows_private_payment_methods_card_present_common_wallet import (
    PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet,
)

__all__ = ["PaymentMethodDetailsCardPresent"]


class PaymentMethodDetailsCardPresent(BaseModel):
    exp_month: int
    """Two-digit number representing the card's expiration month."""

    exp_year: int
    """Four-digit number representing the card's expiration year."""

    incremental_authorization_supported: bool
    """
    Whether this [PaymentIntent](https://docs.stripe.com/api/payment_intents) is
    eligible for incremental authorizations. Request support using
    [request_incremental_authorization_support](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support).
    """

    overcapture_supported: bool
    """Defines whether the authorized amount can be over-captured or not"""

    amount_authorized: Optional[int] = None
    """The authorized amount"""

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

    capture_before: Optional[int] = None
    """
    When using manual capture, a future timestamp after which the charge will be
    automatically refunded if uncaptured.
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

    receipt: Optional[PaymentMethodDetailsCardPresentReceipt] = None

    wallet: Optional[PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet] = None
