# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Coupon", "AppliesTo", "CurrencyOptions"]


class AppliesTo(BaseModel):
    products: List[str]
    """A list of product IDs this coupon applies to"""


class CurrencyOptions(BaseModel):
    amount_off: int
    """
    Amount (in the `currency` specified) that will be taken off the subtotal of any
    invoices for this customer.
    """


class Coupon(BaseModel):
    """
    A coupon contains information about a percent-off or amount-off discount you
    might want to apply to a customer. Coupons may be applied to [subscriptions](https://api.stripe.com#subscriptions), [invoices](https://api.stripe.com#invoices),
    [checkout sessions](https://docs.stripe.com/api/checkout/sessions), [quotes](https://api.stripe.com#quotes), and more. Coupons do not work with conventional one-off [charges](https://api.stripe.com#create_charge) or [payment intents](https://docs.stripe.com/api/payment_intents).
    """

    id: str
    """Unique identifier for the object."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    duration: Literal["forever", "once", "repeating"]
    """One of `forever`, `once`, or `repeating`.

    Describes how long a customer who applies this coupon will get the discount.
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["coupon"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    times_redeemed: int
    """Number of times this coupon has been applied to a customer."""

    valid: bool
    """
    Taking account of the above properties, whether this coupon can still be applied
    to a customer.
    """

    amount_off: Optional[int] = None
    """
    Amount (in the `currency` specified) that will be taken off the subtotal of any
    invoices for this customer.
    """

    applies_to: Optional[AppliesTo] = None

    currency: Optional[str] = None
    """
    If `amount_off` has been set, the three-letter
    [ISO code for the currency](https://stripe.com/docs/currencies) of the amount to
    take off.
    """

    currency_options: Optional[Dict[str, CurrencyOptions]] = None
    """Coupons defined in each available currency option.

    Each key must be a three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a
    [supported currency](https://stripe.com/docs/currencies).
    """

    duration_in_months: Optional[int] = None
    """If `duration` is `repeating`, the number of months the coupon applies.

    Null if coupon `duration` is `forever` or `once`.
    """

    max_redemptions: Optional[int] = None
    """
    Maximum number of times this coupon can be redeemed, in total, across all
    customers, before it is no longer valid.
    """

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    name: Optional[str] = None
    """Name of the coupon displayed to customers on for instance invoices or receipts."""

    percent_off: Optional[float] = None
    """
    Percent that will be taken off the subtotal of any invoices for this customer
    for the duration of the coupon. For example, a coupon with percent_off of 50
    will make a $ (or local equivalent)100 invoice $ (or local equivalent)50
    instead.
    """

    redeem_by: Optional[int] = None
    """Date after which the coupon can no longer be redeemed."""
