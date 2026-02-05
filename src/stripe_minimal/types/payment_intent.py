# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import application
from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.address import Address
from .shared.shipping import Shipping
from .shared.deleted_customer import DeletedCustomer
from .payment_method_options_card_present_routing import PaymentMethodOptionsCardPresentRouting
from .shared.payment_method_details_card_installments_plan import PaymentMethodDetailsCardInstallmentsPlan
from .shared.payment_flows_payment_intent_presentment_details import PaymentFlowsPaymentIntentPresentmentDetails
from .payment_intent_type_specific_payment_method_options_client import (
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
)
from .payment_intent_payment_method_options_mandate_options_payto import (
    PaymentIntentPaymentMethodOptionsMandateOptionsPayto,
)

__all__ = [
    "PaymentIntent",
    "AmountDetails",
    "AmountDetailsPaymentFlowsAmountDetails",
    "AmountDetailsPaymentFlowsAmountDetailsError",
    "AmountDetailsPaymentFlowsAmountDetailsLineItems",
    "AmountDetailsPaymentFlowsAmountDetailsLineItemsData",
    "AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptions",
    "AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsCard",
    "AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsCardPresent",
    "AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsKlarna",
    "AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsPaypal",
    "AmountDetailsPaymentFlowsAmountDetailsLineItemsDataTax",
    "AmountDetailsPaymentFlowsAmountDetailsShipping",
    "AmountDetailsPaymentFlowsAmountDetailsTax",
    "AmountDetailsPaymentFlowsAmountDetailsTip",
    "AmountDetailsPaymentFlowsAmountDetailsClient",
    "AmountDetailsPaymentFlowsAmountDetailsClientTip",
    "Application",
    "AutomaticPaymentMethods",
    "Customer",
    "Hooks",
    "HooksInputs",
    "HooksInputsTax",
    "LatestCharge",
    "NextAction",
    "NextActionAlipayHandleRedirect",
    "NextActionBoletoDisplayDetails",
    "NextActionCardAwaitNotification",
    "NextActionCashappHandleRedirectOrDisplayQrCode",
    "NextActionCashappHandleRedirectOrDisplayQrCodeQrCode",
    "NextActionDisplayBankTransferInstructions",
    "NextActionDisplayBankTransferInstructionsFinancialAddress",
    "NextActionDisplayBankTransferInstructionsFinancialAddressAba",
    "NextActionDisplayBankTransferInstructionsFinancialAddressIban",
    "NextActionDisplayBankTransferInstructionsFinancialAddressSortCode",
    "NextActionDisplayBankTransferInstructionsFinancialAddressSpei",
    "NextActionDisplayBankTransferInstructionsFinancialAddressSwift",
    "NextActionDisplayBankTransferInstructionsFinancialAddressZengin",
    "NextActionKonbiniDisplayDetails",
    "NextActionKonbiniDisplayDetailsStores",
    "NextActionKonbiniDisplayDetailsStoresFamilymart",
    "NextActionKonbiniDisplayDetailsStoresLawson",
    "NextActionKonbiniDisplayDetailsStoresMinistop",
    "NextActionKonbiniDisplayDetailsStoresSeicomart",
    "NextActionMultibancoDisplayDetails",
    "NextActionOxxoDisplayDetails",
    "NextActionPaynowDisplayQrCode",
    "NextActionPixDisplayQrCode",
    "NextActionPromptpayDisplayQrCode",
    "NextActionRedirectToURL",
    "NextActionSwishHandleRedirectOrDisplayQrCode",
    "NextActionSwishHandleRedirectOrDisplayQrCodeQrCode",
    "NextActionVerifyWithMicrodeposits",
    "NextActionWechatPayDisplayQrCode",
    "NextActionWechatPayRedirectToAndroidApp",
    "NextActionWechatPayRedirectToIosApp",
    "OnBehalfOf",
    "PaymentDetails",
    "PaymentMethod",
    "PaymentMethodConfigurationDetails",
    "PaymentMethodOptions",
    "PaymentMethodOptionsAcssDebit",
    "PaymentMethodOptionsAcssDebitPaymentIntentPaymentMethodOptionsAcssDebit",
    "PaymentMethodOptionsAcssDebitPaymentIntentPaymentMethodOptionsAcssDebitMandateOptions",
    "PaymentMethodOptionsAffirm",
    "PaymentMethodOptionsAffirmPaymentMethodOptionsAffirm",
    "PaymentMethodOptionsAfterpayClearpay",
    "PaymentMethodOptionsAfterpayClearpayPaymentMethodOptionsAfterpayClearpay",
    "PaymentMethodOptionsAlipay",
    "PaymentMethodOptionsAlipayPaymentMethodOptionsAlipay",
    "PaymentMethodOptionsAlma",
    "PaymentMethodOptionsAlmaPaymentMethodOptionsAlma",
    "PaymentMethodOptionsAmazonPay",
    "PaymentMethodOptionsAmazonPayPaymentMethodOptionsAmazonPay",
    "PaymentMethodOptionsAuBecsDebit",
    "PaymentMethodOptionsAuBecsDebitPaymentIntentPaymentMethodOptionsAuBecsDebit",
    "PaymentMethodOptionsBacsDebit",
    "PaymentMethodOptionsBacsDebitPaymentIntentPaymentMethodOptionsBacsDebit",
    "PaymentMethodOptionsBacsDebitPaymentIntentPaymentMethodOptionsBacsDebitMandateOptions",
    "PaymentMethodOptionsBancontact",
    "PaymentMethodOptionsBancontactPaymentMethodOptionsBancontact",
    "PaymentMethodOptionsBillie",
    "PaymentMethodOptionsBilliePaymentMethodOptionsBillie",
    "PaymentMethodOptionsBlik",
    "PaymentMethodOptionsBlikPaymentIntentPaymentMethodOptionsBlik",
    "PaymentMethodOptionsBoleto",
    "PaymentMethodOptionsBoletoPaymentMethodOptionsBoleto",
    "PaymentMethodOptionsCard",
    "PaymentMethodOptionsCardPaymentIntentPaymentMethodOptionsCard",
    "PaymentMethodOptionsCardPaymentIntentPaymentMethodOptionsCardInstallments",
    "PaymentMethodOptionsCardPaymentIntentPaymentMethodOptionsCardMandateOptions",
    "PaymentMethodOptionsCardPresent",
    "PaymentMethodOptionsCardPresentPaymentMethodOptionsCardPresent",
    "PaymentMethodOptionsCashapp",
    "PaymentMethodOptionsCashappPaymentMethodOptionsCashapp",
    "PaymentMethodOptionsCrypto",
    "PaymentMethodOptionsCryptoPaymentMethodOptionsCrypto",
    "PaymentMethodOptionsCustomerBalance",
    "PaymentMethodOptionsCustomerBalancePaymentMethodOptionsCustomerBalance",
    "PaymentMethodOptionsCustomerBalancePaymentMethodOptionsCustomerBalanceBankTransfer",
    "PaymentMethodOptionsCustomerBalancePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer",
    "PaymentMethodOptionsEps",
    "PaymentMethodOptionsEpsPaymentIntentPaymentMethodOptionsEps",
    "PaymentMethodOptionsFpx",
    "PaymentMethodOptionsFpxPaymentMethodOptionsFpx",
    "PaymentMethodOptionsGiropay",
    "PaymentMethodOptionsGiropayPaymentMethodOptionsGiropay",
    "PaymentMethodOptionsGrabpay",
    "PaymentMethodOptionsGrabpayPaymentMethodOptionsGrabpay",
    "PaymentMethodOptionsIdeal",
    "PaymentMethodOptionsIdealPaymentMethodOptionsIdeal",
    "PaymentMethodOptionsInteracPresent",
    "PaymentMethodOptionsKakaoPay",
    "PaymentMethodOptionsKakaoPayPaymentFlowsPrivatePaymentMethodsKakaoPayPaymentMethodOptions",
    "PaymentMethodOptionsKlarna",
    "PaymentMethodOptionsKlarnaPaymentMethodOptionsKlarna",
    "PaymentMethodOptionsKonbini",
    "PaymentMethodOptionsKonbiniPaymentMethodOptionsKonbini",
    "PaymentMethodOptionsKrCard",
    "PaymentMethodOptionsKrCardPaymentMethodOptionsKrCard",
    "PaymentMethodOptionsLink",
    "PaymentMethodOptionsLinkPaymentIntentPaymentMethodOptionsLink",
    "PaymentMethodOptionsMBWay",
    "PaymentMethodOptionsMBWayPaymentMethodOptionsMBWay",
    "PaymentMethodOptionsMobilepay",
    "PaymentMethodOptionsMobilepayPaymentIntentPaymentMethodOptionsMobilepay",
    "PaymentMethodOptionsMultibanco",
    "PaymentMethodOptionsMultibancoPaymentMethodOptionsMultibanco",
    "PaymentMethodOptionsNaverPay",
    "PaymentMethodOptionsNaverPayPaymentFlowsPrivatePaymentMethodsNaverPayPaymentMethodOptions",
    "PaymentMethodOptionsNzBankAccount",
    "PaymentMethodOptionsNzBankAccountPaymentIntentPaymentMethodOptionsNzBankAccount",
    "PaymentMethodOptionsOxxo",
    "PaymentMethodOptionsOxxoPaymentMethodOptionsOxxo",
    "PaymentMethodOptionsP24",
    "PaymentMethodOptionsP24PaymentMethodOptionsP24",
    "PaymentMethodOptionsPayByBank",
    "PaymentMethodOptionsPayco",
    "PaymentMethodOptionsPaycoPaymentFlowsPrivatePaymentMethodsPaycoPaymentMethodOptions",
    "PaymentMethodOptionsPaynow",
    "PaymentMethodOptionsPaynowPaymentMethodOptionsPaynow",
    "PaymentMethodOptionsPaypal",
    "PaymentMethodOptionsPaypalPaymentMethodOptionsPaypal",
    "PaymentMethodOptionsPayto",
    "PaymentMethodOptionsPaytoPaymentIntentPaymentMethodOptionsPayto",
    "PaymentMethodOptionsPix",
    "PaymentMethodOptionsPixPaymentMethodOptionsPix",
    "PaymentMethodOptionsPromptpay",
    "PaymentMethodOptionsPromptpayPaymentMethodOptionsPromptpay",
    "PaymentMethodOptionsRevolutPay",
    "PaymentMethodOptionsRevolutPayPaymentMethodOptionsRevolutPay",
    "PaymentMethodOptionsSamsungPay",
    "PaymentMethodOptionsSamsungPayPaymentFlowsPrivatePaymentMethodsSamsungPayPaymentMethodOptions",
    "PaymentMethodOptionsSatispay",
    "PaymentMethodOptionsSatispayPaymentMethodOptionsSatispay",
    "PaymentMethodOptionsSepaDebit",
    "PaymentMethodOptionsSepaDebitPaymentIntentPaymentMethodOptionsSepaDebit",
    "PaymentMethodOptionsSepaDebitPaymentIntentPaymentMethodOptionsSepaDebitMandateOptions",
    "PaymentMethodOptionsSofort",
    "PaymentMethodOptionsSofortPaymentMethodOptionsSofort",
    "PaymentMethodOptionsSwish",
    "PaymentMethodOptionsSwishPaymentIntentPaymentMethodOptionsSwish",
    "PaymentMethodOptionsTwint",
    "PaymentMethodOptionsTwintPaymentMethodOptionsTwint",
    "PaymentMethodOptionsUsBankAccount",
    "PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccount",
    "PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccountFinancialConnections",
    "PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters",
    "PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccountMandateOptions",
    "PaymentMethodOptionsWechatPay",
    "PaymentMethodOptionsWechatPayPaymentMethodOptionsWechatPay",
    "PaymentMethodOptionsZip",
    "PaymentMethodOptionsZipPaymentMethodOptionsZip",
    "Processing",
    "ProcessingCard",
    "ProcessingCardCustomerNotification",
    "Review",
]


