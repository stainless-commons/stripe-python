# Shared Types

```python
from stripe_minimal.types import (
    AccountRequirementsError,
    Address,
    Application,
    BillingClocksResourceStatusDetailsAdvancingStatusDetails,
    BillingClocksResourceStatusDetailsStatusDetails,
    DeletedApplication,
    DeletedCustomer,
    DeletedTaxID,
    InvoiceSettingCustomField,
    PaymentFlowsPaymentIntentPresentmentDetails,
    PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet,
    PaymentMethodDetailsCardInstallmentsPlan,
    PaymentMethodDetailsCardPresent,
    PaymentMethodDetailsCardPresentOffline,
    PaymentMethodDetailsCardPresentReceipt,
    PaymentMethodDetailsPassthroughCard,
    Shipping,
    Source,
    SourceCodeVerificationFlow,
    SourceOrder,
    SourceOrderItem,
    SourceOwner,
    SourceReceiverFlow,
    SourceRedirectFlow,
    SourceTypeACHCreditTransfer,
    SourceTypeACHDebit,
    SourceTypeAcssDebit,
    SourceTypeAlipay,
    SourceTypeAuBecsDebit,
    SourceTypeBancontact,
    SourceTypeCard,
    SourceTypeCardPresent,
    SourceTypeEps,
    SourceTypeGiropay,
    SourceTypeIdeal,
    SourceTypeKlarna,
    SourceTypeMultibanco,
    SourceTypeP24,
    SourceTypeSepaDebit,
    SourceTypeSofort,
    SourceTypeThreeDSecure,
    SourceTypeWechat,
    TaxCode,
    TestHelpersTestClock,
)
```

# Account

Types:

```python
from stripe_minimal.types import (
    Account,
    AccountInvoicesSettings,
    AccountRequirementsAlternative,
    AccountSettings,
    LegalEntityJapanAddress,
)
```

Methods:

- <code title="get /v1/account">client.account.<a href="./src/stripe_minimal/resources/account.py">retrieve</a>(\*\*<a href="src/stripe_minimal/types/account_retrieve_params.py">params</a>) -> <a href="./src/stripe_minimal/types/account.py">Account</a></code>

# Balance

Types:

```python
from stripe_minimal.types import BalanceAmount, BalanceAmountBySourceType, BalanceRetrieveResponse
```

Methods:

- <code title="get /v1/balance">client.balance.<a href="./src/stripe_minimal/resources/balance.py">retrieve</a>(\*\*<a href="src/stripe_minimal/types/balance_retrieve_params.py">params</a>) -> <a href="./src/stripe_minimal/types/balance_retrieve_response.py">BalanceRetrieveResponse</a></code>

# Coupons

Types:

```python
from stripe_minimal.types import Coupon, CouponListResponse
```

Methods:

- <code title="post /v1/coupons">client.coupons.<a href="./src/stripe_minimal/resources/coupons.py">create</a>(\*\*<a href="src/stripe_minimal/types/coupon_create_params.py">params</a>) -> <a href="./src/stripe_minimal/types/coupon.py">Coupon</a></code>
- <code title="get /v1/coupons">client.coupons.<a href="./src/stripe_minimal/resources/coupons.py">list</a>(\*\*<a href="src/stripe_minimal/types/coupon_list_params.py">params</a>) -> <a href="./src/stripe_minimal/types/coupon_list_response.py">CouponListResponse</a></code>

# Customers

Types:

```python
from stripe_minimal.types import (
    BankAccount,
    Card,
    Customer,
    Discount,
    InvoiceSetting,
    PromotionCode,
    TaxID,
    TaxIDsOwner,
    CustomerListResponse,
)
```

Methods:

- <code title="post /v1/customers">client.customers.<a href="./src/stripe_minimal/resources/customers.py">create</a>(\*\*<a href="src/stripe_minimal/types/customer_create_params.py">params</a>) -> <a href="./src/stripe_minimal/types/customer.py">Customer</a></code>
- <code title="get /v1/customers">client.customers.<a href="./src/stripe_minimal/resources/customers.py">list</a>(\*\*<a href="src/stripe_minimal/types/customer_list_params.py">params</a>) -> <a href="./src/stripe_minimal/types/customer_list_response.py">CustomerListResponse</a></code>

# Disputes

Types:

