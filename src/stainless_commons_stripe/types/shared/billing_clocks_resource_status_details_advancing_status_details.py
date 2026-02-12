# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["BillingClocksResourceStatusDetailsAdvancingStatusDetails"]


class BillingClocksResourceStatusDetailsAdvancingStatusDetails(BaseModel):
    target_frozen_time: int
    """The `frozen_time` that the Test Clock is advancing towards."""
