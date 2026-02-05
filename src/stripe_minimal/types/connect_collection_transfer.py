# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["ConnectCollectionTransfer", "Destination"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Destination = TypeAliasType("Destination", Union[str, "Account"])
else:
    Destination: TypeAlias = Union[str, "Account"]


class ConnectCollectionTransfer(BaseModel):
    id: str
    """Unique identifier for the object."""

    amount: int
    """Amount transferred, in cents (or local equivalent)."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    destination: Destination
    """ID of the account that funds are being collected for."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["connect_collection_transfer"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """


from .account import Account
