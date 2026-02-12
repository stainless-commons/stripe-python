# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .balance_amount_by_source_type import BalanceAmountBySourceType

__all__ = ["BalanceAmount"]


class BalanceAmount(BaseModel):
    amount: int
    """Balance amount."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    source_types: Optional[BalanceAmountBySourceType] = None
