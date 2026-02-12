# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    city: Optional[str] = None
    """City, district, suburb, town, or village."""

    country: Optional[str] = None
    """
    Two-letter country code
    ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """

    line1: Optional[str] = None
    """Address line 1, such as the street, PO Box, or company name."""

    line2: Optional[str] = None
    """Address line 2, such as the apartment, suite, unit, or building."""

    postal_code: Optional[str] = None
    """ZIP or postal code."""

    state: Optional[str] = None
    """
    State, county, province, or region
    ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """
