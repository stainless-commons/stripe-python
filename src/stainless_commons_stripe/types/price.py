# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "Price",
    "Product",
    "ProductDeletedProduct",
    "CurrencyOptions",
    "CurrencyOptionsCustomUnitAmount",
    "CurrencyOptionsTier",
    "CustomUnitAmount",
    "Recurring",
    "Tier",
    "TransformQuantity",
]


class ProductDeletedProduct(BaseModel):
    id: str
    """Unique identifier for the object."""

    deleted: Literal[True]
    """Always true for a deleted object"""

    object: Literal["product"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    Product = TypeAliasType("Product", Union[str, "product.Product", ProductDeletedProduct])
else:
    Product: TypeAlias = Union[str, "product.Product", ProductDeletedProduct]


class CurrencyOptionsCustomUnitAmount(BaseModel):
    maximum: Optional[int] = None
    """The maximum unit amount the customer can specify for this item."""

    minimum: Optional[int] = None
    """The minimum unit amount the customer can specify for this item.

    Must be at least the minimum charge amount.
    """

    preset: Optional[int] = None
    """The starting unit amount which can be updated by the customer."""


class CurrencyOptionsTier(BaseModel):
    flat_amount: Optional[int] = None
    """Price for the entire tier."""

    flat_amount_decimal: Optional[str] = None
    """
    Same as `flat_amount`, but contains a decimal value with at most 12 decimal
    places.
    """

    unit_amount: Optional[int] = None
    """Per unit price for units relevant to the tier."""

    unit_amount_decimal: Optional[str] = None
    """
    Same as `unit_amount`, but contains a decimal value with at most 12 decimal
    places.
    """

    up_to: Optional[int] = None
    """Up to and including to this quantity will be contained in the tier."""


class CurrencyOptions(BaseModel):
    custom_unit_amount: Optional[CurrencyOptionsCustomUnitAmount] = None

    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified"]] = None
    """
    Only required if a
    [default tax behavior](<https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)>)
    was not provided in the Stripe Tax settings. Specifies whether the price is
    considered inclusive of taxes or exclusive of taxes. One of `inclusive`,
    `exclusive`, or `unspecified`. Once specified as either `inclusive` or
    `exclusive`, it cannot be changed.
    """

    tiers: Optional[List[CurrencyOptionsTier]] = None
    """Each element represents a pricing tier.

    This parameter requires `billing_scheme` to be set to `tiered`. See also the
    documentation for `billing_scheme`.
    """

    unit_amount: Optional[int] = None
    """
    The unit amount in cents (or local equivalent) to be charged, represented as a
    whole integer if possible. Only set if `billing_scheme=per_unit`.
    """

    unit_amount_decimal: Optional[str] = None
    """
    The unit amount in cents (or local equivalent) to be charged, represented as a
    decimal string with at most 12 decimal places. Only set if
    `billing_scheme=per_unit`.
    """


class CustomUnitAmount(BaseModel):
    maximum: Optional[int] = None
    """The maximum unit amount the customer can specify for this item."""

    minimum: Optional[int] = None
    """The minimum unit amount the customer can specify for this item.

    Must be at least the minimum charge amount.
    """

    preset: Optional[int] = None
    """The starting unit amount which can be updated by the customer."""


class Recurring(BaseModel):
    interval: Literal["day", "month", "week", "year"]
    """The frequency at which a subscription is billed.

    One of `day`, `week`, `month` or `year`.
    """

    interval_count: int
    """
    The number of intervals (specified in the `interval` attribute) between
    subscription billings. For example, `interval=month` and `interval_count=3`
    bills every 3 months.
    """

    usage_type: Literal["licensed", "metered"]
    """Configures how the quantity per period should be determined.

    Can be either `metered` or `licensed`. `licensed` automatically bills the
    `quantity` set when adding it to a subscription. `metered` aggregates the total
    usage based on usage records. Defaults to `licensed`.
    """

    meter: Optional[str] = None
    """The meter tracking the usage of a metered price"""


class Tier(BaseModel):
    flat_amount: Optional[int] = None
    """Price for the entire tier."""

    flat_amount_decimal: Optional[str] = None
    """
    Same as `flat_amount`, but contains a decimal value with at most 12 decimal
    places.
    """

    unit_amount: Optional[int] = None
    """Per unit price for units relevant to the tier."""

    unit_amount_decimal: Optional[str] = None
    """
    Same as `unit_amount`, but contains a decimal value with at most 12 decimal
    places.
    """

    up_to: Optional[int] = None
    """Up to and including to this quantity will be contained in the tier."""


class TransformQuantity(BaseModel):
    divide_by: int
    """Divide usage by this number."""

    round: Literal["down", "up"]
    """After division, either round the result `up` or `down`."""


class Price(BaseModel):
    """
    Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.
    [Products](https://api.stripe.com#products) help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

    For example, you might have a single "gold" product that has prices for $10/month, $100/year, and €9 once.

    Related guides: [Set up a subscription](https://docs.stripe.com/billing/subscriptions/set-up-subscription), [create an invoice](https://docs.stripe.com/billing/invoices/create), and more about [products and prices](https://docs.stripe.com/products-prices/overview).
    """

    id: str
    """Unique identifier for the object."""

    active: bool
    """Whether the price can be used for new purchases."""

    billing_scheme: Literal["per_unit", "tiered"]
    """Describes how to compute the price per period.

    Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount
    (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit
    in `quantity` (for prices with `usage_type=licensed`), or per unit of total
    usage (for prices with `usage_type=metered`). `tiered` indicates that the unit
    pricing will be computed using a tiering strategy as defined using the `tiers`
    and `tiers_mode` attributes.
    """

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

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

    object: Literal["price"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    product: Product
    """The ID of the product this price is associated with."""

    type: Literal["one_time", "recurring"]
    """
    One of `one_time` or `recurring` depending on whether the price is for a
    one-time purchase or a recurring (subscription) purchase.
    """

    currency_options: Optional[Dict[str, CurrencyOptions]] = None
    """Prices defined in each available currency option.

    Each key must be a three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a
    [supported currency](https://stripe.com/docs/currencies).
    """

    custom_unit_amount: Optional[CustomUnitAmount] = None

    lookup_key: Optional[str] = None
    """A lookup key used to retrieve prices dynamically from a static string.

    This may be up to 200 characters.
    """

    nickname: Optional[str] = None
    """A brief description of the price, hidden from customers."""

    recurring: Optional[Recurring] = None

    tax_behavior: Optional[Literal["exclusive", "inclusive", "unspecified"]] = None
    """
    Only required if a
    [default tax behavior](<https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)>)
    was not provided in the Stripe Tax settings. Specifies whether the price is
    considered inclusive of taxes or exclusive of taxes. One of `inclusive`,
    `exclusive`, or `unspecified`. Once specified as either `inclusive` or
    `exclusive`, it cannot be changed.
    """

    tiers: Optional[List[Tier]] = None
    """Each element represents a pricing tier.

    This parameter requires `billing_scheme` to be set to `tiered`. See also the
    documentation for `billing_scheme`.
    """

    tiers_mode: Optional[Literal["graduated", "volume"]] = None
    """Defines if the tiering price should be `graduated` or `volume` based.

    In `volume`-based tiering, the maximum quantity within a period determines the
    per unit price. In `graduated` tiering, pricing can change as the quantity
    grows.
    """

    transform_quantity: Optional[TransformQuantity] = None

    unit_amount: Optional[int] = None
    """
    The unit amount in cents (or local equivalent) to be charged, represented as a
    whole integer if possible. Only set if `billing_scheme=per_unit`.
    """

    unit_amount_decimal: Optional[str] = None
    """
    The unit amount in cents (or local equivalent) to be charged, represented as a
    decimal string with at most 12 decimal places. Only set if
    `billing_scheme=per_unit`.
    """


from . import product
