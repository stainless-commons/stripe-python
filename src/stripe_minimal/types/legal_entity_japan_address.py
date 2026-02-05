# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LegalEntityJapanAddress"]


class LegalEntityJapanAddress(BaseModel):
    city: Optional[str] = None
    """City/Ward."""

    country: Optional[str] = None
    """
    Two-letter country code
    ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """

    line1: Optional[str] = None
    """Block/Building number."""

    line2: Optional[str] = None
    """Building details."""

    postal_code: Optional[str] = None
    """ZIP or postal code."""

    state: Optional[str] = None
    """Prefecture."""

    town: Optional[str] = None
    """Town/cho-me."""
