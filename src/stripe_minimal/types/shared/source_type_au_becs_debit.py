# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeAuBecsDebit"]


class SourceTypeAuBecsDebit(BaseModel):
    bsb_number: Optional[str] = None

    fingerprint: Optional[str] = None

    last4: Optional[str] = None
