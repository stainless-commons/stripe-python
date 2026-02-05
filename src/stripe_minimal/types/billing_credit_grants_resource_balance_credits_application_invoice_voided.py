# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided", "Invoice"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Invoice = TypeAliasType("Invoice", Union[str, "invoice.Invoice"])
else:
    Invoice: TypeAlias = Union[str, "invoice.Invoice"]


class BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided(BaseModel):
    invoice: Invoice
    """The invoice to which the reinstated billing credits were originally applied."""

    invoice_line_item: str
    """
    The invoice line item to which the reinstated billing credits were originally
    applied.
    """


from . import invoice
