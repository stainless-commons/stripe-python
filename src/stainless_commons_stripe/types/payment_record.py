# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .payments_primitives_payment_records_resource_amount import PaymentsPrimitivesPaymentRecordsResourceAmount

__all__ = [
    "PaymentRecord",
    "ProcessorDetails",
    "ProcessorDetailsCustom",
    "CustomerDetails",
    "ShippingDetails",
    "ShippingDetailsAddress",
]


class ProcessorDetailsCustom(BaseModel):
    """
    Custom processors represent payment processors not modeled directly in
    the Stripe API. This resource consists of details about the custom processor
    used for this payment attempt.
    """

    payment_reference: Optional[str] = None
    """
    An opaque string for manual reconciliation of this payment, for example a check
    number or a payment processor ID.
    """


class ProcessorDetails(BaseModel):
    """Processor information associated with this payment."""

    type: Literal["custom"]
    """The processor used for this payment attempt."""

    custom: Optional[ProcessorDetailsCustom] = None
    """
    Custom processors represent payment processors not modeled directly in the
    Stripe API. This resource consists of details about the custom processor used
    for this payment attempt.
    """


class CustomerDetails(BaseModel):
    """Information about the customer for this payment."""

    customer: Optional[str] = None
    """ID of the Stripe Customer associated with this payment."""

    email: Optional[str] = None
    """The customer's email address."""

    name: Optional[str] = None
    """The customer's name."""

    phone: Optional[str] = None
    """The customer's phone number."""


class ShippingDetailsAddress(BaseModel):
    """A representation of a physical address."""

    city: Optional[str] = None
    """City, district, suburb, town, or village."""

    country: Optional[str] = None
    """
    Two-letter country code
    ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """

    line1: Optional[str] = None
    """Address line 1, such as the street, PO Box, or company name."""

    line2: Optional[str] = None
    """Address line 2, such as the apartment, suite, unit, or building."""

    postal_code: Optional[str] = None
    """ZIP or postal code."""

    state: Optional[str] = None
    """
    State, county, province, or region
    ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class ShippingDetails(BaseModel):
    """The customer's shipping information associated with this payment."""

    address: ShippingDetailsAddress
    """A representation of a physical address."""

    name: Optional[str] = None
    """The shipping recipient's name."""

    phone: Optional[str] = None
    """The shipping recipient's phone number."""


class PaymentRecord(BaseModel):
    """
    A Payment Record is a resource that allows you to represent payments that occur on- or off-Stripe.
    For example, you can create a Payment Record to model a payment made on a different payment processor,
    in order to mark an Invoice as paid and a Subscription as active. Payment Records consist of one or
    more Payment Attempt Records, which represent individual attempts made on a payment network.
    """

    id: str
    """Unique identifier for the object."""

    amount: PaymentsPrimitivesPaymentRecordsResourceAmount
    """A representation of an amount of money, consisting of an amount and a currency."""

    amount_authorized: PaymentsPrimitivesPaymentRecordsResourceAmount
    """A representation of an amount of money, consisting of an amount and a currency."""

    amount_canceled: PaymentsPrimitivesPaymentRecordsResourceAmount
    """A representation of an amount of money, consisting of an amount and a currency."""

    amount_failed: PaymentsPrimitivesPaymentRecordsResourceAmount
    """A representation of an amount of money, consisting of an amount and a currency."""

    amount_guaranteed: PaymentsPrimitivesPaymentRecordsResourceAmount
    """A representation of an amount of money, consisting of an amount and a currency."""

    amount_refunded: PaymentsPrimitivesPaymentRecordsResourceAmount
    """A representation of an amount of money, consisting of an amount and a currency."""

    amount_requested: PaymentsPrimitivesPaymentRecordsResourceAmount
    """A representation of an amount of money, consisting of an amount and a currency."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

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

    object: Literal["payment_record"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    processor_details: ProcessorDetails
    """Processor information associated with this payment."""

    reported_by: Literal["self", "stripe"]
    """Indicates who reported the payment."""

    application: Optional[str] = None
    """ID of the Connect application that created the PaymentRecord."""

    customer_details: Optional[CustomerDetails] = None
    """Information about the customer for this payment."""

    customer_presence: Optional[Literal["off_session", "on_session"]] = None
    """
    Indicates whether the customer was present in your checkout flow during this
    payment.
    """

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    latest_payment_attempt_record: Optional[str] = None
    """ID of the latest Payment Attempt Record attached to this Payment Record."""

    payment_method_details: Optional["PaymentsPrimitivesPaymentRecordsResourcePaymentMethodDetails"] = None
    """Details about the Payment Method used in this payment attempt."""

    shipping_details: Optional[ShippingDetails] = None
    """The customer's shipping information associated with this payment."""


from .payments_primitives_payment_records_resource_payment_method_details import (
    PaymentsPrimitivesPaymentRecordsResourcePaymentMethodDetails,
)
