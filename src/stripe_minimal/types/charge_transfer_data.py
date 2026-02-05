# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["ChargeTransferData", "Destination"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Destination = TypeAliasType("Destination", Union[str, "Account"])
else:
    Destination: TypeAlias = Union[str, "Account"]


class ChargeTransferData(BaseModel):
    destination: Destination
    """
    ID of an existing, connected Stripe account to transfer funds to if
    `transfer_data` was specified in the charge request.
    """

    amount: Optional[int] = None
    """The amount transferred to the destination account, if specified.

    By default, the entire charge amount is transferred to the destination account.
    """


from .account import Account
