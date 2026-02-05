# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["AccountInvoicesSettings", "DefaultAccountTaxID"]

if TYPE_CHECKING or not PYDANTIC_V1:
    DefaultAccountTaxID = TypeAliasType("DefaultAccountTaxID", Union[str, "TaxID"])
else:
    DefaultAccountTaxID: TypeAlias = Union[str, "TaxID"]


class AccountInvoicesSettings(BaseModel):
    default_account_tax_ids: Optional[List[DefaultAccountTaxID]] = None
    """The list of default Account Tax IDs to automatically include on invoices.

    Account Tax IDs get added when an invoice is finalized.
    """

    hosted_payment_method_save: Optional[Literal["always", "never", "offer"]] = None
    """
    Whether to save the payment method after a payment is completed for a one-time
    invoice or a subscription invoice when the customer already has a default
    payment method on the hosted invoice page.
    """


from .tax_id import TaxID
