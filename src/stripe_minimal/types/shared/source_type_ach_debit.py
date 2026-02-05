# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeACHDebit"]


class SourceTypeACHDebit(BaseModel):
    bank_name: Optional[str] = None

    country: Optional[str] = None

    fingerprint: Optional[str] = None

    last4: Optional[str] = None

    routing_number: Optional[str] = None

    type: Optional[str] = None
