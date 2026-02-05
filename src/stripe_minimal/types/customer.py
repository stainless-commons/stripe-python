# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.source import Source
from .shared.address import Address
from .shared.shipping import Shipping
from .shared.test_helpers_test_clock import TestHelpersTestClock

__all__ = [
    "Customer",
    "CashBalance",
    "CashBalanceSettings",
    "DefaultSource",
    "Sources",
    "SourcesData",
    "Subscriptions",
    "Tax",
    "TaxLocation",
    "TaxIDs",
    "TestClock",
]


class CashBalanceSettings(BaseModel):
    reconciliation_mode: Literal["automatic", "manual"]
    """
    The configuration for how funds that land in the customer cash balance are
    reconciled.
    """

    using_merchant_default: bool
    """
    A flag to indicate if reconciliation mode returned is the user's default or is
    specific to this customer cash balance
    """


class CashBalance(BaseModel):
    """A customer's `Cash balance` represents real funds.

    Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.
    """

    customer: str
    """The ID of the customer whose cash balance this object represents."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["cash_balance"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    settings: CashBalanceSettings

    available: Optional[Dict[str, int]] = None
    """A hash of all cash balances available to this customer.

    You cannot delete a customer with any cash balances, even if the balance is 0.
    Amounts are represented in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """

    customer_account: Optional[str] = None
    """
    The ID of an Account representing a customer whose cash balance this object
    represents.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    DefaultSource = TypeAliasType("DefaultSource", Union[str, "BankAccount", "Card", Source, None])
