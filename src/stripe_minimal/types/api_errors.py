# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import source
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["APIErrors", "Source"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Source = TypeAliasType("Source", Union["BankAccount", "Card", source.Source])
else:
    Source: TypeAlias = Union["BankAccount", "Card", source.Source]


class APIErrors(BaseModel):
    type: Literal["api_error", "card_error", "idempotency_error", "invalid_request_error"]
    """The type of error returned.

    One of `api_error`, `card_error`, `idempotency_error`, or
    `invalid_request_error`
    """

    advice_code: Optional[str] = None
    """
    For card errors resulting from a card issuer decline, a short string indicating
    [how to proceed with an error](https://docs.stripe.com/declines#retrying-issuer-declines)
    if they provide one.
    """

    charge: Optional[str] = None
    """For card errors, the ID of the failed charge."""

    code: Optional[str] = None
    """
    For some errors that could be handled programmatically, a short string
    indicating the [error code](https://docs.stripe.com/error-codes) reported.
    """

    decline_code: Optional[str] = None
    """
    For card errors resulting from a card issuer decline, a short string indicating
    the
    [card issuer's reason for the decline](https://docs.stripe.com/declines#issuer-declines)
    if they provide one.
    """

    doc_url: Optional[str] = None
    """
    A URL to more information about the
    [error code](https://docs.stripe.com/error-codes) reported.
    """

    message: Optional[str] = None
    """A human-readable message providing more details about the error.

    For card errors, these messages can be shown to your users.
    """

    network_advice_code: Optional[str] = None
    """
    For card errors resulting from a card issuer decline, a 2 digit code which
    indicates the advice given to merchant by the card network on how to proceed
    with an error.
    """

    network_decline_code: Optional[str] = None
    """
    For payments declined by the network, an alphanumeric code which indicates the
    reason the payment failed.
    """

    param: Optional[str] = None
    """If the error is parameter-specific, the parameter related to the error.

    For example, you can use this to display a message near the correct form field.
    """

    payment_intent: Optional["PaymentIntent"] = None
    """
    A PaymentIntent guides you through the process of collecting a payment from your
    customer. We recommend that you create exactly one PaymentIntent for each order
    or customer session in your system. You can reference the PaymentIntent later to
    see the history of payment attempts for a particular session.

    A PaymentIntent transitions through
    [multiple statuses](/payments/paymentintents/lifecycle) throughout its lifetime
    as it interfaces with Stripe.js to perform authentication flows and ultimately
    creates at most one successful charge.

    Related guide:
    [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
    """

    payment_method: Optional["PaymentMethod"] = None
    """
    PaymentMethod objects represent your customer's payment instruments. You can use
    them with [PaymentIntents](https://docs.stripe.com/payments/payment-intents) to
    collect payments or save them to Customer objects to store instrument details
    for future payments.

    Related guides:
    [Payment Methods](https://docs.stripe.com/payments/payment-methods) and
    [More Payment Scenarios](https://docs.stripe.com/payments/more-payment-scenarios).
    """

    payment_method_type: Optional[str] = None
    """
    If the error is specific to the type of payment method, the payment method type
    that had a problem. This field is only populated for invoice-related errors.
    """

    request_log_url: Optional[str] = None
    """A URL to the request log entry in your dashboard."""

    setup_intent: Optional["SetupIntent"] = None
    """
    A SetupIntent guides you through the process of setting up and saving a
    customer's payment credentials for future payments. For example, you can use a
    SetupIntent to set up and save your customer's card without immediately
    collecting a payment. Later, you can use
    [PaymentIntents](https://api.stripe.com#payment_intents) to drive the payment
    flow.

    Create a SetupIntent when you're ready to collect your customer's payment
    credentials. Don't maintain long-lived, unconfirmed SetupIntents because they
    might not be valid. The SetupIntent transitions through multiple
    [statuses](https://docs.stripe.com/payments/intents#intent-statuses) as it
    guides you through the setup process.

    Successful SetupIntents result in payment credentials that are optimized for
    future payments. For example, cardholders in
    [certain regions](https://stripe.com/guides/strong-customer-authentication)
    might need to be run through
    [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication)
    during payment method collection to streamline later
    [off-session payments](https://docs.stripe.com/payments/setup-intents). If you
    use the SetupIntent with a
    [Customer](https://api.stripe.com#setup_intent_object-customer), it
    automatically attaches the resulting payment method to that Customer after
    successful setup. We recommend using SetupIntents or
    [setup_future_usage](https://api.stripe.com#payment_intent_object-setup_future_usage)
    on PaymentIntents to save payment methods to prevent saving invalid or
    unoptimized payment methods.

    By using SetupIntents, you can reduce friction for your customers, even as
    regulations change over time.

    Related guide:
    [Setup Intents API](https://docs.stripe.com/payments/setup-intents)
    """

    source: Optional[Source] = None
    """
    The [source object](https://docs.stripe.com/api/sources/object) for errors
    returned on a request involving a source.
    """


from .card import Card
from .bank_account import BankAccount
from .setup_intent import SetupIntent
from .payment_intent import PaymentIntent
from .payment_method import PaymentMethod
