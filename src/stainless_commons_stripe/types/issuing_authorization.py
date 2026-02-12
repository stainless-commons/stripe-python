# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .issuing_authorization_amount_details import IssuingAuthorizationAmountDetails

__all__ = [
    "IssuingAuthorization",
    "MerchantData",
    "RequestHistory",
    "VerificationData",
    "VerificationDataAuthenticationExemption",
    "VerificationDataThreeDSecure",
    "Token",
    "TokenIssuingToken",
    "TokenIssuingTokenCard",
    "TokenIssuingTokenNetworkData",
    "TokenIssuingTokenNetworkDataDevice",
    "TokenIssuingTokenNetworkDataMastercard",
    "TokenIssuingTokenNetworkDataVisa",
    "TokenIssuingTokenNetworkDataWalletProvider",
    "TokenIssuingTokenNetworkDataWalletProviderCardholderAddress",
    "Cardholder",
    "Fleet",
    "FleetCardholderPromptData",
    "FleetReportedBreakdown",
    "FleetReportedBreakdownFuel",
    "FleetReportedBreakdownNonFuel",
    "FleetReportedBreakdownTax",
    "FraudChallenge",
    "Fuel",
    "NetworkData",
    "PendingRequest",
    "Treasury",
]


class MerchantData(BaseModel):
    category: str
    """A categorization of the seller's type of business.

    See our
    [merchant categories guide](https://docs.stripe.com/issuing/merchant-categories)
    for a list of possible values.
    """

    category_code: str
    """The merchant category code for the seller’s business"""

    network_id: str
    """Identifier assigned to the seller by the card network.

    Different card networks may assign different network_id fields to the same
    merchant.
    """

    city: Optional[str] = None
    """City where the seller is located"""

    country: Optional[str] = None
    """Country where the seller is located"""

    name: Optional[str] = None
    """Name of the seller"""

    postal_code: Optional[str] = None
    """Postal code where the seller is located"""

    state: Optional[str] = None
    """State where the seller is located"""

    tax_id: Optional[str] = None
    """The seller's tax identification number.

    Currently populated for French merchants only.
    """

    terminal_id: Optional[str] = None
    """An ID assigned by the seller to the location of the sale."""

    url: Optional[str] = None
    """URL provided by the merchant on a 3DS request"""


class RequestHistory(BaseModel):
    amount: int
    """
    The `pending_request.amount` at the time of the request, presented in your
    card's currency and in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    Stripe held this amount from your account to fund the authorization if the
    request was approved.
    """

    approved: bool
    """Whether this request was approved."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    merchant_amount: int
    """
    The `pending_request.merchant_amount` at the time of the request, presented in
    the `merchant_currency` and in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """

    merchant_currency: str
    """
    The currency that was collected by the merchant and presented to the cardholder
    for the authorization. Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    reason: Literal[
        "account_disabled",
        "card_active",
        "card_canceled",
        "card_expired",
        "card_inactive",
        "cardholder_blocked",
        "cardholder_inactive",
        "cardholder_verification_required",
        "insecure_authorization_method",
        "insufficient_funds",
        "network_fallback",
        "not_allowed",
        "pin_blocked",
        "spending_controls",
        "suspected_fraud",
        "verification_failed",
        "webhook_approved",
        "webhook_declined",
        "webhook_error",
        "webhook_timeout",
    ]
    """
    When an authorization is approved or declined by you or by Stripe, this field
    provides additional detail on the reason for the outcome.
    """

    amount_details: Optional[IssuingAuthorizationAmountDetails] = None

    authorization_code: Optional[str] = None
    """
    A code created by Stripe which is shared with the merchant to validate the
    authorization. This field will be populated if the authorization message was
    approved. The code typically starts with the letter "S", followed by a six-digit
    number. For example, "S498162". Please note that the code is not guaranteed to
    be unique across authorizations.
    """

    network_risk_score: Optional[int] = None
    """
    The card network's estimate of the likelihood that an authorization is
    fraudulent. Takes on values between 1 and 99.
    """

    reason_message: Optional[str] = None
    """
    If the `request_history.reason` is `webhook_error` because the direct webhook
    response is invalid (for example, parsing errors or missing parameters), we
    surface a more detailed error message via this field.
    """

    requested_at: Optional[int] = None
    """
    Time when the card network received an authorization request from the acquirer
    in UTC. Referred to by networks as transmission time.
    """


