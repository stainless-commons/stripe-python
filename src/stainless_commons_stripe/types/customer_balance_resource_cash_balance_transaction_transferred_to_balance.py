# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["CustomerBalanceResourceCashBalanceTransactionTransferredToBalance", "BalanceTransaction"]

if TYPE_CHECKING or not PYDANTIC_V1:
    BalanceTransaction = TypeAliasType("BalanceTransaction", Union[str, "balance_transaction.BalanceTransaction"])
else:
    BalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction"]


class CustomerBalanceResourceCashBalanceTransactionTransferredToBalance(BaseModel):
    balance_transaction: BalanceTransaction
    """
    The
    [Balance Transaction](https://docs.stripe.com/api/balance_transactions/object)
    that corresponds to funds transferred to your Stripe balance.
    """


from . import balance_transaction
