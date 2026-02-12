# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["SubscriptionCancelParams", "CancellationDetails"]


class SubscriptionCancelParams(TypedDict, total=False):
    cancellation_details: CancellationDetails
    """Details about why this subscription was cancelled"""

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    invoice_now: bool
    """
    Will generate a final invoice that invoices for any un-invoiced metered usage
    and new/pending proration invoice items. Defaults to `false`.
    """

    prorate: bool
    """
    Will generate a proration invoice item that credits remaining unused time until
    the subscription period end. Defaults to `false`.
    """


class CancellationDetails(TypedDict, total=False):
    """Details about why this subscription was cancelled"""

    comment: Union[str, Literal[""]]

    feedback: Literal[
        "",
        "customer_service",
        "low_quality",
        "missing_features",
        "other",
        "switched_service",
        "too_complex",
        "too_expensive",
        "unused",
    ]
