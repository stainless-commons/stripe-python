# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["PriceListParams", "Created", "CreatedRangeQuerySpecs", "Recurring"]


class PriceListParams(TypedDict, total=False):
    active: bool
    """
    Only return prices that are active or inactive (e.g., pass `false` to list all
    inactive prices).
    """

    created: Created
    """A filter on the list, based on the object `created` field.

    The value can be a string with an integer Unix timestamp, or it can be a
    dictionary with a number of different query options.
    """

    currency: str
    """Only return prices for the given currency."""

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

    lookup_keys: SequenceNotStr[str]
    """Only return the price with these lookup_keys, if any exist.

    You can specify up to 10 lookup_keys.
    """

    product: str
    """Only return prices for the given product."""

    recurring: Recurring
    """Only return prices with these recurring fields."""

    starting_after: str
    """A cursor for use in pagination.

    `starting_after` is an object ID that defines your place in the list. For
    instance, if you make a list request and receive 100 objects, ending with
    `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to
    fetch the next page of the list.
    """

    type: Literal["one_time", "recurring"]
    """Only return prices of type `recurring` or `one_time`."""


class CreatedRangeQuerySpecs(TypedDict, total=False):
    gt: int

    gte: int

    lt: int

    lte: int


Created: TypeAlias = Union[CreatedRangeQuerySpecs, int]


class Recurring(TypedDict, total=False):
    """Only return prices with these recurring fields."""

    interval: Literal["day", "month", "week", "year"]

    meter: str

    usage_type: Literal["licensed", "metered"]
