# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeWechat"]


class SourceTypeWechat(BaseModel):
    prepay_id: Optional[str] = None

    qr_code_url: Optional[str] = None

    statement_descriptor: Optional[str] = None
