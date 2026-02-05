# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .address import Address
from ..._models import BaseModel

__all__ = ["Shipping"]


class Shipping(BaseModel):
    address: Optional[Address] = None

    carrier: Optional[str] = None
    """
    The delivery service that shipped a physical product, such as Fedex, UPS, USPS,
    etc.
    """

    name: Optional[str] = None
    """Recipient name."""

    phone: Optional[str] = None
    """Recipient phone (including extension)."""

    tracking_number: Optional[str] = None
    """The tracking number for a physical product, obtained from the delivery service.

    If multiple tracking numbers were generated for this purchase, please separate
    them with commas.
    """
