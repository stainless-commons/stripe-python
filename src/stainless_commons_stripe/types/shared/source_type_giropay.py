# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeGiropay"]


class SourceTypeGiropay(BaseModel):
    bank_code: Optional[str] = None

    bank_name: Optional[str] = None

    bic: Optional[str] = None

    statement_descriptor: Optional[str] = None
