# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import application
from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.deleted_customer import DeletedCustomer
from .shared.deleted_application import DeletedApplication
from .shared.test_helpers_test_clock import TestHelpersTestClock

__all__ = [
    "Schedule",
    "BillingMode",
    "BillingModeFlexible",
    "Customer",
    "Application",
    "CurrentPhase",
    "Subscription",
    "TestClock",
]


class BillingModeFlexible(BaseModel):
    proration_discounts: Optional[Literal["included", "itemized"]] = None
    """
    Controls how invoices and invoice items display proration amounts and discount
    amounts.
    """


class BillingMode(BaseModel):
    """The billing mode of the subscription."""

    type: Literal["classic", "flexible"]
    """
    Controls how prorations and invoices for subscriptions are calculated and
    orchestrated.
    """

    flexible: Optional[BillingModeFlexible] = None

    updated_at: Optional[int] = None
    """Details on when the current billing_mode was adopted."""


if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer]

Application: TypeAlias = Union[str, application.Application, DeletedApplication, None]


class CurrentPhase(BaseModel):
    end_date: int
    """The end of this phase of the subscription schedule."""

    start_date: int
    """The start of this phase of the subscription schedule."""


if TYPE_CHECKING or not PYDANTIC_V1:
    Subscription = TypeAliasType("Subscription", Union[str, "subscription.Subscription", None])
else:
    Subscription: TypeAlias = Union[str, "subscription.Subscription", None]

TestClock: TypeAlias = Union[str, TestHelpersTestClock, None]


class Schedule(BaseModel):
    """
    A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.

    Related guide: [Subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
    """

    id: str
    """Unique identifier for the object."""

    billing_mode: BillingMode
    """The billing mode of the subscription."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    customer: Customer
    """ID of the customer who owns the subscription schedule."""

    default_settings: "DefaultSettings"

    end_behavior: Literal["cancel", "none", "release", "renew"]
    """Behavior of the subscription schedule and underlying subscription when it ends.

    Possible values are `release` or `cancel` with the default being `release`.
    `release` will end the subscription schedule and keep the underlying
    subscription running. `cancel` will end the subscription schedule and cancel the
    underlying subscription.
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["subscription_schedule"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    phases: List["SchedulePhaseConfiguration"]
    """Configuration for the subscription schedule's phases."""

    status: Literal["active", "canceled", "completed", "not_started", "released"]
    """The present status of the subscription schedule.

    Possible values are `not_started`, `active`, `completed`, `released`, and
    `canceled`. You can read more about the different states in our
    [behavior guide](https://docs.stripe.com/billing/subscriptions/subscription-schedules).
    """

    application: Optional[Application] = None
    """ID of the Connect Application that created the schedule."""

    canceled_at: Optional[int] = None
    """Time at which the subscription schedule was canceled.

    Measured in seconds since the Unix epoch.
    """

    completed_at: Optional[int] = None
    """Time at which the subscription schedule was completed.

    Measured in seconds since the Unix epoch.
    """

    current_phase: Optional[CurrentPhase] = None

    customer_account: Optional[str] = None
    """ID of the account who owns the subscription schedule."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    released_at: Optional[int] = None
    """Time at which the subscription schedule was released.

    Measured in seconds since the Unix epoch.
    """

    released_subscription: Optional[str] = None
    """
    ID of the subscription once managed by the subscription schedule (if it is
    released).
    """

    subscription: Optional[Subscription] = None
    """ID of the subscription managed by the subscription schedule."""

    test_clock: Optional[TestClock] = None
    """ID of the test clock this subscription schedule belongs to."""


from . import customer, subscription
from .default_settings import DefaultSettings
from .schedule_phase_configuration import SchedulePhaseConfiguration
