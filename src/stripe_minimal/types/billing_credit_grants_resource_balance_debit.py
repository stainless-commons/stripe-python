# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .billing_credit_grants_resource_amount import BillingCreditGrantsResourceAmount

__all__ = ["BillingCreditGrantsResourceBalanceDebit"]


class BillingCreditGrantsResourceBalanceDebit(BaseModel):
    amount: BillingCreditGrantsResourceAmount

    type: Literal["credits_applied", "credits_expired", "credits_voided"]
    """The type of debit transaction."""

    credits_applied: Optional["BillingCreditGrantsResourceBalanceCreditsApplied"] = None


from .billing_credit_grants_resource_balance_credits_applied import BillingCreditGrantsResourceBalanceCreditsApplied
