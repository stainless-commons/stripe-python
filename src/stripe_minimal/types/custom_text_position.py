# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CustomTextPosition"]


class CustomTextPosition(BaseModel):
    message: str
    """Text may be up to 1200 characters in length."""
