# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .billing_credit_grants_resource_amount import BillingCreditGrantsResourceAmount

__all__ = ["BillingCreditGrantsResourceBalanceCredit"]


class BillingCreditGrantsResourceBalanceCredit(BaseModel):
    amount: BillingCreditGrantsResourceAmount

    type: Literal["credits_application_invoice_voided", "credits_granted"]
    """The type of credit transaction."""

    credits_application_invoice_voided: Optional[
        "BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided"
    ] = None


from .billing_credit_grants_resource_balance_credits_application_invoice_voided import (
    BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided,
)
