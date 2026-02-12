# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["PaymentMethodSepaDebit"]


class PaymentMethodSepaDebit(BaseModel):
    bank_code: Optional[str] = None
    """Bank code of bank associated with the bank account."""

    branch_code: Optional[str] = None
    """Branch code of bank associated with the bank account."""

    country: Optional[str] = None
    """Two-letter ISO code representing the country the bank account is located in."""

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    generated_from: Optional["SepaDebitGeneratedFrom"] = None

    last4: Optional[str] = None
    """Last four characters of the IBAN."""


from .sepa_debit_generated_from import SepaDebitGeneratedFrom
