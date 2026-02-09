# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .tax_rate import TaxRate

__all__ = ["ScheduleConfigurationItem", "Price", "PriceDeletedPrice", "BillingThresholds"]


class PriceDeletedPrice(BaseModel):
    id: str
    """Unique identifier for the object."""

    deleted: Literal[True]
    """Always true for a deleted object"""

    object: Literal["price"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    Price = TypeAliasType("Price", Union[str, "price.Price", PriceDeletedPrice])
else:
    Price: TypeAlias = Union[str, "price.Price", PriceDeletedPrice]


class BillingThresholds(BaseModel):
    usage_gte: Optional[int] = None
    """Usage threshold that triggers the subscription to create an invoice"""


class ScheduleConfigurationItem(BaseModel):
    """A phase item describes the price and quantity of a phase."""

    discounts: List["StackableDiscount"]
    """The discounts applied to the subscription item.

    Subscription item discounts are applied before subscription discounts. Use
    `expand[]=discounts` to expand each discount.
    """

    price: Price
    """ID of the price to which the customer should be subscribed."""

    billing_thresholds: Optional[BillingThresholds] = None

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an item. Metadata on this item will update the underlying subscription
    item's `metadata` when the phase is entered.
    """

    quantity: Optional[int] = None
    """Quantity of the plan to which the customer should be subscribed."""

    tax_rates: Optional[List[TaxRate]] = None
    """The tax rates which apply to this `phase_item`.

    When set, the `default_tax_rates` on the phase do not apply to this
    `phase_item`.
    """


from . import price
from .stackable_discount import StackableDiscount
