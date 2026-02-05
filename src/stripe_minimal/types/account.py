# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.address import Address
from .legal_entity_japan_address import LegalEntityJapanAddress
from .account_requirements_alternative import AccountRequirementsAlternative
from .shared.account_requirements_error import AccountRequirementsError

__all__ = [
    "Account",
    "BusinessProfile",
    "BusinessProfileAnnualRevenue",
    "BusinessProfileMonthlyEstimatedRevenue",
    "Capabilities",
    "Company",
    "CompanyDirectorshipDeclaration",
    "CompanyOwnershipDeclaration",
    "CompanyRegistrationDate",
    "CompanyRepresentativeDeclaration",
    "CompanyVerification",
    "CompanyVerificationDocument",
    "CompanyVerificationDocumentBack",
    "CompanyVerificationDocumentFront",
    "Controller",
    "ControllerFees",
    "ControllerLosses",
    "ControllerStripeDashboard",
    "ExternalAccounts",
    "ExternalAccountsData",
    "FutureRequirements",
    "Groups",
    "Individual",
    "IndividualAdditionalTosAcceptances",
    "IndividualAdditionalTosAcceptancesAccount",
    "IndividualDob",
    "IndividualFutureRequirements",
    "IndividualRelationship",
    "IndividualRequirements",
    "IndividualUsCfpbData",
    "IndividualUsCfpbDataEthnicityDetails",
    "IndividualUsCfpbDataRaceDetails",
    "IndividualVerification",
    "IndividualVerificationAdditionalDocument",
    "IndividualVerificationAdditionalDocumentBack",
    "IndividualVerificationAdditionalDocumentFront",
    "IndividualVerificationDocument",
    "IndividualVerificationDocumentBack",
    "IndividualVerificationDocumentFront",
    "Requirements",
    "TosAcceptance",
]


class BusinessProfileAnnualRevenue(BaseModel):
    amount: Optional[int] = None
    """
    A non-negative integer representing the amount in the
    [smallest currency unit](/currencies#zero-decimal).
    """

    currency: Optional[str] = None
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    fiscal_year_end: Optional[str] = None
    """The close-out date of the preceding fiscal year in ISO 8601 format.

    E.g. 2023-12-31 for the 31st of December, 2023.
    """


class BusinessProfileMonthlyEstimatedRevenue(BaseModel):
    amount: int
    """
    A non-negative integer representing how much to charge in the
    [smallest currency unit](/currencies#zero-decimal).
    """

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """


class BusinessProfile(BaseModel):
    annual_revenue: Optional[BusinessProfileAnnualRevenue] = None

    estimated_worker_count: Optional[int] = None
    """An estimated upper bound of employees, contractors, vendors, etc.

    currently working for the business.
    """

    mcc: Optional[str] = None
    """[The merchant category code for the account](/connect/setting-mcc).

    MCCs are used to classify businesses based on the goods or services they
    provide.
    """

    minority_owned_business_designation: Optional[
        List[
            Literal[
                "lgbtqi_owned_business",
                "minority_owned_business",
                "none_of_these_apply",
                "prefer_not_to_answer",
                "women_owned_business",
            ]
        ]
    ] = None
    """
    Whether the business is a minority-owned, women-owned, and/or LGBTQI+ -owned
    business.
    """

    monthly_estimated_revenue: Optional[BusinessProfileMonthlyEstimatedRevenue] = None

    name: Optional[str] = None
    """The customer-facing business name."""

    product_description: Optional[str] = None
    """
    Internal-only description of the product sold or service provided by the
    business. It's used by Stripe for risk and underwriting purposes.
    """

    support_address: Optional[Address] = None

    support_email: Optional[str] = None
    """A publicly available email address for sending support issues to."""

    support_phone: Optional[str] = None
    """A publicly available phone number to call with support issues."""

    support_url: Optional[str] = None
    """A publicly available website for handling support issues."""

    url: Optional[str] = None
    """The business's publicly available website."""


