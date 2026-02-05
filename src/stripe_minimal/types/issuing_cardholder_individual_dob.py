# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IssuingCardholderIndividualDob"]


class IssuingCardholderIndividualDob(BaseModel):
    day: Optional[int] = None
    """The day of birth, between 1 and 31."""

    month: Optional[int] = None
    """The month of birth, between 1 and 12."""

    year: Optional[int] = None
    """The four-digit year of birth."""
