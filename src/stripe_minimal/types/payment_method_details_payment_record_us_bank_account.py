# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["PaymentMethodDetailsPaymentRecordUsBankAccount", "Mandate"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Mandate = TypeAliasType("Mandate", Union[str, "mandate.Mandate"])
else:
    Mandate: TypeAlias = Union[str, "mandate.Mandate"]


class PaymentMethodDetailsPaymentRecordUsBankAccount(BaseModel):
    account_holder_type: Optional[Literal["company", "individual"]] = None
    """The type of entity that holds the account.

    This can be either 'individual' or 'company'.
    """

    account_type: Optional[Literal["checking", "savings"]] = None
    """The type of the bank account. This can be either 'checking' or 'savings'."""

    bank_name: Optional[str] = None
    """Name of the bank associated with the bank account."""

    expected_debit_date: Optional[str] = None
    """Estimated date to debit the customer's bank account.

    A date string in YYYY-MM-DD format.
    """

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    last4: Optional[str] = None
    """Last four digits of the bank account number."""

    mandate: Optional[Mandate] = None
    """ID of the mandate used to make this payment."""

    payment_reference: Optional[str] = None
    """The ACH payment reference for this transaction."""

    routing_number: Optional[str] = None
    """The routing number for the bank account."""


from . import mandate
