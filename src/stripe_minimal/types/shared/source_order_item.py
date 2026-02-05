# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceOrderItem"]


class SourceOrderItem(BaseModel):
    amount: Optional[int] = None
    """The amount (price) for this order item."""

    currency: Optional[str] = None
    """This currency of this order item. Required when `amount` is present."""

    description: Optional[str] = None
    """Human-readable description for this order item."""

    parent: Optional[str] = None
    """The ID of the associated object for this line item.

    Expandable if not null (e.g., expandable to a SKU).
    """

    quantity: Optional[int] = None
    """The quantity of this order item.

    When type is `sku`, this is the number of instances of the SKU to be ordered.
    """

    type: Optional[str] = None
    """The type of this order item. Must be `sku`, `tax`, or `shipping`."""
