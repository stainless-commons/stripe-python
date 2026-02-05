# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AutomaticTaxSubscription"]


class AutomaticTaxSubscription(BaseModel):
    enabled: bool
    """Whether Stripe automatically computes tax on this subscription."""

    disabled_reason: Optional[Literal["requires_location_inputs"]] = None
    """If Stripe disabled automatic tax, this enum describes why."""

    liability: Optional["ConnectAccountReference"] = None


from .connect_account_reference import ConnectAccountReference
