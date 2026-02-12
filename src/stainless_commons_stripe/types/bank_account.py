# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.deleted_customer import DeletedCustomer
from .shared.account_requirements_error import AccountRequirementsError

__all__ = ["BankAccount", "Account", "Customer", "FutureRequirements", "Requirements"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Account = TypeAliasType("Account", Union[str, "account.Account", None])
else:
    Account: TypeAlias = Union[str, "account.Account", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer, None])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer, None]


class FutureRequirements(BaseModel):
    currently_due: Optional[List[str]] = None
    """Fields that need to be resolved to keep the external account enabled.

    If not resolved by `current_deadline`, these fields will appear in `past_due` as
    well, and the account is disabled.
    """

    errors: Optional[List[AccountRequirementsError]] = None
    """
    Details about validation and verification failures for `due` requirements that
    must be resolved.
    """

    past_due: Optional[List[str]] = None
    """Fields that haven't been resolved by `current_deadline`.

    These fields need to be resolved to enable the external account.
    """

    pending_verification: Optional[List[str]] = None
    """
    Fields that are being reviewed, or might become required depending on the
    results of a review. If the review fails, these fields can move to
    `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might
    appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in
    `pending_verification` if one verification fails but another is still pending.
    """


class Requirements(BaseModel):
    currently_due: Optional[List[str]] = None
    """Fields that need to be resolved to keep the external account enabled.

    If not resolved by `current_deadline`, these fields will appear in `past_due` as
    well, and the account is disabled.
    """

    errors: Optional[List[AccountRequirementsError]] = None
    """
    Details about validation and verification failures for `due` requirements that
    must be resolved.
    """

    past_due: Optional[List[str]] = None
    """Fields that haven't been resolved by `current_deadline`.

    These fields need to be resolved to enable the external account.
    """

    pending_verification: Optional[List[str]] = None
    """
    Fields that are being reviewed, or might become required depending on the
    results of a review. If the review fails, these fields can move to
    `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might
    appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in
    `pending_verification` if one verification fails but another is still pending.
    """


class BankAccount(BaseModel):
    """These bank accounts are payment methods on `Customer` objects.

    On the other hand [External Accounts](/api#external_accounts) are transfer
    destinations on `Account` objects for connected accounts.
    They can be bank accounts or debit cards as well, and are documented in the links above.

    Related guide: [Bank debits and transfers](/payments/bank-debits-transfers)
    """

    id: str
    """Unique identifier for the object."""

    country: str
    """Two-letter ISO code representing the country the bank account is located in."""

    currency: str
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid
    out to the bank account.
    """

    last4: str
    """The last four digits of the bank account number."""

    object: Literal["bank_account"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    status: str
    """
    For bank accounts, possible values are `new`, `validated`, `verified`,
    `verification_failed`, `tokenized_account_number_deactivated` or `errored`. A
    bank account that hasn't had any activity or validation performed is `new`. If
    Stripe can determine that the bank account exists, its status will be
    `validated`. Note that there often isn’t enough information to know (e.g., for
    smaller credit unions), and the validation is not always run. If customer bank
    account verification has succeeded, the bank account status will be `verified`.
    If the verification failed for any reason, such as microdeposit failure, the
    status will be `verification_failed`. If the status is
    `tokenized_account_number_deactivated`, the account utilizes a tokenized account
    number which has been deactivated due to expiration or revocation. This account
    will need to be reverified to continue using it for money movement. If a payout
    sent to this bank account fails, we'll set the status to `errored` and will not
    continue to send
    [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) until the
    bank details are updated.

    For external accounts, possible values are `new`, `errored`,
    `verification_failed`, and `tokenized_account_number_deactivated`. If a payout
    fails, the status is set to `errored` and scheduled payouts are stopped until
    account details are updated. In the US and India, if we can't
    [verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification),
    we'll set the status to `verification_failed`. Other validations aren't run
    against external accounts because they're only used for payouts. This means the
    other statuses don't apply.
    """

    account: Optional[Account] = None
    """The account this bank account belongs to.

    Only applicable on Accounts (not customers or recipients) This property is only
    available when returned as an
    [External Account](/api/external_account_bank_accounts/object) where
    [controller.is_controller](/api/accounts/object#account_object-controller-is_controller)
    is `true`.
    """

    account_holder_name: Optional[str] = None
    """The name of the person or business that owns the bank account."""

    account_holder_type: Optional[str] = None
    """The type of entity that holds the account.

    This can be either `individual` or `company`.
    """

    account_type: Optional[str] = None
    """The bank account type.

    This can only be `checking` or `savings` in most countries. In Japan, this can
    only be `futsu` or `toza`.
    """

    available_payout_methods: Optional[List[Literal["instant", "standard"]]] = None
    """A set of available payout methods for this bank account.

    Only values from this set should be passed as the `method` when creating a
    payout.
    """

    bank_name: Optional[str] = None
    """Name of the bank associated with the routing number (e.g., `WELLS FARGO`)."""

    customer: Optional[Customer] = None
    """The ID of the customer that the bank account is associated with."""

    default_for_currency: Optional[bool] = None
    """Whether this bank account is the default external account for its currency."""

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular bank account.

    You can use this attribute to check whether two bank accounts are the same.
    """

    future_requirements: Optional[FutureRequirements] = None

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    requirements: Optional[Requirements] = None

    routing_number: Optional[str] = None
    """The routing transit number for the bank account."""


from . import account, customer
