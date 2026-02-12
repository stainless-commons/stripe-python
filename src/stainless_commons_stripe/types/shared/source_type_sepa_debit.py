# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeSepaDebit"]


class SourceTypeSepaDebit(BaseModel):
    bank_code: Optional[str] = None

    branch_code: Optional[str] = None

    country: Optional[str] = None

    fingerprint: Optional[str] = None

    last4: Optional[str] = None

    mandate_reference: Optional[str] = None

    mandate_url: Optional[str] = None
