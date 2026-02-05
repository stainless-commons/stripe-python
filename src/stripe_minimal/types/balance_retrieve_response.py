# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .balance_amount import BalanceAmount
from .balance_amount_by_source_type import BalanceAmountBySourceType

__all__ = [
    "BalanceRetrieveResponse",
    "InstantAvailable",
    "InstantAvailableNetAvailable",
    "Issuing",
    "RefundAndDisputePrefunding",
]


class InstantAvailableNetAvailable(BaseModel):
    amount: int
    """Net balance amount, subtracting fees from platform-set pricing."""

    destination: str
    """ID of the external account for this net balance (not expandable)."""

    source_types: Optional[BalanceAmountBySourceType] = None


class InstantAvailable(BaseModel):
    amount: int
    """Balance amount."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    net_available: Optional[List[InstantAvailableNetAvailable]] = None
    """Breakdown of balance by destination."""

    source_types: Optional[BalanceAmountBySourceType] = None


class Issuing(BaseModel):
    available: List[BalanceAmount]
    """Funds that are available for use."""


class RefundAndDisputePrefunding(BaseModel):
    available: List[BalanceAmount]
    """Funds that are available for use."""

    pending: List[BalanceAmount]
    """Funds that are pending"""


class BalanceRetrieveResponse(BaseModel):
    """This is an object representing your Stripe balance.

    You can retrieve it to see
    the balance currently on your Stripe account.

    The top-level `available` and `pending` comprise your "payments balance."

    Related guide: [Balances and settlement time](https://docs.stripe.com/payments/balances), [Understanding Connect account balances](https://docs.stripe.com/connect/account-balances)
    """

    available: List[BalanceAmount]
    """
    Available funds that you can transfer or pay out automatically by Stripe or
    explicitly through the [Transfers API](https://api.stripe.com#transfers) or
    [Payouts API](https://api.stripe.com#payouts). You can find the available
    balance for each currency and payment type in the `source_types` property.
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["balance"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    pending: List[BalanceAmount]
    """Funds that aren't available in the balance yet.

    You can find the pending balance for each currency and each payment type in the
    `source_types` property.
    """

    connect_reserved: Optional[List[BalanceAmount]] = None
    """
    Funds held due to negative balances on connected accounts where
    [account.controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `application`, which includes Custom accounts. You can find the connect
    reserve balance for each currency and payment type in the `source_types`
    property.
    """

    instant_available: Optional[List[InstantAvailable]] = None
    """Funds that you can pay out using Instant Payouts."""

    issuing: Optional[Issuing] = None

    refund_and_dispute_prefunding: Optional[RefundAndDisputePrefunding] = None
