# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["SepaDebitGeneratedFrom", "Charge", "SetupAttempt"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Charge = TypeAliasType("Charge", Union[str, "charge.Charge", None])
else:
    Charge: TypeAlias = Union[str, "charge.Charge", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    SetupAttempt = TypeAliasType("SetupAttempt", Union[str, "setup_attempt.SetupAttempt", None])
else:
    SetupAttempt: TypeAlias = Union[str, "setup_attempt.SetupAttempt", None]


class SepaDebitGeneratedFrom(BaseModel):
    charge: Optional[Charge] = None
    """The ID of the Charge that generated this PaymentMethod, if any."""

    setup_attempt: Optional[SetupAttempt] = None
    """The ID of the SetupAttempt that generated this PaymentMethod, if any."""


from . import charge, setup_attempt
