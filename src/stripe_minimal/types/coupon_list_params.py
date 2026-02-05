# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["CouponListParams", "Created", "CreatedRangeQuerySpecs"]


class CouponListParams(TypedDict, total=False):
    created: Created
    """A filter on the list, based on the object `created` field.

    The value can be a string with an integer Unix timestamp, or it can be a
    dictionary with a number of different query options.
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

    starting_after: str
    """A cursor for use in pagination.

    `starting_after` is an object ID that defines your place in the list. For
    instance, if you make a list request and receive 100 objects, ending with
    `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to
    fetch the next page of the list.
    """


class CreatedRangeQuerySpecs(TypedDict, total=False):
    gt: int

    gte: int

    lt: int

    lte: int


Created: TypeAlias = Union[CreatedRangeQuerySpecs, int]
