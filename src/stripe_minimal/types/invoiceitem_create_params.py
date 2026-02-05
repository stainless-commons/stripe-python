# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["InvoiceitemCreateParams", "DiscountsUnionMember0", "Period", "PriceData", "Pricing"]


class InvoiceitemCreateParams(TypedDict, total=False):
    amount: int
    """
    The integer amount in cents (or local equivalent) of the charge to be applied to
    the upcoming invoice. Passing in a negative `amount` will reduce the
    `amount_due` on the invoice.
    """

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: str
    """The ID of the customer to bill for this invoice item."""

    customer_account: str
    """The ID of the account representing the customer to bill for this invoice item."""

    description: str
    """An arbitrary string which you can attach to the invoice item.

    The description is displayed in the invoice for easy tracking.
    """

    discountable: bool
    """Controls whether discounts apply to this invoice item.

    Defaults to false for prorations or negative invoice items, and true for all
    other invoice items.
    """

    discounts: Union[Iterable[DiscountsUnionMember0], Literal[""]]
    """
    The coupons and promotion codes to redeem into discounts for the invoice item or
    invoice line item.
    """

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    invoice: str
    """The ID of an existing invoice to add this invoice item to.

    For subscription invoices, when left blank, the invoice item will be added to
    the next upcoming scheduled invoice. For standalone invoices, the invoice item
    won't be automatically added unless you pass
    `pending_invoice_item_behavior: 'include'` when creating the invoice. This is
    useful when adding invoice items in response to an invoice.created webhook. You
    can only add invoice items to draft invoices and there is a maximum of 250 items
    per invoice.
    """

    metadata: Union[Dict[str, str], Literal[""]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Individual keys can be unset by posting an
    empty value to them. All keys can be unset by posting an empty value to
    `metadata`.
    """

    period: Period
    """The period associated with this invoice item.

    When set to different values, the period will be rendered on the invoice. If you
    have [Stripe Revenue Recognition](https://docs.stripe.com/revenue-recognition)
    enabled, the period will be used to recognize and defer revenue. See the
    [Revenue Recognition documentation](https://docs.stripe.com/revenue-recognition/methodology/subscriptions-and-invoicing)
    for details.
    """

    price_data: PriceData
    """
    Data used to generate a new [Price](https://docs.stripe.com/api/prices) object
    inline.
    """

    pricing: Pricing
    """The pricing information for the invoice item."""

    quantity: int
    """Non-negative integer. The quantity of units for the invoice item."""

    subscription: str
    """The ID of a subscription to add this invoice item to.

    When left blank, the invoice item is added to the next upcoming scheduled
    invoice. When set, scheduled invoices for subscriptions other than the specified
    subscription will ignore the invoice item. Use this when you want to express
    that an invoice item has been accrued within the context of a particular
    subscription.
    """

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]
    """
    Only required if a
    [default tax behavior](<https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)>)
    was not provided in the Stripe Tax settings. Specifies whether the price is
    considered inclusive of taxes or exclusive of taxes. One of `inclusive`,
    `exclusive`, or `unspecified`. Once specified as either `inclusive` or
    `exclusive`, it cannot be changed.
    """

    tax_code: Union[str, Literal[""]]
    """A [tax code](https://docs.stripe.com/tax/tax-categories) ID."""

    tax_rates: SequenceNotStr[str]
    """The tax rates which apply to the invoice item.

    When set, the `default_tax_rates` on the invoice do not apply to this invoice
    item.
    """

    unit_amount_decimal: str
    """
    The decimal unit amount in cents (or local equivalent) of the charge to be
    applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied
    by the quantity to get the full amount. Passing in a negative
    `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at
    most 12 decimal places.
    """


class DiscountsUnionMember0(TypedDict, total=False):
    coupon: str

    discount: str

    promotion_code: str


class Period(TypedDict, total=False):
    """The period associated with this invoice item.

    When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://docs.stripe.com/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://docs.stripe.com/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
    """

    end: Required[int]

    start: Required[int]


class PriceData(TypedDict, total=False):
    """
    Data used to generate a new [Price](https://docs.stripe.com/api/prices) object inline.
    """

    currency: Required[str]

    product: Required[str]

    tax_behavior: Literal["exclusive", "inclusive", "unspecified"]

    unit_amount: int

    unit_amount_decimal: str


class Pricing(TypedDict, total=False):
    """The pricing information for the invoice item."""

    price: str
