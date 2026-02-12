# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.deleted_customer import DeletedCustomer
from .shared.test_helpers_test_clock import TestHelpersTestClock
from .billing_credit_grants_resource_amount import BillingCreditGrantsResourceAmount

__all__ = [
    "BillingCreditGrant",
    "ApplicabilityConfig",
    "ApplicabilityConfigScope",
    "ApplicabilityConfigScopePrice",
    "Customer",
    "TestClock",
]


class ApplicabilityConfigScopePrice(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""


class ApplicabilityConfigScope(BaseModel):
    price_type: Optional[Literal["metered"]] = None
    """The price type that credit grants can apply to.

    We currently only support the `metered` price type. This refers to prices that
    have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to
    them. Cannot be used in combination with `prices`.
    """

    prices: Optional[List[ApplicabilityConfigScopePrice]] = None
    """The prices that credit grants can apply to.

    We currently only support `metered` prices. This refers to prices that have a
    [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.
    Cannot be used in combination with `price_type`.
    """


class ApplicabilityConfig(BaseModel):
    scope: ApplicabilityConfigScope


if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer]

TestClock: TypeAlias = Union[str, TestHelpersTestClock, None]


class BillingCreditGrant(BaseModel):
    """
    A credit grant is an API resource that documents the allocation of some billing credits to a customer.

    Related guide: [Billing credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
    """

    id: str
    """Unique identifier for the object."""

    amount: BillingCreditGrantsResourceAmount

    applicability_config: ApplicabilityConfig

    category: Literal["paid", "promotional"]
    """The category of this credit grant.

    This is for tracking purposes and isn't displayed to the customer.
    """

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    customer: Customer
    """ID of the customer receiving the billing credits."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    object: Literal["billing.credit_grant"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    updated: int
    """Time at which the object was last updated.

    Measured in seconds since the Unix epoch.
    """

    customer_account: Optional[str] = None
    """ID of the account representing the customer receiving the billing credits"""

    effective_at: Optional[int] = None
    """
    The time when the billing credits become effective-when they're eligible for
    use.
    """

    expires_at: Optional[int] = None
    """The time when the billing credits expire.

    If not present, the billing credits don't expire.
    """

    name: Optional[str] = None
    """A descriptive name shown in dashboard."""

    priority: Optional[int] = None
    """The priority for applying this credit grant.

    The highest priority is 0 and the lowest is 100.
    """

    test_clock: Optional[TestClock] = None
    """ID of the test clock this credit grant belongs to."""

    voided_at: Optional[int] = None
    """The time when this credit grant was voided.

    If not present, the credit grant hasn't been voided.
    """


from . import customer
