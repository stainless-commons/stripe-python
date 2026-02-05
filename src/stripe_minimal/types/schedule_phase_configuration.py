# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .tax_rate import TaxRate
from .subscription_billing_thresholds import SubscriptionBillingThresholds

__all__ = ["SchedulePhaseConfiguration", "DefaultPaymentMethod", "OnBehalfOf"]

if TYPE_CHECKING or not PYDANTIC_V1:
    DefaultPaymentMethod = TypeAliasType("DefaultPaymentMethod", Union[str, "PaymentMethod", None])
else:
    DefaultPaymentMethod: TypeAlias = Union[str, "PaymentMethod", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    OnBehalfOf = TypeAliasType("OnBehalfOf", Union[str, "Account", None])
else:
    OnBehalfOf: TypeAlias = Union[str, "Account", None]


class SchedulePhaseConfiguration(BaseModel):
    """
    A phase describes the plans, coupon, and trialing status of a subscription for a predefined time period.
    """

    add_invoice_items: List["ScheduleAddInvoiceItem"]
    """
    A list of prices and quantities that will generate invoice items appended to the
    next invoice for this phase.
    """

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    discounts: List["StackableDiscount"]
    """The stackable discounts that will be applied to the subscription on this phase.

    Subscription item discounts are applied before subscription discounts.
    """

    end_date: int
    """The end of this phase of the subscription schedule."""

    items: List["ScheduleConfigurationItem"]
    """
    Subscription items to configure the subscription to during this phase of the
    subscription schedule.
    """

    proration_behavior: Literal["always_invoice", "create_prorations", "none"]
    """When transitioning phases, controls how prorations are handled (if any).

    Possible values are `create_prorations`, `none`, and `always_invoice`.
    """

    start_date: int
    """The start of this phase of the subscription schedule."""

    application_fee_percent: Optional[float] = None
    """A non-negative decimal between 0 and 100, with at most two decimal places.

    This represents the percentage of the subscription invoice total that will be
    transferred to the application owner's Stripe account during this phase of the
    schedule.
    """

    automatic_tax: Optional["PhaseAutomaticTax"] = None

    billing_cycle_anchor: Optional[Literal["automatic", "phase_start"]] = None
    """Possible values are `phase_start` or `automatic`.

    If `phase_start` then billing cycle anchor of the subscription is set to the
    start of the phase when entering the phase. If `automatic` then the billing
    cycle anchor is automatically modified as needed when entering the phase. For
    more information, see the billing cycle
    [documentation](https://docs.stripe.com/billing/subscriptions/billing-cycle).
    """

    billing_thresholds: Optional[SubscriptionBillingThresholds] = None

    collection_method: Optional[Literal["charge_automatically", "send_invoice"]] = None
    """Either `charge_automatically`, or `send_invoice`.

    When charging automatically, Stripe will attempt to pay the underlying
    subscription at the end of each billing cycle using the default source attached
    to the customer. When sending an invoice, Stripe will email your customer an
    invoice with payment instructions and mark the subscription as `active`.
    """

    default_payment_method: Optional[DefaultPaymentMethod] = None
    """ID of the default payment method for the subscription schedule.

    It must belong to the customer associated with the subscription schedule. If not
    set, invoices will use the default payment method in the customer's invoice
    settings.
    """

    default_tax_rates: Optional[List[TaxRate]] = None
    """
    The default tax rates to apply to the subscription during this phase of the
    subscription schedule.
    """

    description: Optional[str] = None
    """Subscription description, meant to be displayable to the customer.

    Use this field to optionally store an explanation of the subscription for
    rendering in Stripe surfaces and certain local payment methods UIs.
    """

    invoice_settings: Optional["SchedulePhaseSetting"] = None

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to a phase. Metadata on a schedule's phase will update the underlying
    subscription's `metadata` when the phase is entered. Updating the underlying
    subscription's `metadata` directly will not affect the current phase's
    `metadata`.
    """

    on_behalf_of: Optional[OnBehalfOf] = None
    """
    The account (if any) the charge was made on behalf of for charges associated
    with the schedule's subscription. See the Connect documentation for details.
    """

    transfer_data: Optional["SubscriptionTransferData"] = None

    trial_end: Optional[int] = None
    """When the trial ends within the phase."""


from .account import Account
from .payment_method import PaymentMethod
from .stackable_discount import StackableDiscount
from .phase_automatic_tax import PhaseAutomaticTax
from .schedule_phase_setting import SchedulePhaseSetting
from .schedule_add_invoice_item import ScheduleAddInvoiceItem
from .subscription_transfer_data import SubscriptionTransferData
from .schedule_configuration_item import ScheduleConfigurationItem
