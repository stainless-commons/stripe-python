# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingBillResourceInvoicingParentsInvoiceParent", "QuoteDetails"]


class QuoteDetails(BaseModel):
    quote: str
    """The quote that generated this invoice"""


class BillingBillResourceInvoicingParentsInvoiceParent(BaseModel):
    type: Literal["quote_details", "subscription_details"]
    """The type of parent that generated this invoice"""

    quote_details: Optional[QuoteDetails] = None

    subscription_details: Optional["BillingBillResourceInvoicingParentsInvoiceSubscriptionParent"] = None


from .billing_bill_resource_invoicing_parents_invoice_subscription_parent import (
    BillingBillResourceInvoicingParentsInvoiceSubscriptionParent,
)
