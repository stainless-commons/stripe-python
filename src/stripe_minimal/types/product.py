# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import tax_code
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["Product", "MarketingFeature", "DefaultPrice", "PackageDimensions", "TaxCode"]


class MarketingFeature(BaseModel):
    name: Optional[str] = None
    """The marketing feature name. Up to 80 characters long."""


if TYPE_CHECKING or not PYDANTIC_V1:
    DefaultPrice = TypeAliasType("DefaultPrice", Union[str, "Price", None])
else:
    DefaultPrice: TypeAlias = Union[str, "Price", None]


class PackageDimensions(BaseModel):
    height: float
    """Height, in inches."""

    length: float
    """Length, in inches."""

    weight: float
    """Weight, in ounces."""

    width: float
    """Width, in inches."""


TaxCode: TypeAlias = Union[str, tax_code.TaxCode, None]


class Product(BaseModel):
    """
    Products describe the specific goods or services you offer to your customers.
    For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product.
    They can be used in conjunction with [Prices](https://api.stripe.com#prices) to configure pricing in Payment Links, Checkout, and Subscriptions.

    Related guides: [Set up a subscription](https://docs.stripe.com/billing/subscriptions/set-up-subscription),
    [share a Payment Link](https://docs.stripe.com/payment-links),
    [accept payments with Checkout](https://docs.stripe.com/payments/accept-a-payment#create-product-prices-upfront),
    and more about [Products and Prices](https://docs.stripe.com/products-prices/overview)
    """

    id: str
    """Unique identifier for the object."""

    active: bool
    """Whether the product is currently available for purchase."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    images: List[str]
    """
    A list of up to 8 URLs of images for this product, meant to be displayable to
    the customer.
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    marketing_features: List[MarketingFeature]
    """A list of up to 15 marketing features for this product.

    These are displayed in
    [pricing tables](https://docs.stripe.com/payments/checkout/pricing-table).
    """

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    name: str
    """The product's name, meant to be displayable to the customer."""

    object: Literal["product"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    updated: int
    """Time at which the object was last updated.

    Measured in seconds since the Unix epoch.
    """

    default_price: Optional[DefaultPrice] = None
    """
    The ID of the [Price](https://docs.stripe.com/api/prices) object that is the
    default price for this product.
    """

    description: Optional[str] = None
    """The product's description, meant to be displayable to the customer.

    Use this field to optionally store a long form explanation of the product being
    sold for your own rendering purposes.
    """

    package_dimensions: Optional[PackageDimensions] = None

    shippable: Optional[bool] = None
    """Whether this product is shipped (i.e., physical goods)."""

    statement_descriptor: Optional[str] = None
    """
    Extra information about a product which will appear on your customer's credit
    card statement. In the case that multiple products are billed at once, the first
    statement descriptor will be used. Only used for subscription payments.
    """

    tax_code: Optional[TaxCode] = None
    """A [tax code](https://docs.stripe.com/tax/tax-categories) ID."""

    unit_label: Optional[str] = None
    """A label that represents units of this product.

    When set, this will be included in customers' receipts, invoices, Checkout, and
    the customer portal.
    """

    url: Optional[str] = None
    """A URL of a publicly-accessible webpage for this product."""


from .price import Price
