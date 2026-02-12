# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["InvoiceFinalizeParams"]


class InvoiceFinalizeParams(TypedDict, total=False):
    auto_advance: bool
    """
    Controls whether Stripe performs
    [automatic collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
    of the invoice. If `false`, the invoice's state doesn't automatically advance
    without an explicit action.
    """

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""
