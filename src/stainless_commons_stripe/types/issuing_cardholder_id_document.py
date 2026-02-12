# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["IssuingCardholderIDDocument", "Back", "Front"]

Back: TypeAlias = Union[str, "File", None]

Front: TypeAlias = Union[str, "File", None]


class IssuingCardholderIDDocument(BaseModel):
    back: Optional[Back] = None
    """
    The back of a document returned by a
    [file upload](https://api.stripe.com#create_file) with a `purpose` value of
    `identity_document`.
    """

    front: Optional[Front] = None
    """
    The front of a document returned by a
    [file upload](https://api.stripe.com#create_file) with a `purpose` value of
    `identity_document`.
    """


from .file import File