```python
from stripe_minimal.types import (
    ApplicationFee,
    BalanceTransaction,
    Charge,
    ChargeTransferData,
    ConnectCollectionTransfer,
    CustomerBalanceResourceCashBalanceTransactionAdjustedForOverdraft,
    CustomerBalanceResourceCashBalanceTransactionAppliedToPayment,
    CustomerBalanceResourceCashBalanceTransactionRefundedFromPayment,
    CustomerBalanceResourceCashBalanceTransactionTransferredToBalance,
    CustomerBalanceResourceCashBalanceTransactionUnappliedFromPayment,
    CustomerCashBalanceTransaction,
    Dispute,
    FeeRefund,
    File,
    FileLink,
    IssuingAuthorization,
    IssuingAuthorizationAmountDetails,
    IssuingCard,
    IssuingCardholder,
    IssuingCardholderAddress,
    IssuingCardholderAuthorizationControls,
    IssuingCardholderCardIssuing,
    IssuingCardholderCompany,
    IssuingCardholderIDDocument,
    IssuingCardholderIndividual,
    IssuingCardholderIndividualDob,
    IssuingCardholderRequirements,
    IssuingCardholderSpendingLimit,
    IssuingCardholderUserTermsAcceptance,
    IssuingCardholderVerification,
    IssuingDispute,
    IssuingTransaction,
    PaymentMethodDetails,
    PaymentMethodDetailsBancontactDispute,
    PaymentMethodDetailsIdealDispute,
    PaymentMethodDetailsSofortDispute,
    PaymentMethodDetailsUsBankAccount,
    Payout,
    Topup,
    Transfer,
    DisputeListResponse,
)
```

Methods:

- <code title="post /v1/disputes/{dispute}">client.disputes.<a href="./src/stripe_minimal/resources/disputes.py">update</a>(dispute, \*\*<a href="src/stripe_minimal/types/dispute_update_params.py">params</a>) -> <a href="./src/stripe_minimal/types/dispute.py">Dispute</a></code>
- <code title="get /v1/disputes">client.disputes.<a href="./src/stripe_minimal/resources/disputes.py">list</a>(\*\*<a href="src/stripe_minimal/types/dispute_list_params.py">params</a>) -> <a href="./src/stripe_minimal/types/dispute_list_response.py">DisputeListResponse</a></code>

# Invoices

Types:

```python
from stripe_minimal.types import (
    APIErrors,
    AutomaticTaxInvoice,
    BillingBillResourceInvoicingParentsInvoiceParent,
    BillingBillResourceInvoicingParentsInvoiceSubscriptionParent,
    BillingCreditBalanceTransaction,
    BillingCreditGrant,
    BillingCreditGrantsResourceAmount,
    BillingCreditGrantsResourceBalanceCredit,
    BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided,
    BillingCreditGrantsResourceBalanceCreditsApplied,
    BillingCreditGrantsResourceBalanceDebit,
    BillingCreditGrantsResourceMonetaryAmount,
    ConnectAccountReference,
    DeletedDiscount,
    DiscountsResourceDiscountAmount,
    Invoice,
    InvoicePayment,
    InvoicesPaymentsInvoicePaymentAssociatedPayment,
    InvoicesResourceFromInvoice,
    InvoicesResourcePretaxCreditAmount,
    LineItem,
    PaymentMethod,
    PaymentMethodCard,
    PaymentMethodCardGeneratedCard,
    PaymentMethodDetailsPaymentRecordUsBankAccount,
    PaymentMethodSepaDebit,
    PaymentRecord,
    PaymentsPrimitivesPaymentRecordsResourceAmount,
    PaymentsPrimitivesPaymentRecordsResourcePaymentMethodDetails,
    SepaDebitGeneratedFrom,
    ShippingRateDeliveryEstimateBound,
    TaxRate,
    InvoiceListResponse,
)
```

Methods:

- <code title="post /v1/invoices">client.invoices.<a href="./src/stripe_minimal/resources/invoices.py">create</a>(\*\*<a href="src/stripe_minimal/types/invoice_create_params.py">params</a>) -> <a href="./src/stripe_minimal/types/invoice.py">Invoice</a></code>
- <code title="get /v1/invoices">client.invoices.<a href="./src/stripe_minimal/resources/invoices.py">list</a>(\*\*<a href="src/stripe_minimal/types/invoice_list_params.py">params</a>) -> <a href="./src/stripe_minimal/types/invoice_list_response.py">InvoiceListResponse</a></code>
- <code title="post /v1/invoices/{invoice}/finalize">client.invoices.<a href="./src/stripe_minimal/resources/invoices.py">finalize</a>(invoice, \*\*<a href="src/stripe_minimal/types/invoice_finalize_params.py">params</a>) -> <a href="./src/stripe_minimal/types/invoice.py">Invoice</a></code>

# Invoiceitems

Types:

```python
from stripe_minimal.types import InvoiceitemCreateResponse
```

Methods:

- <code title="post /v1/invoiceitems">client.invoiceitems.<a href="./src/stripe_minimal/resources/invoiceitems.py">create</a>(\*\*<a href="src/stripe_minimal/types/invoiceitem_create_params.py">params</a>) -> <a href="./src/stripe_minimal/types/invoiceitem_create_response.py">InvoiceitemCreateResponse</a></code>

# PaymentLinks

Types:

```python
from stripe_minimal.types import CustomTextPosition, PaymentLinkCreateResponse
```

Methods:

