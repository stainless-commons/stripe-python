# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["PaymentTransferData", "Destination"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Destination = TypeAliasType("Destination", Union[str, "Account"])
else:
    Destination: TypeAlias = Union[str, "Account"]


class PaymentTransferData(BaseModel):
    destination: Destination
    """
    The account (if any) that the payment is attributed to for tax reporting, and
    where funds from the payment are transferred to after payment success.
    """

    amount: Optional[int] = None
    """The amount transferred to the destination account.

    This transfer will occur automatically after the payment succeeds. If no amount
    is specified, by default the entire payment amount is transferred to the
    destination account. The amount must be less than or equal to the
    [amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount),
    and must be a positive integer representing how much to transfer in the smallest
    currency unit (e.g., 100 cents to charge $1.00).
    """


from .account import Account
