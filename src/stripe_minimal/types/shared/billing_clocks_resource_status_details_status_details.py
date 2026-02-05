# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .billing_clocks_resource_status_details_advancing_status_details import (
    BillingClocksResourceStatusDetailsAdvancingStatusDetails,
)

__all__ = ["BillingClocksResourceStatusDetailsStatusDetails"]


class BillingClocksResourceStatusDetailsStatusDetails(BaseModel):
    advancing: Optional[BillingClocksResourceStatusDetailsAdvancingStatusDetails] = None
