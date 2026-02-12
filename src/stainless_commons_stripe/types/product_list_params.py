# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["ProductListParams", "Created", "CreatedRangeQuerySpecs"]


class ProductListParams(TypedDict, total=False):
    active: bool
    """
    Only return products that are active or inactive (e.g., pass `false` to list all
    inactive products).
    """

    created: Created
    """Only return products that were created during the given date interval."""

    ending_before: str
    """A cursor for use in pagination.

    `ending_before` is an object ID that defines your place in the list. For
    instance, if you make a list request and receive 100 objects, starting with
    `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to
    fetch the previous page of the list.
    """

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    ids: SequenceNotStr[str]
    """Only return products with the given IDs.

    Cannot be used with
    [starting_after](https://api.stripe.com#list_products-starting_after) or
    [ending_before](https://api.stripe.com#list_products-ending_before).
    """

    limit: int
    """A limit on the number of objects to be returned.

    Limit can range between 1 and 100, and the default is 10.
    """

    shippable: bool
    """
    Only return products that can be shipped (i.e., physical, not digital products).
    """

    starting_after: str
    """A cursor for use in pagination.

    `starting_after` is an object ID that defines your place in the list. For
    instance, if you make a list request and receive 100 objects, ending with
    `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to
    fetch the next page of the list.
    """

    url: str
    """Only return products with the given url."""


class CreatedRangeQuerySpecs(TypedDict, total=False):
    gt: int

    gte: int

    lt: int

    lte: int


Created: TypeAlias = Union[CreatedRangeQuerySpecs, int]
