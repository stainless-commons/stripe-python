# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .billing_clocks_resource_status_details_status_details import BillingClocksResourceStatusDetailsStatusDetails

__all__ = ["TestHelpersTestClock"]


class TestHelpersTestClock(BaseModel):
    __test__ = False
    """A test clock enables deterministic control over objects in testmode.

    With a test clock, you can create
    objects at a frozen time in the past or future, and advance to a specific future time to observe webhooks and state changes. After the clock advances,
    you can either validate the current state of your scenario (and test your assumptions), change the current state of your scenario (and test more complex scenarios), or keep advancing forward in time.
    """
    id: str
    """Unique identifier for the object."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    deletes_after: int
    """Time at which this clock is scheduled to auto delete."""

    frozen_time: int
    """Time at which all objects belonging to this clock are frozen."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["test_helpers.test_clock"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    status: Literal["advancing", "internal_failure", "ready"]
    """The status of the Test Clock."""

    status_details: BillingClocksResourceStatusDetailsStatusDetails

    name: Optional[str] = None
    """The custom name supplied at creation."""
