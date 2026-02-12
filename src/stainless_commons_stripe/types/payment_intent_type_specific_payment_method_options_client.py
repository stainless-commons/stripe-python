# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .payment_flows_installment_options import PaymentFlowsInstallmentOptions
from .payment_method_options_card_present_routing import PaymentMethodOptionsCardPresentRouting
from .payment_intent_payment_method_options_mandate_options_payto import (
    PaymentIntentPaymentMethodOptionsMandateOptionsPayto,
)

__all__ = ["PaymentIntentTypeSpecificPaymentMethodOptionsClient"]


class PaymentIntentTypeSpecificPaymentMethodOptionsClient(BaseModel):
    capture_method: Optional[Literal["manual", "manual_preferred"]] = None
    """Controls when the funds will be captured from the customer's account."""

    installments: Optional[PaymentFlowsInstallmentOptions] = None

    mandate_options: Optional[PaymentIntentPaymentMethodOptionsMandateOptionsPayto] = None

    request_incremental_authorization_support: Optional[bool] = None
    """
    Request ability to
    [increment](https://docs.stripe.com/terminal/features/incremental-authorizations)
    this PaymentIntent if the combination of MCC and card brand is eligible. Check
    [incremental_authorization_supported](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported)
    in the [Confirm](https://docs.stripe.com/api/payment_intents/confirm) response
    to verify support.
    """

    require_cvc_recollection: Optional[bool] = None
    """
    When enabled, using a card that is attached to a customer will require the CVC
    to be provided again (i.e. using the cvc_token parameter).
    """

    routing: Optional[PaymentMethodOptionsCardPresentRouting] = None

    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """

    verification_method: Optional[Literal["automatic", "instant", "microdeposits"]] = None
    """Bank account verification method."""
