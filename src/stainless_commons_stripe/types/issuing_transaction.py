# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "IssuingTransaction",
    "Card",
    "MerchantData",
    "Token",
    "TokenIssuingToken",
    "TokenIssuingTokenCard",
    "TokenIssuingTokenNetworkData",
    "TokenIssuingTokenNetworkDataDevice",
    "TokenIssuingTokenNetworkDataMastercard",
    "TokenIssuingTokenNetworkDataVisa",
    "TokenIssuingTokenNetworkDataWalletProvider",
    "TokenIssuingTokenNetworkDataWalletProviderCardholderAddress",
    "AmountDetails",
    "Authorization",
    "BalanceTransaction",
    "Cardholder",
    "Dispute",
    "NetworkData",
    "PurchaseDetails",
    "PurchaseDetailsFleet",
    "PurchaseDetailsFleetCardholderPromptData",
    "PurchaseDetailsFleetReportedBreakdown",
    "PurchaseDetailsFleetReportedBreakdownFuel",
    "PurchaseDetailsFleetReportedBreakdownNonFuel",
    "PurchaseDetailsFleetReportedBreakdownTax",
    "PurchaseDetailsFlight",
    "PurchaseDetailsFlightSegment",
    "PurchaseDetailsFuel",
    "PurchaseDetailsLodging",
    "PurchaseDetailsReceipt",
    "Treasury",
]

Card: TypeAlias = Union[str, "IssuingCard"]


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


class AmountDetails(BaseModel):
    atm_fee: Optional[int] = None
    """The fee charged by the ATM for the cash withdrawal."""

    cashback_amount: Optional[int] = None
    """The amount of cash requested by the cardholder."""


if TYPE_CHECKING or not PYDANTIC_V1:
    Authorization = TypeAliasType("Authorization", Union[str, "IssuingAuthorization", None])
