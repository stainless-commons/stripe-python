# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .coupon import Coupon
from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.deleted_customer import DeletedCustomer

__all__ = ["PromotionCode", "Promotion", "PromotionCoupon", "Restrictions", "RestrictionsCurrencyOptions", "Customer"]

PromotionCoupon: TypeAlias = Union[str, Coupon, None]


class Promotion(BaseModel):
    type: Literal["coupon"]
    """The type of promotion."""

    coupon: Optional[PromotionCoupon] = None
    """If promotion `type` is `coupon`, the coupon for this promotion."""


class RestrictionsCurrencyOptions(BaseModel):
    minimum_amount: int
    """
    Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a
    purchase must be $100 or more to work).
    """


class Restrictions(BaseModel):
    first_time_transaction: bool
    """
    A Boolean indicating if the Promotion Code should only be redeemed for Customers
    without any successful payments or invoices
    """

    currency_options: Optional[Dict[str, RestrictionsCurrencyOptions]] = None
    """Promotion code restrictions defined in each available currency option.

    Each key must be a three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a
    [supported currency](https://stripe.com/docs/currencies).
    """

    minimum_amount: Optional[int] = None
    """
    Minimum amount required to redeem this Promotion Code into a Coupon (e.g., a
    purchase must be $100 or more to work).
    """

    minimum_amount_currency: Optional[str] = None
    """Three-letter [ISO code](https://stripe.com/docs/currencies) for minimum_amount"""


if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer, None])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer, None]


class PromotionCode(BaseModel):
    """
    A Promotion Code represents a customer-redeemable code for an underlying promotion.
    You can create multiple codes for a single promotion.

    If you enable promotion codes in your [customer portal configuration](https://docs.stripe.com/customer-management/configure-portal), then customers can redeem a code themselves when updating a subscription in the portal.
    Customers can also view the currently active promotion codes and coupons on each of their subscriptions in the portal.
    """

    id: str
    """Unique identifier for the object."""

    active: bool
    """Whether the promotion code is currently active.

    A promotion code is only active if the coupon is also valid.
    """

    code: str
    """The customer-facing code.

    Regardless of case, this code must be unique across all active promotion codes
    for each customer. Valid characters are lower case letters (a-z), upper case
    letters (A-Z), and digits (0-9).
    """

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["promotion_code"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    promotion: Promotion

    restrictions: Restrictions

    times_redeemed: int
    """Number of times this promotion code has been used."""

    customer: Optional[Customer] = None
    """The customer who can use this promotion code."""

    customer_account: Optional[str] = None
    """The account representing the customer who can use this promotion code."""

    expires_at: Optional[int] = None
    """Date at which the promotion code can no longer be redeemed."""

    max_redemptions: Optional[int] = None
    """Maximum number of times this promotion code can be redeemed."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """


from . import customer
