# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .tax_rate import TaxRate

__all__ = ["SubscriptionItem", "Discount", "BillingThresholds"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Discount = TypeAliasType("Discount", Union[str, "discount.Discount"])
else:
    Discount: TypeAlias = Union[str, "discount.Discount"]


class BillingThresholds(BaseModel):
    usage_gte: Optional[int] = None
    """Usage threshold that triggers the subscription to create an invoice"""


class SubscriptionItem(BaseModel):
    """
    Subscription items allow you to create customer subscriptions with more than
    one plan, making it easy to represent complex billing relationships.
    """

    id: str
    """Unique identifier for the object."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    current_period_end: int
    """The end time of this subscription item's current billing period."""

    current_period_start: int
    """The start time of this subscription item's current billing period."""

    discounts: List[Discount]
    """The discounts applied to the subscription item.

    Subscription item discounts are applied before subscription discounts. Use
    `expand[]=discounts` to expand each discount.
    """

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    object: Literal["subscription_item"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    price: "Price"
    """
    Prices define the unit cost, currency, and (optional) billing cycle for both
    recurring and one-time purchases of products.
    [Products](https://api.stripe.com#products) help you track inventory or
    provisioning, and prices help you track payment terms. Different physical goods
    or levels of service should be represented by products, and pricing options
    should be represented by prices. This approach lets you change prices without
    having to change your provisioning scheme.

    For example, you might have a single "gold" product that has prices for
    $10/month, $100/year, and €9 once.

    Related guides:
    [Set up a subscription](https://docs.stripe.com/billing/subscriptions/set-up-subscription),
    [create an invoice](https://docs.stripe.com/billing/invoices/create), and more
    about [products and prices](https://docs.stripe.com/products-prices/overview).
    """

    subscription: str
    """The `subscription` this `subscription_item` belongs to."""

    billing_thresholds: Optional[BillingThresholds] = None

    quantity: Optional[int] = None
    """
    The [quantity](https://docs.stripe.com/subscriptions/quantities) of the plan to
    which the customer should be subscribed.
    """

    tax_rates: Optional[List[TaxRate]] = None
    """The tax rates which apply to this `subscription_item`.

    When set, the `default_tax_rates` on the subscription do not apply to this
    `subscription_item`.
    """


from . import discount
from .price import Price