class VerificationDataAuthenticationExemption(BaseModel):
    claimed_by: Literal["acquirer", "issuer"]
    """
    The entity that requested the exemption, either the acquiring merchant or the
    Issuing user.
    """

    type: Literal["low_value_transaction", "transaction_risk_analysis", "unknown"]
    """The specific exemption claimed for this authorization."""


class VerificationDataThreeDSecure(BaseModel):
    result: Literal["attempt_acknowledged", "authenticated", "failed", "required"]
    """The outcome of the 3D Secure authentication request."""


class VerificationData(BaseModel):
    address_line1_check: Literal["match", "mismatch", "not_provided"]
    """
    Whether the cardholder provided an address first line and if it matched the
    cardholder’s `billing.address.line1`.
    """

    address_postal_code_check: Literal["match", "mismatch", "not_provided"]
    """
    Whether the cardholder provided a postal code and if it matched the cardholder’s
    `billing.address.postal_code`.
    """

    cvc_check: Literal["match", "mismatch", "not_provided"]
    """Whether the cardholder provided a CVC and if it matched Stripe’s record."""

    expiry_check: Literal["match", "mismatch", "not_provided"]
    """
    Whether the cardholder provided an expiry date and if it matched Stripe’s
    record.
    """

    authentication_exemption: Optional[VerificationDataAuthenticationExemption] = None

    postal_code: Optional[str] = None
    """
    The postal code submitted as part of the authorization used for postal code
    verification.
    """

    three_d_secure: Optional[VerificationDataThreeDSecure] = None


TokenIssuingTokenCard: TypeAlias = Union[str, "IssuingCard"]


class TokenIssuingTokenNetworkDataDevice(BaseModel):
    device_fingerprint: Optional[str] = None
    """An obfuscated ID derived from the device ID."""

    ip_address: Optional[str] = None
    """The IP address of the device at provisioning time."""

    location: Optional[str] = None
    """The geographic latitude/longitude coordinates of the device at provisioning
    time.

    The format is [+-]decimal/[+-]decimal.
    """

    name: Optional[str] = None
    """The name of the device used for tokenization."""

    phone_number: Optional[str] = None
    """The phone number of the device used for tokenization."""

    type: Optional[Literal["other", "phone", "watch"]] = None
    """The type of device used for tokenization."""


class TokenIssuingTokenNetworkDataMastercard(BaseModel):
    token_reference_id: str
    """The network-unique identifier for the token."""

    token_requestor_id: str
    """The ID of the entity requesting tokenization, specific to MasterCard."""

    card_reference_id: Optional[str] = None
    """A unique reference ID from MasterCard to represent the card account number."""

    token_requestor_name: Optional[str] = None
    """The name of the entity requesting tokenization, if known.

    This is directly provided from MasterCard.
    """


class TokenIssuingTokenNetworkDataVisa(BaseModel):
    card_reference_id: str
    """A unique reference ID from Visa to represent the card account number."""

    token_reference_id: str
    """The network-unique identifier for the token."""

    token_requestor_id: str
    """The ID of the entity requesting tokenization, specific to Visa."""

    token_risk_score: Optional[str] = None
    """
    Degree of risk associated with the token between `01` and `99`, with higher
    number indicating higher risk. A `00` value indicates the token was not scored
    by Visa.
    """


class TokenIssuingTokenNetworkDataWalletProviderCardholderAddress(BaseModel):
    line1: str
    """The street address of the cardholder tokenizing the card."""

    postal_code: str
    """The postal code of the cardholder tokenizing the card."""


