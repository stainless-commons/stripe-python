# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .tax_rate import TaxRate
from .shared.deleted_customer import DeletedCustomer
from .shared.test_helpers_test_clock import TestHelpersTestClock

__all__ = [
    "InvoiceitemCreateResponse",
    "Customer",
    "Period",
    "Discount",
    "Invoice",
    "Parent",
    "ParentSubscriptionDetails",
    "Pricing",
    "PricingPriceDetails",
    "PricingPriceDetailsPrice",
    "ProrationDetails",
    "TestClock",
]

Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer]


class Period(BaseModel):
    end: int
    """The end of the period, which must be greater than or equal to the start.

    This value is inclusive.
    """

    start: int
    """The start of the period. This value is inclusive."""


Discount: TypeAlias = Union[str, "discount.Discount"]

Invoice: TypeAlias = Union[str, "invoice.Invoice", None]


class ParentSubscriptionDetails(BaseModel):
    subscription: str
    """The subscription that generated this invoice item"""

    subscription_item: Optional[str] = None
    """The subscription item that generated this invoice item"""


class Parent(BaseModel):
    type: Literal["subscription_details"]
    """The type of parent that generated this invoice item"""

    subscription_details: Optional[ParentSubscriptionDetails] = None


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


class ProrationDetails(BaseModel):
    discount_amounts: List["DiscountsResourceDiscountAmount"]
    """Discount amounts applied when the proration was created."""


TestClock: TypeAlias = Union[str, TestHelpersTestClock, None]


class InvoiceitemCreateResponse(BaseModel):
    """
    Invoice Items represent the component lines of an [invoice](https://docs.stripe.com/api/invoices). When you create an invoice item with an `invoice` field, it is attached to the specified invoice and included as [an invoice line item](https://docs.stripe.com/api/invoices/line_item) within [invoice.lines](https://docs.stripe.com/api/invoices/object#invoice_object-lines).

    Invoice Items can be created before you are ready to actually send the invoice. This can be particularly useful when combined
    with a [subscription](https://docs.stripe.com/api/subscriptions). Sometimes you want to add a charge or credit to a customer, but actually charge
    or credit the customer's card only at the end of a regular billing cycle. This is useful for combining several charges
    (to minimize per-transaction fees), or for having Stripe tabulate your usage-based billing totals.

    Related guides: [Integrate with the Invoicing API](https://docs.stripe.com/invoicing/integration), [Subscription Invoices](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items).
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """Amount (in the `currency` specified) of the invoice item.

    This should always be equal to `unit_amount * quantity`.
    """

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: Customer
    """The ID of the customer to bill for this invoice item."""

    date: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    discountable: bool
    """If true, discounts will apply to this invoice item.

    Always false for prorations.
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["invoiceitem"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    period: Period

    proration: bool
    """
    Whether the invoice item was created automatically as a proration adjustment
    when the customer switched plans.
    """

    quantity: int
    """Quantity of units for the invoice item.

    If the invoice item is a proration, the quantity of the subscription that the
    proration was computed for.
    """

    customer_account: Optional[str] = None
    """The ID of the account to bill for this invoice item."""

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    discounts: Optional[List[Discount]] = None
    """The discounts which apply to the invoice item.

    Item discounts are applied before invoice discounts. Use `expand[]=discounts` to
    expand each discount.
    """

    invoice: Optional[Invoice] = None
    """The ID of the invoice this invoice item belongs to."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    net_amount: Optional[int] = None
    """The amount after discounts, but before credits and taxes.

    This field is `null` for `discountable=true` items.
    """

    parent: Optional[Parent] = None

    pricing: Optional[Pricing] = None

    proration_details: Optional[ProrationDetails] = None

    tax_rates: Optional[List[TaxRate]] = None
    """The tax rates which apply to the invoice item.

    When set, the `default_tax_rates` on the invoice do not apply to this invoice
    item.
    """

    test_clock: Optional[TestClock] = None
    """ID of the test clock this invoice item belongs to."""


from . import invoice, customer, discount
from .price import Price
from .discounts_resource_discount_amount import DiscountsResourceDiscountAmount