class AmountDetailsPaymentFlowsAmountDetailsError(BaseModel):
    code: Optional[
        Literal["amount_details_amount_mismatch", "amount_details_tax_shipping_discount_greater_than_amount"]
    ] = None
    """The code of the error that occurred when validating the current amount details."""

    message: Optional[str] = None
    """A message providing more details about the error."""


class AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsCard(BaseModel):
    commodity_code: Optional[str] = None


class AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsCardPresent(BaseModel):
    commodity_code: Optional[str] = None


class AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsKlarna(BaseModel):
    image_url: Optional[str] = None

    product_url: Optional[str] = None

    reference: Optional[str] = None

    subscription_reference: Optional[str] = None


class AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsPaypal(BaseModel):
    category: Optional[Literal["digital_goods", "donation", "physical_goods"]] = None
    """Type of the line item."""

    description: Optional[str] = None
    """Description of the line item."""

    sold_by: Optional[str] = None
    """The Stripe account ID of the connected account that sells the item.

    This is only needed when using
    [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers).
    """


class AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptions(BaseModel):
    card: Optional[AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsCard] = None

    card_present: Optional[AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsCardPresent] = None

    klarna: Optional[AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsKlarna] = None

    paypal: Optional[AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptionsPaypal] = None


class AmountDetailsPaymentFlowsAmountDetailsLineItemsDataTax(BaseModel):
    total_tax_amount: int
    """
    The total amount of tax on the transaction represented in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    Required for L2 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the
    `amount_details[line_items][#][tax][total_tax_amount]` field.
    """


