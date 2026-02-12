# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ShippingRateDeliveryEstimateBound"]


class ShippingRateDeliveryEstimateBound(BaseModel):
    unit: Literal["business_day", "day", "hour", "month", "week"]
    """A unit of time."""

    value: int
    """Must be greater than 0."""