else:
    DefaultSource: TypeAlias = Union[str, "BankAccount", "Card", Source, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    SourcesData = TypeAliasType("SourcesData", Union["BankAccount", "Card", Source])
else:
    SourcesData: TypeAlias = Union["BankAccount", "Card", Source]


class Sources(BaseModel):
    """The customer's payment sources, if any."""

    data: List[SourcesData]
    """Details about each object."""

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


class Subscriptions(BaseModel):
    """The customer's current subscriptions, if any."""

    data: List["Subscription"]
    """Details about each object."""

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


class TaxLocation(BaseModel):
    country: str
    """The identified tax country of the customer."""

    source: Literal["billing_address", "ip_address", "payment_method", "shipping_destination"]
    """The data source used to infer the customer's location."""

    state: Optional[str] = None
    """The identified tax state, county, province, or region of the customer."""


class Tax(BaseModel):
    automatic_tax: Literal["failed", "not_collecting", "supported", "unrecognized_location"]
    """
    Surfaces if automatic tax computation is possible given the current customer
    location information.
    """

    provider: Literal["anrok", "avalara", "sphere", "stripe"]
    """The tax calculation provider used for location resolution.

    Defaults to `stripe` when not using a
    [third-party provider](/tax/third-party-apps).
    """

    ip_address: Optional[str] = None
    """
    A recent IP address of the customer used for tax reporting and tax location
    inference.
    """

    location: Optional[TaxLocation] = None


class TaxIDs(BaseModel):
    """The customer's tax IDs."""

    data: List["TaxID"]
    """Details about each object."""

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


TestClock: TypeAlias = Union[str, TestHelpersTestClock, None]


class Customer(BaseModel):
    """This object represents a customer of your business.

    Use it to [create recurring charges](https://docs.stripe.com/invoicing/customer), [save payment](https://docs.stripe.com/payments/save-during-payment) and contact information,
    and track payments that belong to the same customer.
    """

    id: str
    """Unique identifier for the object."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["customer"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    address: Optional[Address] = None

    balance: Optional[int] = None
    """
    The current balance, if any, that's stored on the customer in their default
    currency. If negative, the customer has credit to apply to their next invoice.
    If positive, the customer has an amount owed that's added to their next invoice.
    The balance only considers amounts that Stripe hasn't successfully applied to
    any invoice. It doesn't reflect unpaid invoices. This balance is only taken into
    account after invoices finalize. For multi-currency balances, see
    [invoice_credit_balance](https://docs.stripe.com/api/customers/object#customer_object-invoice_credit_balance).
    """

    business_name: Optional[str] = None
    """The customer's business name."""

    cash_balance: Optional[CashBalance] = None
    """A customer's `Cash balance` represents real funds.

    Customers can add funds to their cash balance by sending a bank transfer. These
    funds can be used for payment and can eventually be paid out to your bank
    account.
    """

    currency: Optional[str] = None
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) the
    customer can be charged in for recurring billing purposes.
    """

    customer_account: Optional[str] = None
    """The ID of an Account representing a customer.

    You can use this ID with any v1 API that accepts a customer_account parameter.
    """

    default_source: Optional[DefaultSource] = None
    """ID of the default payment source for the customer.

    If you use payment methods created through the PaymentMethods API, see the
    [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
    field instead.
    """

    delinquent: Optional[bool] = None
    """Tracks the most recent state change on any invoice belonging to the customer.

    Paying an invoice or marking it uncollectible via the API will set this field to
    false. An automatic payment failure or passing the `invoice.due_date` will set
    this field to `true`.

    If an invoice becomes uncollectible by
    [dunning](https://docs.stripe.com/billing/automatic-collection), `delinquent`
    doesn't reset to `false`.

    If you care whether the customer has paid their most recent subscription
    invoice, use `subscription.status` instead. Paying or marking uncollectible any
    customer invoice regardless of whether it is the latest invoice for a
    subscription will always set this field to `false`.
    """

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    discount: Optional["Discount"] = None
    """
    A discount represents the actual application of a
    [coupon](https://api.stripe.com#coupons) or
    [promotion code](https://api.stripe.com#promotion_codes). It contains
    information about when the discount began, when it will end, and what it is
    applied to.

    Related guide:
    [Applying discounts to subscriptions](https://docs.stripe.com/billing/subscriptions/discounts)
    """

    email: Optional[str] = None
    """The customer's email address."""

    individual_name: Optional[str] = None
    """The customer's individual name."""

    invoice_credit_balance: Optional[Dict[str, int]] = None
    """The current multi-currency balances, if any, that's stored on the customer.

    If positive in a currency, the customer has a credit to apply to their next
    invoice denominated in that currency. If negative, the customer has an amount
    owed that's added to their next invoice denominated in that currency. These
    balances don't apply to unpaid invoices. They solely track amounts that Stripe
    hasn't successfully applied to any invoice. Stripe only applies a balance in a
    specific currency to an invoice after that invoice (which is in the same
    currency) finalizes.
    """

    invoice_prefix: Optional[str] = None
    """The prefix for the customer used to generate unique invoice numbers."""

    invoice_settings: Optional["InvoiceSetting"] = None

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    name: Optional[str] = None
    """The customer's full name or business name."""

    next_invoice_sequence: Optional[int] = None
    """The suffix of the customer's next invoice number (for example, 0001).

    When the account uses account level sequencing, this parameter is ignored in API
    requests and the field omitted in API responses.
    """

    phone: Optional[str] = None
    """The customer's phone number."""

    preferred_locales: Optional[List[str]] = None
    """The customer's preferred locales (languages), ordered by preference."""

    shipping: Optional[Shipping] = None

    sources: Optional[Sources] = None
    """The customer's payment sources, if any."""

    subscriptions: Optional[Subscriptions] = None
    """The customer's current subscriptions, if any."""

    tax: Optional[Tax] = None

    tax_exempt: Optional[Literal["exempt", "none", "reverse"]] = None
    """
    Describes the customer's tax exemption status, which is `none`, `exempt`, or
    `reverse`. When set to `reverse`, invoice and receipt PDFs include the following
    text: **"Reverse charge"**.
    """

    tax_ids: Optional[TaxIDs] = None
    """The customer's tax IDs."""

    test_clock: Optional[TestClock] = None
    """ID of the test clock that this customer belongs to."""


from .card import Card
from .tax_id import TaxID
from .discount import Discount
from .bank_account import BankAccount
from .subscription import Subscription
from .invoice_setting import InvoiceSetting
