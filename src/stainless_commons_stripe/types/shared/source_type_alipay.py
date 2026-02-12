# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeAlipay"]


class SourceTypeAlipay(BaseModel):
    data_string: Optional[str] = None

    native_url: Optional[str] = None

    statement_descriptor: Optional[str] = None
