# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "PriceCreateParams",
    "CurrencyOptions",
    "CurrencyOptionsCustomUnitAmount",
    "CurrencyOptionsTier",
    "CustomUnitAmount",
    "ProductData",
    "Recurring",
    "Tier",
    "TransformQuantity",
]


class PriceCreateParams(TypedDict, total=False):
    currency: Required[str]
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    active: bool
    """Whether the price can be used for new purchases. Defaults to `true`."""

    billing_scheme: Literal["per_unit", "tiered"]
    """Describes how to compute the price per period.

    Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount
    (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit
    in `quantity` (for prices with `usage_type=licensed`), or per unit of total
    usage (for prices with `usage_type=metered`). `tiered` indicates that the unit
    pricing will be computed using a tiering strategy as defined using the `tiers`
    and `tiers_mode` attributes.
    """

    currency_options: Dict[str, CurrencyOptions]
    """Prices defined in each available currency option.

    Each key must be a three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a
    [supported currency](https://stripe.com/docs/currencies).
    """

    custom_unit_amount: CustomUnitAmount
    """
    When set, provides configuration for the amount to be adjusted by the customer
    during Checkout Sessions and Payment Links.
    """

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    lookup_key: str
    """A lookup key used to retrieve prices dynamically from a static string.

    This may be up to 200 characters.
    """

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Individual keys can be unset by posting an
    empty value to them. All keys can be unset by posting an empty value to
    `metadata`.
    """

    nickname: str
    """A brief description of the price, hidden from customers."""

    product: str
    """
    The ID of the [Product](https://docs.stripe.com/api/products) that this
    [Price](https://docs.stripe.com/api/prices) will belong to.
    """

    product_data: ProductData
    """
    These fields can be used to create a new product that this price will belong to.
    """

    recurring: Recurring
    """The recurring components of a price such as `interval` and `usage_type`."""

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]
    """
    Only required if a
    [default tax behavior](<https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)>)
    was not provided in the Stripe Tax settings. Specifies whether the price is
    considered inclusive of taxes or exclusive of taxes. One of `inclusive`,
    `exclusive`, or `unspecified`. Once specified as either `inclusive` or
    `exclusive`, it cannot be changed.
    """

    tiers: Iterable[Tier]
    """Each element represents a pricing tier.

    This parameter requires `billing_scheme` to be set to `tiered`. See also the
    documentation for `billing_scheme`.
    """

    tiers_mode: Literal["graduated", "volume"]
    """Defines if the tiering price should be `graduated` or `volume` based.

    In `volume`-based tiering, the maximum quantity within a period determines the
    per unit price, in `graduated` tiering pricing can successively change as the
    quantity grows.
    """

    transfer_lookup_key: bool
    """
    If set to true, will atomically remove the lookup key from the existing price,
    and assign it to this price.
    """

    transform_quantity: TransformQuantity
    """
    Apply a transformation to the reported usage or set quantity before computing
    the billed price. Cannot be combined with `tiers`.
    """

    unit_amount: int
    """
    A positive integer in cents (or local equivalent) (or 0 for a free price)
    representing how much to charge. One of `unit_amount`, `unit_amount_decimal`, or
    `custom_unit_amount` is required, unless `billing_scheme=tiered`.
    """

    unit_amount_decimal: str
    """
    Same as `unit_amount`, but accepts a decimal value in cents (or local
    equivalent) with at most 12 decimal places. Only one of `unit_amount` and
    `unit_amount_decimal` can be set.
    """


class CurrencyOptionsCustomUnitAmount(TypedDict, total=False):
    enabled: Required[bool]

    maximum: int

    minimum: int

    preset: int


class CurrencyOptionsTier(TypedDict, total=False):
    up_to: Required[Union[Literal["inf"], int]]

    flat_amount: int

    flat_amount_decimal: str

    unit_amount: int

    unit_amount_decimal: str


class CurrencyOptions(TypedDict, total=False):
    custom_unit_amount: CurrencyOptionsCustomUnitAmount

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]

    tiers: Iterable[CurrencyOptionsTier]

    unit_amount: int

    unit_amount_decimal: str


class CustomUnitAmount(TypedDict, total=False):
    """
    When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.
    """

    enabled: Required[bool]

    maximum: int

    minimum: int

    preset: int


class ProductData(TypedDict, total=False):
    """
    These fields can be used to create a new product that this price will belong to.
    """

    name: Required[str]

    id: str

    active: bool

    metadata: Dict[str, str]

    statement_descriptor: str

    tax_code: str

    unit_label: str


class Recurring(TypedDict, total=False):
    """The recurring components of a price such as `interval` and `usage_type`."""

    interval: Required[Literal["day", "month", "week", "year"]]

    interval_count: int

    meter: str

    usage_type: Literal["licensed", "metered"]


class Tier(TypedDict, total=False):
    up_to: Required[Union[Literal["inf"], int]]

    flat_amount: int

    flat_amount_decimal: str

    unit_amount: int

    unit_amount_decimal: str


class TransformQuantity(TypedDict, total=False):
    """
    Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
    """

    divide_by: Required[int]

    round: Required[Literal["down", "up"]]
