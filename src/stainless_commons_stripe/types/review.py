# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["Review", "Charge", "IPAddressLocation", "PaymentIntent", "Session"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Charge = TypeAliasType("Charge", Union[str, "charge.Charge", None])
else:
    Charge: TypeAlias = Union[str, "charge.Charge", None]


class IPAddressLocation(BaseModel):
    city: Optional[str] = None
    """The city where the payment originated."""

    country: Optional[str] = None
    """Two-letter ISO code representing the country where the payment originated."""

    latitude: Optional[float] = None
    """The geographic latitude where the payment originated."""

    longitude: Optional[float] = None
    """The geographic longitude where the payment originated."""

    region: Optional[str] = None
    """The state/county/province/region where the payment originated."""


if TYPE_CHECKING or not PYDANTIC_V1:
    PaymentIntent = TypeAliasType("PaymentIntent", Union[str, "payment_intent.PaymentIntent"])
else:
    PaymentIntent: TypeAlias = Union[str, "payment_intent.PaymentIntent"]


class Session(BaseModel):
    browser: Optional[str] = None
    """The browser used in this browser session (e.g., `Chrome`)."""

    device: Optional[str] = None
    """
    Information about the device used for the browser session (e.g.,
    `Samsung SM-G930T`).
    """

    platform: Optional[str] = None
    """The platform for the browser session (e.g., `Macintosh`)."""

    version: Optional[str] = None
    """The version for the browser session (e.g., `61.0.3163.100`)."""


class Review(BaseModel):
    """
    Reviews can be used to supplement automated fraud detection with human expertise.

    Learn more about [Radar](/radar) and reviewing payments
    [here](https://docs.stripe.com/radar/reviews).
    """

    id: str
    """Unique identifier for the object."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["review"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    open: bool
    """If `true`, the review needs action."""

    opened_reason: Literal["manual", "rule"]
    """The reason the review was opened. One of `rule` or `manual`."""

    reason: str
    """The reason the review is currently open or closed.

    One of `rule`, `manual`, `approved`, `refunded`, `refunded_as_fraud`,
    `disputed`, `redacted`, `canceled`, `payment_never_settled`, or `acknowledged`.
    """

    billing_zip: Optional[str] = None
    """The ZIP or postal code of the card used, if applicable."""

    charge: Optional[Charge] = None
    """The charge associated with this review."""

    closed_reason: Optional[
        Literal[
            "acknowledged",
            "approved",
            "canceled",
            "disputed",
            "payment_never_settled",
            "redacted",
            "refunded",
            "refunded_as_fraud",
        ]
    ] = None
    """The reason the review was closed, or null if it has not yet been closed.

    One of `approved`, `refunded`, `refunded_as_fraud`, `disputed`, `redacted`,
    `canceled`, `payment_never_settled`, or `acknowledged`.
    """

    ip_address: Optional[str] = None
    """The IP address where the payment originated."""

    ip_address_location: Optional[IPAddressLocation] = None

    payment_intent: Optional[PaymentIntent] = None
    """The PaymentIntent ID associated with this review, if one exists."""

    session: Optional[Session] = None


from . import charge, payment_intent
