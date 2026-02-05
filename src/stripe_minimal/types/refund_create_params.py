# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["RefundCreateParams"]


class RefundCreateParams(TypedDict, total=False):
    amount: int

    charge: str
    """The identifier of the charge to refund."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: str
    """Customer whose customer balance to refund from."""

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    instructions_email: str
    """
    For payment methods without native refund support (e.g., Konbini, PromptPay),
    use this email from the customer to receive refund instructions.
    """

    metadata: Union[Dict[str, str], Literal[""]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Individual keys can be unset by posting an
    empty value to them. All keys can be unset by posting an empty value to
    `metadata`.
    """

    origin: Literal["customer_balance"]
    """Origin of the refund"""

    payment_intent: str
    """The identifier of the PaymentIntent to refund."""

    reason: Literal["duplicate", "fraudulent", "requested_by_customer"]
    """String indicating the reason for the refund.

    If set, possible values are `duplicate`, `fraudulent`, and
    `requested_by_customer`. If you believe the charge to be fraudulent, specifying
    `fraudulent` as the reason will add the associated card and email to your
    [block lists](https://docs.stripe.com/radar/lists), and will also help us
    improve our fraud detection algorithms.
    """

    refund_application_fee: bool
    """
    Boolean indicating whether the application fee should be refunded when refunding
    this charge. If a full charge refund is given, the full application fee will be
    refunded. Otherwise, the application fee will be refunded in an amount
    proportional to the amount of the charge refunded. An application fee can be
    refunded only by the application that created the charge.
    """

    reverse_transfer: bool
    """
    Boolean indicating whether the transfer should be reversed when refunding this
    charge. The transfer will be reversed proportionally to the amount being
    refunded (either the entire or partial amount).

    A transfer can be reversed only by the application that created the charge.
    """
