# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentMethodOptionsCardPresentRouting"]


class PaymentMethodOptionsCardPresentRouting(BaseModel):
    requested_priority: Optional[Literal["domestic", "international"]] = None
    """Requested routing priority"""
