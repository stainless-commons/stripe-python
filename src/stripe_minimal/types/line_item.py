# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "LineItem",
    "Discount",
    "Period",
    "Parent",
    "ParentInvoiceItemDetails",
    "ParentInvoiceItemDetailsProrationDetails",
    "ParentInvoiceItemDetailsProrationDetailsCreditedItems",
    "ParentSubscriptionItemDetails",
    "ParentSubscriptionItemDetailsProrationDetails",
    "ParentSubscriptionItemDetailsProrationDetailsCreditedItems",
    "Pricing",
    "PricingPriceDetails",
    "PricingPriceDetailsPrice",
    "Subscription",
    "Tax",
    "TaxTaxRateDetails",
]

if TYPE_CHECKING or not PYDANTIC_V1:
    Discount = TypeAliasType("Discount", Union[str, "discount.Discount"])
else:
    Discount: TypeAlias = Union[str, "discount.Discount"]


class Period(BaseModel):
    end: int
    """The end of the period, which must be greater than or equal to the start.

    This value is inclusive.
    """

    start: int
    """The start of the period. This value is inclusive."""


class ParentInvoiceItemDetailsProrationDetailsCreditedItems(BaseModel):
    invoice: str
    """Invoice containing the credited invoice line items"""

    invoice_line_items: List[str]
    """Credited invoice line items"""


class ParentInvoiceItemDetailsProrationDetails(BaseModel):
    credited_items: Optional[ParentInvoiceItemDetailsProrationDetailsCreditedItems] = None


class ParentInvoiceItemDetails(BaseModel):
    invoice_item: str
    """The invoice item that generated this line item"""

    proration: bool
    """Whether this is a proration"""

    proration_details: Optional[ParentInvoiceItemDetailsProrationDetails] = None

    subscription: Optional[str] = None
    """The subscription that the invoice item belongs to"""


class ParentSubscriptionItemDetailsProrationDetailsCreditedItems(BaseModel):
    invoice: str
    """Invoice containing the credited invoice line items"""

    invoice_line_items: List[str]
    """Credited invoice line items"""


class ParentSubscriptionItemDetailsProrationDetails(BaseModel):
    credited_items: Optional[ParentSubscriptionItemDetailsProrationDetailsCreditedItems] = None


class ParentSubscriptionItemDetails(BaseModel):
    proration: bool
    """Whether this is a proration"""

    subscription_item: str
    """The subscription item that generated this line item"""

    invoice_item: Optional[str] = None
    """The invoice item that generated this line item"""

    proration_details: Optional[ParentSubscriptionItemDetailsProrationDetails] = None

    subscription: Optional[str] = None
    """The subscription that the subscription item belongs to"""


class Parent(BaseModel):
    type: Literal["invoice_item_details", "subscription_item_details"]
    """The type of parent that generated this line item"""

    invoice_item_details: Optional[ParentInvoiceItemDetails] = None

    subscription_item_details: Optional[ParentSubscriptionItemDetails] = None


PricingPriceDetailsPrice: TypeAlias = Union[str, "Price"]


class PricingPriceDetails(BaseModel):
    price: PricingPriceDetailsPrice
    """The ID of the price this item is associated with."""

    product: str
    """The ID of the product this item is associated with."""


class Pricing(BaseModel):
    type: Literal["price_details"]
    """The type of the pricing details."""

    price_details: Optional[PricingPriceDetails] = None

    unit_amount_decimal: Optional[str] = None
    """
    The unit amount (in the `currency` specified) of the item which contains a
    decimal value with at most 12 decimal places.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    Subscription = TypeAliasType("Subscription", Union[str, "subscription.Subscription", None])
else:
    Subscription: TypeAlias = Union[str, "subscription.Subscription", None]


class TaxTaxRateDetails(BaseModel):
    tax_rate: str
    """ID of the tax rate"""


class Tax(BaseModel):
    amount: int
    """The amount of the tax, in cents (or local equivalent)."""

    tax_behavior: Literal["exclusive", "inclusive"]
    """Whether this tax is inclusive or exclusive."""

    taxability_reason: Literal[
        "customer_exempt",
        "not_available",
        "not_collecting",
        "not_subject_to_tax",
        "not_supported",
        "portion_product_exempt",
        "portion_reduced_rated",
        "portion_standard_rated",
        "product_exempt",
        "product_exempt_holiday",
        "proportionally_rated",
        "reduced_rated",
        "reverse_charge",
        "standard_rated",
        "taxable_basis_reduced",
        "zero_rated",
    ]
    """The reasoning behind this tax, for example, if the product is tax exempt.

    The possible values for this field may be extended as new tax rules are
    supported.
    """

    type: Literal["tax_rate_details"]
    """The type of tax information."""

    tax_rate_details: Optional[TaxTaxRateDetails] = None

    taxable_amount: Optional[int] = None
    """The amount on which tax is calculated, in cents (or local equivalent)."""


class LineItem(BaseModel):
    """
    Invoice Line Items represent the individual lines within an [invoice](https://docs.stripe.com/api/invoices) and only exist within the context of an invoice.

    Each line item is backed by either an [invoice item](https://docs.stripe.com/api/invoiceitems) or a [subscription item](https://docs.stripe.com/api/subscription_items).
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """The amount, in cents (or local equivalent)."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    discountable: bool
    """If true, discounts will apply to this line item. Always false for prorations."""

    discounts: List[Discount]
    """The discounts applied to the invoice line item.

    Line item discounts are applied before invoice discounts. Use
    `expand[]=discounts` to expand each discount.
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
    the object in a structured format. Note that for line items with
    `type=subscription`, `metadata` reflects the current metadata from the
    subscription associated with the line item, unless the invoice line was directly
    updated with different metadata after creation.
    """

    object: Literal["line_item"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    period: Period

    subtotal: int
    """
    The subtotal of the line item, in cents (or local equivalent), before any
    discounts or taxes.
    """

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    discount_amounts: Optional[List["DiscountsResourceDiscountAmount"]] = None
    """The amount of discount calculated per discount for this line item."""

    invoice: Optional[str] = None
    """The ID of the invoice that contains this line item."""

    parent: Optional[Parent] = None

    pretax_credit_amounts: Optional[List["InvoicesResourcePretaxCreditAmount"]] = None
    """
    Contains pretax credit amounts (ex: discount, credit grants, etc) that apply to
    this line item.
    """

    pricing: Optional[Pricing] = None

    quantity: Optional[int] = None
    """
    The quantity of the subscription, if the line item is a subscription or a
    proration.
    """

    subscription: Optional[Subscription] = None
    """Subscriptions allow you to charge a customer on a recurring basis.

    Related guide:
    [Creating subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
    """

    taxes: Optional[List[Tax]] = None
    """The tax information of the line item."""


from . import discount, subscription
from .price import Price
from .discounts_resource_discount_amount import DiscountsResourceDiscountAmount
from .invoices_resource_pretax_credit_amount import InvoicesResourcePretaxCreditAmount
