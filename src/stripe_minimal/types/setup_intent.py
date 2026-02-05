# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import application
from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.deleted_customer import DeletedCustomer
from .setup_intent_type_specific_payment_method_options_client import SetupIntentTypeSpecificPaymentMethodOptionsClient
from .setup_intent_payment_method_options_mandate_options_payto import (
    SetupIntentPaymentMethodOptionsMandateOptionsPayto,
)

__all__ = [
    "SetupIntent",
    "Application",
    "AutomaticPaymentMethods",
    "Customer",
    "LatestAttempt",
    "Mandate",
    "NextAction",
    "NextActionCashappHandleRedirectOrDisplayQrCode",
    "NextActionCashappHandleRedirectOrDisplayQrCodeQrCode",
    "NextActionRedirectToURL",
    "NextActionVerifyWithMicrodeposits",
    "OnBehalfOf",
    "PaymentMethod",
    "PaymentMethodConfigurationDetails",
    "PaymentMethodOptions",
    "PaymentMethodOptionsAcssDebit",
    "PaymentMethodOptionsAcssDebitSetupIntentPaymentMethodOptionsAcssDebit",
    "PaymentMethodOptionsAcssDebitSetupIntentPaymentMethodOptionsAcssDebitMandateOptions",
    "PaymentMethodOptionsAmazonPay",
    "PaymentMethodOptionsBacsDebit",
    "PaymentMethodOptionsBacsDebitSetupIntentPaymentMethodOptionsBacsDebit",
    "PaymentMethodOptionsBacsDebitSetupIntentPaymentMethodOptionsBacsDebitMandateOptions",
    "PaymentMethodOptionsCard",
    "PaymentMethodOptionsCardSetupIntentPaymentMethodOptionsCard",
    "PaymentMethodOptionsCardSetupIntentPaymentMethodOptionsCardMandateOptions",
    "PaymentMethodOptionsCardPresent",
    "PaymentMethodOptionsKlarna",
    "PaymentMethodOptionsKlarnaSetupIntentPaymentMethodOptionsKlarna",
    "PaymentMethodOptionsLink",
    "PaymentMethodOptionsPaypal",
    "PaymentMethodOptionsPaypalSetupIntentPaymentMethodOptionsPaypal",
    "PaymentMethodOptionsPayto",
    "PaymentMethodOptionsPaytoSetupIntentPaymentMethodOptionsPayto",
    "PaymentMethodOptionsSepaDebit",
    "PaymentMethodOptionsSepaDebitSetupIntentPaymentMethodOptionsSepaDebit",
    "PaymentMethodOptionsSepaDebitSetupIntentPaymentMethodOptionsSepaDebitMandateOptions",
    "PaymentMethodOptionsUsBankAccount",
    "PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccount",
    "PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccountFinancialConnections",
    "PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters",
    "PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccountMandateOptions",
    "SingleUseMandate",
]

Application: TypeAlias = Union[str, application.Application, None]


class AutomaticPaymentMethods(BaseModel):
    allow_redirects: Optional[Literal["always", "never"]] = None
    """Controls whether this SetupIntent will accept redirect-based payment methods.

    Redirect-based payment methods may require your customer to be redirected to a
    payment method's app or site for authentication or additional steps. To
    [confirm](https://docs.stripe.com/api/setup_intents/confirm) this SetupIntent,
    you may be required to provide a `return_url` to redirect customers back to your
    site after they authenticate or complete the setup.
    """

    enabled: Optional[bool] = None
    """Automatically calculates compatible payment methods"""


if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer, None])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer, None]

if TYPE_CHECKING or not PYDANTIC_V1:
    LatestAttempt = TypeAliasType("LatestAttempt", Union[str, "SetupAttempt", None])
