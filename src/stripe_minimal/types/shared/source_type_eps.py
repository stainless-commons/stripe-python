# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeEps"]


class SourceTypeEps(BaseModel):
    reference: Optional[str] = None

    statement_descriptor: Optional[str] = None
