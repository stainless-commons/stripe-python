# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "SubscriptionListParams",
    "AutomaticTax",
    "Created",
    "CreatedRangeQuerySpecs",
    "CurrentPeriodEnd",
    "CurrentPeriodEndRangeQuerySpecs",
    "CurrentPeriodStart",
    "CurrentPeriodStartRangeQuerySpecs",
]


class SubscriptionListParams(TypedDict, total=False):
    automatic_tax: AutomaticTax
    """Filter subscriptions by their automatic tax settings."""

    collection_method: Literal["charge_automatically", "send_invoice"]
    """The collection method of the subscriptions to retrieve.

    Either `charge_automatically` or `send_invoice`.
    """

    created: Created
    """Only return subscriptions that were created during the given date interval."""

    current_period_end: CurrentPeriodEnd
    """
    Only return subscriptions whose minimum item current_period_end falls within the
    given date interval.
    """

    current_period_start: CurrentPeriodStart
    """
    Only return subscriptions whose maximum item current_period_start falls within
    the given date interval.
    """

    customer: str
    """The ID of the customer whose subscriptions you're retrieving."""

    customer_account: str
    """
    The ID of the account representing the customer whose subscriptions you're
    retrieving.
    """

    ending_before: str
    """A cursor for use in pagination.

    `ending_before` is an object ID that defines your place in the list. For
    instance, if you make a list request and receive 100 objects, starting with
    `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to
    fetch the previous page of the list.
    """

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    limit: int
    """A limit on the number of objects to be returned.

    Limit can range between 1 and 100, and the default is 10.
    """

    price: str
    """Filter for subscriptions that contain this recurring price ID."""

    starting_after: str
    """A cursor for use in pagination.

    `starting_after` is an object ID that defines your place in the list. For
    instance, if you make a list request and receive 100 objects, ending with
    `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to
    fetch the next page of the list.
    """

    status: Literal[
        "active",
        "all",
        "canceled",
        "ended",
        "incomplete",
        "incomplete_expired",
        "past_due",
        "paused",
        "trialing",
        "unpaid",
    ]
    """The status of the subscriptions to retrieve.

    Passing in a value of `canceled` will return all canceled subscriptions,
    including those belonging to deleted customers. Pass `ended` to find
    subscriptions that are canceled and subscriptions that are expired due to
    [incomplete payment](https://docs.stripe.com/billing/subscriptions/overview#subscription-statuses).
    Passing in a value of `all` will return subscriptions of all statuses. If no
    value is supplied, all subscriptions that have not been canceled are returned.
    """

    test_clock: str
    """Filter for subscriptions that are associated with the specified test clock.

    The response will not include subscriptions with test clocks if this and the
    customer parameter is not set.
    """


class AutomaticTax(TypedDict, total=False):
    """Filter subscriptions by their automatic tax settings."""

    enabled: Required[bool]


class CreatedRangeQuerySpecs(TypedDict, total=False):
    gt: int

    gte: int

    lt: int

    lte: int


Created: TypeAlias = Union[CreatedRangeQuerySpecs, int]


class CurrentPeriodEndRangeQuerySpecs(TypedDict, total=False):
    gt: int

    gte: int

    lt: int

    lte: int


CurrentPeriodEnd: TypeAlias = Union[CurrentPeriodEndRangeQuerySpecs, int]


class CurrentPeriodStartRangeQuerySpecs(TypedDict, total=False):
    gt: int

    gte: int

    lt: int

    lte: int


CurrentPeriodStart: TypeAlias = Union[CurrentPeriodStartRangeQuerySpecs, int]
