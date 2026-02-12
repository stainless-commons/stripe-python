# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .address import Address
from ..._models import BaseModel

__all__ = ["SourceOwner"]


class SourceOwner(BaseModel):
    address: Optional[Address] = None

    email: Optional[str] = None
    """Owner's email address."""

    name: Optional[str] = None
    """Owner's full name."""

    phone: Optional[str] = None
    """Owner's phone number (including extension)."""

    verified_address: Optional[Address] = None

    verified_email: Optional[str] = None
    """Verified owner's email address.

    Verified values are verified or provided by the payment method directly (and if
    supported) at the time of authorization or settlement. They cannot be set or
    mutated.
    """

    verified_name: Optional[str] = None
    """Verified owner's full name.

    Verified values are verified or provided by the payment method directly (and if
    supported) at the time of authorization or settlement. They cannot be set or
    mutated.
    """

    verified_phone: Optional[str] = None
    """Verified owner's phone number (including extension).

    Verified values are verified or provided by the payment method directly (and if
    supported) at the time of authorization or settlement. They cannot be set or
    mutated.
    """
