# Shared Types

```python
from stainless_commons_stripe.types import (
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

# Accounts

Types:

```python
from stainless_commons_stripe.types import (
    Account,
    AccountInvoicesSettings,
    AccountRequirementsAlternative,
    AccountSettings,
    LegalEntityJapanAddress,
)
```

Methods:

- <code title="get /v1/account">client.accounts.<a href="./src/stainless_commons_stripe/resources/accounts.py">retrieve</a>(\*\*<a href="src/stainless_commons_stripe/types/account_retrieve_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/account.py">Account</a></code>

# Balance

Types:

```python
from stainless_commons_stripe.types import (
    BalanceAmount,
    BalanceAmountBySourceType,
    BalanceRetrieveResponse,
)
```

Methods:

- <code title="get /v1/balance">client.balance.<a href="./src/stainless_commons_stripe/resources/balance.py">retrieve</a>(\*\*<a href="src/stainless_commons_stripe/types/balance_retrieve_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/balance_retrieve_response.py">BalanceRetrieveResponse</a></code>

# Coupons

Types:

```python
from stainless_commons_stripe.types import Coupon
```

Methods:

- <code title="post /v1/coupons">client.coupons.<a href="./src/stainless_commons_stripe/resources/coupons.py">create</a>(\*\*<a href="src/stainless_commons_stripe/types/coupon_create_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/coupon.py">Coupon</a></code>
- <code title="get /v1/coupons">client.coupons.<a href="./src/stainless_commons_stripe/resources/coupons.py">list</a>(\*\*<a href="src/stainless_commons_stripe/types/coupon_list_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/coupon.py">SyncMyCursorIDPage[Coupon]</a></code>

# Customers

Types:

```python
from stainless_commons_stripe.types import (
    BankAccount,
    Card,
    Customer,
    Discount,
    InvoiceSetting,
    PromotionCode,
    TaxID,
    TaxIDsOwner,
)
```

Methods:

- <code title="post /v1/customers">client.customers.<a href="./src/stainless_commons_stripe/resources/customers.py">create</a>(\*\*<a href="src/stainless_commons_stripe/types/customer_create_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/customer.py">Customer</a></code>
- <code title="get /v1/customers">client.customers.<a href="./src/stainless_commons_stripe/resources/customers.py">list</a>(\*\*<a href="src/stainless_commons_stripe/types/customer_list_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/customer.py">SyncMyCursorIDPage[Customer]</a></code>

# Disputes

Types:

```python
from stainless_commons_stripe.types import (
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
)
```

Methods:

- <code title="post /v1/disputes/{dispute}">client.disputes.<a href="./src/stainless_commons_stripe/resources/disputes.py">update</a>(dispute, \*\*<a href="src/stainless_commons_stripe/types/dispute_update_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/dispute.py">Dispute</a></code>
- <code title="get /v1/disputes">client.disputes.<a href="./src/stainless_commons_stripe/resources/disputes.py">list</a>(\*\*<a href="src/stainless_commons_stripe/types/dispute_list_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/dispute.py">SyncMyCursorIDPage[Dispute]</a></code>

# Invoices

Types:

```python
from stainless_commons_stripe.types import (
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
)
```

Methods:

- <code title="post /v1/invoices">client.invoices.<a href="./src/stainless_commons_stripe/resources/invoices.py">create</a>(\*\*<a href="src/stainless_commons_stripe/types/invoice_create_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/invoice.py">Invoice</a></code>
- <code title="get /v1/invoices">client.invoices.<a href="./src/stainless_commons_stripe/resources/invoices.py">list</a>(\*\*<a href="src/stainless_commons_stripe/types/invoice_list_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/invoice.py">SyncMyCursorIDPage[Invoice]</a></code>
- <code title="post /v1/invoices/{invoice}/finalize">client.invoices.<a href="./src/stainless_commons_stripe/resources/invoices.py">finalize</a>(invoice, \*\*<a href="src/stainless_commons_stripe/types/invoice_finalize_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/invoice.py">Invoice</a></code>

# Invoiceitems

Types:

```python
from stainless_commons_stripe.types import InvoiceitemCreateResponse
```

Methods:

- <code title="post /v1/invoiceitems">client.invoiceitems.<a href="./src/stainless_commons_stripe/resources/invoiceitems.py">create</a>(\*\*<a href="src/stainless_commons_stripe/types/invoiceitem_create_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/invoiceitem_create_response.py">InvoiceitemCreateResponse</a></code>

# PaymentLinks

Types:

```python
from stainless_commons_stripe.types import CustomTextPosition, PaymentLinkCreateResponse
```

Methods:

- <code title="post /v1/payment_links">client.payment_links.<a href="./src/stainless_commons_stripe/resources/payment_links.py">create</a>(\*\*<a href="src/stainless_commons_stripe/types/payment_link_create_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/payment_link_create_response.py">PaymentLinkCreateResponse</a></code>

# PaymentIntents

Types:

```python
from stainless_commons_stripe.types import (
    PaymentFlowsInstallmentOptions,
    PaymentIntent,
    PaymentIntentPaymentMethodOptionsMandateOptionsPayto,
    PaymentIntentTypeSpecificPaymentMethodOptionsClient,
    PaymentMethodOptionsCardPresentRouting,
    PaymentTransferData,
    Review,
)
```

Methods:

- <code title="get /v1/payment_intents">client.payment_intents.<a href="./src/stainless_commons_stripe/resources/payment_intents.py">list</a>(\*\*<a href="src/stainless_commons_stripe/types/payment_intent_list_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/payment_intent.py">SyncMyCursorIDPage[PaymentIntent]</a></code>

# Prices

Types:

```python
from stainless_commons_stripe.types import Price
```

Methods:

- <code title="post /v1/prices">client.prices.<a href="./src/stainless_commons_stripe/resources/prices.py">create</a>(\*\*<a href="src/stainless_commons_stripe/types/price_create_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/price.py">Price</a></code>
- <code title="get /v1/prices">client.prices.<a href="./src/stainless_commons_stripe/resources/prices.py">list</a>(\*\*<a href="src/stainless_commons_stripe/types/price_list_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/price.py">SyncMyCursorIDPage[Price]</a></code>

# Products

Types:

```python
from stainless_commons_stripe.types import Product
```

Methods:

- <code title="post /v1/products">client.products.<a href="./src/stainless_commons_stripe/resources/products.py">create</a>(\*\*<a href="src/stainless_commons_stripe/types/product_create_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/product.py">Product</a></code>
- <code title="get /v1/products">client.products.<a href="./src/stainless_commons_stripe/resources/products.py">list</a>(\*\*<a href="src/stainless_commons_stripe/types/product_list_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/product.py">SyncMyCursorIDPage[Product]</a></code>

# Refunds

Types:

```python
from stainless_commons_stripe.types import Refund, TransferReversal
```

Methods:

- <code title="post /v1/refunds">client.refunds.<a href="./src/stainless_commons_stripe/resources/refunds.py">create</a>(\*\*<a href="src/stainless_commons_stripe/types/refund_create_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/refund.py">Refund</a></code>

# Subscriptions

Types:

```python
from stainless_commons_stripe.types import (
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
)
```

Methods:

- <code title="post /v1/subscriptions/{subscription_exposed_id}">client.subscriptions.<a href="./src/stainless_commons_stripe/resources/subscriptions.py">update</a>(subscription_exposed_id, \*\*<a href="src/stainless_commons_stripe/types/subscription_update_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/subscription.py">Subscription</a></code>
- <code title="get /v1/subscriptions">client.subscriptions.<a href="./src/stainless_commons_stripe/resources/subscriptions.py">list</a>(\*\*<a href="src/stainless_commons_stripe/types/subscription_list_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/subscription.py">SyncMyCursorIDPage[Subscription]</a></code>
- <code title="delete /v1/subscriptions/{subscription_exposed_id}">client.subscriptions.<a href="./src/stainless_commons_stripe/resources/subscriptions.py">cancel</a>(subscription_exposed_id, \*\*<a href="src/stainless_commons_stripe/types/subscription_cancel_params.py">params</a>) -> <a href="./src/stainless_commons_stripe/types/subscription.py">Subscription</a></code>
