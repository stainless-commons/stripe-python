# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["FileLink", "File"]

if TYPE_CHECKING or not PYDANTIC_V1:
    File = TypeAliasType("File", Union[str, "file.File"])
else:
    File: TypeAlias = Union[str, "file.File"]


class FileLink(BaseModel):
    """
    To share the contents of a `File` object with non-Stripe users, you can
    create a `FileLink`. `FileLink`s contain a URL that you can use to
    retrieve the contents of the file without authentication.
    """

    id: str
    """Unique identifier for the object."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    expired: bool
    """Returns if the link is already expired."""

    file: File
    """The file object this link points to."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    object: Literal["file_link"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    expires_at: Optional[int] = None
    """Time that the link expires."""

    url: Optional[str] = None
    """The publicly accessible URL to download the file."""


from . import file
