# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "AccountSettings",
    "Branding",
    "BrandingIcon",
    "BrandingLogo",
    "CardPayments",
    "CardPaymentsDeclineOn",
    "Dashboard",
    "Payments",
    "BacsDebitPayments",
    "CardIssuing",
    "CardIssuingTosAcceptance",
    "Payouts",
    "PayoutsSchedule",
    "SepaDebitPayments",
    "Treasury",
    "TreasuryTosAcceptance",
]

BrandingIcon: TypeAlias = Union[str, "File", None]

BrandingLogo: TypeAlias = Union[str, "File", None]


class Branding(BaseModel):
    icon: Optional[BrandingIcon] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) An icon for
    the account. Must be square and at least 128px x 128px.
    """

    logo: Optional[BrandingLogo] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for
    the account that will be used in Checkout instead of the icon and without the
    account's name next to it if provided. Must be at least 128px x 128px.
    """

    primary_color: Optional[str] = None
    """A CSS hex color value representing the primary branding color for this account"""

    secondary_color: Optional[str] = None
    """
    A CSS hex color value representing the secondary branding color for this account
    """


class CardPaymentsDeclineOn(BaseModel):
    avs_failure: bool
    """
    Whether Stripe automatically declines charges with an incorrect ZIP or postal
    code. This setting only applies when a ZIP or postal code is provided and they
    fail bank verification.
    """

    cvc_failure: bool
    """Whether Stripe automatically declines charges with an incorrect CVC.

    This setting only applies when a CVC is provided and it fails bank verification.
    """


class CardPayments(BaseModel):
    decline_on: Optional[CardPaymentsDeclineOn] = None

    statement_descriptor_prefix: Optional[str] = None
    """The default text that appears on credit card statements when a charge is made.

    This field prefixes any dynamic `statement_descriptor` specified on the charge.
    `statement_descriptor_prefix` is useful for maximizing descriptor space for the
    dynamic portion.
    """

    statement_descriptor_prefix_kana: Optional[str] = None
    """
    The Kana variation of the default text that appears on credit card statements
    when a charge is made (Japan only). This field prefixes any dynamic
    `statement_descriptor_suffix_kana` specified on the charge.
    `statement_descriptor_prefix_kana` is useful for maximizing descriptor space for
    the dynamic portion.
    """

    statement_descriptor_prefix_kanji: Optional[str] = None
    """
    The Kanji variation of the default text that appears on credit card statements
    when a charge is made (Japan only). This field prefixes any dynamic
    `statement_descriptor_suffix_kanji` specified on the charge.
    `statement_descriptor_prefix_kanji` is useful for maximizing descriptor space
    for the dynamic portion.
    """


class Dashboard(BaseModel):
    display_name: Optional[str] = None
    """The display name for this account.

    This is used on the Stripe Dashboard to differentiate between accounts.
    """

    timezone: Optional[str] = None
    """The timezone used in the Stripe Dashboard for this account.

    A list of possible time zone values is maintained at the
    [IANA Time Zone Database](http://www.iana.org/time-zones).
    """


class Payments(BaseModel):
    statement_descriptor: Optional[str] = None
    """The default text that appears on credit card statements when a charge is made.

    This field prefixes any dynamic `statement_descriptor` specified on the charge.
    """

    statement_descriptor_kana: Optional[str] = None
    """The Kana variation of `statement_descriptor` used for charges in Japan.

    Japanese statement descriptors have
    [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors#set-japanese-statement-descriptors).
    """

    statement_descriptor_kanji: Optional[str] = None
    """The Kanji variation of `statement_descriptor` used for charges in Japan.

    Japanese statement descriptors have
    [special requirements](https://docs.stripe.com/get-started/account/statement-descriptors#set-japanese-statement-descriptors).
    """


