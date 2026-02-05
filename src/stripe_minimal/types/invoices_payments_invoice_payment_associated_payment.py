# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["InvoicesPaymentsInvoicePaymentAssociatedPayment", "Charge", "PaymentIntent", "PaymentRecord"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Charge = TypeAliasType("Charge", Union[str, "charge.Charge"])
else:
    Charge: TypeAlias = Union[str, "charge.Charge"]

if TYPE_CHECKING or not PYDANTIC_V1:
    PaymentIntent = TypeAliasType("PaymentIntent", Union[str, "payment_intent.PaymentIntent"])
else:
    PaymentIntent: TypeAlias = Union[str, "payment_intent.PaymentIntent"]

if TYPE_CHECKING or not PYDANTIC_V1:
    PaymentRecord = TypeAliasType("PaymentRecord", Union[str, "payment_record.PaymentRecord"])
else:
    PaymentRecord: TypeAlias = Union[str, "payment_record.PaymentRecord"]


class InvoicesPaymentsInvoicePaymentAssociatedPayment(BaseModel):
    type: Literal["charge", "payment_intent", "payment_record"]
    """Type of payment object associated with this invoice payment."""

    charge: Optional[Charge] = None
    """
    ID of the successful charge for this payment when `type` is `charge`.Note:
    charge is only surfaced if the charge object is not associated with a payment
    intent. If the charge object does have a payment intent, the Invoice Payment
    surfaces the payment intent instead.
    """

    payment_intent: Optional[PaymentIntent] = None
    """
    ID of the PaymentIntent associated with this payment when `type` is
    `payment_intent`. Note: This property is only populated for invoices finalized
    on or after March 15th, 2019.
    """

    payment_record: Optional[PaymentRecord] = None
    """
    ID of the PaymentRecord associated with this payment when `type` is
    `payment_record`.
    """


from . import charge, payment_intent, payment_record