class TokenIssuingTokenNetworkDataWalletProvider(BaseModel):
    account_id: Optional[str] = None
    """
    The wallet provider-given account ID of the digital wallet the token belongs to.
    """

    account_trust_score: Optional[int] = None
    """An evaluation on the trustworthiness of the wallet account between 1 and 5.

    A higher score indicates more trustworthy.
    """

    card_number_source: Optional[Literal["app", "manual", "on_file", "other"]] = None
    """The method used for tokenizing a card."""

    cardholder_address: Optional[TokenIssuingTokenNetworkDataWalletProviderCardholderAddress] = None

    cardholder_name: Optional[str] = None
    """The name of the cardholder tokenizing the card."""

    device_trust_score: Optional[int] = None
    """An evaluation on the trustworthiness of the device.

    A higher score indicates more trustworthy.
    """

    hashed_account_email_address: Optional[str] = None
    """The hashed email address of the cardholder's account with the wallet provider."""

    reason_codes: Optional[
        List[
            Literal[
                "account_card_too_new",
                "account_recently_changed",
                "account_too_new",
                "account_too_new_since_launch",
                "additional_device",
                "data_expired",
                "defer_id_v_decision",
                "device_recently_lost",
                "good_activity_history",
                "has_suspended_tokens",
                "high_risk",
                "inactive_account",
                "long_account_tenure",
                "low_account_score",
                "low_device_score",
                "low_phone_number_score",
                "network_service_error",
                "outside_home_territory",
                "provisioning_cardholder_mismatch",
                "provisioning_device_and_cardholder_mismatch",
                "provisioning_device_mismatch",
                "same_device_no_prior_authentication",
                "same_device_successful_prior_authentication",
                "software_update",
                "suspicious_activity",
                "too_many_different_cardholders",
                "too_many_recent_attempts",
                "too_many_recent_tokens",
            ]
        ]
    ] = None
    """The reasons for suggested tokenization given by the card network."""

    suggested_decision: Optional[Literal["approve", "decline", "require_auth"]] = None
    """The recommendation on responding to the tokenization request."""

    suggested_decision_version: Optional[str] = None
    """
    The version of the standard for mapping reason codes followed by the wallet
    provider.
    """


class TokenIssuingTokenNetworkData(BaseModel):
    type: Literal["mastercard", "visa"]
    """The network that the token is associated with.

    An additional hash is included with a name matching this value, containing
    tokenization data specific to the card network.
    """

    device: Optional[TokenIssuingTokenNetworkDataDevice] = None

    mastercard: Optional[TokenIssuingTokenNetworkDataMastercard] = None

    visa: Optional[TokenIssuingTokenNetworkDataVisa] = None

    wallet_provider: Optional[TokenIssuingTokenNetworkDataWalletProvider] = None


