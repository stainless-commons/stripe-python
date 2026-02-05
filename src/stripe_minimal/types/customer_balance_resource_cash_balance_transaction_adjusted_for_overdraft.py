# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "CustomerBalanceResourceCashBalanceTransactionAdjustedForOverdraft",
    "BalanceTransaction",
    "LinkedTransaction",
]

if TYPE_CHECKING or not PYDANTIC_V1:
    BalanceTransaction = TypeAliasType("BalanceTransaction", Union[str, "balance_transaction.BalanceTransaction"])
else:
    BalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction"]

if TYPE_CHECKING or not PYDANTIC_V1:
    LinkedTransaction = TypeAliasType("LinkedTransaction", Union[str, "CustomerCashBalanceTransaction"])
else:
    LinkedTransaction: TypeAlias = Union[str, "CustomerCashBalanceTransaction"]


class CustomerBalanceResourceCashBalanceTransactionAdjustedForOverdraft(BaseModel):
    balance_transaction: BalanceTransaction
    """
    The
    [Balance Transaction](https://docs.stripe.com/api/balance_transactions/object)
    that corresponds to funds taken out of your Stripe balance.
    """

    linked_transaction: LinkedTransaction
    """
    The
    [Cash Balance Transaction](https://docs.stripe.com/api/cash_balance_transactions/object)
    that brought the customer balance negative, triggering the clawback of funds.
    """


from . import balance_transaction
from .customer_cash_balance_transaction import CustomerCashBalanceTransaction
