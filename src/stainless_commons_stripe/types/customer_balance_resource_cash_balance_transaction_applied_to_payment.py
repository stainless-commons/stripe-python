# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["CustomerBalanceResourceCashBalanceTransactionAppliedToPayment", "PaymentIntent"]

if TYPE_CHECKING or not PYDANTIC_V1:
    PaymentIntent = TypeAliasType("PaymentIntent", Union[str, "payment_intent.PaymentIntent"])
else:
    PaymentIntent: TypeAlias = Union[str, "payment_intent.PaymentIntent"]


class CustomerBalanceResourceCashBalanceTransactionAppliedToPayment(BaseModel):
    payment_intent: PaymentIntent
    """
    The [Payment Intent](https://docs.stripe.com/api/payment_intents/object) that
    funds were applied to.
    """


from . import payment_intent
