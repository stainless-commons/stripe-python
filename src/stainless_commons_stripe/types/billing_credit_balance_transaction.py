# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.test_helpers_test_clock import TestHelpersTestClock

__all__ = ["BillingCreditBalanceTransaction", "CreditGrant", "TestClock"]

if TYPE_CHECKING or not PYDANTIC_V1:
    CreditGrant = TypeAliasType("CreditGrant", Union[str, "BillingCreditGrant"])
else:
    CreditGrant: TypeAlias = Union[str, "BillingCreditGrant"]

TestClock: TypeAlias = Union[str, TestHelpersTestClock, None]


class BillingCreditBalanceTransaction(BaseModel):
    """
    A credit balance transaction is a resource representing a transaction (either a credit or a debit) against an existing credit grant.
    """

    id: str
    """Unique identifier for the object."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    credit_grant: CreditGrant
    """The credit grant associated with this credit balance transaction."""

    effective_at: int
    """The effective time of this credit balance transaction."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["billing.credit_balance_transaction"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    credit: Optional["BillingCreditGrantsResourceBalanceCredit"] = None

    debit: Optional["BillingCreditGrantsResourceBalanceDebit"] = None

    test_clock: Optional[TestClock] = None
    """ID of the test clock this credit balance transaction belongs to."""

    type: Optional[Literal["credit", "debit"]] = None
    """The type of credit balance transaction (credit or debit)."""


from .billing_credit_grant import BillingCreditGrant
from .billing_credit_grants_resource_balance_debit import BillingCreditGrantsResourceBalanceDebit
from .billing_credit_grants_resource_balance_credit import BillingCreditGrantsResourceBalanceCredit
