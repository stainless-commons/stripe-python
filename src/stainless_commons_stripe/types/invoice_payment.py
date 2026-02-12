# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["InvoicePayment", "Invoice", "InvoiceDeletedInvoice", "StatusTransitions"]


class InvoiceDeletedInvoice(BaseModel):
    id: str
    """Unique identifier for the object."""

    deleted: Literal[True]
    """Always true for a deleted object"""

    object: Literal["invoice"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    Invoice = TypeAliasType("Invoice", Union[str, "invoice.Invoice", InvoiceDeletedInvoice])
else:
    Invoice: TypeAlias = Union[str, "invoice.Invoice", InvoiceDeletedInvoice]


class StatusTransitions(BaseModel):
    canceled_at: Optional[int] = None
    """The time that the payment was canceled."""

    paid_at: Optional[int] = None
    """The time that the payment succeeded."""


class InvoicePayment(BaseModel):
    """Invoice Payments represent payments made against invoices.

    Invoice Payments can
    be accessed in two ways:
    1. By expanding the `payments` field on the [Invoice](https://api.stripe.com#invoice) resource.
    2. By using the Invoice Payment retrieve and list endpoints.

    Invoice Payments include the mapping between payment objects, such as Payment Intent, and Invoices.
    This resource and its endpoints allows you to easily track if a payment is associated with a specific invoice and
    monitor the allocation details of the payments.
    """

    id: str
    """Unique identifier for the object."""

    amount_requested: int
    """Amount intended to be paid toward this invoice, in cents (or local equivalent)"""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    invoice: Invoice
    """The invoice that was paid."""

    is_default: bool
    """
    Stripe automatically creates a default InvoicePayment when the invoice is
    finalized, and keeps it synchronized with the invoice’s `amount_remaining`. The
    PaymentIntent associated with the default payment can’t be edited or canceled
    directly.
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["invoice_payment"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    payment: "InvoicesPaymentsInvoicePaymentAssociatedPayment"

    status: str
    """The status of the payment, one of `open`, `paid`, or `canceled`."""

    status_transitions: StatusTransitions

    amount_paid: Optional[int] = None
    """Amount that was actually paid for this invoice, in cents (or local equivalent).

    This field is null until the payment is `paid`. This amount can be less than the
    `amount_requested` if the PaymentIntent’s `amount_received` is not sufficient to
    pay all of the invoices that it is attached to.
    """


from . import invoice
from .invoices_payments_invoice_payment_associated_payment import InvoicesPaymentsInvoicePaymentAssociatedPayment
