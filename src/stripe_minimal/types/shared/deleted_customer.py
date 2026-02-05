# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DeletedCustomer"]


class DeletedCustomer(BaseModel):
    id: str
    """Unique identifier for the object."""

    deleted: Literal[True]
    """Always true for a deleted object"""

    object: Literal["customer"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """
