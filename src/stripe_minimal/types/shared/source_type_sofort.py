# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeSofort"]


class SourceTypeSofort(BaseModel):
    bank_code: Optional[str] = None

    bank_name: Optional[str] = None

    bic: Optional[str] = None

    country: Optional[str] = None

    iban_last4: Optional[str] = None

    preferred_language: Optional[str] = None

    statement_descriptor: Optional[str] = None
