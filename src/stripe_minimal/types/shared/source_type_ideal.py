# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeIdeal"]


class SourceTypeIdeal(BaseModel):
    bank: Optional[str] = None

    bic: Optional[str] = None

    iban_last4: Optional[str] = None

    statement_descriptor: Optional[str] = None
