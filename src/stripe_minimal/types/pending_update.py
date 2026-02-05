# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PendingUpdate"]


class PendingUpdate(BaseModel):
    """
    Pending Updates store the changes pending from a previous update that will be applied
    to the Subscription upon successful payment.
    """

    expires_at: int
    """
    The point after which the changes reflected by this update will be discarded and
    no longer applied.
    """

    billing_cycle_anchor: Optional[int] = None
    """
    If the update is applied, determines the date of the first full invoice, and,
    for plans with `month` or `year` intervals, the day of the month for subsequent
    invoices. The timestamp is in UTC format.
    """

    subscription_items: Optional[List["SubscriptionItem"]] = None
    """
    List of subscription items, each with an attached plan, that will be set if the
    update is applied.
    """

    trial_end: Optional[int] = None
    """
    Unix timestamp representing the end of the trial period the customer will get
    before being charged for the first time, if the update is applied.
    """

    trial_from_plan: Optional[bool] = None
    """Indicates if a plan's `trial_period_days` should be applied to the subscription.

    Setting `trial_end` per subscription is preferred, and this defaults to `false`.
    Setting this flag to `true` together with `trial_end` is not allowed. See
    [Using trial periods on subscriptions](https://docs.stripe.com/billing/subscriptions/trials)
    to learn more.
    """


from .subscription_item import SubscriptionItem
