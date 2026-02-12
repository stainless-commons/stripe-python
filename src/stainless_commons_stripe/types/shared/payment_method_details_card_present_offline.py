# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PaymentMethodDetailsCardPresentOffline"]


class PaymentMethodDetailsCardPresentOffline(BaseModel):
    stored_at: Optional[int] = None
    """Time at which the payment was collected while offline"""

    type: Optional[Literal["deferred"]] = None
    """The method used to process this payment method offline.

    Only deferred is allowed.
    """
