# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.deleted_customer import DeletedCustomer

__all__ = ["Card", "Account", "Customer", "Networks"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Account = TypeAliasType("Account", Union[str, "account.Account", None])
else:
    Account: TypeAlias = Union[str, "account.Account", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer, None])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer, None]


class Networks(BaseModel):
    preferred: Optional[str] = None
    """The preferred network for co-branded cards.

    Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if
    requested network is not valid for the card.
    """


class Card(BaseModel):
    """You can store multiple cards on a customer in order to charge the customer
    later.

    You can also store multiple debit cards on a recipient in order to
    transfer to those cards later.

    Related guide: [Card payments with Sources](https://docs.stripe.com/sources/cards)
    """

    id: str
    """Unique identifier for the object."""

    brand: str
    """Card brand.

    Can be `American Express`, `Cartes Bancaires`, `Diners Club`, `Discover`,
    `Eftpos Australia`, `Girocard`, `JCB`, `MasterCard`, `UnionPay`, `Visa`, or
    `Unknown`.
    """

    exp_month: int
    """Two-digit number representing the card's expiration month."""

    exp_year: int
    """Four-digit number representing the card's expiration year."""

    funding: str
    """Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`."""

    last4: str
    """The last four digits of the card."""

    object: Literal["card"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    account: Optional[Account] = None
    """This is an object representing a Stripe account.

    You can retrieve it to see properties on the account like its current
    requirements or if the account is enabled to make live charges or receive
    payouts.

    For accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `application`, which includes Custom accounts, the properties below are
    always returned.

    For accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`, which includes Standard and Express accounts, some properties are
    only returned until you create an [Account Link](/api/account_links) or
    [Account Session](/api/account_sessions) to start Connect Onboarding. Learn
    about the [differences between accounts](/connect/accounts).
    """

    address_city: Optional[str] = None
    """City/District/Suburb/Town/Village."""

    address_country: Optional[str] = None
    """Billing address country, if provided when creating card."""

    address_line1: Optional[str] = None
    """Address line 1 (Street address/PO Box/Company name)."""

    address_line1_check: Optional[str] = None
    """
    If `address_line1` was provided, results of the check: `pass`, `fail`,
    `unavailable`, or `unchecked`.
    """

    address_line2: Optional[str] = None
    """Address line 2 (Apartment/Suite/Unit/Building)."""

    address_state: Optional[str] = None
    """State/County/Province/Region."""

    address_zip: Optional[str] = None
    """ZIP or postal code."""

    address_zip_check: Optional[str] = None
    """
    If `address_zip` was provided, results of the check: `pass`, `fail`,
    `unavailable`, or `unchecked`.
    """

    allow_redisplay: Optional[Literal["always", "limited", "unspecified"]] = None
    """
    This field indicates whether this payment method can be shown again to its
    customer in a checkout flow. Stripe products such as Checkout and Elements use
    this field to determine whether a payment method can be shown as a saved payment
    method in a checkout flow. The field defaults to “unspecified”.
    """

    available_payout_methods: Optional[List[Literal["instant", "standard"]]] = None
    """A set of available payout methods for this card.

    Only values from this set should be passed as the `method` when creating a
    payout.
    """

    country: Optional[str] = None
    """Two-letter ISO code representing the country of the card.

    You could use this attribute to get a sense of the international breakdown of
    cards you've collected.
    """

    currency: Optional[str] = None
    """
    Three-letter
    [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in
    lowercase. Must be a [supported currency](https://docs.stripe.com/currencies).
    Only applicable on accounts (not customers or recipients). The card can be used
    as a transfer destination for funds in this currency. This property is only
    available when returned as an
    [External Account](/api/external_account_cards/object) where
    [controller.is_controller](/api/accounts/object#account_object-controller-is_controller)
    is `true`.
    """

    customer: Optional[Customer] = None
    """The customer that this card belongs to.

    This attribute will not be in the card object if the card belongs to an account
    or recipient instead.
    """

    cvc_check: Optional[str] = None
    """
    If a CVC was provided, results of the check: `pass`, `fail`, `unavailable`, or
    `unchecked`. A result of unchecked indicates that CVC was provided but hasn't
    been checked yet. Checks are typically performed when attaching a card to a
    Customer object, or when creating a charge. For more details, see
    [Check if a card is valid without a charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge).
    """

    default_for_currency: Optional[bool] = None
    """Whether this card is the default external account for its currency.

    This property is only available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `application`, which includes Custom accounts.
    """

    dynamic_last4: Optional[str] = None
    """
    (For tokenized numbers only.) The last four digits of the device account number.
    """

    fingerprint: Optional[str] = None
    """Uniquely identifies this particular card number.

    You can use this attribute to check whether two customers who’ve signed up with
    you are using the same card number, for example. For payment methods that
    tokenize card information (Apple Pay, Google Pay), the tokenized number might be
    provided instead of the underlying card number.

    _As of May 1, 2021, card fingerprint in India for Connect changed to allow two
    fingerprints for the same card---one for India and one for the rest of the
    world._
    """

    iin: Optional[str] = None
    """Issuer identification number of the card."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    name: Optional[str] = None
    """Cardholder name."""

    networks: Optional[Networks] = None

    regulated_status: Optional[Literal["regulated", "unregulated"]] = None
    """Status of a card based on the card issuer."""

    status: Optional[str] = None
    """For external accounts that are cards, possible values are `new` and `errored`.

    If a payout fails, the status is set to `errored` and
    [scheduled payouts](https://stripe.com/docs/payouts#payout-schedule) are stopped
    until account details are updated.
    """

    tokenization_method: Optional[str] = None
    """If the card number is tokenized, this is the method that was used.

    Can be `android_pay` (includes Google Pay), `apple_pay`, `masterpass`,
    `visa_checkout`, or null.
    """


from . import account, customer
