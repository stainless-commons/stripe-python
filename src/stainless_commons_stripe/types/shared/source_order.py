# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .shipping import Shipping
from ..._models import BaseModel
from .source_order_item import SourceOrderItem

__all__ = ["SourceOrder"]


class SourceOrder(BaseModel):
    amount: int
    """
    A positive integer in the smallest currency unit (that is, 100 cents for $1.00,
    or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total
    amount for the order.
    """

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    email: Optional[str] = None
    """The email address of the customer placing the order."""

    items: Optional[List[SourceOrderItem]] = None
    """List of items constituting the order."""

    shipping: Optional[Shipping] = None
