# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeAcssDebit"]


class SourceTypeAcssDebit(BaseModel):
    bank_address_city: Optional[str] = None

    bank_address_line_1: Optional[str] = None

    bank_address_line_2: Optional[str] = None

    bank_address_postal_code: Optional[str] = None

    bank_name: Optional[str] = None

    category: Optional[str] = None

    country: Optional[str] = None

    fingerprint: Optional[str] = None

    last4: Optional[str] = None

    routing_number: Optional[str] = None
