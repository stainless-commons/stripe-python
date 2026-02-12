# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["BillingBillResourceInvoicingParentsInvoiceSubscriptionParent", "Subscription"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Subscription = TypeAliasType("Subscription", Union[str, "subscription.Subscription"])
else:
    Subscription: TypeAlias = Union[str, "subscription.Subscription"]


class BillingBillResourceInvoicingParentsInvoiceSubscriptionParent(BaseModel):
    subscription: Subscription
    """The subscription that generated this invoice"""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) defined as
    subscription metadata when an invoice is created. Becomes an immutable snapshot
    of the subscription metadata at the time of invoice finalization. _Note: This
    attribute is populated only for invoices created on or after June 29, 2023._
    """

    subscription_proration_date: Optional[int] = None
    """Only set for upcoming invoices that preview prorations.

    The time used to calculate prorations.
    """


from . import subscription
