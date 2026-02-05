# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BalanceAmountBySourceType"]


class BalanceAmountBySourceType(BaseModel):
    bank_account: Optional[int] = None
    """
    Amount coming from
    [legacy US ACH payments](https://docs.stripe.com/ach-deprecated).
    """

    card: Optional[int] = None
    """
    Amount coming from most payment methods, including cards as well as
    [non-legacy bank debits](https://docs.stripe.com/payments/bank-debits).
    """

    fpx: Optional[int] = None
    """
    Amount coming from [FPX](https://docs.stripe.com/payments/fpx), a Malaysian
    payment method.
    """
