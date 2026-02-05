# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.payment_method_details_card_present import PaymentMethodDetailsCardPresent

__all__ = ["PaymentMethodCardGeneratedCard", "PaymentMethodDetails", "SetupAttempt"]


class PaymentMethodDetails(BaseModel):
    type: str
    """
    The type of payment method transaction-specific details from the transaction
    that generated this `card` payment method. Always `card_present`.
    """

    card_present: Optional[PaymentMethodDetailsCardPresent] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    SetupAttempt = TypeAliasType("SetupAttempt", Union[str, "setup_attempt.SetupAttempt", None])
else:
    SetupAttempt: TypeAlias = Union[str, "setup_attempt.SetupAttempt", None]


class PaymentMethodCardGeneratedCard(BaseModel):
    charge: Optional[str] = None
    """The charge that created this object."""

    payment_method_details: Optional[PaymentMethodDetails] = None

    setup_attempt: Optional[SetupAttempt] = None
    """The ID of the SetupAttempt that generated this PaymentMethod, if any."""


from . import setup_attempt
