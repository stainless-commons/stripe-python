# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .tax_rate import TaxRate

__all__ = ["ScheduleAddInvoiceItem", "Period", "PeriodEnd", "PeriodStart", "Price", "PriceDeletedPrice"]


class PeriodEnd(BaseModel):
    type: Literal["min_item_period_end", "phase_end", "timestamp"]
    """Select how to calculate the end of the invoice item period."""

    timestamp: Optional[int] = None
    """A precise Unix timestamp for the end of the invoice item period.

    Must be greater than or equal to `period.start`.
    """


class PeriodStart(BaseModel):
    type: Literal["max_item_period_start", "phase_start", "timestamp"]
    """Select how to calculate the start of the invoice item period."""

    timestamp: Optional[int] = None
    """A precise Unix timestamp for the start of the invoice item period.

    Must be less than or equal to `period.end`.
    """


class Period(BaseModel):
    end: PeriodEnd

    start: PeriodStart


class PriceDeletedPrice(BaseModel):
    id: str
    """Unique identifier for the object."""

    deleted: Literal[True]
    """Always true for a deleted object"""

    object: Literal["price"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """


Price: TypeAlias = Union[str, "price.Price", PriceDeletedPrice]


class ScheduleAddInvoiceItem(BaseModel):
    """
    An Add Invoice Item describes the prices and quantities that will be added as pending invoice items when entering a phase.
    """

    discounts: List["StackableDiscount"]
    """The stackable discounts that will be applied to the item."""

    period: Period

    price: Price
    """ID of the price used to generate the invoice item."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    quantity: Optional[int] = None
    """The quantity of the invoice item."""

    tax_rates: Optional[List[TaxRate]] = None
    """The tax rates which apply to the item.

    When set, the `default_tax_rates` do not apply to this item.
    """


from . import price
from .stackable_discount import StackableDiscount
