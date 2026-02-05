# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import TypeAlias, TypeAliasType

from . import coupon, discount, promotion_code
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["StackableDiscount", "Coupon", "Discount", "PromotionCode"]

Coupon: TypeAlias = Union[str, coupon.Coupon, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Discount = TypeAliasType("Discount", Union[str, "discount.Discount", None])
else:
    Discount: TypeAlias = Union[str, "discount.Discount", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    PromotionCode = TypeAliasType("PromotionCode", Union[str, "promotion_code.PromotionCode", None])
else:
    PromotionCode: TypeAlias = Union[str, "promotion_code.PromotionCode", None]


class StackableDiscount(BaseModel):
    coupon: Optional[Coupon] = None
    """ID of the coupon to create a new discount for."""

    discount: Optional[Discount] = None
    """ID of an existing discount on the object (or one of its ancestors) to reuse."""

    promotion_code: Optional[PromotionCode] = None
    """ID of the promotion code to create a new discount for."""


from . import coupon, discount, promotion_code
