# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SubscriptionBillingThresholds"]


class SubscriptionBillingThresholds(BaseModel):
    amount_gte: Optional[int] = None
    """Monetary threshold that triggers the subscription to create an invoice"""

    reset_billing_cycle_anchor: Optional[bool] = None
    """
    Indicates if the `billing_cycle_anchor` should be reset when a threshold is
    reached. If true, `billing_cycle_anchor` will be updated to the date/time the
    threshold was last reached; otherwise, the value will remain unchanged. This
    value may not be `true` if the subscription contains items with plans that have
    `aggregate_usage=last_ever`.
    """
