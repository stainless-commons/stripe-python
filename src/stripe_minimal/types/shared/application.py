# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Application"]


class Application(BaseModel):
    id: str
    """Unique identifier for the object."""

    object: Literal["application"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    name: Optional[str] = None
    """The name of the application."""
