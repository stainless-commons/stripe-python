# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .subscription_billing_thresholds import SubscriptionBillingThresholds

__all__ = ["DefaultSettings", "DefaultPaymentMethod", "OnBehalfOf"]

if TYPE_CHECKING or not PYDANTIC_V1:
    DefaultPaymentMethod = TypeAliasType("DefaultPaymentMethod", Union[str, "PaymentMethod", None])
else:
    DefaultPaymentMethod: TypeAlias = Union[str, "PaymentMethod", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    OnBehalfOf = TypeAliasType("OnBehalfOf", Union[str, "Account", None])
else:
    OnBehalfOf: TypeAlias = Union[str, "Account", None]


class DefaultSettings(BaseModel):
    billing_cycle_anchor: Literal["automatic", "phase_start"]
    """Possible values are `phase_start` or `automatic`.

    If `phase_start` then billing cycle anchor of the subscription is set to the
    start of the phase when entering the phase. If `automatic` then the billing
    cycle anchor is automatically modified as needed when entering the phase. For
    more information, see the billing cycle
    [documentation](https://docs.stripe.com/billing/subscriptions/billing-cycle).
    """

    invoice_settings: "ScheduleSetting"

    application_fee_percent: Optional[float] = None
    """A non-negative decimal between 0 and 100, with at most two decimal places.

    This represents the percentage of the subscription invoice total that will be
    transferred to the application owner's Stripe account during this phase of the
    schedule.
    """

    automatic_tax: Optional["DefaultSettingsAutomaticTax"] = None

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

    If not set, invoices will use the default payment method in the customer's
    invoice settings.
    """

    description: Optional[str] = None
    """Subscription description, meant to be displayable to the customer.

    Use this field to optionally store an explanation of the subscription for
    rendering in Stripe surfaces and certain local payment methods UIs.
    """

    on_behalf_of: Optional[OnBehalfOf] = None
    """
    The account (if any) the charge was made on behalf of for charges associated
    with the schedule's subscription. See the Connect documentation for details.
    """

    transfer_data: Optional["SubscriptionTransferData"] = None


from .account import Account
from .payment_method import PaymentMethod
from .schedule_setting import ScheduleSetting
from .subscription_transfer_data import SubscriptionTransferData
from .default_settings_automatic_tax import DefaultSettingsAutomaticTax