class Capabilities(BaseModel):
    acss_debit_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Canadian pre-authorized debits payments capability of the
    account, or whether the account can directly process Canadian pre-authorized
    debits charges.
    """

    affirm_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Affirm capability of the account, or whether the account can
    directly process Affirm charges.
    """

    afterpay_clearpay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Afterpay Clearpay capability of the account, or whether the
    account can directly process Afterpay Clearpay charges.
    """

    alma_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Alma capability of the account, or whether the account can
    directly process Alma payments.
    """

    amazon_pay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the AmazonPay capability of the account, or whether the account
    can directly process AmazonPay payments.
    """

    au_becs_debit_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the BECS Direct Debit (AU) payments capability of the account, or
    whether the account can directly process BECS Direct Debit (AU) charges.
    """

    bacs_debit_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Bacs Direct Debits payments capability of the account, or
    whether the account can directly process Bacs Direct Debits charges.
    """

    bancontact_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Bancontact payments capability of the account, or whether the
    account can directly process Bancontact charges.
    """

    bank_transfer_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the customer_balance payments capability of the account, or
    whether the account can directly process customer_balance charges.
    """

    billie_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Billie capability of the account, or whether the account can
    directly process Billie payments.
    """

    blik_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the blik payments capability of the account, or whether the
    account can directly process blik charges.
    """

    boleto_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the boleto payments capability of the account, or whether the
    account can directly process boleto charges.
    """

    card_issuing: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the card issuing capability of the account, or whether you can use
    Issuing to distribute funds on cards
    """

    card_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the card payments capability of the account, or whether the
    account can directly process credit and debit card charges.
    """

    cartes_bancaires_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Cartes Bancaires payments capability of the account, or
    whether the account can directly process Cartes Bancaires card charges in EUR
    currency.
    """

    cashapp_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Cash App Pay capability of the account, or whether the account
    can directly process Cash App Pay payments.
    """

    crypto_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Crypto capability of the account, or whether the account can
    directly process Crypto payments.
    """

    eps_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the EPS payments capability of the account, or whether the account
    can directly process EPS charges.
    """

    fpx_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the FPX payments capability of the account, or whether the account
    can directly process FPX charges.
    """

    gb_bank_transfer_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the GB customer_balance payments (GBP currency) capability of the
    account, or whether the account can directly process GB customer_balance
    charges.
    """

    giropay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the giropay payments capability of the account, or whether the
    account can directly process giropay charges.
    """

    grabpay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the GrabPay payments capability of the account, or whether the
    account can directly process GrabPay charges.
    """

    ideal_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the iDEAL payments capability of the account, or whether the
    account can directly process iDEAL charges.
    """

    india_international_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the india_international_payments capability of the account, or
    whether the account can process international charges (non INR) in India.
    """

    jcb_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the JCB payments capability of the account, or whether the account
    (Japan only) can directly process JCB credit card charges in JPY currency.
    """

    jp_bank_transfer_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Japanese customer_balance payments (JPY currency) capability
    of the account, or whether the account can directly process Japanese
    customer_balance charges.
    """

    kakao_pay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the KakaoPay capability of the account, or whether the account can
    directly process KakaoPay payments.
    """

    klarna_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Klarna payments capability of the account, or whether the
    account can directly process Klarna charges.
    """

    konbini_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the konbini payments capability of the account, or whether the
    account can directly process konbini charges.
    """

    kr_card_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the KrCard capability of the account, or whether the account can
    directly process KrCard payments.
    """

    legacy_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """The status of the legacy payments capability of the account."""

    link_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the link_payments capability of the account, or whether the
    account can directly process Link charges.
    """

    mb_way_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the MB WAY payments capability of the account, or whether the
    account can directly process MB WAY charges.
    """

    mobilepay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the MobilePay capability of the account, or whether the account
    can directly process MobilePay charges.
    """

    multibanco_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Multibanco payments capability of the account, or whether the
    account can directly process Multibanco charges.
    """

    mx_bank_transfer_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Mexican customer_balance payments (MXN currency) capability of
    the account, or whether the account can directly process Mexican
    customer_balance charges.
    """

    naver_pay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the NaverPay capability of the account, or whether the account can
    directly process NaverPay payments.
    """

    nz_bank_account_becs_debit_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the New Zealand BECS Direct Debit payments capability of the
    account, or whether the account can directly process New Zealand BECS Direct
    Debit charges.
    """

    oxxo_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the OXXO payments capability of the account, or whether the
    account can directly process OXXO charges.
    """

    p24_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the P24 payments capability of the account, or whether the account
    can directly process P24 charges.
    """

    pay_by_bank_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the pay_by_bank payments capability of the account, or whether the
    account can directly process pay_by_bank charges.
    """

    payco_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Payco capability of the account, or whether the account can
    directly process Payco payments.
    """

    paynow_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the paynow payments capability of the account, or whether the
    account can directly process paynow charges.
    """

    payto_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the PayTo capability of the account, or whether the account can
    directly process PayTo charges.
    """

    pix_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the pix payments capability of the account, or whether the account
    can directly process pix charges.
    """

    promptpay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the promptpay payments capability of the account, or whether the
    account can directly process promptpay charges.
    """

    revolut_pay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the RevolutPay capability of the account, or whether the account
    can directly process RevolutPay payments.
    """

    samsung_pay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the SamsungPay capability of the account, or whether the account
    can directly process SamsungPay payments.
    """

    satispay_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Satispay capability of the account, or whether the account can
    directly process Satispay payments.
    """

    sepa_bank_transfer_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the SEPA customer_balance payments (EUR currency) capability of
    the account, or whether the account can directly process SEPA customer_balance
    charges.
    """

    sepa_debit_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the SEPA Direct Debits payments capability of the account, or
    whether the account can directly process SEPA Direct Debits charges.
    """

    sofort_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Sofort payments capability of the account, or whether the
    account can directly process Sofort charges.
    """

    swish_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Swish capability of the account, or whether the account can
    directly process Swish payments.
    """

    tax_reporting_us_1099_k: Optional[Literal["active", "inactive", "pending"]] = None
    """The status of the tax reporting 1099-K (US) capability of the account."""

    tax_reporting_us_1099_misc: Optional[Literal["active", "inactive", "pending"]] = None
    """The status of the tax reporting 1099-MISC (US) capability of the account."""

    transfers: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the transfers capability of the account, or whether your platform
    can transfer funds to the account.
    """

    treasury: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the banking capability, or whether the account can have bank
    accounts.
    """

    twint_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the TWINT capability of the account, or whether the account can
    directly process TWINT charges.
    """

    us_bank_account_ach_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the US bank account ACH payments capability of the account, or
    whether the account can directly process US bank account charges.
    """

    us_bank_transfer_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the US customer_balance payments (USD currency) capability of the
    account, or whether the account can directly process US customer_balance
    charges.
    """

    zip_payments: Optional[Literal["active", "inactive", "pending"]] = None
    """
    The status of the Zip capability of the account, or whether the account can
    directly process Zip charges.
    """


class CompanyDirectorshipDeclaration(BaseModel):
    date: Optional[int] = None
    """
    The Unix timestamp marking when the directorship declaration attestation was
    made.
    """

    ip: Optional[str] = None
    """The IP address from which the directorship declaration attestation was made."""

    user_agent: Optional[str] = None
    """
    The user-agent string from the browser where the directorship declaration
    attestation was made.
    """


class CompanyOwnershipDeclaration(BaseModel):
    date: Optional[int] = None
    """The Unix timestamp marking when the beneficial owner attestation was made."""

    ip: Optional[str] = None
    """The IP address from which the beneficial owner attestation was made."""

    user_agent: Optional[str] = None
    """
    The user-agent string from the browser where the beneficial owner attestation
    was made.
    """


class CompanyRegistrationDate(BaseModel):
    day: Optional[int] = None
    """The day of registration, between 1 and 31."""

    month: Optional[int] = None
    """The month of registration, between 1 and 12."""

    year: Optional[int] = None
    """The four-digit year of registration."""


class CompanyRepresentativeDeclaration(BaseModel):
    date: Optional[int] = None
    """
    The Unix timestamp marking when the representative declaration attestation was
    made.
    """

    ip: Optional[str] = None
    """The IP address from which the representative declaration attestation was made."""

    user_agent: Optional[str] = None
    """
    The user-agent string from the browser where the representative declaration
    attestation was made.
    """


CompanyVerificationDocumentBack: TypeAlias = Union[str, "File", None]

CompanyVerificationDocumentFront: TypeAlias = Union[str, "File", None]


class CompanyVerificationDocument(BaseModel):
    back: Optional[CompanyVerificationDocumentBack] = None
    """
    The back of a document returned by a
    [file upload](https://api.stripe.com#create_file) with a `purpose` value of
    `additional_verification`. Note that `additional_verification` files are
    [not downloadable](/file-upload#uploading-a-file).
    """

    details: Optional[str] = None
    """A user-displayable string describing the verification state of this document."""

    details_code: Optional[str] = None
    """
    One of `document_corrupt`, `document_expired`, `document_failed_copy`,
    `document_failed_greyscale`, `document_failed_other`,
    `document_failed_test_mode`, `document_fraudulent`, `document_incomplete`,
    `document_invalid`, `document_manipulated`, `document_not_readable`,
    `document_not_uploaded`, `document_type_not_supported`, or `document_too_large`.
    A machine-readable code specifying the verification state for this document.
    """

    front: Optional[CompanyVerificationDocumentFront] = None
    """
    The front of a document returned by a
    [file upload](https://api.stripe.com#create_file) with a `purpose` value of
    `additional_verification`. Note that `additional_verification` files are
    [not downloadable](/file-upload#uploading-a-file).
    """


class CompanyVerification(BaseModel):
    document: CompanyVerificationDocument


class Company(BaseModel):
    address: Optional[Address] = None

    address_kana: Optional[LegalEntityJapanAddress] = None

    address_kanji: Optional[LegalEntityJapanAddress] = None

    directors_provided: Optional[bool] = None
    """Whether the company's directors have been provided.

    This Boolean will be `true` if you've manually indicated that all directors are
    provided via
    [the `directors_provided` parameter](https://docs.stripe.com/api/accounts/update#update_account-company-directors_provided).
    """

    directorship_declaration: Optional[CompanyDirectorshipDeclaration] = None

    executives_provided: Optional[bool] = None
    """Whether the company's executives have been provided.

    This Boolean will be `true` if you've manually indicated that all executives are
    provided via
    [the `executives_provided` parameter](https://docs.stripe.com/api/accounts/update#update_account-company-executives_provided),
    or if Stripe determined that sufficient executives were provided.
    """

    export_license_id: Optional[str] = None
    """
    The export license ID number of the company, also referred as Import Export Code
    (India only).
    """

    export_purpose_code: Optional[str] = None
    """The purpose code to use for export transactions (India only)."""

    name: Optional[str] = None
    """The company's legal name.

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    name_kana: Optional[str] = None
    """The Kana variation of the company's legal name (Japan only).

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    name_kanji: Optional[str] = None
    """The Kanji variation of the company's legal name (Japan only).

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    owners_provided: Optional[bool] = None
    """Whether the company's owners have been provided.

    This Boolean will be `true` if you've manually indicated that all owners are
    provided via
    [the `owners_provided` parameter](https://docs.stripe.com/api/accounts/update#update_account-company-owners_provided),
    or if Stripe determined that sufficient owners were provided. Stripe determines
    ownership requirements using both the number of owners provided and their total
    percent ownership (calculated by adding the `percent_ownership` of each owner
    together).
    """

    ownership_declaration: Optional[CompanyOwnershipDeclaration] = None

    ownership_exemption_reason: Optional[
        Literal["qualified_entity_exceeds_ownership_threshold", "qualifies_as_financial_institution"]
    ] = None
    """
    This value is used to determine if a business is exempt from providing ultimate
    beneficial owners. See
    [this support article](https://support.stripe.com/questions/exemption-from-providing-ownership-details)
    and
    [changelog](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api)
    for more details.
    """

    phone: Optional[str] = None
    """The company's phone number (used for verification)."""

    registration_date: Optional[CompanyRegistrationDate] = None

    representative_declaration: Optional[CompanyRepresentativeDeclaration] = None

    structure: Optional[
        Literal[
            "free_zone_establishment",
            "free_zone_llc",
            "government_instrumentality",
            "governmental_unit",
            "incorporated_non_profit",
            "incorporated_partnership",
            "limited_liability_partnership",
            "llc",
            "multi_member_llc",
            "private_company",
            "private_corporation",
            "private_partnership",
            "public_company",
            "public_corporation",
            "public_partnership",
            "registered_charity",
            "single_member_llc",
            "sole_establishment",
            "sole_proprietorship",
            "tax_exempt_government_instrumentality",
            "unincorporated_association",
            "unincorporated_non_profit",
            "unincorporated_partnership",
        ]
    ] = None
    """The category identifying the legal structure of the company or legal entity.

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`. See
    [Business structure](https://docs.stripe.com/connect/identity-verification#business-structure)
    for more details.
    """

    tax_id_provided: Optional[bool] = None
    """Whether the company's business ID number was provided."""

    tax_id_registrar: Optional[str] = None
    """
    The jurisdiction in which the `tax_id` is registered (Germany-based companies
    only).
    """

    vat_id_provided: Optional[bool] = None
    """Whether the company's business VAT number was provided."""

    verification: Optional[CompanyVerification] = None


class ControllerFees(BaseModel):
    payer: Literal["account", "application", "application_custom", "application_express"]
    """
    A value indicating the responsible payer of a bundle of Stripe fees for
    pricing-control eligible products on this account. Learn more about
    [fee behavior on connected accounts](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior).
    """


class ControllerLosses(BaseModel):
    payments: Literal["application", "stripe"]
    """
    A value indicating who is liable when this account can't pay back negative
    balances from payments.
    """


class ControllerStripeDashboard(BaseModel):
    type: Literal["express", "full", "none"]
    """
    A value indicating the Stripe dashboard this account has access to independent
    of the Connect application.
    """


class Controller(BaseModel):
    type: Literal["account", "application"]
    """The controller type.

    Can be `application`, if a Connect application controls the account, or
    `account`, if the account controls itself.
    """

    fees: Optional[ControllerFees] = None

    is_controller: Optional[bool] = None
    """
    `true` if the Connect application retrieving the resource controls the account
    and can therefore exercise
    [platform controls](https://docs.stripe.com/connect/platform-controls-for-standard-accounts).
    Otherwise, this field is null.
    """

    losses: Optional[ControllerLosses] = None

    requirement_collection: Optional[Literal["application", "stripe"]] = None
    """A value indicating responsibility for collecting requirements on this account.

    Only returned when the Connect application retrieving the resource controls the
    account.
    """

    stripe_dashboard: Optional[ControllerStripeDashboard] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    ExternalAccountsData = TypeAliasType("ExternalAccountsData", Union["BankAccount", "Card"])
else:
    ExternalAccountsData: TypeAlias = Union["BankAccount", "Card"]


class ExternalAccounts(BaseModel):
    """
    External accounts (bank accounts and debit cards) currently attached to this account. External accounts are only returned for requests where `controller[is_controller]` is true.
    """

    data: List[ExternalAccountsData]
    """
    The list contains all external accounts that have been attached to the Stripe
    account. These may be bank accounts or cards.
    """

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


class FutureRequirements(BaseModel):
    alternatives: Optional[List[AccountRequirementsAlternative]] = None
    """
    Fields that are due and can be resolved by providing the corresponding
    alternative fields instead. Many alternatives can list the same
    `original_fields_due`, and any of these alternatives can serve as a pathway for
    attempting to resolve the fields again. Re-providing `original_fields_due` also
    serves as a pathway for attempting to resolve the fields again.
    """

    current_deadline: Optional[int] = None
    """
    Date on which `future_requirements` becomes the main `requirements` hash and
    `future_requirements` becomes empty. After the transition, `currently_due`
    requirements may immediately become `past_due`, but the account may also be
    given a grace period depending on its enablement state prior to transitioning.
    """

    currently_due: Optional[List[str]] = None
    """Fields that need to be resolved to keep the account enabled.

    If not resolved by `future_requirements[current_deadline]`, these fields will
    transition to the main `requirements` hash.
    """

    disabled_reason: Optional[
        Literal[
            "action_required.requested_capabilities",
            "listed",
            "other",
            "platform_paused",
            "rejected.fraud",
            "rejected.incomplete_verification",
            "rejected.listed",
            "rejected.other",
            "rejected.platform_fraud",
            "rejected.platform_other",
            "rejected.platform_terms_of_service",
            "rejected.terms_of_service",
            "requirements.past_due",
            "requirements.pending_verification",
            "under_review",
        ]
    ] = None
    """This is typed as an enum for consistency with `requirements.disabled_reason`."""

    errors: Optional[List[AccountRequirementsError]] = None
    """
    Details about validation and verification failures for `due` requirements that
    must be resolved.
    """

    eventually_due: Optional[List[str]] = None
    """Fields you must collect when all thresholds are reached.

    As they become required, they appear in `currently_due` as well.
    """

    past_due: Optional[List[str]] = None
    """Fields that haven't been resolved by `requirements.current_deadline`.

    These fields need to be resolved to enable the capability on the account.
    `future_requirements.past_due` is a subset of `requirements.past_due`.
    """

    pending_verification: Optional[List[str]] = None
    """
    Fields that are being reviewed, or might become required depending on the
    results of a review. If the review fails, these fields can move to
    `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might
    appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in
    `pending_verification` if one verification fails but another is still pending.
    """


class Groups(BaseModel):
    payments_pricing: Optional[str] = None
    """
    The group the account is in to determine their payments pricing, and null if the
    account is on customized pricing.
    [See the Platform pricing tool documentation](https://docs.stripe.com/connect/platform-pricing-tools)
    for details.
    """


class IndividualAdditionalTosAcceptancesAccount(BaseModel):
    date: Optional[int] = None
    """
    The Unix timestamp marking when the legal guardian accepted the service
    agreement.
    """

    ip: Optional[str] = None
    """The IP address from which the legal guardian accepted the service agreement."""

    user_agent: Optional[str] = None
    """
    The user agent of the browser from which the legal guardian accepted the service
    agreement.
    """


class IndividualAdditionalTosAcceptances(BaseModel):
    account: Optional[IndividualAdditionalTosAcceptancesAccount] = None


class IndividualDob(BaseModel):
    day: Optional[int] = None
    """The day of birth, between 1 and 31."""

    month: Optional[int] = None
    """The month of birth, between 1 and 12."""

    year: Optional[int] = None
    """The four-digit year of birth."""


class IndividualFutureRequirements(BaseModel):
    currently_due: List[str]
    """Fields that need to be resolved to keep the person's account enabled.

    If not resolved by the account's `future_requirements[current_deadline]`, these
    fields will transition to the main `requirements` hash, and may immediately
    become `past_due`, but the account may also be given a grace period depending on
    the account's enablement state prior to transition.
    """

    errors: List[AccountRequirementsError]
    """
    Details about validation and verification failures for `due` requirements that
    must be resolved.
    """

    eventually_due: List[str]
    """Fields you must collect when all thresholds are reached.

    As they become required, they appear in `currently_due` as well, and the
    account's `future_requirements[current_deadline]` becomes set.
    """

    past_due: List[str]
    """
    Fields that haven't been resolved by the account's
    `requirements.current_deadline`. These fields need to be resolved to enable the
    person's account. `future_requirements.past_due` is a subset of
    `requirements.past_due`.
    """

    pending_verification: List[str]
    """
    Fields that are being reviewed, or might become required depending on the
    results of a review. If the review fails, these fields can move to
    `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might
    appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in
    `pending_verification` if one verification fails but another is still pending.
    """

    alternatives: Optional[List[AccountRequirementsAlternative]] = None
    """
    Fields that are due and can be resolved by providing the corresponding
    alternative fields instead. Many alternatives can list the same
    `original_fields_due`, and any of these alternatives can serve as a pathway for
    attempting to resolve the fields again. Re-providing `original_fields_due` also
    serves as a pathway for attempting to resolve the fields again.
    """


class IndividualRelationship(BaseModel):
    authorizer: Optional[bool] = None
    """Whether the person is the authorizer of the account's representative."""

    director: Optional[bool] = None
    """Whether the person is a director of the account's legal entity.

    Directors are typically members of the governing board of the company, or
    responsible for ensuring the company meets its regulatory obligations.
    """

    executive: Optional[bool] = None
    """
    Whether the person has significant responsibility to control, manage, or direct
    the organization.
    """

    legal_guardian: Optional[bool] = None
    """Whether the person is the legal guardian of the account's representative."""

    owner: Optional[bool] = None
    """Whether the person is an owner of the account’s legal entity."""

    percent_ownership: Optional[float] = None
    """The percent owned by the person of the account's legal entity."""

    representative: Optional[bool] = None
    """Whether the person is authorized as the primary representative of the account.

    This is the person nominated by the business to provide information about
    themselves, and general information about the account. There can only be one
    representative at any given time. At the time the account is created, this
    person should be set to the person responsible for opening the account.
    """

    title: Optional[str] = None
    """The person's title (e.g., CEO, Support Engineer)."""


class IndividualRequirements(BaseModel):
    currently_due: List[str]
    """Fields that need to be resolved to keep the person's account enabled.

    If not resolved by the account's `current_deadline`, these fields will appear in
    `past_due` as well, and the account is disabled.
    """

    errors: List[AccountRequirementsError]
    """
    Details about validation and verification failures for `due` requirements that
    must be resolved.
    """

    eventually_due: List[str]
    """Fields you must collect when all thresholds are reached.

    As they become required, they appear in `currently_due` as well, and the
    account's `current_deadline` becomes set.
    """

    past_due: List[str]
    """Fields that haven't been resolved by `current_deadline`.

    These fields need to be resolved to enable the person's account.
    """

    pending_verification: List[str]
    """
    Fields that are being reviewed, or might become required depending on the
    results of a review. If the review fails, these fields can move to
    `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might
    appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in
    `pending_verification` if one verification fails but another is still pending.
    """

    alternatives: Optional[List[AccountRequirementsAlternative]] = None
    """
    Fields that are due and can be resolved by providing the corresponding
    alternative fields instead. Many alternatives can list the same
    `original_fields_due`, and any of these alternatives can serve as a pathway for
    attempting to resolve the fields again. Re-providing `original_fields_due` also
    serves as a pathway for attempting to resolve the fields again.
    """


class IndividualUsCfpbDataEthnicityDetails(BaseModel):
    ethnicity: Optional[
        List[
            Literal[
                "cuban",
                "hispanic_or_latino",
                "mexican",
                "not_hispanic_or_latino",
                "other_hispanic_or_latino",
                "prefer_not_to_answer",
                "puerto_rican",
            ]
        ]
    ] = None
    """The persons ethnicity"""

    ethnicity_other: Optional[str] = None
    """Please specify your origin, when other is selected."""


class IndividualUsCfpbDataRaceDetails(BaseModel):
    race: Optional[
        List[
            Literal[
                "african_american",
                "american_indian_or_alaska_native",
                "asian",
                "asian_indian",
                "black_or_african_american",
                "chinese",
                "ethiopian",
                "filipino",
                "guamanian_or_chamorro",
                "haitian",
                "jamaican",
                "japanese",
                "korean",
                "native_hawaiian",
                "native_hawaiian_or_other_pacific_islander",
                "nigerian",
                "other_asian",
                "other_black_or_african_american",
                "other_pacific_islander",
                "prefer_not_to_answer",
                "samoan",
                "somali",
                "vietnamese",
                "white",
            ]
        ]
    ] = None
    """The persons race."""

    race_other: Optional[str] = None
    """Please specify your race, when other is selected."""


class IndividualUsCfpbData(BaseModel):
    ethnicity_details: Optional[IndividualUsCfpbDataEthnicityDetails] = None

    race_details: Optional[IndividualUsCfpbDataRaceDetails] = None

    self_identified_gender: Optional[str] = None
    """The persons self-identified gender"""


IndividualVerificationAdditionalDocumentBack: TypeAlias = Union[str, "File", None]

IndividualVerificationAdditionalDocumentFront: TypeAlias = Union[str, "File", None]


class IndividualVerificationAdditionalDocument(BaseModel):
    back: Optional[IndividualVerificationAdditionalDocumentBack] = None
    """
    The back of an ID returned by a
    [file upload](https://api.stripe.com#create_file) with a `purpose` value of
    `identity_document`.
    """

    details: Optional[str] = None
    """A user-displayable string describing the verification state of this document.

    For example, if a document is uploaded and the picture is too fuzzy, this may
    say "Identity document is too unclear to read".
    """

    details_code: Optional[str] = None
    """
    One of `document_corrupt`, `document_country_not_supported`, `document_expired`,
    `document_failed_copy`, `document_failed_other`, `document_failed_test_mode`,
    `document_fraudulent`, `document_failed_greyscale`, `document_incomplete`,
    `document_invalid`, `document_manipulated`, `document_missing_back`,
    `document_missing_front`, `document_not_readable`, `document_not_uploaded`,
    `document_photo_mismatch`, `document_too_large`, or
    `document_type_not_supported`. A machine-readable code specifying the
    verification state for this document.
    """

    front: Optional[IndividualVerificationAdditionalDocumentFront] = None
    """
    The front of an ID returned by a
    [file upload](https://api.stripe.com#create_file) with a `purpose` value of
    `identity_document`.
    """


IndividualVerificationDocumentBack: TypeAlias = Union[str, "File", None]

IndividualVerificationDocumentFront: TypeAlias = Union[str, "File", None]


class IndividualVerificationDocument(BaseModel):
    back: Optional[IndividualVerificationDocumentBack] = None
    """
    The back of an ID returned by a
    [file upload](https://api.stripe.com#create_file) with a `purpose` value of
    `identity_document`.
    """

    details: Optional[str] = None
    """A user-displayable string describing the verification state of this document.

    For example, if a document is uploaded and the picture is too fuzzy, this may
    say "Identity document is too unclear to read".
    """

    details_code: Optional[str] = None
    """
    One of `document_corrupt`, `document_country_not_supported`, `document_expired`,
    `document_failed_copy`, `document_failed_other`, `document_failed_test_mode`,
    `document_fraudulent`, `document_failed_greyscale`, `document_incomplete`,
    `document_invalid`, `document_manipulated`, `document_missing_back`,
    `document_missing_front`, `document_not_readable`, `document_not_uploaded`,
    `document_photo_mismatch`, `document_too_large`, or
    `document_type_not_supported`. A machine-readable code specifying the
    verification state for this document.
    """

    front: Optional[IndividualVerificationDocumentFront] = None
    """
    The front of an ID returned by a
    [file upload](https://api.stripe.com#create_file) with a `purpose` value of
    `identity_document`.
    """


class IndividualVerification(BaseModel):
    status: str
    """The state of verification for the person.

    Possible values are `unverified`, `pending`, or `verified`. Please refer
    [guide](https://docs.stripe.com/connect/handling-api-verification) to handle
    verification updates.
    """

    additional_document: Optional[IndividualVerificationAdditionalDocument] = None

    details: Optional[str] = None
    """A user-displayable string describing the verification state for the person.

    For example, this may say "Provided identity information could not be verified".
    """

    details_code: Optional[str] = None
    """
    One of `document_address_mismatch`, `document_dob_mismatch`,
    `document_duplicate_type`, `document_id_number_mismatch`,
    `document_name_mismatch`, `document_nationality_mismatch`,
    `failed_keyed_identity`, or `failed_other`. A machine-readable code specifying
    the verification state for the person.
    """

    document: Optional[IndividualVerificationDocument] = None


class Individual(BaseModel):
    """This is an object representing a person associated with a Stripe account.

    A platform can only access a subset of data in a person for an account where [account.controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `stripe`, which includes Standard and Express accounts, after creating an Account Link or Account Session to start Connect onboarding.

    See the [Standard onboarding](/connect/standard-accounts) or [Express onboarding](/connect/express-accounts) documentation for information about prefilling information and account onboarding steps. Learn more about [handling identity verification with the API](/connect/handling-api-verification#person-information).
    """

    id: str
    """Unique identifier for the object."""

    account: str
    """The account the person is associated with."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    object: Literal["person"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    additional_tos_acceptances: Optional[IndividualAdditionalTosAcceptances] = None

    address: Optional[Address] = None

    address_kana: Optional[LegalEntityJapanAddress] = None

    address_kanji: Optional[LegalEntityJapanAddress] = None

    dob: Optional[IndividualDob] = None

    email: Optional[str] = None
    """The person's email address.

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    first_name: Optional[str] = None
    """The person's first name.

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    first_name_kana: Optional[str] = None
    """The Kana variation of the person's first name (Japan only).

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    first_name_kanji: Optional[str] = None
    """The Kanji variation of the person's first name (Japan only).

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    full_name_aliases: Optional[List[str]] = None
    """A list of alternate names or aliases that the person is known by.

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    future_requirements: Optional[IndividualFutureRequirements] = None

    gender: Optional[str] = None
    """The person's gender."""

    id_number_provided: Optional[bool] = None
    """Whether the person's `id_number` was provided.

    True if either the full ID number was provided or if only the required part of
    the ID number was provided (ex. last four of an individual's SSN for the US
    indicated by `ssn_last_4_provided`).
    """

    id_number_secondary_provided: Optional[bool] = None
    """Whether the person's `id_number_secondary` was provided."""

    last_name: Optional[str] = None
    """The person's last name.

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    last_name_kana: Optional[str] = None
    """The Kana variation of the person's last name (Japan only).

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    last_name_kanji: Optional[str] = None
    """The Kanji variation of the person's last name (Japan only).

    Also available for accounts where
    [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`.
    """

    maiden_name: Optional[str] = None
    """The person's maiden name."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    nationality: Optional[str] = None
    """The country where the person is a national."""

    phone: Optional[str] = None
    """The person's phone number."""

    political_exposure: Optional[Literal["existing", "none"]] = None
    """
    Indicates if the person or any of their representatives, family members, or
    other closely related persons, declares that they hold or have held an important
    public job or function, in any jurisdiction.
    """

    registered_address: Optional[Address] = None

    relationship: Optional[IndividualRelationship] = None

    requirements: Optional[IndividualRequirements] = None

    ssn_last_4_provided: Optional[bool] = None
    """
    Whether the last four digits of the person's Social Security number have been
    provided (U.S. only).
    """

    us_cfpb_data: Optional[IndividualUsCfpbData] = None

    verification: Optional[IndividualVerification] = None


class Requirements(BaseModel):
    alternatives: Optional[List[AccountRequirementsAlternative]] = None
    """
    Fields that are due and can be resolved by providing the corresponding
    alternative fields instead. Many alternatives can list the same
    `original_fields_due`, and any of these alternatives can serve as a pathway for
    attempting to resolve the fields again. Re-providing `original_fields_due` also
    serves as a pathway for attempting to resolve the fields again.
    """

    current_deadline: Optional[int] = None
    """
    Date by which the fields in `currently_due` must be collected to keep the
    account enabled. These fields may disable the account sooner if the next
    threshold is reached before they are collected.
    """

    currently_due: Optional[List[str]] = None
    """Fields that need to be resolved to keep the account enabled.

    If not resolved by `current_deadline`, these fields will appear in `past_due` as
    well, and the account is disabled.
    """

    disabled_reason: Optional[
        Literal[
            "action_required.requested_capabilities",
            "listed",
            "other",
            "platform_paused",
            "rejected.fraud",
            "rejected.incomplete_verification",
            "rejected.listed",
            "rejected.other",
            "rejected.platform_fraud",
            "rejected.platform_other",
            "rejected.platform_terms_of_service",
            "rejected.terms_of_service",
            "requirements.past_due",
            "requirements.pending_verification",
            "under_review",
        ]
    ] = None
    """If the account is disabled, this enum describes why.

    [Learn more about handling verification issues](https://docs.stripe.com/connect/handling-api-verification).
    """

    errors: Optional[List[AccountRequirementsError]] = None
    """
    Details about validation and verification failures for `due` requirements that
    must be resolved.
    """

    eventually_due: Optional[List[str]] = None
    """Fields you must collect when all thresholds are reached.

    As they become required, they appear in `currently_due` as well, and
    `current_deadline` becomes set.
    """

    past_due: Optional[List[str]] = None
    """Fields that haven't been resolved by `current_deadline`.

    These fields need to be resolved to enable the account.
    """

    pending_verification: Optional[List[str]] = None
    """
    Fields that are being reviewed, or might become required depending on the
    results of a review. If the review fails, these fields can move to
    `eventually_due`, `currently_due`, `past_due` or `alternatives`. Fields might
    appear in `eventually_due`, `currently_due`, `past_due` or `alternatives` and in
    `pending_verification` if one verification fails but another is still pending.
    """


class TosAcceptance(BaseModel):
    date: Optional[int] = None
    """
    The Unix timestamp marking when the account representative accepted their
    service agreement
    """

    ip: Optional[str] = None
    """
    The IP address from which the account representative accepted their service
    agreement
    """

    service_agreement: Optional[str] = None
    """The user's service agreement type"""

    user_agent: Optional[str] = None
    """
    The user agent of the browser from which the account representative accepted
    their service agreement
    """


class Account(BaseModel):
    """This is an object representing a Stripe account.

    You can retrieve it to see
    properties on the account like its current requirements or if the account is
    enabled to make live charges or receive payouts.

    For accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `application`, which includes Custom accounts, the properties below are always
    returned.

    For accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`, which includes Standard and Express accounts, some properties are only returned
    until you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions)
    to start Connect Onboarding. Learn about the [differences between accounts](/connect/accounts).
    """

    id: str
    """Unique identifier for the object."""

    object: Literal["account"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    business_profile: Optional[BusinessProfile] = None

    business_type: Optional[Literal["company", "government_entity", "individual", "non_profit"]] = None
    """The business type."""

    capabilities: Optional[Capabilities] = None

    charges_enabled: Optional[bool] = None
    """Whether the account can process charges."""

    company: Optional[Company] = None

    controller: Optional[Controller] = None

    country: Optional[str] = None
    """The account's country."""

    created: Optional[int] = None
    """Time at which the account was connected.

    Measured in seconds since the Unix epoch.
    """

    default_currency: Optional[str] = None
    """Three-letter ISO currency code representing the default currency for the
    account.

    This must be a currency that
    [Stripe supports in the account's country](https://stripe.com/docs/payouts).
    """

    details_submitted: Optional[bool] = None
    """Whether account details have been submitted.

    Accounts with Stripe Dashboard access, which includes Standard accounts, cannot
    receive payouts before this is true. Accounts where this is false should be
    directed to [an onboarding flow](/connect/onboarding) to finish submitting
    account details.
    """

    email: Optional[str] = None
    """An email address associated with the account.

    It's not used for authentication and Stripe doesn't market to this field without
    explicit approval from the platform.
    """

    external_accounts: Optional[ExternalAccounts] = None
    """
    External accounts (bank accounts and debit cards) currently attached to this
    account. External accounts are only returned for requests where
    `controller[is_controller]` is true.
    """

    future_requirements: Optional[FutureRequirements] = None

    groups: Optional[Groups] = None

    individual: Optional[Individual] = None
    """This is an object representing a person associated with a Stripe account.

    A platform can only access a subset of data in a person for an account where
    [account.controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection)
    is `stripe`, which includes Standard and Express accounts, after creating an
    Account Link or Account Session to start Connect onboarding.

    See the [Standard onboarding](/connect/standard-accounts) or
    [Express onboarding](/connect/express-accounts) documentation for information
    about prefilling information and account onboarding steps. Learn more about
    [handling identity verification with the API](/connect/handling-api-verification#person-information).
    """

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    payouts_enabled: Optional[bool] = None
    """Whether the funds in this account can be paid out."""

    requirements: Optional[Requirements] = None

    settings: Optional["AccountSettings"] = None

    tos_acceptance: Optional[TosAcceptance] = None

    type: Optional[Literal["custom", "express", "none", "standard"]] = None
    """The Stripe account type. Can be `standard`, `express`, `custom`, or `none`."""


from .card import Card
from .file import File
from .bank_account import BankAccount
from .account_settings import AccountSettings