else:
    Authorization: TypeAlias = Union[str, "IssuingAuthorization", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    BalanceTransaction = TypeAliasType("BalanceTransaction", Union[str, "balance_transaction.BalanceTransaction", None])
else:
    BalanceTransaction: TypeAlias = Union[str, "balance_transaction.BalanceTransaction", None]

Cardholder: TypeAlias = Union[str, "IssuingCardholder", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Dispute = TypeAliasType("Dispute", Union[str, "IssuingDispute", None])
else:
    Dispute: TypeAlias = Union[str, "IssuingDispute", None]


class NetworkData(BaseModel):
    authorization_code: Optional[str] = None
    """
    A code created by Stripe which is shared with the merchant to validate the
    authorization. This field will be populated if the authorization message was
    approved. The code typically starts with the letter "S", followed by a six-digit
    number. For example, "S498162". Please note that the code is not guaranteed to
    be unique across authorizations.
    """

    processing_date: Optional[str] = None
    """The date the transaction was processed by the card network.

    This can be different from the date the seller recorded the transaction
    depending on when the acquirer submits the transaction to the network.
    """

    transaction_id: Optional[str] = None
    """
    Unique identifier for the authorization assigned by the card network used to
    match subsequent messages, disputes, and transactions.
    """


class PurchaseDetailsFleetCardholderPromptData(BaseModel):
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


class PurchaseDetailsFleetReportedBreakdownFuel(BaseModel):
    gross_amount_decimal: Optional[str] = None
    """
    Gross fuel amount that should equal Fuel Volume multipled by Fuel Unit Cost,
    inclusive of taxes.
    """


class PurchaseDetailsFleetReportedBreakdownNonFuel(BaseModel):
    gross_amount_decimal: Optional[str] = None
    """
    Gross non-fuel amount that should equal the sum of the line items, inclusive of
    taxes.
    """


class PurchaseDetailsFleetReportedBreakdownTax(BaseModel):
    local_amount_decimal: Optional[str] = None
    """Amount of state or provincial Sales Tax included in the transaction amount.

    Null if not reported by merchant or not subject to tax.
    """

    national_amount_decimal: Optional[str] = None
    """Amount of national Sales Tax or VAT included in the transaction amount.

    Null if not reported by merchant or not subject to tax.
    """


class PurchaseDetailsFleetReportedBreakdown(BaseModel):
    fuel: Optional[PurchaseDetailsFleetReportedBreakdownFuel] = None

    non_fuel: Optional[PurchaseDetailsFleetReportedBreakdownNonFuel] = None

    tax: Optional[PurchaseDetailsFleetReportedBreakdownTax] = None


class PurchaseDetailsFleet(BaseModel):
    cardholder_prompt_data: Optional[PurchaseDetailsFleetCardholderPromptData] = None

    purchase_type: Optional[str] = None
    """The type of purchase.

    One of `fuel_purchase`, `non_fuel_purchase`, or `fuel_and_non_fuel_purchase`.
    """

    reported_breakdown: Optional[PurchaseDetailsFleetReportedBreakdown] = None

    service_type: Optional[str] = None
    """The type of fuel service.

    One of `non_fuel_transaction`, `full_service`, or `self_service`.
    """


class PurchaseDetailsFlightSegment(BaseModel):
    arrival_airport_code: Optional[str] = None
    """The three-letter IATA airport code of the flight's destination."""

    carrier: Optional[str] = None
    """The airline carrier code."""

    departure_airport_code: Optional[str] = None
    """The three-letter IATA airport code that the flight departed from."""

    flight_number: Optional[str] = None
    """The flight number."""

    service_class: Optional[str] = None
    """The flight's service class."""

    stopover_allowed: Optional[bool] = None
    """Whether a stopover is allowed on this flight."""


class PurchaseDetailsFlight(BaseModel):
    departure_at: Optional[int] = None
    """The time that the flight departed."""

    passenger_name: Optional[str] = None
    """The name of the passenger."""

    refundable: Optional[bool] = None
    """Whether the ticket is refundable."""

    segments: Optional[List[PurchaseDetailsFlightSegment]] = None
    """The legs of the trip."""

    travel_agency: Optional[str] = None
    """The travel agency that issued the ticket."""


class PurchaseDetailsFuel(BaseModel):
    type: str
    """The type of fuel that was purchased.

    One of `diesel`, `unleaded_plus`, `unleaded_regular`, `unleaded_super`, or
    `other`.
    """

    unit: str
    """The units for `quantity_decimal`.

    One of `charging_minute`, `imperial_gallon`, `kilogram`, `kilowatt_hour`,
    `liter`, `pound`, `us_gallon`, or `other`.
    """

    unit_cost_decimal: str
    """
    The cost in cents per each unit of fuel, represented as a decimal string with at
    most 12 decimal places.
    """

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


class PurchaseDetailsLodging(BaseModel):
    check_in_at: Optional[int] = None
    """The time of checking into the lodging."""

    nights: Optional[int] = None
    """The number of nights stayed at the lodging."""


class PurchaseDetailsReceipt(BaseModel):
    description: Optional[str] = None
    """The description of the item. The maximum length of this field is 26 characters."""

    quantity: Optional[float] = None
    """The quantity of the item."""

    total: Optional[int] = None
    """The total for this line item in cents."""

    unit_cost: Optional[int] = None
    """The unit cost of the item in cents."""


class PurchaseDetails(BaseModel):
    fleet: Optional[PurchaseDetailsFleet] = None

    flight: Optional[PurchaseDetailsFlight] = None

    fuel: Optional[PurchaseDetailsFuel] = None

    lodging: Optional[PurchaseDetailsLodging] = None

    receipt: Optional[List[PurchaseDetailsReceipt]] = None
    """The line items in the purchase."""

    reference: Optional[str] = None
    """A merchant-specific order number."""


class Treasury(BaseModel):
    received_credit: Optional[str] = None
    """
    The Treasury
    [ReceivedCredit](https://docs.stripe.com/api/treasury/received_credits)
    representing this Issuing transaction if it is a refund
    """

    received_debit: Optional[str] = None
    """
    The Treasury
    [ReceivedDebit](https://docs.stripe.com/api/treasury/received_debits)
    representing this Issuing transaction if it is a capture
    """


class IssuingTransaction(BaseModel):
    """
    Any use of an [issued card](https://docs.stripe.com/issuing) that results in funds entering or leaving
    your Stripe account, such as a completed purchase or refund, is represented by an Issuing
    `Transaction` object.

    Related guide: [Issued card transactions](https://docs.stripe.com/issuing/purchases/transactions)
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """The transaction amount, which will be reflected in your balance.

    This amount is in your currency and in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """

    card: Card
    """The card used to make this transaction."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    merchant_amount: int
    """
    The amount that the merchant will receive, denominated in `merchant_currency`
    and in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). It
    will be different from `amount` if the merchant is taking payment in a different
    currency.
    """

    merchant_currency: str
    """The currency with which the merchant is taking payment."""

    merchant_data: MerchantData

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    object: Literal["issuing.transaction"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    type: Literal["capture", "refund"]
    """The nature of the transaction."""

    token: Optional[Token] = None
    """
    [Token](https://docs.stripe.com/api/issuing/tokens/object) object used for this
    transaction. If a network token was not used for this transaction, this field
    will be null.
    """

    amount_details: Optional[AmountDetails] = None

    authorization: Optional[Authorization] = None
    """The `Authorization` object that led to this transaction."""

    balance_transaction: Optional[BalanceTransaction] = None
    """
    ID of the
    [balance transaction](https://docs.stripe.com/api/balance_transactions)
    associated with this transaction.
    """

    cardholder: Optional[Cardholder] = None
    """The cardholder to whom this transaction belongs."""

    dispute: Optional[Dispute] = None
    """If you've disputed the transaction, the ID of the dispute."""

    network_data: Optional[NetworkData] = None

    purchase_details: Optional[PurchaseDetails] = None

    treasury: Optional[Treasury] = None

    wallet: Optional[Literal["apple_pay", "google_pay", "samsung_pay"]] = None
    """The digital wallet used for this transaction.

    One of `apple_pay`, `google_pay`, or `samsung_pay`.
    """


from . import balance_transaction
from .issuing_card import IssuingCard
from .issuing_dispute import IssuingDispute
from .issuing_cardholder import IssuingCardholder
from .issuing_authorization import IssuingAuthorization
