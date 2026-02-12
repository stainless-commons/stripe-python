# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["ConnectAccountReference", "Account"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Account = TypeAliasType("Account", Union[str, "account.Account"])
else:
    Account: TypeAlias = Union[str, "account.Account"]


class ConnectAccountReference(BaseModel):
    type: Literal["account", "self"]
    """Type of the account referenced."""

    account: Optional[Account] = None
    """The connected account being referenced when `type` is `account`."""


from . import account
