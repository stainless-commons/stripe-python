# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["InvoicesResourceFromInvoice", "Invoice"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Invoice = TypeAliasType("Invoice", Union[str, "invoice.Invoice"])
else:
    Invoice: TypeAlias = Union[str, "invoice.Invoice"]


class InvoicesResourceFromInvoice(BaseModel):
    action: str
    """The relation between this invoice and the cloned invoice"""

    invoice: Invoice
    """The invoice that was cloned."""


from . import invoice
