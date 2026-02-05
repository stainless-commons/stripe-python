# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeCard"]


class SourceTypeCard(BaseModel):
    address_line1_check: Optional[str] = None

    address_zip_check: Optional[str] = None

    brand: Optional[str] = None

    country: Optional[str] = None

    cvc_check: Optional[str] = None

    dynamic_last4: Optional[str] = None

    exp_month: Optional[int] = None

    exp_year: Optional[int] = None

    fingerprint: Optional[str] = None

    funding: Optional[str] = None

    last4: Optional[str] = None

    name: Optional[str] = None

    three_d_secure: Optional[str] = None

    tokenization_method: Optional[str] = None
