# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["SubscriptionTransferData", "Destination"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Destination = TypeAliasType("Destination", Union[str, "Account"])
else:
    Destination: TypeAlias = Union[str, "Account"]


class SubscriptionTransferData(BaseModel):
    destination: Destination
    """
    The account where funds from the payment will be transferred to upon payment
    success.
    """

    amount_percent: Optional[float] = None
    """A non-negative decimal between 0 and 100, with at most two decimal places.

    This represents the percentage of the subscription invoice total that will be
    transferred to the destination account. By default, the entire amount is
    transferred to the destination.
    """


from .account import Account