class AmountDetailsPaymentFlowsAmountDetailsLineItemsData(BaseModel):
    id: str
    """Unique identifier for the object."""

    object: Literal["payment_intent_amount_details_line_item"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    product_name: str
    """The product name of the line item.

    Required for L3 rates. At most 1024 characters long.

    For Cards, this field is truncated to 26 alphanumeric characters before being
    sent to the card networks. For Paypal, this field is truncated to 127
    characters.
    """

    quantity: int
    """The quantity of items. Required for L3 rates. An integer greater than 0."""

    unit_cost: int
    """
    The unit cost of the line item represented in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    Required for L3 rates. An integer greater than or equal to 0.
    """

    discount_amount: Optional[int] = None
    """
    The discount applied on this line item represented in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An
    integer greater than 0.

    This field is mutually exclusive with the `amount_details[discount_amount]`
    field.
    """

    payment_method_options: Optional[AmountDetailsPaymentFlowsAmountDetailsLineItemsDataPaymentMethodOptions] = None

    product_code: Optional[str] = None
    """The product code of the line item, such as an SKU.

    Required for L3 rates. At most 12 characters long.
    """

    tax: Optional[AmountDetailsPaymentFlowsAmountDetailsLineItemsDataTax] = None

    unit_of_measure: Optional[str] = None
    """A unit of measure for the line item, such as gallons, feet, meters, etc.

    Required for L3 rates. At most 12 alphanumeric characters long.
    """


class AmountDetailsPaymentFlowsAmountDetailsLineItems(BaseModel):
    """
    A list of line items, each containing information about a product in the PaymentIntent. There is a maximum of 200 line items.
    """

    data: List[AmountDetailsPaymentFlowsAmountDetailsLineItemsData]
    """Details about each object."""

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


class AmountDetailsPaymentFlowsAmountDetailsShipping(BaseModel):
    amount: Optional[int] = None
    """
    If a physical good is being shipped, the cost of shipping represented in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An
    integer greater than or equal to 0.
    """

    from_postal_code: Optional[str] = None
    """
    If a physical good is being shipped, the postal code of where it is being
    shipped from. At most 10 alphanumeric characters long, hyphens are allowed.
    """

    to_postal_code: Optional[str] = None
    """
    If a physical good is being shipped, the postal code of where it is being
    shipped to. At most 10 alphanumeric characters long, hyphens are allowed.
    """


class AmountDetailsPaymentFlowsAmountDetailsTax(BaseModel):
    total_tax_amount: Optional[int] = None
    """
    The total amount of tax on the transaction represented in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    Required for L2 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the
    `amount_details[line_items][#][tax][total_tax_amount]` field.
    """


class AmountDetailsPaymentFlowsAmountDetailsTip(BaseModel):
    amount: Optional[int] = None
    """Portion of the amount that corresponds to a tip."""


class AmountDetailsPaymentFlowsAmountDetails(BaseModel):
    discount_amount: Optional[int] = None
    """
    The total discount applied on the transaction represented in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An
    integer greater than 0.

    This field is mutually exclusive with the
    `amount_details[line_items][#][discount_amount]` field.
    """

    error: Optional[AmountDetailsPaymentFlowsAmountDetailsError] = None

    line_items: Optional[AmountDetailsPaymentFlowsAmountDetailsLineItems] = None
    """
    A list of line items, each containing information about a product in the
    PaymentIntent. There is a maximum of 200 line items.
    """

    shipping: Optional[AmountDetailsPaymentFlowsAmountDetailsShipping] = None

    tax: Optional[AmountDetailsPaymentFlowsAmountDetailsTax] = None

    tip: Optional[AmountDetailsPaymentFlowsAmountDetailsTip] = None


class AmountDetailsPaymentFlowsAmountDetailsClientTip(BaseModel):
    amount: Optional[int] = None
    """Portion of the amount that corresponds to a tip."""


class AmountDetailsPaymentFlowsAmountDetailsClient(BaseModel):
    tip: Optional[AmountDetailsPaymentFlowsAmountDetailsClientTip] = None


AmountDetails: TypeAlias = Union[AmountDetailsPaymentFlowsAmountDetails, AmountDetailsPaymentFlowsAmountDetailsClient]

Application: TypeAlias = Union[str, application.Application, None]


class AutomaticPaymentMethods(BaseModel):
    enabled: bool
    """Automatically calculates compatible payment methods"""

    allow_redirects: Optional[Literal["always", "never"]] = None
    """Controls whether this PaymentIntent will accept redirect-based payment methods.

    Redirect-based payment methods may require your customer to be redirected to a
    payment method's app or site for authentication or additional steps. To
    [confirm](https://docs.stripe.com/api/payment_intents/confirm) this
    PaymentIntent, you may be required to provide a `return_url` to redirect
    customers back to your site after they authenticate or complete the payment.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer", DeletedCustomer, None])
else:
    Customer: TypeAlias = Union[str, "customer.Customer", DeletedCustomer, None]


class HooksInputsTax(BaseModel):
    calculation: str
    """The [TaxCalculation](https://docs.stripe.com/api/tax/calculations) id"""


class HooksInputs(BaseModel):
    tax: Optional[HooksInputsTax] = None


class Hooks(BaseModel):
    inputs: Optional[HooksInputs] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    LatestCharge = TypeAliasType("LatestCharge", Union[str, "Charge", None])
else:
    LatestCharge: TypeAlias = Union[str, "Charge", None]


class NextActionAlipayHandleRedirect(BaseModel):
    native_data: Optional[str] = None
    """
    The native data to be used with Alipay SDK you must redirect your customer to in
    order to authenticate the payment in an Android App.
    """

    native_url: Optional[str] = None
    """
    The native URL you must redirect your customer to in order to authenticate the
    payment in an iOS App.
    """

    return_url: Optional[str] = None
    """
    If the customer does not exit their browser while authenticating, they will be
    redirected to this specified URL after completion.
    """

    url: Optional[str] = None
    """
    The URL you must redirect your customer to in order to authenticate the payment.
    """


class NextActionBoletoDisplayDetails(BaseModel):
    expires_at: Optional[int] = None
    """The timestamp after which the boleto expires."""

    hosted_voucher_url: Optional[str] = None
    """
    The URL to the hosted boleto voucher page, which allows customers to view the
    boleto voucher.
    """

    number: Optional[str] = None
    """The boleto number."""

    pdf: Optional[str] = None
    """The URL to the downloadable boleto voucher PDF."""


class NextActionCardAwaitNotification(BaseModel):
    charge_attempt_at: Optional[int] = None
    """The time that payment will be attempted.

    If customer approval is required, they need to provide approval before this
    time.
    """

    customer_approval_required: Optional[bool] = None
    """
    For payments greater than INR 15000, the customer must provide explicit approval
    of the payment with their bank. For payments of lower amount, no customer action
    is required.
    """


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


class NextActionDisplayBankTransferInstructionsFinancialAddressAba(BaseModel):
    """ABA Records contain U.S. bank account details per the ABA format."""

    account_holder_address: Address

    account_holder_name: str
    """The account holder name"""

    account_number: str
    """The ABA account number"""

    account_type: str
    """The account type"""

    bank_address: Address

    bank_name: str
    """The bank name"""

    routing_number: str
    """The ABA routing number"""


class NextActionDisplayBankTransferInstructionsFinancialAddressIban(BaseModel):
    """Iban Records contain E.U. bank account details per the SEPA format."""

    account_holder_address: Address

    account_holder_name: str
    """The name of the person or business that owns the bank account"""

    bank_address: Address

    bic: str
    """The BIC/SWIFT code of the account."""

    country: str
    """
    Two-letter country code
    ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """

    iban: str
    """The IBAN of the account."""


class NextActionDisplayBankTransferInstructionsFinancialAddressSortCode(BaseModel):
    """Sort Code Records contain U.K. bank account details per the sort code format."""

    account_holder_address: Address

    account_holder_name: str
    """The name of the person or business that owns the bank account"""

    account_number: str
    """The account number"""

    bank_address: Address

    sort_code: str
    """The six-digit sort code"""


class NextActionDisplayBankTransferInstructionsFinancialAddressSpei(BaseModel):
    """SPEI Records contain Mexico bank account details per the SPEI format."""

    account_holder_address: Address

    account_holder_name: str
    """The account holder name"""

    bank_address: Address

    bank_code: str
    """The three-digit bank code"""

    bank_name: str
    """The short banking institution name"""

    clabe: str
    """The CLABE number"""


class NextActionDisplayBankTransferInstructionsFinancialAddressSwift(BaseModel):
    """SWIFT Records contain U.S. bank account details per the SWIFT format."""

    account_holder_address: Address

    account_holder_name: str
    """The account holder name"""

    account_number: str
    """The account number"""

    account_type: str
    """The account type"""

    bank_address: Address

    bank_name: str
    """The bank name"""

    swift_code: str
    """The SWIFT code"""


class NextActionDisplayBankTransferInstructionsFinancialAddressZengin(BaseModel):
    """Zengin Records contain Japan bank account details per the Zengin format."""

    account_holder_address: Address

    bank_address: Address

    account_holder_name: Optional[str] = None
    """The account holder name"""

    account_number: Optional[str] = None
    """The account number"""

    account_type: Optional[str] = None
    """The bank account type. In Japan, this can only be `futsu` or `toza`."""

    bank_code: Optional[str] = None
    """The bank code of the account"""

    bank_name: Optional[str] = None
    """The bank name of the account"""

    branch_code: Optional[str] = None
    """The branch code of the account"""

    branch_name: Optional[str] = None
    """The branch name of the account"""


class NextActionDisplayBankTransferInstructionsFinancialAddress(BaseModel):
    """
    FinancialAddresses contain identifying information that resolves to a FinancialAccount.
    """

    type: Literal["aba", "iban", "sort_code", "spei", "swift", "zengin"]
    """The type of financial address"""

    aba: Optional[NextActionDisplayBankTransferInstructionsFinancialAddressAba] = None
    """ABA Records contain U.S. bank account details per the ABA format."""

    iban: Optional[NextActionDisplayBankTransferInstructionsFinancialAddressIban] = None
    """Iban Records contain E.U. bank account details per the SEPA format."""

    sort_code: Optional[NextActionDisplayBankTransferInstructionsFinancialAddressSortCode] = None
    """Sort Code Records contain U.K. bank account details per the sort code format."""

    spei: Optional[NextActionDisplayBankTransferInstructionsFinancialAddressSpei] = None
    """SPEI Records contain Mexico bank account details per the SPEI format."""

    supported_networks: Optional[
        List[Literal["ach", "bacs", "domestic_wire_us", "fps", "sepa", "spei", "swift", "zengin"]]
    ] = None
    """The payment networks supported by this FinancialAddress"""

    swift: Optional[NextActionDisplayBankTransferInstructionsFinancialAddressSwift] = None
    """SWIFT Records contain U.S. bank account details per the SWIFT format."""

    zengin: Optional[NextActionDisplayBankTransferInstructionsFinancialAddressZengin] = None
    """Zengin Records contain Japan bank account details per the Zengin format."""


class NextActionDisplayBankTransferInstructions(BaseModel):
    type: Literal["eu_bank_transfer", "gb_bank_transfer", "jp_bank_transfer", "mx_bank_transfer", "us_bank_transfer"]
    """Type of bank transfer"""

    amount_remaining: Optional[int] = None
    """The remaining amount that needs to be transferred to complete the payment."""

    currency: Optional[str] = None
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    financial_addresses: Optional[List[NextActionDisplayBankTransferInstructionsFinancialAddress]] = None
    """A list of financial addresses that can be used to fund the customer balance"""

    hosted_instructions_url: Optional[str] = None
    """
    A link to a hosted page that guides your customer through completing the
    transfer.
    """

    reference: Optional[str] = None
    """A string identifying this payment.

    Instruct your customer to include this code in the reference or memo field of
    their bank transfer.
    """


class NextActionKonbiniDisplayDetailsStoresFamilymart(BaseModel):
    payment_code: str
    """The payment code."""

    confirmation_number: Optional[str] = None
    """The confirmation number."""


class NextActionKonbiniDisplayDetailsStoresLawson(BaseModel):
    payment_code: str
    """The payment code."""

    confirmation_number: Optional[str] = None
    """The confirmation number."""


class NextActionKonbiniDisplayDetailsStoresMinistop(BaseModel):
    payment_code: str
    """The payment code."""

    confirmation_number: Optional[str] = None
    """The confirmation number."""


class NextActionKonbiniDisplayDetailsStoresSeicomart(BaseModel):
    payment_code: str
    """The payment code."""

    confirmation_number: Optional[str] = None
    """The confirmation number."""


class NextActionKonbiniDisplayDetailsStores(BaseModel):
    familymart: Optional[NextActionKonbiniDisplayDetailsStoresFamilymart] = None

    lawson: Optional[NextActionKonbiniDisplayDetailsStoresLawson] = None

    ministop: Optional[NextActionKonbiniDisplayDetailsStoresMinistop] = None

    seicomart: Optional[NextActionKonbiniDisplayDetailsStoresSeicomart] = None


class NextActionKonbiniDisplayDetails(BaseModel):
    expires_at: int
    """The timestamp at which the pending Konbini payment expires."""

    stores: NextActionKonbiniDisplayDetailsStores

    hosted_voucher_url: Optional[str] = None
    """
    The URL for the Konbini payment instructions page, which allows customers to
    view and print a Konbini voucher.
    """


class NextActionMultibancoDisplayDetails(BaseModel):
    entity: Optional[str] = None
    """Entity number associated with this Multibanco payment."""

    expires_at: Optional[int] = None
    """The timestamp at which the Multibanco voucher expires."""

    hosted_voucher_url: Optional[str] = None
    """
    The URL for the hosted Multibanco voucher page, which allows customers to view a
    Multibanco voucher.
    """

    reference: Optional[str] = None
    """Reference number associated with this Multibanco payment."""


class NextActionOxxoDisplayDetails(BaseModel):
    expires_after: Optional[int] = None
    """The timestamp after which the OXXO voucher expires."""

    hosted_voucher_url: Optional[str] = None
    """
    The URL for the hosted OXXO voucher page, which allows customers to view and
    print an OXXO voucher.
    """

    number: Optional[str] = None
    """OXXO reference number."""


class NextActionPaynowDisplayQrCode(BaseModel):
    data: str
    """
    The raw data string used to generate QR code, it should be used together with QR
    code library.
    """

    image_url_png: str
    """The image_url_png string used to render QR code"""

    image_url_svg: str
    """The image_url_svg string used to render QR code"""

    hosted_instructions_url: Optional[str] = None
    """
    The URL to the hosted PayNow instructions page, which allows customers to view
    the PayNow QR code.
    """


class NextActionPixDisplayQrCode(BaseModel):
    data: Optional[str] = None
    """
    The raw data string used to generate QR code, it should be used together with QR
    code library.
    """

    expires_at: Optional[int] = None
    """The date (unix timestamp) when the PIX expires."""

    hosted_instructions_url: Optional[str] = None
    """
    The URL to the hosted pix instructions page, which allows customers to view the
    pix QR code.
    """

    image_url_png: Optional[str] = None
    """The image_url_png string used to render png QR code"""

    image_url_svg: Optional[str] = None
    """The image_url_svg string used to render svg QR code"""


class NextActionPromptpayDisplayQrCode(BaseModel):
    data: str
    """
    The raw data string used to generate QR code, it should be used together with QR
    code library.
    """

    hosted_instructions_url: str
    """
    The URL to the hosted PromptPay instructions page, which allows customers to
    view the PromptPay QR code.
    """

    image_url_png: str
    """
    The PNG path used to render the QR code, can be used as the source in an HTML
    img tag
    """

    image_url_svg: str
    """
    The SVG path used to render the QR code, can be used as the source in an HTML
    img tag
    """


class NextActionRedirectToURL(BaseModel):
    return_url: Optional[str] = None
    """
    If the customer does not exit their browser while authenticating, they will be
    redirected to this specified URL after completion.
    """

    url: Optional[str] = None
    """
    The URL you must redirect your customer to in order to authenticate the payment.
    """


class NextActionSwishHandleRedirectOrDisplayQrCodeQrCode(BaseModel):
    data: str
    """
    The raw data string used to generate QR code, it should be used together with QR
    code library.
    """

    image_url_png: str
    """The image_url_png string used to render QR code"""

    image_url_svg: str
    """The image_url_svg string used to render QR code"""


class NextActionSwishHandleRedirectOrDisplayQrCode(BaseModel):
    hosted_instructions_url: str
    """
    The URL to the hosted Swish instructions page, which allows customers to view
    the QR code.
    """

    qr_code: NextActionSwishHandleRedirectOrDisplayQrCodeQrCode


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


class NextActionWechatPayDisplayQrCode(BaseModel):
    data: str
    """The data being used to generate QR code"""

    hosted_instructions_url: str
    """
    The URL to the hosted WeChat Pay instructions page, which allows customers to
    view the WeChat Pay QR code.
    """

    image_data_url: str
    """The base64 image data for a pre-generated QR code"""

    image_url_png: str
    """The image_url_png string used to render QR code"""

    image_url_svg: str
    """The image_url_svg string used to render QR code"""


class NextActionWechatPayRedirectToAndroidApp(BaseModel):
    app_id: str
    """app_id is the APP ID registered on WeChat open platform"""

    nonce_str: str
    """nonce_str is a random string"""

    package: str
    """package is static value"""

    partner_id: str
    """an unique merchant ID assigned by WeChat Pay"""

    prepay_id: str
    """an unique trading ID assigned by WeChat Pay"""

    sign: str
    """A signature"""

    timestamp: str
    """Specifies the current time in epoch format"""


class NextActionWechatPayRedirectToIosApp(BaseModel):
    native_url: str
    """An universal link that redirect to WeChat Pay app"""


class NextAction(BaseModel):
    type: str
    """Type of the next action to perform.

    Refer to the other child attributes under `next_action` for available values.
    Examples include: `redirect_to_url`, `use_stripe_sdk`, `alipay_handle_redirect`,
    `oxxo_display_details`, or `verify_with_microdeposits`.
    """

    alipay_handle_redirect: Optional[NextActionAlipayHandleRedirect] = None

    boleto_display_details: Optional[NextActionBoletoDisplayDetails] = None

    card_await_notification: Optional[NextActionCardAwaitNotification] = None

    cashapp_handle_redirect_or_display_qr_code: Optional[NextActionCashappHandleRedirectOrDisplayQrCode] = None

    display_bank_transfer_instructions: Optional[NextActionDisplayBankTransferInstructions] = None

    konbini_display_details: Optional[NextActionKonbiniDisplayDetails] = None

    multibanco_display_details: Optional[NextActionMultibancoDisplayDetails] = None

    oxxo_display_details: Optional[NextActionOxxoDisplayDetails] = None

    paynow_display_qr_code: Optional[NextActionPaynowDisplayQrCode] = None

    pix_display_qr_code: Optional[NextActionPixDisplayQrCode] = None

    promptpay_display_qr_code: Optional[NextActionPromptpayDisplayQrCode] = None

    redirect_to_url: Optional[NextActionRedirectToURL] = None

    swish_handle_redirect_or_display_qr_code: Optional[NextActionSwishHandleRedirectOrDisplayQrCode] = None

    use_stripe_sdk: Optional[object] = None
    """
    When confirming a PaymentIntent with Stripe.js, Stripe.js depends on the
    contents of this dictionary to invoke authentication flows. The shape of the
    contents is subject to change and is only intended to be used by Stripe.js.
    """

    verify_with_microdeposits: Optional[NextActionVerifyWithMicrodeposits] = None

    wechat_pay_display_qr_code: Optional[NextActionWechatPayDisplayQrCode] = None

    wechat_pay_redirect_to_android_app: Optional[NextActionWechatPayRedirectToAndroidApp] = None

    wechat_pay_redirect_to_ios_app: Optional[NextActionWechatPayRedirectToIosApp] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    OnBehalfOf = TypeAliasType("OnBehalfOf", Union[str, "Account", None])
else:
    OnBehalfOf: TypeAlias = Union[str, "Account", None]


class PaymentDetails(BaseModel):
    customer_reference: Optional[str] = None
    """A unique value to identify the customer.

    This field is available only for card payments.

    This field is truncated to 25 alphanumeric characters, excluding spaces, before
    being sent to card networks.
    """

    order_reference: Optional[str] = None
    """A unique value assigned by the business to identify the transaction.

    Required for L2 and L3 rates.

    Required when the Payment Method Types array contains `card`, including when
    [automatic_payment_methods.enabled](/api/payment_intents/create#create_payment_intent-automatic_payment_methods-enabled)
    is set to `true`.

    For Cards, this field is truncated to 25 alphanumeric characters, excluding
    spaces, before being sent to card networks. For Klarna, this field is truncated
    to 255 characters and is visible to customers when they view the order in the
    Klarna app.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    PaymentMethod = TypeAliasType("PaymentMethod", Union[str, "payment_method.PaymentMethod", None])
else:
    PaymentMethod: TypeAlias = Union[str, "payment_method.PaymentMethod", None]


class PaymentMethodConfigurationDetails(BaseModel):
    id: str
    """ID of the payment method configuration used."""

    parent: Optional[str] = None
    """ID of the parent payment method configuration used."""


class PaymentMethodOptionsAcssDebitPaymentIntentPaymentMethodOptionsAcssDebitMandateOptions(BaseModel):
    custom_mandate_url: Optional[str] = None
    """A URL for custom mandate text"""

    interval_description: Optional[str] = None
    """Description of the interval.

    Only required if the 'payment_schedule' parameter is 'interval' or 'combined'.
    """

    payment_schedule: Optional[Literal["combined", "interval", "sporadic"]] = None
    """Payment schedule for the mandate."""

    transaction_type: Optional[Literal["business", "personal"]] = None
    """Transaction type of the mandate."""


class PaymentMethodOptionsAcssDebitPaymentIntentPaymentMethodOptionsAcssDebit(BaseModel):
    mandate_options: Optional[PaymentMethodOptionsAcssDebitPaymentIntentPaymentMethodOptionsAcssDebitMandateOptions] = (
        None
    )

    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """

    target_date: Optional[str] = None
    """Controls when Stripe will attempt to debit the funds from the customer's
    account.

    The date must be a string in YYYY-MM-DD format. The date must be in the future
    and between 3 and 15 calendar days from now.
    """

    verification_method: Optional[Literal["automatic", "instant", "microdeposits"]] = None
    """Bank account verification method."""


PaymentMethodOptionsAcssDebit: TypeAlias = Union[
    PaymentMethodOptionsAcssDebitPaymentIntentPaymentMethodOptionsAcssDebit,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsAffirmPaymentMethodOptionsAffirm(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    preferred_locale: Optional[str] = None
    """
    Preferred language of the Affirm authorization page that the customer is
    redirected to.
    """

    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsAffirm: TypeAlias = Union[
    PaymentMethodOptionsAffirmPaymentMethodOptionsAffirm, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsAfterpayClearpayPaymentMethodOptionsAfterpayClearpay(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    reference: Optional[str] = None
    """An internal identifier or reference that this payment corresponds to.

    You must limit the identifier to 128 characters, and it can only contain
    letters, numbers, underscores, backslashes, and dashes. This field differs from
    the statement descriptor and item name.
    """

    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsAfterpayClearpay: TypeAlias = Union[
    PaymentMethodOptionsAfterpayClearpayPaymentMethodOptionsAfterpayClearpay,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsAlipayPaymentMethodOptionsAlipay(BaseModel):
    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsAlipay: TypeAlias = Union[
    PaymentMethodOptionsAlipayPaymentMethodOptionsAlipay, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsAlmaPaymentMethodOptionsAlma(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""


PaymentMethodOptionsAlma: TypeAlias = Union[
    PaymentMethodOptionsAlmaPaymentMethodOptionsAlma, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsAmazonPayPaymentMethodOptionsAmazonPay(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsAmazonPay: TypeAlias = Union[
    PaymentMethodOptionsAmazonPayPaymentMethodOptionsAmazonPay, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsAuBecsDebitPaymentIntentPaymentMethodOptionsAuBecsDebit(BaseModel):
    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """

    target_date: Optional[str] = None
    """Controls when Stripe will attempt to debit the funds from the customer's
    account.

    The date must be a string in YYYY-MM-DD format. The date must be in the future
    and between 3 and 15 calendar days from now.
    """


PaymentMethodOptionsAuBecsDebit: TypeAlias = Union[
    PaymentMethodOptionsAuBecsDebitPaymentIntentPaymentMethodOptionsAuBecsDebit,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsBacsDebitPaymentIntentPaymentMethodOptionsBacsDebitMandateOptions(BaseModel):
    reference_prefix: Optional[str] = None
    """Prefix used to generate the Mandate reference.

    Must be at most 12 characters long. Must consist of only uppercase letters,
    numbers, spaces, or the following special characters: '/', '\\__', '-', '&', '.'.
    Cannot begin with 'DDIC' or 'STRIPE'.
    """


class PaymentMethodOptionsBacsDebitPaymentIntentPaymentMethodOptionsBacsDebit(BaseModel):
    mandate_options: Optional[PaymentMethodOptionsBacsDebitPaymentIntentPaymentMethodOptionsBacsDebitMandateOptions] = (
        None
    )

    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """

    target_date: Optional[str] = None
    """Controls when Stripe will attempt to debit the funds from the customer's
    account.

    The date must be a string in YYYY-MM-DD format. The date must be in the future
    and between 3 and 15 calendar days from now.
    """


PaymentMethodOptionsBacsDebit: TypeAlias = Union[
    PaymentMethodOptionsBacsDebitPaymentIntentPaymentMethodOptionsBacsDebit,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsBancontactPaymentMethodOptionsBancontact(BaseModel):
    preferred_language: Literal["de", "en", "fr", "nl"]
    """
    Preferred language of the Bancontact authorization page that the customer is
    redirected to.
    """

    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsBancontact: TypeAlias = Union[
    PaymentMethodOptionsBancontactPaymentMethodOptionsBancontact, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsBilliePaymentMethodOptionsBillie(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""


PaymentMethodOptionsBillie: TypeAlias = Union[
    PaymentMethodOptionsBilliePaymentMethodOptionsBillie, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsBlikPaymentIntentPaymentMethodOptionsBlik(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsBlik: TypeAlias = Union[
    PaymentMethodOptionsBlikPaymentIntentPaymentMethodOptionsBlik, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsBoletoPaymentMethodOptionsBoleto(BaseModel):
    expires_after_days: int
    """The number of calendar days before a Boleto voucher expires.

    For example, if you create a Boleto voucher on Monday and you set
    expires_after_days to 2, the Boleto voucher will expire on Wednesday at 23:59
    America/Sao_Paulo time.
    """

    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsBoleto: TypeAlias = Union[
    PaymentMethodOptionsBoletoPaymentMethodOptionsBoleto, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsCardPaymentIntentPaymentMethodOptionsCardInstallments(BaseModel):
    enabled: bool
    """Whether Installments are enabled for this PaymentIntent."""

    available_plans: Optional[List[PaymentMethodDetailsCardInstallmentsPlan]] = None
    """Installment plans that may be selected for this PaymentIntent."""

    plan: Optional[PaymentMethodDetailsCardInstallmentsPlan] = None


class PaymentMethodOptionsCardPaymentIntentPaymentMethodOptionsCardMandateOptions(BaseModel):
    amount: int
    """Amount to be charged for future payments."""

    amount_type: Literal["fixed", "maximum"]
    """One of `fixed` or `maximum`.

    If `fixed`, the `amount` param refers to the exact amount to be charged in
    future payments. If `maximum`, the amount charged can be up to the value passed
    for the `amount` param.
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


class PaymentMethodOptionsCardPaymentIntentPaymentMethodOptionsCard(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    installments: Optional[PaymentMethodOptionsCardPaymentIntentPaymentMethodOptionsCardInstallments] = None

    mandate_options: Optional[PaymentMethodOptionsCardPaymentIntentPaymentMethodOptionsCardMandateOptions] = None

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
    """Selected network to process this payment intent on.

    Depends on the available networks of the card attached to the payment intent.
    Can be only set confirm-time.
    """

    request_extended_authorization: Optional[Literal["if_available", "never"]] = None
    """
    Request ability to
    [capture beyond the standard authorization validity window](https://docs.stripe.com/payments/extended-authorization)
    for this PaymentIntent.
    """

    request_incremental_authorization: Optional[Literal["if_available", "never"]] = None
    """
    Request ability to
    [increment the authorization](https://docs.stripe.com/payments/incremental-authorization)
    for this PaymentIntent.
    """

    request_multicapture: Optional[Literal["if_available", "never"]] = None
    """
    Request ability to make
    [multiple captures](https://docs.stripe.com/payments/multicapture) for this
    PaymentIntent.
    """

    request_overcapture: Optional[Literal["if_available", "never"]] = None
    """
    Request ability to [overcapture](https://docs.stripe.com/payments/overcapture)
    for this PaymentIntent.
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

    require_cvc_recollection: Optional[bool] = None
    """
    When enabled, using a card that is attached to a customer will require the CVC
    to be provided again (i.e. using the cvc_token parameter).
    """

    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """

    statement_descriptor_suffix_kana: Optional[str] = None
    """Provides information about a card payment that customers see on their
    statements.

    Concatenated with the Kana prefix (shortened Kana descriptor) or Kana statement
    descriptor that’s set on the account to form the complete statement descriptor.
    Maximum 22 characters. On card statements, the _concatenation_ of both prefix
    and suffix (including separators) will appear truncated to 22 characters.
    """

    statement_descriptor_suffix_kanji: Optional[str] = None
    """Provides information about a card payment that customers see on their
    statements.

    Concatenated with the Kanji prefix (shortened Kanji descriptor) or Kanji
    statement descriptor that’s set on the account to form the complete statement
    descriptor. Maximum 17 characters. On card statements, the _concatenation_ of
    both prefix and suffix (including separators) will appear truncated to 17
    characters.
    """


PaymentMethodOptionsCard: TypeAlias = Union[
    PaymentMethodOptionsCardPaymentIntentPaymentMethodOptionsCard, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsCardPresentPaymentMethodOptionsCardPresent(BaseModel):
    capture_method: Optional[Literal["manual", "manual_preferred"]] = None
    """Controls when the funds will be captured from the customer's account."""

    request_extended_authorization: Optional[bool] = None
    """
    Request ability to capture this payment beyond the standard
    [authorization validity window](https://docs.stripe.com/terminal/features/extended-authorizations#authorization-validity)
    """

    request_incremental_authorization_support: Optional[bool] = None
    """
    Request ability to
    [increment](https://docs.stripe.com/terminal/features/incremental-authorizations)
    this PaymentIntent if the combination of MCC and card brand is eligible. Check
    [incremental_authorization_supported](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported)
    in the [Confirm](https://docs.stripe.com/api/payment_intents/confirm) response
    to verify support.
    """

    routing: Optional[PaymentMethodOptionsCardPresentRouting] = None


PaymentMethodOptionsCardPresent: TypeAlias = Union[
    PaymentMethodOptionsCardPresentPaymentMethodOptionsCardPresent, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsCashappPaymentMethodOptionsCashapp(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsCashapp: TypeAlias = Union[
    PaymentMethodOptionsCashappPaymentMethodOptionsCashapp, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsCryptoPaymentMethodOptionsCrypto(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsCrypto: TypeAlias = Union[
    PaymentMethodOptionsCryptoPaymentMethodOptionsCrypto, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsCustomerBalancePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(BaseModel):
    country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]
    """The desired country code of the bank account information.

    Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
    """


class PaymentMethodOptionsCustomerBalancePaymentMethodOptionsCustomerBalanceBankTransfer(BaseModel):
    eu_bank_transfer: Optional[
        PaymentMethodOptionsCustomerBalancePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer
    ] = None

    requested_address_types: Optional[List[Literal["aba", "iban", "sepa", "sort_code", "spei", "swift", "zengin"]]] = (
        None
    )
    """
    List of address types that should be returned in the financial_addresses
    response. If not specified, all valid types will be returned.

    Permitted values include: `sort_code`, `zengin`, `iban`, or `spei`.
    """

    type: Optional[
        Literal["eu_bank_transfer", "gb_bank_transfer", "jp_bank_transfer", "mx_bank_transfer", "us_bank_transfer"]
    ] = None
    """
    The bank transfer type that this PaymentIntent is allowed to use for funding
    Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`,
    `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
    """


class PaymentMethodOptionsCustomerBalancePaymentMethodOptionsCustomerBalance(BaseModel):
    bank_transfer: Optional[PaymentMethodOptionsCustomerBalancePaymentMethodOptionsCustomerBalanceBankTransfer] = None

    funding_type: Optional[Literal["bank_transfer"]] = None
    """
    The funding method type to be used when there are not enough funds in the
    customer balance. Permitted values include: `bank_transfer`.
    """

    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsCustomerBalance: TypeAlias = Union[
    PaymentMethodOptionsCustomerBalancePaymentMethodOptionsCustomerBalance,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsEpsPaymentIntentPaymentMethodOptionsEps(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsEps: TypeAlias = Union[
    PaymentMethodOptionsEpsPaymentIntentPaymentMethodOptionsEps, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsFpxPaymentMethodOptionsFpx(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsFpx: TypeAlias = Union[
    PaymentMethodOptionsFpxPaymentMethodOptionsFpx, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsGiropayPaymentMethodOptionsGiropay(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsGiropay: TypeAlias = Union[
    PaymentMethodOptionsGiropayPaymentMethodOptionsGiropay, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsGrabpayPaymentMethodOptionsGrabpay(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsGrabpay: TypeAlias = Union[
    PaymentMethodOptionsGrabpayPaymentMethodOptionsGrabpay, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsIdealPaymentMethodOptionsIdeal(BaseModel):
    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsIdeal: TypeAlias = Union[
    PaymentMethodOptionsIdealPaymentMethodOptionsIdeal, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]

PaymentMethodOptionsInteracPresent: TypeAlias = Union[PaymentIntentTypeSpecificPaymentMethodOptionsClient, object]


class PaymentMethodOptionsKakaoPayPaymentFlowsPrivatePaymentMethodsKakaoPayPaymentMethodOptions(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsKakaoPay: TypeAlias = Union[
    PaymentMethodOptionsKakaoPayPaymentFlowsPrivatePaymentMethodsKakaoPayPaymentMethodOptions,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsKlarnaPaymentMethodOptionsKlarna(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    preferred_locale: Optional[str] = None
    """
    Preferred locale of the Klarna checkout page that the customer is redirected to.
    """

    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsKlarna: TypeAlias = Union[
    PaymentMethodOptionsKlarnaPaymentMethodOptionsKlarna, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsKonbiniPaymentMethodOptionsKonbini(BaseModel):
    confirmation_number: Optional[str] = None
    """
    An optional 10 to 11 digit numeric-only string determining the confirmation code
    at applicable convenience stores.
    """

    expires_after_days: Optional[int] = None
    """
    The number of calendar days (between 1 and 60) after which Konbini payment
    instructions will expire. For example, if a PaymentIntent is confirmed with
    Konbini and `expires_after_days` set to 2 on Monday JST, the instructions will
    expire on Wednesday 23:59:59 JST.
    """

    expires_at: Optional[int] = None
    """The timestamp at which the Konbini payment instructions will expire.

    Only one of `expires_after_days` or `expires_at` may be set.
    """

    product_description: Optional[str] = None
    """
    A product descriptor of up to 22 characters, which will appear to customers at
    the convenience store.
    """

    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsKonbini: TypeAlias = Union[
    PaymentMethodOptionsKonbiniPaymentMethodOptionsKonbini, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsKrCardPaymentMethodOptionsKrCard(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsKrCard: TypeAlias = Union[
    PaymentMethodOptionsKrCardPaymentMethodOptionsKrCard, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsLinkPaymentIntentPaymentMethodOptionsLink(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsLink: TypeAlias = Union[
    PaymentMethodOptionsLinkPaymentIntentPaymentMethodOptionsLink, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsMBWayPaymentMethodOptionsMBWay(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsMBWay: TypeAlias = Union[
    PaymentMethodOptionsMBWayPaymentMethodOptionsMBWay, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsMobilepayPaymentIntentPaymentMethodOptionsMobilepay(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsMobilepay: TypeAlias = Union[
    PaymentMethodOptionsMobilepayPaymentIntentPaymentMethodOptionsMobilepay,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsMultibancoPaymentMethodOptionsMultibanco(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsMultibanco: TypeAlias = Union[
    PaymentMethodOptionsMultibancoPaymentMethodOptionsMultibanco, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsNaverPayPaymentFlowsPrivatePaymentMethodsNaverPayPaymentMethodOptions(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsNaverPay: TypeAlias = Union[
    PaymentMethodOptionsNaverPayPaymentFlowsPrivatePaymentMethodsNaverPayPaymentMethodOptions,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsNzBankAccountPaymentIntentPaymentMethodOptionsNzBankAccount(BaseModel):
    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """

    target_date: Optional[str] = None
    """Controls when Stripe will attempt to debit the funds from the customer's
    account.

    The date must be a string in YYYY-MM-DD format. The date must be in the future
    and between 3 and 15 calendar days from now.
    """


PaymentMethodOptionsNzBankAccount: TypeAlias = Union[
    PaymentMethodOptionsNzBankAccountPaymentIntentPaymentMethodOptionsNzBankAccount,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsOxxoPaymentMethodOptionsOxxo(BaseModel):
    expires_after_days: int
    """The number of calendar days before an OXXO invoice expires.

    For example, if you create an OXXO invoice on Monday and you set
    expires_after_days to 2, the OXXO invoice will expire on Wednesday at 23:59
    America/Mexico_City time.
    """

    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsOxxo: TypeAlias = Union[
    PaymentMethodOptionsOxxoPaymentMethodOptionsOxxo, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsP24PaymentMethodOptionsP24(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsP24: TypeAlias = Union[
    PaymentMethodOptionsP24PaymentMethodOptionsP24, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]

PaymentMethodOptionsPayByBank: TypeAlias = Union[PaymentIntentTypeSpecificPaymentMethodOptionsClient, object]


class PaymentMethodOptionsPaycoPaymentFlowsPrivatePaymentMethodsPaycoPaymentMethodOptions(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""


PaymentMethodOptionsPayco: TypeAlias = Union[
    PaymentMethodOptionsPaycoPaymentFlowsPrivatePaymentMethodsPaycoPaymentMethodOptions,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsPaynowPaymentMethodOptionsPaynow(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsPaynow: TypeAlias = Union[
    PaymentMethodOptionsPaynowPaymentMethodOptionsPaynow, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsPaypalPaymentMethodOptionsPaypal(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    preferred_locale: Optional[str] = None
    """
    Preferred locale of the PayPal checkout page that the customer is redirected to.
    """

    reference: Optional[str] = None
    """
    A reference of the PayPal transaction visible to customer which is mapped to
    PayPal's invoice ID. This must be a globally unique ID if you have configured in
    your PayPal settings to block multiple payments per invoice ID.
    """

    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsPaypal: TypeAlias = Union[
    PaymentMethodOptionsPaypalPaymentMethodOptionsPaypal, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsPaytoPaymentIntentPaymentMethodOptionsPayto(BaseModel):
    mandate_options: Optional[PaymentIntentPaymentMethodOptionsMandateOptionsPayto] = None

    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsPayto: TypeAlias = Union[
    PaymentMethodOptionsPaytoPaymentIntentPaymentMethodOptionsPayto, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsPixPaymentMethodOptionsPix(BaseModel):
    amount_includes_iof: Optional[Literal["always", "never"]] = None
    """Determines if the amount includes the IOF tax."""

    expires_after_seconds: Optional[int] = None
    """
    The number of seconds (between 10 and 1209600) after which Pix payment will
    expire.
    """

    expires_at: Optional[int] = None
    """The timestamp at which the Pix expires."""

    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsPix: TypeAlias = Union[
    PaymentMethodOptionsPixPaymentMethodOptionsPix, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsPromptpayPaymentMethodOptionsPromptpay(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsPromptpay: TypeAlias = Union[
    PaymentMethodOptionsPromptpayPaymentMethodOptionsPromptpay, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsRevolutPayPaymentMethodOptionsRevolutPay(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsRevolutPay: TypeAlias = Union[
    PaymentMethodOptionsRevolutPayPaymentMethodOptionsRevolutPay, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsSamsungPayPaymentFlowsPrivatePaymentMethodsSamsungPayPaymentMethodOptions(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""


PaymentMethodOptionsSamsungPay: TypeAlias = Union[
    PaymentMethodOptionsSamsungPayPaymentFlowsPrivatePaymentMethodsSamsungPayPaymentMethodOptions,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsSatispayPaymentMethodOptionsSatispay(BaseModel):
    capture_method: Optional[Literal["manual"]] = None
    """Controls when the funds will be captured from the customer's account."""


PaymentMethodOptionsSatispay: TypeAlias = Union[
    PaymentMethodOptionsSatispayPaymentMethodOptionsSatispay, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsSepaDebitPaymentIntentPaymentMethodOptionsSepaDebitMandateOptions(BaseModel):
    reference_prefix: Optional[str] = None
    """Prefix used to generate the Mandate reference.

    Must be at most 12 characters long. Must consist of only uppercase letters,
    numbers, spaces, or the following special characters: '/', '\\__', '-', '&', '.'.
    Cannot begin with 'STRIPE'.
    """


class PaymentMethodOptionsSepaDebitPaymentIntentPaymentMethodOptionsSepaDebit(BaseModel):
    mandate_options: Optional[PaymentMethodOptionsSepaDebitPaymentIntentPaymentMethodOptionsSepaDebitMandateOptions] = (
        None
    )

    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """

    target_date: Optional[str] = None
    """Controls when Stripe will attempt to debit the funds from the customer's
    account.

    The date must be a string in YYYY-MM-DD format. The date must be in the future
    and between 3 and 15 calendar days from now.
    """


PaymentMethodOptionsSepaDebit: TypeAlias = Union[
    PaymentMethodOptionsSepaDebitPaymentIntentPaymentMethodOptionsSepaDebit,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsSofortPaymentMethodOptionsSofort(BaseModel):
    preferred_language: Optional[Literal["de", "en", "es", "fr", "it", "nl", "pl"]] = None
    """
    Preferred language of the SOFORT authorization page that the customer is
    redirected to.
    """

    setup_future_usage: Optional[Literal["none", "off_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsSofort: TypeAlias = Union[
    PaymentMethodOptionsSofortPaymentMethodOptionsSofort, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsSwishPaymentIntentPaymentMethodOptionsSwish(BaseModel):
    reference: Optional[str] = None
    """A reference for this payment to be displayed in the Swish app."""

    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsSwish: TypeAlias = Union[
    PaymentMethodOptionsSwishPaymentIntentPaymentMethodOptionsSwish, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsTwintPaymentMethodOptionsTwint(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsTwint: TypeAlias = Union[
    PaymentMethodOptionsTwintPaymentMethodOptionsTwint, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
    BaseModel
):
    account_subcategories: Optional[List[Literal["checking", "savings"]]] = None
    """The account subcategories to use to filter for possible accounts to link.

    Valid subcategories are `checking` and `savings`.
    """


class PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccountFinancialConnections(BaseModel):
    filters: Optional[
        PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters
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


class PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccountMandateOptions(BaseModel):
    collection_method: Optional[Literal["paper"]] = None
    """Mandate collection method"""


class PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccount(BaseModel):
    financial_connections: Optional[
        PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccountFinancialConnections
    ] = None

    mandate_options: Optional[
        PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccountMandateOptions
    ] = None

    setup_future_usage: Optional[Literal["none", "off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """

    target_date: Optional[str] = None
    """Controls when Stripe will attempt to debit the funds from the customer's
    account.

    The date must be a string in YYYY-MM-DD format. The date must be in the future
    and between 3 and 15 calendar days from now.
    """

    verification_method: Optional[Literal["automatic", "instant", "microdeposits"]] = None
    """Bank account verification method."""


PaymentMethodOptionsUsBankAccount: TypeAlias = Union[
    PaymentMethodOptionsUsBankAccountPaymentIntentPaymentMethodOptionsUsBankAccount,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
]


class PaymentMethodOptionsWechatPayPaymentMethodOptionsWechatPay(BaseModel):
    app_id: Optional[str] = None
    """The app ID registered with WeChat Pay.

    Only required when client is ios or android.
    """

    client: Optional[Literal["android", "ios", "web"]] = None
    """The client type that the end customer will pay from"""

    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsWechatPay: TypeAlias = Union[
    PaymentMethodOptionsWechatPayPaymentMethodOptionsWechatPay, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptionsZipPaymentMethodOptionsZip(BaseModel):
    setup_future_usage: Optional[Literal["none"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """


PaymentMethodOptionsZip: TypeAlias = Union[
    PaymentMethodOptionsZipPaymentMethodOptionsZip, PaymentIntentTypeSpecificPaymentMethodOptionsClient
]


class PaymentMethodOptions(BaseModel):
    acss_debit: Optional[PaymentMethodOptionsAcssDebit] = None

    affirm: Optional[PaymentMethodOptionsAffirm] = None

    afterpay_clearpay: Optional[PaymentMethodOptionsAfterpayClearpay] = None

    alipay: Optional[PaymentMethodOptionsAlipay] = None

    alma: Optional[PaymentMethodOptionsAlma] = None

    amazon_pay: Optional[PaymentMethodOptionsAmazonPay] = None

    au_becs_debit: Optional[PaymentMethodOptionsAuBecsDebit] = None

    bacs_debit: Optional[PaymentMethodOptionsBacsDebit] = None

    bancontact: Optional[PaymentMethodOptionsBancontact] = None

    billie: Optional[PaymentMethodOptionsBillie] = None

    blik: Optional[PaymentMethodOptionsBlik] = None

    boleto: Optional[PaymentMethodOptionsBoleto] = None

    card: Optional[PaymentMethodOptionsCard] = None

    card_present: Optional[PaymentMethodOptionsCardPresent] = None

    cashapp: Optional[PaymentMethodOptionsCashapp] = None

    crypto: Optional[PaymentMethodOptionsCrypto] = None

    customer_balance: Optional[PaymentMethodOptionsCustomerBalance] = None

    eps: Optional[PaymentMethodOptionsEps] = None

    fpx: Optional[PaymentMethodOptionsFpx] = None

    giropay: Optional[PaymentMethodOptionsGiropay] = None

    grabpay: Optional[PaymentMethodOptionsGrabpay] = None

    ideal: Optional[PaymentMethodOptionsIdeal] = None

    interac_present: Optional[PaymentMethodOptionsInteracPresent] = None

    kakao_pay: Optional[PaymentMethodOptionsKakaoPay] = None

    klarna: Optional[PaymentMethodOptionsKlarna] = None

    konbini: Optional[PaymentMethodOptionsKonbini] = None

    kr_card: Optional[PaymentMethodOptionsKrCard] = None

    link: Optional[PaymentMethodOptionsLink] = None

    mb_way: Optional[PaymentMethodOptionsMBWay] = None

    mobilepay: Optional[PaymentMethodOptionsMobilepay] = None

    multibanco: Optional[PaymentMethodOptionsMultibanco] = None

    naver_pay: Optional[PaymentMethodOptionsNaverPay] = None

    nz_bank_account: Optional[PaymentMethodOptionsNzBankAccount] = None

    oxxo: Optional[PaymentMethodOptionsOxxo] = None

    p24: Optional[PaymentMethodOptionsP24] = None

    pay_by_bank: Optional[PaymentMethodOptionsPayByBank] = None

    payco: Optional[PaymentMethodOptionsPayco] = None

    paynow: Optional[PaymentMethodOptionsPaynow] = None

    paypal: Optional[PaymentMethodOptionsPaypal] = None

    payto: Optional[PaymentMethodOptionsPayto] = None

    pix: Optional[PaymentMethodOptionsPix] = None

    promptpay: Optional[PaymentMethodOptionsPromptpay] = None

    revolut_pay: Optional[PaymentMethodOptionsRevolutPay] = None

    samsung_pay: Optional[PaymentMethodOptionsSamsungPay] = None

    satispay: Optional[PaymentMethodOptionsSatispay] = None

    sepa_debit: Optional[PaymentMethodOptionsSepaDebit] = None

    sofort: Optional[PaymentMethodOptionsSofort] = None

    swish: Optional[PaymentMethodOptionsSwish] = None

    twint: Optional[PaymentMethodOptionsTwint] = None

    us_bank_account: Optional[PaymentMethodOptionsUsBankAccount] = None

    wechat_pay: Optional[PaymentMethodOptionsWechatPay] = None

    zip: Optional[PaymentMethodOptionsZip] = None


class ProcessingCardCustomerNotification(BaseModel):
    approval_requested: Optional[bool] = None
    """Whether customer approval has been requested for this payment.

    For payments greater than INR 15000 or mandate amount, the customer must provide
    explicit approval of the payment with their bank.
    """

    completes_at: Optional[int] = None
    """
    If customer approval is required, they need to provide approval before this
    time.
    """


class ProcessingCard(BaseModel):
    customer_notification: Optional[ProcessingCardCustomerNotification] = None


class Processing(BaseModel):
    type: Literal["card"]
    """
    Type of the payment method for which payment is in `processing` state, one of
    `card`.
    """

    card: Optional[ProcessingCard] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    Review = TypeAliasType("Review", Union[str, "review.Review", None])
else:
    Review: TypeAlias = Union[str, "review.Review", None]


class PaymentIntent(BaseModel):
    """
    A PaymentIntent guides you through the process of collecting a payment from your customer.
    We recommend that you create exactly one PaymentIntent for each order or
    customer session in your system. You can reference the PaymentIntent later to
    see the history of payment attempts for a particular session.

    A PaymentIntent transitions through
    [multiple statuses](/payments/paymentintents/lifecycle)
    throughout its lifetime as it interfaces with Stripe.js to perform
    authentication flows and ultimately creates at most one successful charge.

    Related guide: [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
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

    object: Literal["payment_intent"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    status: Literal[
        "canceled",
        "processing",
        "requires_action",
        "requires_capture",
        "requires_confirmation",
        "requires_payment_method",
        "succeeded",
    ]
    """
    Status of this PaymentIntent, one of `requires_payment_method`,
    `requires_confirmation`, `requires_action`, `processing`, `requires_capture`,
    `canceled`, or `succeeded`. Read more about each PaymentIntent
    [status](https://docs.stripe.com/payments/intents#intent-statuses).
    """

    amount: Optional[int] = None
    """Amount intended to be collected by this PaymentIntent.

    A positive integer representing how much to charge in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal) (e.g.,
    100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The
    minimum amount is $0.50 US or
    [equivalent in charge currency](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts).
    The amount value supports up to eight digits (e.g., a value of 99999999 for a
    USD charge of $999,999.99).
    """

    amount_capturable: Optional[int] = None
    """Amount that can be captured from this PaymentIntent."""

    amount_details: Optional[AmountDetails] = None

    amount_received: Optional[int] = None
    """Amount that this PaymentIntent collects."""

    application: Optional[Application] = None
    """ID of the Connect application that created the PaymentIntent."""

    application_fee_amount: Optional[int] = None
    """
    The amount of the application fee (if any) that will be requested to be applied
    to the payment and transferred to the application owner's Stripe account. The
    amount of the application fee collected will be capped at the total amount
    captured. For more information, see the PaymentIntents
    [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """

    automatic_payment_methods: Optional[AutomaticPaymentMethods] = None

    canceled_at: Optional[int] = None
    """
    Populated when `status` is `canceled`, this is the time at which the
    PaymentIntent was canceled. Measured in seconds since the Unix epoch.
    """

    cancellation_reason: Optional[
        Literal[
            "abandoned",
            "automatic",
            "duplicate",
            "expired",
            "failed_invoice",
            "fraudulent",
            "requested_by_customer",
            "void_invoice",
        ]
    ] = None
    """
    Reason for cancellation of this PaymentIntent, either user-provided
    (`duplicate`, `fraudulent`, `requested_by_customer`, or `abandoned`) or
    generated by Stripe internally (`failed_invoice`, `void_invoice`, `automatic`,
    or `expired`).
    """

    capture_method: Optional[Literal["automatic", "automatic_async", "manual"]] = None
    """Controls when the funds will be captured from the customer's account."""

    client_secret: Optional[str] = None
    """The client secret of this PaymentIntent.

    Used for client-side retrieval using a publishable key.

    The client secret can be used to complete a payment from your frontend. It
    should not be stored, logged, or exposed to anyone other than the customer. Make
    sure that you have TLS enabled on any page that includes the client secret.

    Refer to our docs to
    [accept a payment](https://docs.stripe.com/payments/accept-a-payment?ui=elements)
    and learn about how `client_secret` should be handled.
    """

    confirmation_method: Optional[Literal["automatic", "manual"]] = None
    """
    Describes whether we can confirm this PaymentIntent automatically, or if it
    requires customer action to confirm the payment.
    """

    currency: Optional[str] = None
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: Optional[Customer] = None
    """ID of the Customer this PaymentIntent belongs to, if one exists.

    Payment methods attached to other Customers cannot be used with this
    PaymentIntent.

    If
    [setup_future_usage](https://api.stripe.com#payment_intent_object-setup_future_usage)
    is set and this PaymentIntent's payment method is not `card_present`, then the
    payment method attaches to the Customer after the PaymentIntent has been
    confirmed and any required actions from the user are complete. If the payment
    method is `card_present` and isn't a digital wallet, then a
    [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card is created and attached to the Customer
    instead.
    """

    customer_account: Optional[str] = None
    """
    ID of the Account representing the customer that this PaymentIntent belongs to,
    if one exists.

    Payment methods attached to other Accounts cannot be used with this
    PaymentIntent.

    If
    [setup_future_usage](https://api.stripe.com#payment_intent_object-setup_future_usage)
    is set and this PaymentIntent's payment method is not `card_present`, then the
    payment method attaches to the Account after the PaymentIntent has been
    confirmed and any required actions from the user are complete. If the payment
    method is `card_present` and isn't a digital wallet, then a
    [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card is created and attached to the Account
    instead.
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
    """The list of payment method types to exclude from use with this payment."""

    hooks: Optional[Hooks] = None

    last_payment_error: Optional["APIErrors"] = None

    latest_charge: Optional[LatestCharge] = None
    """
    ID of the latest [Charge object](https://docs.stripe.com/api/charges) created by
    this PaymentIntent. This property is `null` until PaymentIntent confirmation is
    attempted.
    """

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Learn more about
    [storing information in metadata](https://docs.stripe.com/payments/payment-intents/creating-payment-intents#storing-information-in-metadata).
    """

    next_action: Optional[NextAction] = None

    on_behalf_of: Optional[OnBehalfOf] = None
    """
    You can specify the settlement merchant as the connected account using the
    `on_behalf_of` attribute on the charge. See the PaymentIntents
    [use case for connected accounts](/payments/connected-accounts) for details.
    """

    payment_details: Optional[PaymentDetails] = None

    payment_method: Optional[PaymentMethod] = None
    """ID of the payment method used in this PaymentIntent."""

    payment_method_configuration_details: Optional[PaymentMethodConfigurationDetails] = None

    payment_method_options: Optional[PaymentMethodOptions] = None

    payment_method_types: Optional[List[str]] = None
    """The list of payment method types (e.g.

    card) that this PaymentIntent is allowed to use. A comprehensive list of valid
    payment method types can be found
    [here](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type).
    """

    presentment_details: Optional[PaymentFlowsPaymentIntentPresentmentDetails] = None

    processing: Optional[Processing] = None

    receipt_email: Optional[str] = None
    """Email address that the receipt for the resulting payment will be sent to.

    If `receipt_email` is specified for a payment in live mode, a receipt will be
    sent regardless of your
    [email settings](https://dashboard.stripe.com/account/emails).
    """

    review: Optional[Review] = None
    """ID of the review associated with this PaymentIntent, if any."""

    setup_future_usage: Optional[Literal["off_session", "on_session"]] = None
    """
    Indicates that you intend to make future payments with this PaymentIntent's
    payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to
    [attach the payment method](/payments/save-during-payment) to the Customer after
    the PaymentIntent is confirmed and the customer completes any required actions.
    If you don't provide a Customer, you can still
    [attach](/api/payment_methods/attach) the payment method to a Customer after the
    transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe
    creates and attaches a
    [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
    payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you
    comply with regional legislation and network rules, such as
    [SCA](/strong-customer-authentication).
    """

    shipping: Optional[Shipping] = None

    statement_descriptor: Optional[str] = None
    """
    Text that appears on the customer's statement as the statement descriptor for a
    non-card charge. This value overrides the account's default statement
    descriptor. For information about requirements, including the 22-character
    limit, see
    [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

    Setting this value for a card charge returns an error. For card charges, set the
    [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic)
    instead.
    """

    statement_descriptor_suffix: Optional[str] = None
    """Provides information about a card charge.

    Concatenated to the account's
    [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static)
    to form the complete statement descriptor that appears on the customer's
    statement.
    """

    transfer_data: Optional["PaymentTransferData"] = None

    transfer_group: Optional[str] = None
    """A string that identifies the resulting payment as part of a group.

    Learn more about the
    [use case for connected accounts](https://docs.stripe.com/connect/separate-charges-and-transfers).
    """


from . import review, customer, payment_method
from .charge import Charge
from .account import Account
from .api_errors import APIErrors
from .payment_transfer_data import PaymentTransferData
