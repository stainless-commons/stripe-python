# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["BalanceRetrieveParams"]


class BalanceRetrieveParams(TypedDict, total=False):
    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""