else:
    LatestAttempt: TypeAlias = Union[str, "SetupAttempt", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    Mandate = TypeAliasType("Mandate", Union[str, "mandate.Mandate", None])
else:
    Mandate: TypeAlias = Union[str, "mandate.Mandate", None]


class NextActionCashappHandleRedirectOrDisplayQrCodeQrCode(BaseModel):
    expires_at: int
    """The date (unix timestamp) when the QR code expires."""

    image_url_png: str
    """The image_url_png string used to render QR code"""

    image_url_svg: str
    """The image_url_svg string used to render QR code"""


class NextActionCashappHandleRedirectOrDisplayQrCode(BaseModel):
    hosted_instructions_url: str
    """
    The URL to the hosted Cash App Pay instructions page, which allows customers to
    view the QR code, and supports QR code refreshing on expiration.
    """

    mobile_auth_url: str
    """The url for mobile redirect based auth"""

    qr_code: NextActionCashappHandleRedirectOrDisplayQrCodeQrCode


class NextActionRedirectToURL(BaseModel):
    return_url: Optional[str] = None
    """
    If the customer does not exit their browser while authenticating, they will be
    redirected to this specified URL after completion.
    """

    url: Optional[str] = None
    """The URL you must redirect your customer to in order to authenticate."""


class NextActionVerifyWithMicrodeposits(BaseModel):
    arrival_date: int
    """The timestamp when the microdeposits are expected to land."""

    hosted_verification_url: str
    """
    The URL for the hosted verification page, which allows customers to verify their
    bank account.
    """

    microdeposit_type: Optional[Literal["amounts", "descriptor_code"]] = None
    """The type of the microdeposit sent to the customer.

    Used to distinguish between different verification methods.
    """


class NextAction(BaseModel):
    type: str
    """Type of the next action to perform.

    Refer to the other child attributes under `next_action` for available values.
    Examples include: `redirect_to_url`, `use_stripe_sdk`, `alipay_handle_redirect`,
    `oxxo_display_details`, or `verify_with_microdeposits`.
    """

    cashapp_handle_redirect_or_display_qr_code: Optional[NextActionCashappHandleRedirectOrDisplayQrCode] = None

    redirect_to_url: Optional[NextActionRedirectToURL] = None

    use_stripe_sdk: Optional[object] = None
    """
    When confirming a SetupIntent with Stripe.js, Stripe.js depends on the contents
    of this dictionary to invoke authentication flows. The shape of the contents is
    subject to change and is only intended to be used by Stripe.js.
    """

    verify_with_microdeposits: Optional[NextActionVerifyWithMicrodeposits] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    OnBehalfOf = TypeAliasType("OnBehalfOf", Union[str, "Account", None])
else:
    OnBehalfOf: TypeAlias = Union[str, "Account", None]

if TYPE_CHECKING or not PYDANTIC_V1:
    PaymentMethod = TypeAliasType("PaymentMethod", Union[str, "payment_method.PaymentMethod", None])
else:
    PaymentMethod: TypeAlias = Union[str, "payment_method.PaymentMethod", None]


class PaymentMethodConfigurationDetails(BaseModel):
    id: str
    """ID of the payment method configuration used."""

    parent: Optional[str] = None
    """ID of the parent payment method configuration used."""


class PaymentMethodOptionsAcssDebitSetupIntentPaymentMethodOptionsAcssDebitMandateOptions(BaseModel):
    custom_mandate_url: Optional[str] = None
    """A URL for custom mandate text"""

    default_for: Optional[List[Literal["invoice", "subscription"]]] = None
    """List of Stripe products where this mandate can be selected automatically."""

    interval_description: Optional[str] = None
    """Description of the interval.

    Only required if the 'payment_schedule' parameter is 'interval' or 'combined'.
    """

    payment_schedule: Optional[Literal["combined", "interval", "sporadic"]] = None
    """Payment schedule for the mandate."""

    transaction_type: Optional[Literal["business", "personal"]] = None
    """Transaction type of the mandate."""


class PaymentMethodOptionsAcssDebitSetupIntentPaymentMethodOptionsAcssDebit(BaseModel):
    currency: Optional[Literal["cad", "usd"]] = None
    """Currency supported by the bank account"""

    mandate_options: Optional[PaymentMethodOptionsAcssDebitSetupIntentPaymentMethodOptionsAcssDebitMandateOptions] = (
        None
    )

    verification_method: Optional[Literal["automatic", "instant", "microdeposits"]] = None
    """Bank account verification method."""


PaymentMethodOptionsAcssDebit: TypeAlias = Union[
    PaymentMethodOptionsAcssDebitSetupIntentPaymentMethodOptionsAcssDebit,
    SetupIntentTypeSpecificPaymentMethodOptionsClient,
]

PaymentMethodOptionsAmazonPay: TypeAlias = Union[SetupIntentTypeSpecificPaymentMethodOptionsClient, object]


class PaymentMethodOptionsBacsDebitSetupIntentPaymentMethodOptionsBacsDebitMandateOptions(BaseModel):
    reference_prefix: Optional[str] = None
    """Prefix used to generate the Mandate reference.

    Must be at most 12 characters long. Must consist of only uppercase letters,
    numbers, spaces, or the following special characters: '/', '\\__', '-', '&', '.'.
    Cannot begin with 'DDIC' or 'STRIPE'.
    """


class PaymentMethodOptionsBacsDebitSetupIntentPaymentMethodOptionsBacsDebit(BaseModel):
    mandate_options: Optional[PaymentMethodOptionsBacsDebitSetupIntentPaymentMethodOptionsBacsDebitMandateOptions] = (
        None
    )


PaymentMethodOptionsBacsDebit: TypeAlias = Union[
    PaymentMethodOptionsBacsDebitSetupIntentPaymentMethodOptionsBacsDebit,
    SetupIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsCardSetupIntentPaymentMethodOptionsCardMandateOptions(BaseModel):
    amount: int
    """Amount to be charged for future payments."""

    amount_type: Literal["fixed", "maximum"]
    """One of `fixed` or `maximum`.

    If `fixed`, the `amount` param refers to the exact amount to be charged in
    future payments. If `maximum`, the amount charged can be up to the value passed
    for the `amount` param.
    """

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    interval: Literal["day", "month", "sporadic", "week", "year"]
    """Specifies payment frequency.

    One of `day`, `week`, `month`, `year`, or `sporadic`.
    """

    reference: str
    """Unique identifier for the mandate or subscription."""

    start_date: int
    """Start date of the mandate or subscription.

    Start date should not be lesser than yesterday.
    """

    description: Optional[str] = None
    """
    A description of the mandate or subscription that is meant to be displayed to
    the customer.
    """

    end_date: Optional[int] = None
    """End date of the mandate or subscription.

    If not provided, the mandate will be active until canceled. If provided, end
    date should be after start date.
    """

    interval_count: Optional[int] = None
    """The number of intervals between payments.

    For example, `interval=month` and `interval_count=3` indicates one payment every
    three months. Maximum of one year interval allowed (1 year, 12 months, or 52
    weeks). This parameter is optional when `interval=sporadic`.
    """

    supported_types: Optional[List[Literal["india"]]] = None
    """Specifies the type of mandates supported. Possible values are `india`."""


class PaymentMethodOptionsCardSetupIntentPaymentMethodOptionsCard(BaseModel):
    mandate_options: Optional[PaymentMethodOptionsCardSetupIntentPaymentMethodOptionsCardMandateOptions] = None

    network: Optional[
        Literal[
            "amex",
            "cartes_bancaires",
            "diners",
            "discover",
            "eftpos_au",
            "girocard",
            "interac",
            "jcb",
            "link",
            "mastercard",
            "unionpay",
            "unknown",
            "visa",
        ]
    ] = None
    """Selected network to process this SetupIntent on.

    Depends on the available networks of the card attached to the setup intent. Can
    be only set confirm-time.
    """

    request_three_d_secure: Optional[Literal["any", "automatic", "challenge"]] = None
    """
    We strongly recommend that you rely on our SCA Engine to automatically prompt
    your customers for authentication based on risk level and
    [other requirements](https://docs.stripe.com/strong-customer-authentication).
    However, if you wish to request 3D Secure based on logic from your own fraud
    engine, provide this option. If not provided, this value defaults to
    `automatic`. Read our guide on
    [manually requesting 3D Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds)
    for more information on how this configuration interacts with Radar and our SCA
    Engine.
    """


PaymentMethodOptionsCard: TypeAlias = Union[
    PaymentMethodOptionsCardSetupIntentPaymentMethodOptionsCard, SetupIntentTypeSpecificPaymentMethodOptionsClient
]

PaymentMethodOptionsCardPresent: TypeAlias = Union[SetupIntentTypeSpecificPaymentMethodOptionsClient, object]


class PaymentMethodOptionsKlarnaSetupIntentPaymentMethodOptionsKlarna(BaseModel):
    currency: Optional[str] = None
    """The currency of the setup intent. Three letter ISO currency code."""

    preferred_locale: Optional[str] = None
    """
    Preferred locale of the Klarna checkout page that the customer is redirected to.
    """


PaymentMethodOptionsKlarna: TypeAlias = Union[
    PaymentMethodOptionsKlarnaSetupIntentPaymentMethodOptionsKlarna, SetupIntentTypeSpecificPaymentMethodOptionsClient
]

PaymentMethodOptionsLink: TypeAlias = Union[SetupIntentTypeSpecificPaymentMethodOptionsClient, object]


class PaymentMethodOptionsPaypalSetupIntentPaymentMethodOptionsPaypal(BaseModel):
    billing_agreement_id: Optional[str] = None
    """The PayPal Billing Agreement ID (BAID).

    This is an ID generated by PayPal which represents the mandate between the
    merchant and the customer.
    """


PaymentMethodOptionsPaypal: TypeAlias = Union[
    PaymentMethodOptionsPaypalSetupIntentPaymentMethodOptionsPaypal, SetupIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsPaytoSetupIntentPaymentMethodOptionsPayto(BaseModel):
    mandate_options: Optional[SetupIntentPaymentMethodOptionsMandateOptionsPayto] = None


PaymentMethodOptionsPayto: TypeAlias = Union[
    PaymentMethodOptionsPaytoSetupIntentPaymentMethodOptionsPayto, SetupIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsSepaDebitSetupIntentPaymentMethodOptionsSepaDebitMandateOptions(BaseModel):
    reference_prefix: Optional[str] = None
    """Prefix used to generate the Mandate reference.

    Must be at most 12 characters long. Must consist of only uppercase letters,
    numbers, spaces, or the following special characters: '/', '\\__', '-', '&', '.'.
    Cannot begin with 'STRIPE'.
    """


class PaymentMethodOptionsSepaDebitSetupIntentPaymentMethodOptionsSepaDebit(BaseModel):
    mandate_options: Optional[PaymentMethodOptionsSepaDebitSetupIntentPaymentMethodOptionsSepaDebitMandateOptions] = (
        None
    )


PaymentMethodOptionsSepaDebit: TypeAlias = Union[
    PaymentMethodOptionsSepaDebitSetupIntentPaymentMethodOptionsSepaDebit,
    SetupIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
    BaseModel
):
    account_subcategories: Optional[List[Literal["checking", "savings"]]] = None
    """The account subcategories to use to filter for possible accounts to link.

    Valid subcategories are `checking` and `savings`.
    """


class PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccountFinancialConnections(BaseModel):
    filters: Optional[
        PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters
    ] = None

    permissions: Optional[List[Literal["balances", "ownership", "payment_method", "transactions"]]] = None
    """The list of permissions to request.

    The `payment_method` permission must be included.
    """

    prefetch: Optional[List[Literal["balances", "ownership", "transactions"]]] = None
    """Data features requested to be retrieved upon account creation."""

    return_url: Optional[str] = None
    """For webview integrations only.

    Upon completing OAuth login in the native browser, the user will be redirected
    to this URL to return to your app.
    """


class PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccountMandateOptions(BaseModel):
    collection_method: Optional[Literal["paper"]] = None
    """Mandate collection method"""


class PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccount(BaseModel):
    financial_connections: Optional[
        PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccountFinancialConnections
    ] = None

    mandate_options: Optional[
        PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccountMandateOptions
    ] = None

    verification_method: Optional[Literal["automatic", "instant", "microdeposits"]] = None
    """Bank account verification method."""


PaymentMethodOptionsUsBankAccount: TypeAlias = Union[
    PaymentMethodOptionsUsBankAccountSetupIntentPaymentMethodOptionsUsBankAccount,
    SetupIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptions(BaseModel):
    acss_debit: Optional[PaymentMethodOptionsAcssDebit] = None

    amazon_pay: Optional[PaymentMethodOptionsAmazonPay] = None

    bacs_debit: Optional[PaymentMethodOptionsBacsDebit] = None

    card: Optional[PaymentMethodOptionsCard] = None

    card_present: Optional[PaymentMethodOptionsCardPresent] = None

    klarna: Optional[PaymentMethodOptionsKlarna] = None

    link: Optional[PaymentMethodOptionsLink] = None

    paypal: Optional[PaymentMethodOptionsPaypal] = None

    payto: Optional[PaymentMethodOptionsPayto] = None

    sepa_debit: Optional[PaymentMethodOptionsSepaDebit] = None

    us_bank_account: Optional[PaymentMethodOptionsUsBankAccount] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    SingleUseMandate = TypeAliasType("SingleUseMandate", Union[str, "mandate.Mandate", None])
else:
    SingleUseMandate: TypeAlias = Union[str, "mandate.Mandate", None]


class SetupIntent(BaseModel):
    """
    A SetupIntent guides you through the process of setting up and saving a customer's payment credentials for future payments.
    For example, you can use a SetupIntent to set up and save your customer's card without immediately collecting a payment.
    Later, you can use [PaymentIntents](https://api.stripe.com#payment_intents) to drive the payment flow.

    Create a SetupIntent when you're ready to collect your customer's payment credentials.
    Don't maintain long-lived, unconfirmed SetupIntents because they might not be valid.
    The SetupIntent transitions through multiple [statuses](https://docs.stripe.com/payments/intents#intent-statuses) as it guides
    you through the setup process.

    Successful SetupIntents result in payment credentials that are optimized for future payments.
    For example, cardholders in [certain regions](https://stripe.com/guides/strong-customer-authentication) might need to be run through
    [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication) during payment method collection
    to streamline later [off-session payments](https://docs.stripe.com/payments/setup-intents).
    If you use the SetupIntent with a [Customer](https://api.stripe.com#setup_intent_object-customer),
    it automatically attaches the resulting payment method to that Customer after successful setup.
    We recommend using SetupIntents or [setup_future_usage](https://api.stripe.com#payment_intent_object-setup_future_usage) on
    PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

    By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

    Related guide: [Setup Intents API](https://docs.stripe.com/payments/setup-intents)
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

    object: Literal["setup_intent"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    payment_method_types: List[str]
    """The list of payment method types (e.g.

    card) that this SetupIntent is allowed to set up. A list of valid payment method
    types can be found
    [here](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type).
    """

    status: Literal[
        "canceled", "processing", "requires_action", "requires_confirmation", "requires_payment_method", "succeeded"
    ]
    """
    [Status](https://docs.stripe.com/payments/intents#intent-statuses) of this
    SetupIntent, one of `requires_payment_method`, `requires_confirmation`,
    `requires_action`, `processing`, `canceled`, or `succeeded`.
    """

    usage: str
    """Indicates how the payment method is intended to be used in the future.

    Use `on_session` if you intend to only reuse the payment method when the
    customer is in your checkout flow. Use `off_session` if your customer may or may
    not be in your checkout flow. If not provided, this value defaults to
    `off_session`.
    """

    application: Optional[Application] = None
    """ID of the Connect application that created the SetupIntent."""

    attach_to_self: Optional[bool] = None
    """
    If present, the SetupIntent's payment method will be attached to the in-context
    Stripe Account.

    It can only be used for this Stripe Account’s own money movement flows like
    InboundTransfer and OutboundTransfers. It cannot be set to true when setting up
    a PaymentMethod for a Customer, and defaults to false when attaching a
    PaymentMethod to a Customer.
    """

    automatic_payment_methods: Optional[AutomaticPaymentMethods] = None

    cancellation_reason: Optional[Literal["abandoned", "duplicate", "requested_by_customer"]] = None
    """
    Reason for cancellation of this SetupIntent, one of `abandoned`,
    `requested_by_customer`, or `duplicate`.
    """

    client_secret: Optional[str] = None
    """The client secret of this SetupIntent.

    Used for client-side retrieval using a publishable key.

    The client secret can be used to complete payment setup from your frontend. It
    should not be stored, logged, or exposed to anyone other than the customer. Make
    sure that you have TLS enabled on any page that includes the client secret.
    """

    customer: Optional[Customer] = None
    """ID of the Customer this SetupIntent belongs to, if one exists.

    If present, the SetupIntent's payment method will be attached to the Customer on
    successful setup. Payment methods attached to other Customers cannot be used
    with this SetupIntent.
    """

    customer_account: Optional[str] = None
    """ID of the Account this SetupIntent belongs to, if one exists.

    If present, the SetupIntent's payment method will be attached to the Account on
    successful setup. Payment methods attached to other Accounts cannot be used with
    this SetupIntent.
    """

    description: Optional[str] = None
    """An arbitrary string attached to the object.

    Often useful for displaying to users.
    """

    excluded_payment_method_types: Optional[
        List[
            Literal[
                "acss_debit",
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "amazon_pay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "billie",
                "blik",
                "boleto",
                "card",
                "cashapp",
                "crypto",
                "customer_balance",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "kakao_pay",
                "klarna",
                "konbini",
                "kr_card",
                "mb_way",
                "mobilepay",
                "multibanco",
                "naver_pay",
                "nz_bank_account",
                "oxxo",
                "p24",
                "pay_by_bank",
                "payco",
                "paynow",
                "paypal",
                "payto",
                "pix",
                "promptpay",
                "revolut_pay",
                "samsung_pay",
                "satispay",
                "sepa_debit",
                "sofort",
                "swish",
                "twint",
                "us_bank_account",
                "wechat_pay",
                "zip",
            ]
        ]
    ] = None
    """Payment method types that are excluded from this SetupIntent."""

    flow_directions: Optional[List[Literal["inbound", "outbound"]]] = None
    """
    Indicates the directions of money movement for which this payment method is
    intended to be used.

    Include `inbound` if you intend to use the payment method as the origin to pull
    funds from. Include `outbound` if you intend to use the payment method as the
    destination to send funds to. You can include both if you intend to use the
    payment method for both purposes.
    """

    last_setup_error: Optional["APIErrors"] = None

    latest_attempt: Optional[LatestAttempt] = None
    """The most recent SetupAttempt for this SetupIntent."""

    mandate: Optional[Mandate] = None
    """ID of the multi use Mandate generated by the SetupIntent."""

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    next_action: Optional[NextAction] = None

    on_behalf_of: Optional[OnBehalfOf] = None
    """The account (if any) for which the setup is intended."""

    payment_method: Optional[PaymentMethod] = None
    """ID of the payment method used with this SetupIntent.

    If the payment method is `card_present` and isn't a digital wallet, then the
    [generated_card](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-payment_method_details-card_present-generated_card)
    associated with the `latest_attempt` is attached to the Customer instead.
    """

    payment_method_configuration_details: Optional[PaymentMethodConfigurationDetails] = None

    payment_method_options: Optional[PaymentMethodOptions] = None

    single_use_mandate: Optional[SingleUseMandate] = None
    """ID of the single_use Mandate generated by the SetupIntent."""


from . import mandate, customer, payment_method
from .account import Account
from .api_errors import APIErrors
from .setup_attempt import SetupAttempt
