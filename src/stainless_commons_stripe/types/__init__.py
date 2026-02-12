# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import (
    card,
    file,
    price,
    topup,
    charge,
    payout,
    refund,
    review,
    tax_id,
    account,
    dispute,
    invoice,
    mandate,
    product,
    customer,
    discount,
    schedule,
    transfer,
    file_link,
    line_item,
    api_errors,
    fee_refund,
    bank_account,
    issuing_card,
    setup_intent,
    subscription,
    setup_attempt,
    tax_ids_owner,
    payment_intent,
    payment_method,
    payment_record,
    pending_update,
    promotion_code,
    application_fee,
    invoice_payment,
    invoice_setting,
    issuing_dispute,
    account_settings,
    default_settings,
    deleted_discount,
    schedule_setting,
    subscription_item,
    transfer_reversal,
    issuing_cardholder,
    stackable_discount,
    balance_transaction,
    issuing_transaction,
    payment_method_card,
    phase_automatic_tax,
    billing_credit_grant,
    charge_transfer_data,
    automatic_tax_invoice,
    issuing_authorization,
    payment_transfer_data,
    payment_method_details,
    schedule_phase_setting,
    account_invoices_settings,
    connect_account_reference,
    payment_method_sepa_debit,
    schedule_add_invoice_item,
    sepa_debit_generated_from,
    automatic_tax_subscription,
    subscription_transfer_data,
    connect_collection_transfer,
    invoiceitem_create_response,
    schedule_configuration_item,
    payment_link_create_response,
    schedule_phase_configuration,
    issuing_cardholder_individual,
    subscription_invoice_settings,
    default_settings_automatic_tax,
    invoices_resource_from_invoice,
    issuing_cardholder_id_document,
    issuing_cardholder_verification,
    customer_cash_balance_transaction,
    billing_credit_balance_transaction,
    discounts_resource_discount_amount,
    payment_method_card_generated_card,
    payment_method_details_ideal_dispute,
    setup_attempt_payment_method_details,
    payment_method_details_sofort_dispute,
    invoices_resource_pretax_credit_amount,
    payment_method_details_us_bank_account,
    payment_method_details_bancontact_dispute,
    payment_method_details_ideal_setup_attempt,
    payment_method_details_sofort_setup_attempt,
    billing_credit_grants_resource_balance_debit,
    billing_credit_grants_resource_balance_credit,
    payment_method_details_bancontact_setup_attempt,
    setup_attempt_payment_method_details_card_present,
    invoices_payments_invoice_payment_associated_payment,
    payment_method_details_payment_record_us_bank_account,
    billing_bill_resource_invoicing_parents_invoice_parent,
    billing_credit_grants_resource_balance_credits_applied,
    billing_bill_resource_invoicing_parents_invoice_subscription_parent,
    payments_primitives_payment_records_resource_payment_method_details,
    customer_balance_resource_cash_balance_transaction_applied_to_payment,
    customer_balance_resource_cash_balance_transaction_refunded_from_payment,
    billing_credit_grants_resource_balance_credits_application_invoice_voided,
    customer_balance_resource_cash_balance_transaction_adjusted_for_overdraft,
    customer_balance_resource_cash_balance_transaction_transferred_to_balance,
    customer_balance_resource_cash_balance_transaction_unapplied_from_payment,
)
from .. import _compat
from .card import Card as Card
from .file import File as File
from .price import Price as Price
from .topup import Topup as Topup
from .charge import Charge as Charge
from .coupon import Coupon as Coupon
from .payout import Payout as Payout
from .refund import Refund as Refund
from .review import Review as Review
from .shared import (
    Source as Source,
    Address as Address,
    TaxCode as TaxCode,
    Shipping as Shipping,
    Application as Application,
    SourceOrder as SourceOrder,
    SourceOwner as SourceOwner,
    DeletedTaxID as DeletedTaxID,
    SourceTypeEps as SourceTypeEps,
    SourceTypeP24 as SourceTypeP24,
    SourceTypeCard as SourceTypeCard,
    DeletedCustomer as DeletedCustomer,
    SourceOrderItem as SourceOrderItem,
    SourceTypeIdeal as SourceTypeIdeal,
    SourceTypeAlipay as SourceTypeAlipay,
    SourceTypeKlarna as SourceTypeKlarna,
    SourceTypeSofort as SourceTypeSofort,
    SourceTypeWechat as SourceTypeWechat,
    SourceTypeGiropay as SourceTypeGiropay,
    DeletedApplication as DeletedApplication,
    SourceReceiverFlow as SourceReceiverFlow,
    SourceRedirectFlow as SourceRedirectFlow,
    SourceTypeACHDebit as SourceTypeACHDebit,
    SourceTypeAcssDebit as SourceTypeAcssDebit,
    SourceTypeSepaDebit as SourceTypeSepaDebit,
    SourceTypeBancontact as SourceTypeBancontact,
    SourceTypeMultibanco as SourceTypeMultibanco,
    TestHelpersTestClock as TestHelpersTestClock,
    SourceTypeAuBecsDebit as SourceTypeAuBecsDebit,
    SourceTypeCardPresent as SourceTypeCardPresent,
    SourceTypeThreeDSecure as SourceTypeThreeDSecure,
    AccountRequirementsError as AccountRequirementsError,
    InvoiceSettingCustomField as InvoiceSettingCustomField,
    SourceCodeVerificationFlow as SourceCodeVerificationFlow,
    SourceTypeACHCreditTransfer as SourceTypeACHCreditTransfer,
    PaymentMethodDetailsCardPresent as PaymentMethodDetailsCardPresent,
    PaymentMethodDetailsPassthroughCard as PaymentMethodDetailsPassthroughCard,
    PaymentMethodDetailsCardPresentOffline as PaymentMethodDetailsCardPresentOffline,
    PaymentMethodDetailsCardPresentReceipt as PaymentMethodDetailsCardPresentReceipt,
    PaymentMethodDetailsCardInstallmentsPlan as PaymentMethodDetailsCardInstallmentsPlan,
    PaymentFlowsPaymentIntentPresentmentDetails as PaymentFlowsPaymentIntentPresentmentDetails,
    BillingClocksResourceStatusDetailsStatusDetails as BillingClocksResourceStatusDetailsStatusDetails,
    BillingClocksResourceStatusDetailsAdvancingStatusDetails as BillingClocksResourceStatusDetailsAdvancingStatusDetails,
    PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet as PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet,
)
from .tax_id import TaxID as TaxID
from .account import Account as Account
from .dispute import Dispute as Dispute
from .invoice import Invoice as Invoice
from .mandate import Mandate as Mandate
from .product import Product as Product
from .customer import Customer as Customer
from .discount import Discount as Discount
from .schedule import Schedule as Schedule
from .tax_rate import TaxRate as TaxRate
from .transfer import Transfer as Transfer
from .file_link import FileLink as FileLink
from .line_item import LineItem as LineItem
from .api_errors import APIErrors as APIErrors
from .fee_refund import FeeRefund as FeeRefund
from .bank_account import BankAccount as BankAccount
from .issuing_card import IssuingCard as IssuingCard
from .setup_intent import SetupIntent as SetupIntent
from .subscription import Subscription as Subscription
from .setup_attempt import SetupAttempt as SetupAttempt
from .tax_ids_owner import TaxIDsOwner as TaxIDsOwner
from .balance_amount import BalanceAmount as BalanceAmount
from .payment_intent import PaymentIntent as PaymentIntent
from .payment_method import PaymentMethod as PaymentMethod
from .payment_record import PaymentRecord as PaymentRecord
from .pending_update import PendingUpdate as PendingUpdate
from .promotion_code import PromotionCode as PromotionCode
from .application_fee import ApplicationFee as ApplicationFee
from .invoice_payment import InvoicePayment as InvoicePayment
from .invoice_setting import InvoiceSetting as InvoiceSetting
from .issuing_dispute import IssuingDispute as IssuingDispute
from .account_settings import AccountSettings as AccountSettings
from .default_settings import DefaultSettings as DefaultSettings
from .deleted_discount import DeletedDiscount as DeletedDiscount
from .schedule_setting import ScheduleSetting as ScheduleSetting
from .price_list_params import PriceListParams as PriceListParams
from .subscription_item import SubscriptionItem as SubscriptionItem
from .transfer_reversal import TransferReversal as TransferReversal
from .coupon_list_params import CouponListParams as CouponListParams
from .issuing_cardholder import IssuingCardholder as IssuingCardholder
from .stackable_discount import StackableDiscount as StackableDiscount
from .balance_transaction import BalanceTransaction as BalanceTransaction
from .dispute_list_params import DisputeListParams as DisputeListParams
from .invoice_list_params import InvoiceListParams as InvoiceListParams
from .issuing_transaction import IssuingTransaction as IssuingTransaction
from .payment_method_card import PaymentMethodCard as PaymentMethodCard
from .phase_automatic_tax import PhaseAutomaticTax as PhaseAutomaticTax
from .price_create_params import PriceCreateParams as PriceCreateParams
from .product_list_params import ProductListParams as ProductListParams
from .billing_credit_grant import BillingCreditGrant as BillingCreditGrant
from .charge_transfer_data import ChargeTransferData as ChargeTransferData
from .coupon_create_params import CouponCreateParams as CouponCreateParams
from .custom_text_position import CustomTextPosition as CustomTextPosition
from .customer_list_params import CustomerListParams as CustomerListParams
from .refund_create_params import RefundCreateParams as RefundCreateParams
from .automatic_tax_invoice import AutomaticTaxInvoice as AutomaticTaxInvoice
from .dispute_update_params import DisputeUpdateParams as DisputeUpdateParams
from .invoice_create_params import InvoiceCreateParams as InvoiceCreateParams
from .issuing_authorization import IssuingAuthorization as IssuingAuthorization
from .payment_transfer_data import PaymentTransferData as PaymentTransferData
from .product_create_params import ProductCreateParams as ProductCreateParams
from .customer_create_params import CustomerCreateParams as CustomerCreateParams
from .payment_method_details import PaymentMethodDetails as PaymentMethodDetails
from .schedule_phase_setting import SchedulePhaseSetting as SchedulePhaseSetting
from .account_retrieve_params import AccountRetrieveParams as AccountRetrieveParams
from .balance_retrieve_params import BalanceRetrieveParams as BalanceRetrieveParams
from .invoice_finalize_params import InvoiceFinalizeParams as InvoiceFinalizeParams
from .subscription_list_params import SubscriptionListParams as SubscriptionListParams
from .account_invoices_settings import AccountInvoicesSettings as AccountInvoicesSettings
from .balance_retrieve_response import BalanceRetrieveResponse as BalanceRetrieveResponse
from .connect_account_reference import ConnectAccountReference as ConnectAccountReference
from .invoiceitem_create_params import InvoiceitemCreateParams as InvoiceitemCreateParams
from .payment_method_sepa_debit import PaymentMethodSepaDebit as PaymentMethodSepaDebit
from .schedule_add_invoice_item import ScheduleAddInvoiceItem as ScheduleAddInvoiceItem
from .sepa_debit_generated_from import SepaDebitGeneratedFrom as SepaDebitGeneratedFrom
from .automatic_tax_subscription import AutomaticTaxSubscription as AutomaticTaxSubscription
from .issuing_cardholder_address import IssuingCardholderAddress as IssuingCardholderAddress
from .issuing_cardholder_company import IssuingCardholderCompany as IssuingCardholderCompany
from .legal_entity_japan_address import LegalEntityJapanAddress as LegalEntityJapanAddress
from .payment_intent_list_params import PaymentIntentListParams as PaymentIntentListParams
from .payment_link_create_params import PaymentLinkCreateParams as PaymentLinkCreateParams
from .subscription_cancel_params import SubscriptionCancelParams as SubscriptionCancelParams
from .subscription_transfer_data import SubscriptionTransferData as SubscriptionTransferData
from .subscription_update_params import SubscriptionUpdateParams as SubscriptionUpdateParams
from .connect_collection_transfer import ConnectCollectionTransfer as ConnectCollectionTransfer
from .invoiceitem_create_response import InvoiceitemCreateResponse as InvoiceitemCreateResponse
from .schedule_configuration_item import ScheduleConfigurationItem as ScheduleConfigurationItem
from .payment_link_create_response import PaymentLinkCreateResponse as PaymentLinkCreateResponse
from .schedule_phase_configuration import SchedulePhaseConfiguration as SchedulePhaseConfiguration
from .balance_amount_by_source_type import BalanceAmountBySourceType as BalanceAmountBySourceType
from .issuing_cardholder_individual import IssuingCardholderIndividual as IssuingCardholderIndividual
from .subscription_invoice_settings import SubscriptionInvoiceSettings as SubscriptionInvoiceSettings
from .default_settings_automatic_tax import DefaultSettingsAutomaticTax as DefaultSettingsAutomaticTax
from .invoices_resource_from_invoice import InvoicesResourceFromInvoice as InvoicesResourceFromInvoice
from .issuing_cardholder_id_document import IssuingCardholderIDDocument as IssuingCardholderIDDocument
from .issuing_cardholder_card_issuing import IssuingCardholderCardIssuing as IssuingCardholderCardIssuing
from .issuing_cardholder_requirements import IssuingCardholderRequirements as IssuingCardholderRequirements
from .issuing_cardholder_verification import IssuingCardholderVerification as IssuingCardholderVerification
from .subscription_billing_thresholds import SubscriptionBillingThresholds as SubscriptionBillingThresholds
from .account_requirements_alternative import AccountRequirementsAlternative as AccountRequirementsAlternative
from .customer_cash_balance_transaction import CustomerCashBalanceTransaction as CustomerCashBalanceTransaction
from .issuing_cardholder_individual_dob import IssuingCardholderIndividualDob as IssuingCardholderIndividualDob
from .issuing_cardholder_spending_limit import IssuingCardholderSpendingLimit as IssuingCardholderSpendingLimit
from .payment_flows_installment_options import PaymentFlowsInstallmentOptions as PaymentFlowsInstallmentOptions
from .billing_credit_balance_transaction import BillingCreditBalanceTransaction as BillingCreditBalanceTransaction
from .discounts_resource_discount_amount import DiscountsResourceDiscountAmount as DiscountsResourceDiscountAmount
from .payment_method_card_generated_card import PaymentMethodCardGeneratedCard as PaymentMethodCardGeneratedCard
from .issuing_authorization_amount_details import IssuingAuthorizationAmountDetails as IssuingAuthorizationAmountDetails
from .payment_method_details_ideal_dispute import PaymentMethodDetailsIdealDispute as PaymentMethodDetailsIdealDispute
from .setup_attempt_payment_method_details import SetupAttemptPaymentMethodDetails as SetupAttemptPaymentMethodDetails
from .billing_credit_grants_resource_amount import (
    BillingCreditGrantsResourceAmount as BillingCreditGrantsResourceAmount,
)
from .payment_method_details_sofort_dispute import (
    PaymentMethodDetailsSofortDispute as PaymentMethodDetailsSofortDispute,
)
from .shipping_rate_delivery_estimate_bound import (
    ShippingRateDeliveryEstimateBound as ShippingRateDeliveryEstimateBound,
)
from .invoices_resource_pretax_credit_amount import (
    InvoicesResourcePretaxCreditAmount as InvoicesResourcePretaxCreditAmount,
)
from .payment_method_details_us_bank_account import (
    PaymentMethodDetailsUsBankAccount as PaymentMethodDetailsUsBankAccount,
)
from .issuing_cardholder_user_terms_acceptance import (
    IssuingCardholderUserTermsAcceptance as IssuingCardholderUserTermsAcceptance,
)
from .issuing_cardholder_authorization_controls import (
    IssuingCardholderAuthorizationControls as IssuingCardholderAuthorizationControls,
)
from .payment_method_details_bancontact_dispute import (
    PaymentMethodDetailsBancontactDispute as PaymentMethodDetailsBancontactDispute,
)
from .payment_method_details_ideal_setup_attempt import (
    PaymentMethodDetailsIdealSetupAttempt as PaymentMethodDetailsIdealSetupAttempt,
)
from .payment_method_details_sofort_setup_attempt import (
    PaymentMethodDetailsSofortSetupAttempt as PaymentMethodDetailsSofortSetupAttempt,
)
from .payment_method_options_card_present_routing import (
    PaymentMethodOptionsCardPresentRouting as PaymentMethodOptionsCardPresentRouting,
)
from .billing_credit_grants_resource_balance_debit import (
    BillingCreditGrantsResourceBalanceDebit as BillingCreditGrantsResourceBalanceDebit,
)
from .billing_credit_grants_resource_balance_credit import (
    BillingCreditGrantsResourceBalanceCredit as BillingCreditGrantsResourceBalanceCredit,
)
from .billing_credit_grants_resource_monetary_amount import (
    BillingCreditGrantsResourceMonetaryAmount as BillingCreditGrantsResourceMonetaryAmount,
)
from .payment_method_details_bancontact_setup_attempt import (
    PaymentMethodDetailsBancontactSetupAttempt as PaymentMethodDetailsBancontactSetupAttempt,
)
from .setup_attempt_payment_method_details_card_present import (
    SetupAttemptPaymentMethodDetailsCardPresent as SetupAttemptPaymentMethodDetailsCardPresent,
)
from .payments_primitives_payment_records_resource_amount import (
    PaymentsPrimitivesPaymentRecordsResourceAmount as PaymentsPrimitivesPaymentRecordsResourceAmount,
)
from .invoices_payments_invoice_payment_associated_payment import (
    InvoicesPaymentsInvoicePaymentAssociatedPayment as InvoicesPaymentsInvoicePaymentAssociatedPayment,
)
from .payment_method_details_payment_record_us_bank_account import (
    PaymentMethodDetailsPaymentRecordUsBankAccount as PaymentMethodDetailsPaymentRecordUsBankAccount,
)
from .billing_bill_resource_invoicing_parents_invoice_parent import (
    BillingBillResourceInvoicingParentsInvoiceParent as BillingBillResourceInvoicingParentsInvoiceParent,
)
from .billing_credit_grants_resource_balance_credits_applied import (
    BillingCreditGrantsResourceBalanceCreditsApplied as BillingCreditGrantsResourceBalanceCreditsApplied,
)
from .setup_intent_type_specific_payment_method_options_client import (
    SetupIntentTypeSpecificPaymentMethodOptionsClient as SetupIntentTypeSpecificPaymentMethodOptionsClient,
)
from .setup_intent_payment_method_options_mandate_options_payto import (
    SetupIntentPaymentMethodOptionsMandateOptionsPayto as SetupIntentPaymentMethodOptionsMandateOptionsPayto,
)
from .payment_intent_type_specific_payment_method_options_client import (
    PaymentIntentTypeSpecificPaymentMethodOptionsClient as PaymentIntentTypeSpecificPaymentMethodOptionsClient,
)
from .payment_intent_payment_method_options_mandate_options_payto import (
    PaymentIntentPaymentMethodOptionsMandateOptionsPayto as PaymentIntentPaymentMethodOptionsMandateOptionsPayto,
)
from .billing_bill_resource_invoicing_parents_invoice_subscription_parent import (
    BillingBillResourceInvoicingParentsInvoiceSubscriptionParent as BillingBillResourceInvoicingParentsInvoiceSubscriptionParent,
)
from .payments_primitives_payment_records_resource_payment_method_details import (
    PaymentsPrimitivesPaymentRecordsResourcePaymentMethodDetails as PaymentsPrimitivesPaymentRecordsResourcePaymentMethodDetails,
)
from .customer_balance_resource_cash_balance_transaction_applied_to_payment import (
    CustomerBalanceResourceCashBalanceTransactionAppliedToPayment as CustomerBalanceResourceCashBalanceTransactionAppliedToPayment,
)
from .customer_balance_resource_cash_balance_transaction_refunded_from_payment import (
    CustomerBalanceResourceCashBalanceTransactionRefundedFromPayment as CustomerBalanceResourceCashBalanceTransactionRefundedFromPayment,
)
from .billing_credit_grants_resource_balance_credits_application_invoice_voided import (
    BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided as BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided,
)
from .customer_balance_resource_cash_balance_transaction_adjusted_for_overdraft import (
    CustomerBalanceResourceCashBalanceTransactionAdjustedForOverdraft as CustomerBalanceResourceCashBalanceTransactionAdjustedForOverdraft,
)
from .customer_balance_resource_cash_balance_transaction_transferred_to_balance import (
    CustomerBalanceResourceCashBalanceTransactionTransferredToBalance as CustomerBalanceResourceCashBalanceTransactionTransferredToBalance,
)
from .customer_balance_resource_cash_balance_transaction_unapplied_from_payment import (
    CustomerBalanceResourceCashBalanceTransactionUnappliedFromPayment as CustomerBalanceResourceCashBalanceTransactionUnappliedFromPayment,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    account.Account.update_forward_refs()  # type: ignore
    account_invoices_settings.AccountInvoicesSettings.update_forward_refs()  # type: ignore
    account_settings.AccountSettings.update_forward_refs()  # type: ignore
    bank_account.BankAccount.update_forward_refs()  # type: ignore
    card.Card.update_forward_refs()  # type: ignore
    customer.Customer.update_forward_refs()  # type: ignore
    discount.Discount.update_forward_refs()  # type: ignore
    invoice_setting.InvoiceSetting.update_forward_refs()  # type: ignore
    promotion_code.PromotionCode.update_forward_refs()  # type: ignore
    tax_id.TaxID.update_forward_refs()  # type: ignore
    tax_ids_owner.TaxIDsOwner.update_forward_refs()  # type: ignore
    application_fee.ApplicationFee.update_forward_refs()  # type: ignore
    balance_transaction.BalanceTransaction.update_forward_refs()  # type: ignore
    charge.Charge.update_forward_refs()  # type: ignore
    charge_transfer_data.ChargeTransferData.update_forward_refs()  # type: ignore
    connect_collection_transfer.ConnectCollectionTransfer.update_forward_refs()  # type: ignore
    customer_balance_resource_cash_balance_transaction_adjusted_for_overdraft.CustomerBalanceResourceCashBalanceTransactionAdjustedForOverdraft.update_forward_refs()  # type: ignore
    customer_balance_resource_cash_balance_transaction_applied_to_payment.CustomerBalanceResourceCashBalanceTransactionAppliedToPayment.update_forward_refs()  # type: ignore
    customer_balance_resource_cash_balance_transaction_refunded_from_payment.CustomerBalanceResourceCashBalanceTransactionRefundedFromPayment.update_forward_refs()  # type: ignore
    customer_balance_resource_cash_balance_transaction_transferred_to_balance.CustomerBalanceResourceCashBalanceTransactionTransferredToBalance.update_forward_refs()  # type: ignore
    customer_balance_resource_cash_balance_transaction_unapplied_from_payment.CustomerBalanceResourceCashBalanceTransactionUnappliedFromPayment.update_forward_refs()  # type: ignore
    customer_cash_balance_transaction.CustomerCashBalanceTransaction.update_forward_refs()  # type: ignore
    dispute.Dispute.update_forward_refs()  # type: ignore
    fee_refund.FeeRefund.update_forward_refs()  # type: ignore
    file.File.update_forward_refs()  # type: ignore
    file_link.FileLink.update_forward_refs()  # type: ignore
    issuing_authorization.IssuingAuthorization.update_forward_refs()  # type: ignore
    issuing_card.IssuingCard.update_forward_refs()  # type: ignore
    issuing_cardholder.IssuingCardholder.update_forward_refs()  # type: ignore
    issuing_cardholder_id_document.IssuingCardholderIDDocument.update_forward_refs()  # type: ignore
    issuing_cardholder_individual.IssuingCardholderIndividual.update_forward_refs()  # type: ignore
    issuing_cardholder_verification.IssuingCardholderVerification.update_forward_refs()  # type: ignore
    issuing_dispute.IssuingDispute.update_forward_refs()  # type: ignore
    issuing_transaction.IssuingTransaction.update_forward_refs()  # type: ignore
    payment_method_details.PaymentMethodDetails.update_forward_refs()  # type: ignore
    payment_method_details_bancontact_dispute.PaymentMethodDetailsBancontactDispute.update_forward_refs()  # type: ignore
    payment_method_details_ideal_dispute.PaymentMethodDetailsIdealDispute.update_forward_refs()  # type: ignore
    payment_method_details_sofort_dispute.PaymentMethodDetailsSofortDispute.update_forward_refs()  # type: ignore
    payment_method_details_us_bank_account.PaymentMethodDetailsUsBankAccount.update_forward_refs()  # type: ignore
    payout.Payout.update_forward_refs()  # type: ignore
    topup.Topup.update_forward_refs()  # type: ignore
    transfer.Transfer.update_forward_refs()  # type: ignore
    api_errors.APIErrors.update_forward_refs()  # type: ignore
    automatic_tax_invoice.AutomaticTaxInvoice.update_forward_refs()  # type: ignore
    billing_bill_resource_invoicing_parents_invoice_parent.BillingBillResourceInvoicingParentsInvoiceParent.update_forward_refs()  # type: ignore
    billing_bill_resource_invoicing_parents_invoice_subscription_parent.BillingBillResourceInvoicingParentsInvoiceSubscriptionParent.update_forward_refs()  # type: ignore
    billing_credit_balance_transaction.BillingCreditBalanceTransaction.update_forward_refs()  # type: ignore
    billing_credit_grant.BillingCreditGrant.update_forward_refs()  # type: ignore
    billing_credit_grants_resource_balance_credit.BillingCreditGrantsResourceBalanceCredit.update_forward_refs()  # type: ignore
    billing_credit_grants_resource_balance_credits_application_invoice_voided.BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided.update_forward_refs()  # type: ignore
    billing_credit_grants_resource_balance_credits_applied.BillingCreditGrantsResourceBalanceCreditsApplied.update_forward_refs()  # type: ignore
    billing_credit_grants_resource_balance_debit.BillingCreditGrantsResourceBalanceDebit.update_forward_refs()  # type: ignore
    connect_account_reference.ConnectAccountReference.update_forward_refs()  # type: ignore
    deleted_discount.DeletedDiscount.update_forward_refs()  # type: ignore
    discounts_resource_discount_amount.DiscountsResourceDiscountAmount.update_forward_refs()  # type: ignore
    invoice.Invoice.update_forward_refs()  # type: ignore
    invoice_payment.InvoicePayment.update_forward_refs()  # type: ignore
    invoices_payments_invoice_payment_associated_payment.InvoicesPaymentsInvoicePaymentAssociatedPayment.update_forward_refs()  # type: ignore
    invoices_resource_from_invoice.InvoicesResourceFromInvoice.update_forward_refs()  # type: ignore
    invoices_resource_pretax_credit_amount.InvoicesResourcePretaxCreditAmount.update_forward_refs()  # type: ignore
    line_item.LineItem.update_forward_refs()  # type: ignore
    payment_method.PaymentMethod.update_forward_refs()  # type: ignore
    payment_method_card.PaymentMethodCard.update_forward_refs()  # type: ignore
    payment_method_card_generated_card.PaymentMethodCardGeneratedCard.update_forward_refs()  # type: ignore
    payment_method_details_payment_record_us_bank_account.PaymentMethodDetailsPaymentRecordUsBankAccount.update_forward_refs()  # type: ignore
    payment_method_sepa_debit.PaymentMethodSepaDebit.update_forward_refs()  # type: ignore
    payment_record.PaymentRecord.update_forward_refs()  # type: ignore
    payments_primitives_payment_records_resource_payment_method_details.PaymentsPrimitivesPaymentRecordsResourcePaymentMethodDetails.update_forward_refs()  # type: ignore
    sepa_debit_generated_from.SepaDebitGeneratedFrom.update_forward_refs()  # type: ignore
    invoiceitem_create_response.InvoiceitemCreateResponse.update_forward_refs()  # type: ignore
    payment_link_create_response.PaymentLinkCreateResponse.update_forward_refs()  # type: ignore
    payment_intent.PaymentIntent.update_forward_refs()  # type: ignore
    payment_transfer_data.PaymentTransferData.update_forward_refs()  # type: ignore
    review.Review.update_forward_refs()  # type: ignore
    price.Price.update_forward_refs()  # type: ignore
    product.Product.update_forward_refs()  # type: ignore
    refund.Refund.update_forward_refs()  # type: ignore
    transfer_reversal.TransferReversal.update_forward_refs()  # type: ignore
    automatic_tax_subscription.AutomaticTaxSubscription.update_forward_refs()  # type: ignore
    default_settings.DefaultSettings.update_forward_refs()  # type: ignore
    default_settings_automatic_tax.DefaultSettingsAutomaticTax.update_forward_refs()  # type: ignore
    mandate.Mandate.update_forward_refs()  # type: ignore
    payment_method_details_bancontact_setup_attempt.PaymentMethodDetailsBancontactSetupAttempt.update_forward_refs()  # type: ignore
    payment_method_details_ideal_setup_attempt.PaymentMethodDetailsIdealSetupAttempt.update_forward_refs()  # type: ignore
    payment_method_details_sofort_setup_attempt.PaymentMethodDetailsSofortSetupAttempt.update_forward_refs()  # type: ignore
    pending_update.PendingUpdate.update_forward_refs()  # type: ignore
    phase_automatic_tax.PhaseAutomaticTax.update_forward_refs()  # type: ignore
    schedule.Schedule.update_forward_refs()  # type: ignore
    schedule_add_invoice_item.ScheduleAddInvoiceItem.update_forward_refs()  # type: ignore
    schedule_configuration_item.ScheduleConfigurationItem.update_forward_refs()  # type: ignore
    schedule_phase_configuration.SchedulePhaseConfiguration.update_forward_refs()  # type: ignore
    schedule_phase_setting.SchedulePhaseSetting.update_forward_refs()  # type: ignore
    schedule_setting.ScheduleSetting.update_forward_refs()  # type: ignore
    setup_attempt.SetupAttempt.update_forward_refs()  # type: ignore
    setup_attempt_payment_method_details.SetupAttemptPaymentMethodDetails.update_forward_refs()  # type: ignore
    setup_attempt_payment_method_details_card_present.SetupAttemptPaymentMethodDetailsCardPresent.update_forward_refs()  # type: ignore
    setup_intent.SetupIntent.update_forward_refs()  # type: ignore
    stackable_discount.StackableDiscount.update_forward_refs()  # type: ignore
    subscription.Subscription.update_forward_refs()  # type: ignore
    subscription_invoice_settings.SubscriptionInvoiceSettings.update_forward_refs()  # type: ignore
    subscription_item.SubscriptionItem.update_forward_refs()  # type: ignore
    subscription_transfer_data.SubscriptionTransferData.update_forward_refs()  # type: ignore
else:
    account.Account.model_rebuild(_parent_namespace_depth=0)
    account_invoices_settings.AccountInvoicesSettings.model_rebuild(_parent_namespace_depth=0)
    account_settings.AccountSettings.model_rebuild(_parent_namespace_depth=0)
    bank_account.BankAccount.model_rebuild(_parent_namespace_depth=0)
    card.Card.model_rebuild(_parent_namespace_depth=0)
    customer.Customer.model_rebuild(_parent_namespace_depth=0)
    discount.Discount.model_rebuild(_parent_namespace_depth=0)
    invoice_setting.InvoiceSetting.model_rebuild(_parent_namespace_depth=0)
    promotion_code.PromotionCode.model_rebuild(_parent_namespace_depth=0)
    tax_id.TaxID.model_rebuild(_parent_namespace_depth=0)
    tax_ids_owner.TaxIDsOwner.model_rebuild(_parent_namespace_depth=0)
    application_fee.ApplicationFee.model_rebuild(_parent_namespace_depth=0)
    balance_transaction.BalanceTransaction.model_rebuild(_parent_namespace_depth=0)
    charge.Charge.model_rebuild(_parent_namespace_depth=0)
    charge_transfer_data.ChargeTransferData.model_rebuild(_parent_namespace_depth=0)
    connect_collection_transfer.ConnectCollectionTransfer.model_rebuild(_parent_namespace_depth=0)
    customer_balance_resource_cash_balance_transaction_adjusted_for_overdraft.CustomerBalanceResourceCashBalanceTransactionAdjustedForOverdraft.model_rebuild(
        _parent_namespace_depth=0
    )
    customer_balance_resource_cash_balance_transaction_applied_to_payment.CustomerBalanceResourceCashBalanceTransactionAppliedToPayment.model_rebuild(
        _parent_namespace_depth=0
    )
    customer_balance_resource_cash_balance_transaction_refunded_from_payment.CustomerBalanceResourceCashBalanceTransactionRefundedFromPayment.model_rebuild(
        _parent_namespace_depth=0
    )
    customer_balance_resource_cash_balance_transaction_transferred_to_balance.CustomerBalanceResourceCashBalanceTransactionTransferredToBalance.model_rebuild(
        _parent_namespace_depth=0
    )
    customer_balance_resource_cash_balance_transaction_unapplied_from_payment.CustomerBalanceResourceCashBalanceTransactionUnappliedFromPayment.model_rebuild(
        _parent_namespace_depth=0
    )
    customer_cash_balance_transaction.CustomerCashBalanceTransaction.model_rebuild(_parent_namespace_depth=0)
    dispute.Dispute.model_rebuild(_parent_namespace_depth=0)
    fee_refund.FeeRefund.model_rebuild(_parent_namespace_depth=0)
    file.File.model_rebuild(_parent_namespace_depth=0)
    file_link.FileLink.model_rebuild(_parent_namespace_depth=0)
    issuing_authorization.IssuingAuthorization.model_rebuild(_parent_namespace_depth=0)
    issuing_card.IssuingCard.model_rebuild(_parent_namespace_depth=0)
    issuing_cardholder.IssuingCardholder.model_rebuild(_parent_namespace_depth=0)
    issuing_cardholder_id_document.IssuingCardholderIDDocument.model_rebuild(_parent_namespace_depth=0)
    issuing_cardholder_individual.IssuingCardholderIndividual.model_rebuild(_parent_namespace_depth=0)
    issuing_cardholder_verification.IssuingCardholderVerification.model_rebuild(_parent_namespace_depth=0)
    issuing_dispute.IssuingDispute.model_rebuild(_parent_namespace_depth=0)
    issuing_transaction.IssuingTransaction.model_rebuild(_parent_namespace_depth=0)
    payment_method_details.PaymentMethodDetails.model_rebuild(_parent_namespace_depth=0)
    payment_method_details_bancontact_dispute.PaymentMethodDetailsBancontactDispute.model_rebuild(
        _parent_namespace_depth=0
    )
    payment_method_details_ideal_dispute.PaymentMethodDetailsIdealDispute.model_rebuild(_parent_namespace_depth=0)
    payment_method_details_sofort_dispute.PaymentMethodDetailsSofortDispute.model_rebuild(_parent_namespace_depth=0)
    payment_method_details_us_bank_account.PaymentMethodDetailsUsBankAccount.model_rebuild(_parent_namespace_depth=0)
    payout.Payout.model_rebuild(_parent_namespace_depth=0)
    topup.Topup.model_rebuild(_parent_namespace_depth=0)
    transfer.Transfer.model_rebuild(_parent_namespace_depth=0)
    api_errors.APIErrors.model_rebuild(_parent_namespace_depth=0)
    automatic_tax_invoice.AutomaticTaxInvoice.model_rebuild(_parent_namespace_depth=0)
    billing_bill_resource_invoicing_parents_invoice_parent.BillingBillResourceInvoicingParentsInvoiceParent.model_rebuild(
        _parent_namespace_depth=0
    )
    billing_bill_resource_invoicing_parents_invoice_subscription_parent.BillingBillResourceInvoicingParentsInvoiceSubscriptionParent.model_rebuild(
        _parent_namespace_depth=0
    )
    billing_credit_balance_transaction.BillingCreditBalanceTransaction.model_rebuild(_parent_namespace_depth=0)
    billing_credit_grant.BillingCreditGrant.model_rebuild(_parent_namespace_depth=0)
    billing_credit_grants_resource_balance_credit.BillingCreditGrantsResourceBalanceCredit.model_rebuild(
        _parent_namespace_depth=0
    )
    billing_credit_grants_resource_balance_credits_application_invoice_voided.BillingCreditGrantsResourceBalanceCreditsApplicationInvoiceVoided.model_rebuild(
        _parent_namespace_depth=0
    )
    billing_credit_grants_resource_balance_credits_applied.BillingCreditGrantsResourceBalanceCreditsApplied.model_rebuild(
        _parent_namespace_depth=0
    )
    billing_credit_grants_resource_balance_debit.BillingCreditGrantsResourceBalanceDebit.model_rebuild(
        _parent_namespace_depth=0
    )
    connect_account_reference.ConnectAccountReference.model_rebuild(_parent_namespace_depth=0)
    deleted_discount.DeletedDiscount.model_rebuild(_parent_namespace_depth=0)
    discounts_resource_discount_amount.DiscountsResourceDiscountAmount.model_rebuild(_parent_namespace_depth=0)
    invoice.Invoice.model_rebuild(_parent_namespace_depth=0)
    invoice_payment.InvoicePayment.model_rebuild(_parent_namespace_depth=0)
    invoices_payments_invoice_payment_associated_payment.InvoicesPaymentsInvoicePaymentAssociatedPayment.model_rebuild(
        _parent_namespace_depth=0
    )
    invoices_resource_from_invoice.InvoicesResourceFromInvoice.model_rebuild(_parent_namespace_depth=0)
    invoices_resource_pretax_credit_amount.InvoicesResourcePretaxCreditAmount.model_rebuild(_parent_namespace_depth=0)
    line_item.LineItem.model_rebuild(_parent_namespace_depth=0)
    payment_method.PaymentMethod.model_rebuild(_parent_namespace_depth=0)
    payment_method_card.PaymentMethodCard.model_rebuild(_parent_namespace_depth=0)
    payment_method_card_generated_card.PaymentMethodCardGeneratedCard.model_rebuild(_parent_namespace_depth=0)
    payment_method_details_payment_record_us_bank_account.PaymentMethodDetailsPaymentRecordUsBankAccount.model_rebuild(
        _parent_namespace_depth=0
    )
    payment_method_sepa_debit.PaymentMethodSepaDebit.model_rebuild(_parent_namespace_depth=0)
    payment_record.PaymentRecord.model_rebuild(_parent_namespace_depth=0)
    payments_primitives_payment_records_resource_payment_method_details.PaymentsPrimitivesPaymentRecordsResourcePaymentMethodDetails.model_rebuild(
        _parent_namespace_depth=0
    )
    sepa_debit_generated_from.SepaDebitGeneratedFrom.model_rebuild(_parent_namespace_depth=0)
    invoiceitem_create_response.InvoiceitemCreateResponse.model_rebuild(_parent_namespace_depth=0)
    payment_link_create_response.PaymentLinkCreateResponse.model_rebuild(_parent_namespace_depth=0)
    payment_intent.PaymentIntent.model_rebuild(_parent_namespace_depth=0)
    payment_transfer_data.PaymentTransferData.model_rebuild(_parent_namespace_depth=0)
    review.Review.model_rebuild(_parent_namespace_depth=0)
    price.Price.model_rebuild(_parent_namespace_depth=0)
    product.Product.model_rebuild(_parent_namespace_depth=0)
    refund.Refund.model_rebuild(_parent_namespace_depth=0)
    transfer_reversal.TransferReversal.model_rebuild(_parent_namespace_depth=0)
    automatic_tax_subscription.AutomaticTaxSubscription.model_rebuild(_parent_namespace_depth=0)
    default_settings.DefaultSettings.model_rebuild(_parent_namespace_depth=0)
    default_settings_automatic_tax.DefaultSettingsAutomaticTax.model_rebuild(_parent_namespace_depth=0)
    mandate.Mandate.model_rebuild(_parent_namespace_depth=0)
    payment_method_details_bancontact_setup_attempt.PaymentMethodDetailsBancontactSetupAttempt.model_rebuild(
        _parent_namespace_depth=0
    )
    payment_method_details_ideal_setup_attempt.PaymentMethodDetailsIdealSetupAttempt.model_rebuild(
        _parent_namespace_depth=0
    )
    payment_method_details_sofort_setup_attempt.PaymentMethodDetailsSofortSetupAttempt.model_rebuild(
        _parent_namespace_depth=0
    )
    pending_update.PendingUpdate.model_rebuild(_parent_namespace_depth=0)
    phase_automatic_tax.PhaseAutomaticTax.model_rebuild(_parent_namespace_depth=0)
    schedule.Schedule.model_rebuild(_parent_namespace_depth=0)
    schedule_add_invoice_item.ScheduleAddInvoiceItem.model_rebuild(_parent_namespace_depth=0)
    schedule_configuration_item.ScheduleConfigurationItem.model_rebuild(_parent_namespace_depth=0)
    schedule_phase_configuration.SchedulePhaseConfiguration.model_rebuild(_parent_namespace_depth=0)
    schedule_phase_setting.SchedulePhaseSetting.model_rebuild(_parent_namespace_depth=0)
    schedule_setting.ScheduleSetting.model_rebuild(_parent_namespace_depth=0)
    setup_attempt.SetupAttempt.model_rebuild(_parent_namespace_depth=0)
    setup_attempt_payment_method_details.SetupAttemptPaymentMethodDetails.model_rebuild(_parent_namespace_depth=0)
    setup_attempt_payment_method_details_card_present.SetupAttemptPaymentMethodDetailsCardPresent.model_rebuild(
        _parent_namespace_depth=0
    )
    setup_intent.SetupIntent.model_rebuild(_parent_namespace_depth=0)
    stackable_discount.StackableDiscount.model_rebuild(_parent_namespace_depth=0)
    subscription.Subscription.model_rebuild(_parent_namespace_depth=0)
    subscription_invoice_settings.SubscriptionInvoiceSettings.model_rebuild(_parent_namespace_depth=0)
    subscription_item.SubscriptionItem.model_rebuild(_parent_namespace_depth=0)
    subscription_transfer_data.SubscriptionTransferData.model_rebuild(_parent_namespace_depth=0)