- <code title="post /v1/payment_links">client.payment_links.<a href="./src/stripe_minimal/resources/payment_links.py">create</a>(\*\*<a href="src/stripe_minimal/types/payment_link_create_params.py">params</a>) -> <a href="./src/stripe_minimal/types/payment_link_create_response.py">PaymentLinkCreateResponse</a></code>

# PaymentIntents

Types:

```python
from stripe_minimal.types import (
    PaymentFlowsInstallmentOptions,
    PaymentIntent,
    PaymentIntentPaymentMethodOptionsMandateOptionsPayto,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
    PaymentMethodOptionsCardPresentRouting,
    PaymentTransferData,
    Review,
    PaymentIntentListResponse,
)
```

Methods:

- <code title="get /v1/payment_intents">client.payment_intents.<a href="./src/stripe_minimal/resources/payment_intents.py">list</a>(\*\*<a href="src/stripe_minimal/types/payment_intent_list_params.py">params</a>) -> <a href="./src/stripe_minimal/types/payment_intent_list_response.py">PaymentIntentListResponse</a></code>

# Prices

Types:

```python
from stripe_minimal.types import Price, PriceListResponse
```

Methods:

- <code title="post /v1/prices">client.prices.<a href="./src/stripe_minimal/resources/prices.py">create</a>(\*\*<a href="src/stripe_minimal/types/price_create_params.py">params</a>) -> <a href="./src/stripe_minimal/types/price.py">Price</a></code>
- <code title="get /v1/prices">client.prices.<a href="./src/stripe_minimal/resources/prices.py">list</a>(\*\*<a href="src/stripe_minimal/types/price_list_params.py">params</a>) -> <a href="./src/stripe_minimal/types/price_list_response.py">PriceListResponse</a></code>

# Products

Types:

```python
from stripe_minimal.types import Product, ProductListResponse
```

Methods:

- <code title="post /v1/products">client.products.<a href="./src/stripe_minimal/resources/products.py">create</a>(\*\*<a href="src/stripe_minimal/types/product_create_params.py">params</a>) -> <a href="./src/stripe_minimal/types/product.py">Product</a></code>
- <code title="get /v1/products">client.products.<a href="./src/stripe_minimal/resources/products.py">list</a>(\*\*<a href="src/stripe_minimal/types/product_list_params.py">params</a>) -> <a href="./src/stripe_minimal/types/product_list_response.py">ProductListResponse</a></code>

# Refunds

Types:

```python
from stripe_minimal.types import Refund, TransferReversal
```

Methods:

- <code title="post /v1/refunds">client.refunds.<a href="./src/stripe_minimal/resources/refunds.py">create</a>(\*\*<a href="src/stripe_minimal/types/refund_create_params.py">params</a>) -> <a href="./src/stripe_minimal/types/refund.py">Refund</a></code>

# Subscriptions

Types:

```python
from stripe_minimal.types import (
    AutomaticTaxSubscription,
    DefaultSettings,
    DefaultSettingsAutomaticTax,
    Mandate,
    PaymentMethodDetailsBancontactSetupAttempt,
    PaymentMethodDetailsIdealSetupAttempt,
    PaymentMethodDetailsSofortSetupAttempt,
    PendingUpdate,
    PhaseAutomaticTax,
    Schedule,
    ScheduleAddInvoiceItem,
    ScheduleConfigurationItem,
    SchedulePhaseConfiguration,
    SchedulePhaseSetting,
    ScheduleSetting,
    SetupAttempt,
    SetupAttemptPaymentMethodDetails,
    SetupAttemptPaymentMethodDetailsCardPresent,
    SetupIntent,
    SetupIntentPaymentMethodOptionsMandateOptionsPayto,
    SetupIntentTypeSpecificPaymentMethodOptionsClient,
    StackableDiscount,
    Subscription,
    SubscriptionBillingThresholds,
    SubscriptionInvoiceSettings,
    SubscriptionItem,
    SubscriptionTransferData,
    SubscriptionListResponse,
)
```

Methods:

- <code title="post /v1/subscriptions/{subscription_exposed_id}">client.subscriptions.<a href="./src/stripe_minimal/resources/subscriptions.py">update</a>(subscription_exposed_id, \*\*<a href="src/stripe_minimal/types/subscription_update_params.py">params</a>) -> <a href="./src/stripe_minimal/types/subscription.py">Subscription</a></code>
- <code title="get /v1/subscriptions">client.subscriptions.<a href="./src/stripe_minimal/resources/subscriptions.py">list</a>(\*\*<a href="src/stripe_minimal/types/subscription_list_params.py">params</a>) -> <a href="./src/stripe_minimal/types/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /v1/subscriptions/{subscription_exposed_id}">client.subscriptions.<a href="./src/stripe_minimal/resources/subscriptions.py">cancel</a>(subscription_exposed_id, \*\*<a href="src/stripe_minimal/types/subscription_cancel_params.py">params</a>) -> <a href="./src/stripe_minimal/types/subscription.py">Subscription</a></code>
