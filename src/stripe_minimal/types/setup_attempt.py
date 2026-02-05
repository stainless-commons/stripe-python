# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import application
from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.deleted_customer import DeletedCustomer

__all__ = ["SetupAttempt", "PaymentMethod", "SetupIntent", "Application", "Customer", "OnBehalfOf"]

if TYPE_CHECKING or not PYDANTIC_V1:
    PaymentMethod = TypeAliasType("PaymentMethod", Union[str, "payment_method.PaymentMethod"])
else:
    PaymentMethod: TypeAlias = Union[str, "payment_method.PaymentMethod"]

if TYPE_CHECKING or not PYDANTIC_V1:
    SetupIntent = TypeAliasType("SetupIntent", Union[str, "setup_intent.SetupIntent"])
else:
    SetupIntent: TypeAlias = Union[str, "setup_intent.SetupIntent"]

Application: TypeAlias = Union[str, application.Application, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer, None])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    OnBehalfOf = TypeAliasType("OnBehalfOf", Union[str, "Account", None])
else:
    OnBehalfOf: TypeAlias = Union[str, "Account", None]


class SetupAttempt(BaseModel):
    """
    A SetupAttempt describes one attempted confirmation of a SetupIntent,
    whether that confirmation is successful or unsuccessful. You can use
    SetupAttempts to inspect details of a specific attempt at setting up a
    payment method using a SetupIntent.
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

    object: Literal["setup_attempt"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    payment_method: PaymentMethod
    """ID of the payment method used with this SetupAttempt."""

    payment_method_details: "SetupAttemptPaymentMethodDetails"

    setup_intent: SetupIntent
    """ID of the SetupIntent that this attempt belongs to."""

    status: str
    """
    Status of this SetupAttempt, one of `requires_confirmation`, `requires_action`,
    `processing`, `succeeded`, `failed`, or `abandoned`.
    """

    usage: str
    """
    The value of
    [usage](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-usage)
    on the SetupIntent at the time of this confirmation, one of `off_session` or
    `on_session`.
    """

    application: Optional[Application] = None
    """
    The value of
    [application](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-application)
    on the SetupIntent at the time of this confirmation.
    """

    attach_to_self: Optional[bool] = None
    """
    If present, the SetupIntent's payment method will be attached to the in-context
    Stripe Account.

    It can only be used for this Stripe Account’s own money movement flows like
    InboundTransfer and OutboundTransfers. It cannot be set to true when setting up
    a PaymentMethod for a Customer, and defaults to false when attaching a
    PaymentMethod to a Customer.
    """

    customer: Optional[Customer] = None
    """
    The value of
    [customer](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-customer)
    on the SetupIntent at the time of this confirmation.
    """

    customer_account: Optional[str] = None
    """
    The value of
    [customer_account](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-customer_account)
    on the SetupIntent at the time of this confirmation.
    """

    flow_directions: Optional[List[Literal["inbound", "outbound"]]] = None
    """
    Indicates the directions of money movement for which this payment method is
    intended to be used.

    Include `inbound` if you intend to use the payment method as the origin to pull
    funds from. Include `outbound` if you intend to use the payment method as the
    destination to send funds to. You can include both if you intend to use the
    payment method for both purposes.
    """

    on_behalf_of: Optional[OnBehalfOf] = None
    """
    The value of
    [on_behalf_of](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-on_behalf_of)
    on the SetupIntent at the time of this confirmation.
    """

    setup_error: Optional["APIErrors"] = None


from . import customer, setup_intent, payment_method
from .account import Account
from .api_errors import APIErrors
from .setup_attempt_payment_method_details import SetupAttemptPaymentMethodDetails