class BacsDebitPayments(BaseModel):
    display_name: Optional[str] = None
    """The Bacs Direct Debit display name for this account.

    For payments made with Bacs Direct Debit, this name appears on the mandate as
    the statement descriptor. Mobile banking apps display it as the name of the
    business. To use custom branding, set the Bacs Direct Debit Display Name during
    or right after creation. Custom branding incurs an additional monthly fee for
    the platform. The fee appears 5 business days after requesting Bacs. If you
    don't set the display name before requesting Bacs capability, it's automatically
    set as "Stripe" and the account is onboarded to Stripe branding, which is free.
    """

    service_user_number: Optional[str] = None
    """The Bacs Direct Debit Service user number for this account.

    For payments made with Bacs Direct Debit, this number is a unique identifier of
    the account with our banking partners.
    """


class CardIssuingTosAcceptance(BaseModel):
    date: Optional[int] = None
    """
    The Unix timestamp marking when the account representative accepted the service
    agreement.
    """

    ip: Optional[str] = None
    """
    The IP address from which the account representative accepted the service
    agreement.
    """

    user_agent: Optional[str] = None
    """
    The user agent of the browser from which the account representative accepted the
    service agreement.
    """


class CardIssuing(BaseModel):
    tos_acceptance: Optional[CardIssuingTosAcceptance] = None


class PayoutsSchedule(BaseModel):
    delay_days: int
    """The number of days charges for the account will be held before being paid out."""

    interval: str
    """How frequently funds will be paid out.

    One of `manual` (payouts only created via API call), `daily`, `weekly`, or
    `monthly`.
    """

    monthly_anchor: Optional[int] = None
    """The day of the month funds will be paid out.

    Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st
    of the month are sent on the last day of shorter months.
    """

    monthly_payout_days: Optional[List[int]] = None
    """The days of the month funds will be paid out.

    Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st
    of the month are sent on the last day of shorter months.
    """

    weekly_anchor: Optional[str] = None
    """
    The day of the week funds will be paid out, of the style 'monday', 'tuesday',
    etc. Only shown if `interval` is weekly.
    """

    weekly_payout_days: Optional[List[Literal["friday", "monday", "thursday", "tuesday", "wednesday"]]] = None
    """
    The days of the week when available funds are paid out, specified as an array,
    for example, [`monday`, `tuesday`]. Only shown if `interval` is weekly.
    """


class Payouts(BaseModel):
    debit_negative_balances: bool
    """
    A Boolean indicating if Stripe should try to reclaim negative balances from an
    attached bank account. See
    [Understanding Connect account balances](/connect/account-balances) for details.
    The default value is `false` when
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `application`, which includes Custom accounts, otherwise `true`.
    """

    schedule: PayoutsSchedule

    statement_descriptor: Optional[str] = None
    """The text that appears on the bank account statement for payouts.

    If not set, this defaults to the platform's bank descriptor as set in the
    Dashboard.
    """


class SepaDebitPayments(BaseModel):
    creditor_id: Optional[str] = None
    """SEPA creditor identifier that identifies the company making the payment."""


class TreasuryTosAcceptance(BaseModel):
    date: Optional[int] = None
    """
    The Unix timestamp marking when the account representative accepted the service
    agreement.
    """

    ip: Optional[str] = None
    """
    The IP address from which the account representative accepted the service
    agreement.
    """

    user_agent: Optional[str] = None
    """
    The user agent of the browser from which the account representative accepted the
    service agreement.
    """


class Treasury(BaseModel):
    tos_acceptance: Optional[TreasuryTosAcceptance] = None


class AccountSettings(BaseModel):
    branding: Branding

    card_payments: CardPayments

    dashboard: Dashboard

    payments: Payments

    bacs_debit_payments: Optional[BacsDebitPayments] = None

    card_issuing: Optional[CardIssuing] = None

    invoices: Optional["AccountInvoicesSettings"] = None

    payouts: Optional[Payouts] = None

    sepa_debit_payments: Optional[SepaDebitPayments] = None

    treasury: Optional[Treasury] = None


from .file import File
from .account_invoices_settings import AccountInvoicesSettings
