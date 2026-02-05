# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["DiscountsResourceDiscountAmount", "Discount"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Discount = TypeAliasType("Discount", Union[str, "discount.Discount", "DeletedDiscount"])
else:
    Discount: TypeAlias = Union[str, "discount.Discount", "DeletedDiscount"]


class DiscountsResourceDiscountAmount(BaseModel):
    amount: int
    """The amount, in cents (or local equivalent), of the discount."""

    discount: Discount
    """The discount that was applied to get this discount amount."""


from . import discount
from .deleted_discount import DeletedDiscount
