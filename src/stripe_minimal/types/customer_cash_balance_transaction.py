# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "CustomerCashBalanceTransaction",
    "Customer",
    "Funded",
    "FundedBankTransfer",
    "FundedBankTransferEuBankTransfer",
    "FundedBankTransferGBBankTransfer",
    "FundedBankTransferJpBankTransfer",
    "FundedBankTransferUsBankTransfer",
]

if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer"])
else:
    Customer: TypeAlias = Union[str, "customer.Customer"]


class FundedBankTransferEuBankTransfer(BaseModel):
    bic: Optional[str] = None
    """The BIC of the bank of the sender of the funding."""

    iban_last4: Optional[str] = None
    """The last 4 digits of the IBAN of the sender of the funding."""

    sender_name: Optional[str] = None
    """The full name of the sender, as supplied by the sending bank."""


class FundedBankTransferGBBankTransfer(BaseModel):
    account_number_last4: Optional[str] = None
    """The last 4 digits of the account number of the sender of the funding."""

    sender_name: Optional[str] = None
    """The full name of the sender, as supplied by the sending bank."""

    sort_code: Optional[str] = None
    """The sort code of the bank of the sender of the funding"""


class FundedBankTransferJpBankTransfer(BaseModel):
    sender_bank: Optional[str] = None
    """The name of the bank of the sender of the funding."""

    sender_branch: Optional[str] = None
    """The name of the bank branch of the sender of the funding."""

    sender_name: Optional[str] = None
    """The full name of the sender, as supplied by the sending bank."""


class FundedBankTransferUsBankTransfer(BaseModel):
    network: Optional[Literal["ach", "domestic_wire_us", "swift"]] = None
    """The banking network used for this funding."""

    sender_name: Optional[str] = None
    """The full name of the sender, as supplied by the sending bank."""


class FundedBankTransfer(BaseModel):
    type: Literal["eu_bank_transfer", "gb_bank_transfer", "jp_bank_transfer", "mx_bank_transfer", "us_bank_transfer"]
    """The funding method type used to fund the customer balance.

    Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`,
    `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
    """

    eu_bank_transfer: Optional[FundedBankTransferEuBankTransfer] = None

    gb_bank_transfer: Optional[FundedBankTransferGBBankTransfer] = None

    jp_bank_transfer: Optional[FundedBankTransferJpBankTransfer] = None

    reference: Optional[str] = None
    """The user-supplied reference field on the bank transfer."""

    us_bank_transfer: Optional[FundedBankTransferUsBankTransfer] = None


class Funded(BaseModel):
    bank_transfer: FundedBankTransfer


class CustomerCashBalanceTransaction(BaseModel):
    """
    Customers with certain payments enabled have a cash balance, representing funds that were paid
    by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions
    represent when funds are moved into or out of this balance. This includes funding by the customer, allocation
    to payments, and refunds to the customer.
    """

    id: str
    """Unique identifier for the object."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: Customer
    """
    The customer whose available cash balance changed as a result of this
    transaction.
    """

    ending_balance: int
    """
    The total available cash balance for the specified currency after this
    transaction was applied. Represented in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    net_amount: int
    """
    The amount by which the cash balance changed, represented in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). A
    positive value represents funds being added to the cash balance, a negative
    value represents funds being removed from the cash balance.
    """

    object: Literal["customer_cash_balance_transaction"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    type: Literal[
        "adjusted_for_overdraft",
        "applied_to_payment",
        "funded",
        "funding_reversed",
        "refunded_from_payment",
        "return_canceled",
        "return_initiated",
        "transferred_to_balance",
        "unapplied_from_payment",
    ]
    """The type of the cash balance transaction.

    New types may be added in future. See
    [Customer Balance](https://docs.stripe.com/payments/customer-balance#types) to
    learn more about these types.
    """

    adjusted_for_overdraft: Optional["CustomerBalanceResourceCashBalanceTransactionAdjustedForOverdraft"] = None

    applied_to_payment: Optional["CustomerBalanceResourceCashBalanceTransactionAppliedToPayment"] = None

    customer_account: Optional[str] = None
    """
    The ID of an Account representing a customer whose available cash balance
    changed as a result of this transaction.
    """

    funded: Optional[Funded] = None

    refunded_from_payment: Optional["CustomerBalanceResourceCashBalanceTransactionRefundedFromPayment"] = None

    transferred_to_balance: Optional["CustomerBalanceResourceCashBalanceTransactionTransferredToBalance"] = None

    unapplied_from_payment: Optional["CustomerBalanceResourceCashBalanceTransactionUnappliedFromPayment"] = None


from . import customer
from .customer_balance_resource_cash_balance_transaction_applied_to_payment import (
    CustomerBalanceResourceCashBalanceTransactionAppliedToPayment,
)
from .customer_balance_resource_cash_balance_transaction_refunded_from_payment import (
    CustomerBalanceResourceCashBalanceTransactionRefundedFromPayment,
)
from .customer_balance_resource_cash_balance_transaction_adjusted_for_overdraft import (
    CustomerBalanceResourceCashBalanceTransactionAdjustedForOverdraft,
)
from .customer_balance_resource_cash_balance_transaction_transferred_to_balance import (
    CustomerBalanceResourceCashBalanceTransactionTransferredToBalance,
)
from .customer_balance_resource_cash_balance_transaction_unapplied_from_payment import (
    CustomerBalanceResourceCashBalanceTransactionUnappliedFromPayment,
)
