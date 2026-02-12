# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .coupon import Coupon
from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.deleted_customer import DeletedCustomer

__all__ = ["DeletedDiscount", "Source", "SourceCoupon", "Customer", "PromotionCode"]

SourceCoupon: TypeAlias = Union[str, Coupon, None]


class Source(BaseModel):
    type: Literal["coupon"]
    """The source type of the discount."""

    coupon: Optional[SourceCoupon] = None
    """The coupon that was redeemed to create this discount."""


if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer, None])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    PromotionCode = TypeAliasType("PromotionCode", Union[str, "promotion_code.PromotionCode", None])
else:
    PromotionCode: TypeAlias = Union[str, "promotion_code.PromotionCode", None]


class DeletedDiscount(BaseModel):
    id: str
    """The ID of the discount object.

    Discounts cannot be fetched by ID. Use `expand[]=discounts` in API calls to
    expand discount IDs in an array.
    """

    deleted: Literal[True]
    """Always true for a deleted object"""

    object: Literal["discount"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    source: Source

    start: int
    """Date that the coupon was applied."""

    checkout_session: Optional[str] = None
    """
    The Checkout session that this coupon is applied to, if it is applied to a
    particular session in payment mode. Will not be present for subscription mode.
    """

    customer: Optional[Customer] = None
    """The ID of the customer associated with this discount."""

    customer_account: Optional[str] = None
    """The ID of the account representing the customer associated with this discount."""

    invoice: Optional[str] = None
    """
    The invoice that the discount's coupon was applied to, if it was applied
    directly to a particular invoice.
    """

    invoice_item: Optional[str] = None
    """
    The invoice item `id` (or invoice line item `id` for invoice line items of
    type='subscription') that the discount's coupon was applied to, if it was
    applied directly to a particular invoice item or invoice line item.
    """

    promotion_code: Optional[PromotionCode] = None
    """The promotion code applied to create this discount."""

    subscription: Optional[str] = None
    """
    The subscription that this coupon is applied to, if it is applied to a
    particular subscription.
    """

    subscription_item: Optional[str] = None
    """
    The subscription item that this coupon is applied to, if it is applied to a
    particular subscription item.
    """


from . import customer, promotion_code
