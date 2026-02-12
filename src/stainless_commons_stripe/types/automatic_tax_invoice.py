# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AutomaticTaxInvoice"]


class AutomaticTaxInvoice(BaseModel):
    enabled: bool
    """Whether Stripe automatically computes tax on this invoice.

    Note that incompatible invoice items (invoice items with manually specified
    [tax rates](https://docs.stripe.com/api/tax_rates), negative amounts, or
    `tax_behavior=unspecified`) cannot be added to automatic tax invoices.
    """

    disabled_reason: Optional[Literal["finalization_requires_location_inputs", "finalization_system_error"]] = None
    """If Stripe disabled automatic tax, this enum describes why."""

    liability: Optional["ConnectAccountReference"] = None

    provider: Optional[str] = None
    """The tax provider powering automatic tax."""

    status: Optional[Literal["complete", "failed", "requires_location_inputs"]] = None
    """The status of the most recent automated tax calculation for this invoice."""


from .connect_account_reference import ConnectAccountReference