class TokenIssuingToken(BaseModel):
    """
    An issuing token object is created when an issued card is added to a digital wallet. As a [card issuer](https://docs.stripe.com/issuing), you can [view and manage these tokens](https://docs.stripe.com/issuing/controls/token-management) through Stripe.
    """

    id: str
    """Unique identifier for the object."""

    card: TokenIssuingTokenCard
    """Card associated with this token."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    network: Literal["mastercard", "visa"]
    """The token service provider / card network associated with the token."""

    network_updated_at: int
    """Time at which the token was last updated by the card network.

    Measured in seconds since the Unix epoch.
    """

    object: Literal["issuing.token"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    status: Literal["active", "deleted", "requested", "suspended"]
    """The usage state of the token."""

    device_fingerprint: Optional[str] = None
    """
    The hashed ID derived from the device ID from the card network associated with
    the token.
    """

    last4: Optional[str] = None
    """The last four digits of the token."""

    network_data: Optional[TokenIssuingTokenNetworkData] = None

    wallet_provider: Optional[Literal["apple_pay", "google_pay", "samsung_pay"]] = None
    """The digital wallet for this token, if one was used."""


Token: TypeAlias = Union[str, TokenIssuingToken, None]

Cardholder: TypeAlias = Union[str, "IssuingCardholder", None]


class FleetCardholderPromptData(BaseModel):
    alphanumeric_id: Optional[str] = None
    """
    [Deprecated] An alphanumeric ID, though typical point of sales only support
    numeric entry. The card program can be configured to prompt for a vehicle ID,
    driver ID, or generic ID.
    """

    driver_id: Optional[str] = None
    """Driver ID."""

    odometer: Optional[int] = None
    """Odometer reading."""

    unspecified_id: Optional[str] = None
    """An alphanumeric ID.

    This field is used when a vehicle ID, driver ID, or generic ID is entered by the
    cardholder, but the merchant or card network did not specify the prompt type.
    """

    user_id: Optional[str] = None
    """User ID."""

    vehicle_number: Optional[str] = None
    """Vehicle number."""


class FleetReportedBreakdownFuel(BaseModel):
    gross_amount_decimal: Optional[str] = None
    """
    Gross fuel amount that should equal Fuel Quantity multiplied by Fuel Unit Cost,
    inclusive of taxes.
    """


class FleetReportedBreakdownNonFuel(BaseModel):
    gross_amount_decimal: Optional[str] = None
    """
    Gross non-fuel amount that should equal the sum of the line items, inclusive of
    taxes.
    """


class FleetReportedBreakdownTax(BaseModel):
    local_amount_decimal: Optional[str] = None
    """Amount of state or provincial Sales Tax included in the transaction amount.

    `null` if not reported by merchant or not subject to tax.
    """

    national_amount_decimal: Optional[str] = None
    """Amount of national Sales Tax or VAT included in the transaction amount.

    `null` if not reported by merchant or not subject to tax.
    """


class FleetReportedBreakdown(BaseModel):
    fuel: Optional[FleetReportedBreakdownFuel] = None

    non_fuel: Optional[FleetReportedBreakdownNonFuel] = None

    tax: Optional[FleetReportedBreakdownTax] = None


class Fleet(BaseModel):
    cardholder_prompt_data: Optional[FleetCardholderPromptData] = None

    purchase_type: Optional[Literal["fuel_and_non_fuel_purchase", "fuel_purchase", "non_fuel_purchase"]] = None
    """The type of purchase."""

    reported_breakdown: Optional[FleetReportedBreakdown] = None

    service_type: Optional[Literal["full_service", "non_fuel_transaction", "self_service"]] = None
    """The type of fuel service."""


class FraudChallenge(BaseModel):
    channel: Literal["sms"]
    """The method by which the fraud challenge was delivered to the cardholder."""

    status: Literal["expired", "pending", "rejected", "undeliverable", "verified"]
    """The status of the fraud challenge."""

    undeliverable_reason: Optional[Literal["no_phone_number", "unsupported_phone_number"]] = None
    """If the challenge is not deliverable, the reason why."""


class Fuel(BaseModel):
    industry_product_code: Optional[str] = None
    """
    [Conexxus Payment System Product Code](https://www.conexxus.org/conexxus-payment-system-product-codes)
    identifying the primary fuel product purchased.
    """

    quantity_decimal: Optional[str] = None
    """
    The quantity of `unit`s of fuel that was dispensed, represented as a decimal
    string with at most 12 decimal places.
    """

    type: Optional[Literal["diesel", "other", "unleaded_plus", "unleaded_regular", "unleaded_super"]] = None
    """The type of fuel that was purchased."""

    unit: Optional[
        Literal[
            "charging_minute", "imperial_gallon", "kilogram", "kilowatt_hour", "liter", "other", "pound", "us_gallon"
        ]
    ] = None
    """The units for `quantity_decimal`."""

    unit_cost_decimal: Optional[str] = None
    """
    The cost in cents per each unit of fuel, represented as a decimal string with at
    most 12 decimal places.
    """


class NetworkData(BaseModel):
    acquiring_institution_id: Optional[str] = None
    """Identifier assigned to the acquirer by the card network.

    Sometimes this value is not provided by the network; in this case, the value
    will be `null`.
    """

    system_trace_audit_number: Optional[str] = None
    """
    The System Trace Audit Number (STAN) is a 6-digit identifier assigned by the
    acquirer. Prefer `network_data.transaction_id` if present, unless you have
    special requirements.
    """

    transaction_id: Optional[str] = None
    """
    Unique identifier for the authorization assigned by the card network used to
    match subsequent messages, disputes, and transactions.
    """


class PendingRequest(BaseModel):
    amount: int
    """
    The additional amount Stripe will hold if the authorization is approved, in the
    card's
    [currency](https://docs.stripe.com/api#issuing_authorization_object-pending-request-currency)
    and in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    is_amount_controllable: bool
    """
    If set `true`, you may provide
    [amount](https://docs.stripe.com/api/issuing/authorizations/approve#approve_issuing_authorization-amount)
    to control how much to hold for the authorization.
    """

    merchant_amount: int
    """
    The amount the merchant is requesting to be authorized in the
    `merchant_currency`. The amount is in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """

    merchant_currency: str
    """The local currency the merchant is requesting to authorize."""

    amount_details: Optional[IssuingAuthorizationAmountDetails] = None

    network_risk_score: Optional[int] = None
    """
    The card network's estimate of the likelihood that an authorization is
    fraudulent. Takes on values between 1 and 99.
    """


class Treasury(BaseModel):
    received_credits: List[str]
    """
    The array of
    [ReceivedCredits](https://docs.stripe.com/api/treasury/received_credits)
    associated with this authorization
    """

    received_debits: List[str]
    """
    The array of
    [ReceivedDebits](https://docs.stripe.com/api/treasury/received_debits)
    associated with this authorization
    """

    transaction: Optional[str] = None
    """
    The Treasury [Transaction](https://docs.stripe.com/api/treasury/transactions)
    associated with this authorization
    """


class IssuingAuthorization(BaseModel):
    """
    When an [issued card](https://docs.stripe.com/issuing) is used to make a purchase, an Issuing `Authorization`
    object is created. [Authorizations](https://docs.stripe.com/issuing/purchases/authorizations) must be approved for the
    purchase to be completed successfully.

    Related guide: [Issued card authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """The total amount that was authorized or rejected.

    This amount is in `currency` and in the
    [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    `amount` should be the same as `merchant_amount`, unless `currency` and
    `merchant_currency` are different.
    """

    approved: bool
    """Whether the authorization has been approved."""

    authorization_method: Literal["chip", "contactless", "keyed_in", "online", "swipe"]
    """How the card details were provided."""

    balance_transactions: List["BalanceTransaction"]
    """List of balance transactions associated with this authorization."""

    card: "IssuingCard"
    """
    You can [create physical or virtual cards](https://docs.stripe.com/issuing) that
    are issued to cardholders.
    """

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """The currency of the cardholder.

    This currency can be different from the currency presented at authorization and
    the `merchant_currency` field on this authorization. Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    merchant_amount: int
    """The total amount that was authorized or rejected.

    This amount is in the `merchant_currency` and in the
    [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    `merchant_amount` should be the same as `amount`, unless `merchant_currency` and
    `currency` are different.
    """

    merchant_currency: str
    """The local currency that was presented to the cardholder for the authorization.

    This currency can be different from the cardholder currency and the `currency`
    field on this authorization. Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    merchant_data: MerchantData

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    object: Literal["issuing.authorization"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    request_history: List[RequestHistory]
    """
    History of every time a `pending_request` authorization was approved/declined,
    either by you directly or by Stripe (e.g. based on your spending_controls). If
    the merchant changes the authorization by performing an incremental
    authorization, you can look at this field to see the previous requests for the
    authorization. This field can be helpful in determining why a given
    authorization was approved/declined.
    """

    status: Literal["closed", "expired", "pending", "reversed"]
    """The current status of the authorization in its lifecycle."""

    transactions: List["IssuingTransaction"]
    """
    List of [transactions](https://docs.stripe.com/api/issuing/transactions)
    associated with this authorization.
    """

    verification_data: VerificationData

    token: Optional[Token] = None
    """
    [Token](https://docs.stripe.com/api/issuing/tokens/object) object used for this
    authorization. If a network token was not used for this authorization, this
    field will be null.
    """

    amount_details: Optional[IssuingAuthorizationAmountDetails] = None

    cardholder: Optional[Cardholder] = None
    """The cardholder to whom this authorization belongs."""

    fleet: Optional[Fleet] = None

    fraud_challenges: Optional[List[FraudChallenge]] = None
    """
    Fraud challenges sent to the cardholder, if this authorization was declined for
    fraud risk reasons.
    """

    fuel: Optional[Fuel] = None

    network_data: Optional[NetworkData] = None

    pending_request: Optional[PendingRequest] = None

    treasury: Optional[Treasury] = None

    verified_by_fraud_challenge: Optional[bool] = None
    """
    Whether the authorization bypassed fraud risk checks because the cardholder has
    previously completed a fraud challenge on a similar high-risk authorization from
    the same merchant.
    """

    wallet: Optional[str] = None
    """The digital wallet used for this transaction.

    One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when
    no digital wallet was utilized.
    """


from .issuing_card import IssuingCard
from .issuing_cardholder import IssuingCardholder
from .balance_transaction import BalanceTransaction
from .issuing_transaction import IssuingTransaction
