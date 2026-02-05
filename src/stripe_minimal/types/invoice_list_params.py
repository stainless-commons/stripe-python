# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["InvoiceListParams", "Created", "CreatedRangeQuerySpecs", "DueDate", "DueDateRangeQuerySpecs"]


class InvoiceListParams(TypedDict, total=False):
    collection_method: Literal["charge_automatically", "send_invoice"]
    """The collection method of the invoice to retrieve.

    Either `charge_automatically` or `send_invoice`.
    """

    created: Created
    """Only return invoices that were created during the given date interval."""

    customer: str
    """Only return invoices for the customer specified by this customer ID."""

    customer_account: str
    """
    Only return invoices for the account representing the customer specified by this
    account ID.
    """

    due_date: DueDate

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

    status: Literal["draft", "open", "paid", "uncollectible", "void"]
    """
    The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or
    `void`.
    [Learn more](https://docs.stripe.com/billing/invoices/workflow#workflow-overview)
    """

    subscription: str
    """Only return invoices for the subscription specified by this subscription ID."""


class CreatedRangeQuerySpecs(TypedDict, total=False):
    gt: int

    gte: int

    lt: int

    lte: int


Created: TypeAlias = Union[CreatedRangeQuerySpecs, int]


class DueDateRangeQuerySpecs(TypedDict, total=False):
    gt: int

    gte: int

    lt: int

    lte: int


DueDate: TypeAlias = Union[DueDateRangeQuerySpecs, int]
