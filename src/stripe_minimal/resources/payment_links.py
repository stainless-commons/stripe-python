# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from ..types import payment_link_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.payment_link_create_response import PaymentLinkCreateResponse

__all__ = ["PaymentLinksResource", "AsyncPaymentLinksResource"]


class PaymentLinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return PaymentLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return PaymentLinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        line_items: Iterable[payment_link_create_params.LineItem],
        after_completion: payment_link_create_params.AfterCompletion | Omit = omit,
        allow_promotion_codes: bool | Omit = omit,
        application_fee_amount: int | Omit = omit,
        application_fee_percent: float | Omit = omit,
        automatic_tax: payment_link_create_params.AutomaticTax | Omit = omit,
        billing_address_collection: Literal["auto", "required"] | Omit = omit,
        consent_collection: payment_link_create_params.ConsentCollection | Omit = omit,
        currency: str | Omit = omit,
        custom_fields: Iterable[payment_link_create_params.CustomField] | Omit = omit,
        custom_text: payment_link_create_params.CustomText | Omit = omit,
        customer_creation: Literal["always", "if_required"] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        inactive_message: str | Omit = omit,
        invoice_creation: payment_link_create_params.InvoiceCreation | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        name_collection: payment_link_create_params.NameCollection | Omit = omit,
        on_behalf_of: str | Omit = omit,
        optional_items: Iterable[payment_link_create_params.OptionalItem] | Omit = omit,
        payment_intent_data: payment_link_create_params.PaymentIntentData | Omit = omit,
        payment_method_collection: Literal["always", "if_required"] | Omit = omit,
        payment_method_types: List[
            Literal[
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "billie",
                "blik",
                "boleto",
                "card",
                "cashapp",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "klarna",
                "konbini",
                "link",
                "mb_way",
                "mobilepay",
                "multibanco",
                "oxxo",
                "p24",
                "pay_by_bank",
                "paynow",
                "paypal",
                "payto",
                "pix",
                "promptpay",
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
        | Omit = omit,
        phone_number_collection: payment_link_create_params.PhoneNumberCollection | Omit = omit,
        restrictions: payment_link_create_params.Restrictions | Omit = omit,
        shipping_address_collection: payment_link_create_params.ShippingAddressCollection | Omit = omit,
        shipping_options: Iterable[payment_link_create_params.ShippingOption] | Omit = omit,
        submit_type: Literal["auto", "book", "donate", "pay", "subscribe"] | Omit = omit,
        subscription_data: payment_link_create_params.SubscriptionData | Omit = omit,
        tax_id_collection: payment_link_create_params.TaxIDCollection | Omit = omit,
        transfer_data: payment_link_create_params.TransferData | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentLinkCreateResponse:
        """
        <p>Creates a payment link.</p>

        Args:
          line_items: The line items representing what is being sold. Each line item represents an
              item being sold. Up to 20 line items are supported.

          after_completion: Behavior after the purchase is complete.

          allow_promotion_codes: Enables user redeemable promotion codes.

          application_fee_amount: The amount of the application fee (if any) that will be requested to be applied
              to the payment and transferred to the application owner's Stripe account. Can
              only be applied when there are no line items with recurring prices.

          application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This
              represents the percentage of the subscription invoice total that will be
              transferred to the application owner's Stripe account. There must be at least 1
              line item with a recurring price to use this field.

          automatic_tax: Configuration for automatic tax collection.

          billing_address_collection: Configuration for collecting the customer's billing address. Defaults to `auto`.

          consent_collection: Configure fields to gather active consent from customers.

          currency: Three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
              lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)
              and supported by each line item's price.

          custom_fields: Collect additional information from your customer using custom fields. Up to 3
              fields are supported. You can't set this parameter if `ui_mode` is `custom`.

          custom_text: Display additional text for your customers using custom text. You can't set this
              parameter if `ui_mode` is `custom`.

          customer_creation: Configures whether
              [checkout sessions](https://docs.stripe.com/api/checkout/sessions) created by
              this payment link create a [Customer](https://docs.stripe.com/api/customers).

          expand: Specifies which fields in the response should be expanded.

          inactive_message: The custom message to be displayed to a customer when a payment link is no
              longer active.

          invoice_creation: Generate a post-purchase Invoice for one-time payments.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`. Metadata associated with this Payment Link will automatically be
              copied to [checkout sessions](https://docs.stripe.com/api/checkout/sessions)
              created by this payment link.

          name_collection: Controls settings applied for collecting the customer's name.

          on_behalf_of: The account on behalf of which to charge.

          optional_items: A list of optional items the customer can add to their order at checkout. Use
              this parameter to pass one-time or recurring
              [Prices](https://docs.stripe.com/api/prices). There is a maximum of 10 optional
              items allowed on a payment link, and the existing limits on the number of line
              items allowed on a payment link apply to the combined number of line items and
              optional items. There is a maximum of 20 combined line items and optional items.

          payment_intent_data: A subset of parameters to be passed to PaymentIntent creation for Checkout
              Sessions in `payment` mode.

          payment_method_collection: Specify whether Checkout should collect a payment method. When set to
              `if_required`, Checkout will not collect a payment method when the total due for
              the session is 0.This may occur if the Checkout Session includes a free trial or
              a discount.

              Can only be set in `subscription` mode. Defaults to `always`.

              If you'd like information on how to collect a payment method outside of
              Checkout, read the guide on
              [configuring subscriptions with a free trial](https://docs.stripe.com/payments/checkout/free-trials).

          payment_method_types: The list of payment method types that customers can use. If no value is passed,
              Stripe will dynamically show relevant payment methods from your
              [payment method settings](https://dashboard.stripe.com/settings/payment_methods)
              (20+ payment methods
              [supported](https://docs.stripe.com/payments/payment-methods/integration-options#payment-method-product-support)).

          phone_number_collection: Controls phone number collection settings during checkout.

              We recommend that you review your privacy policy and check with your legal
              contacts.

          restrictions: Settings that restrict the usage of a payment link.

          shipping_address_collection: Configuration for collecting the customer's shipping address.

          shipping_options: The shipping rate options to apply to
              [checkout sessions](https://docs.stripe.com/api/checkout/sessions) created by
              this payment link.

          submit_type: Describes the type of transaction being performed in order to customize relevant
              text on the page, such as the submit button. Changing this value will also
              affect the hostname in the
              [url](https://docs.stripe.com/api/payment_links/payment_links/object#url)
              property (example: `donate.stripe.com`).

          subscription_data: When creating a subscription, the specified configuration data will be used.
              There must be at least one line item with a recurring price to use
              `subscription_data`.

          tax_id_collection: Controls tax ID collection during checkout.

          transfer_data: The account (if any) the payments will be attributed to for tax reporting, and
              where funds from each payment will be transferred to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/payment_links",
            body=maybe_transform(
                {
                    "line_items": line_items,
                    "after_completion": after_completion,
                    "allow_promotion_codes": allow_promotion_codes,
                    "application_fee_amount": application_fee_amount,
                    "application_fee_percent": application_fee_percent,
                    "automatic_tax": automatic_tax,
                    "billing_address_collection": billing_address_collection,
                    "consent_collection": consent_collection,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "custom_text": custom_text,
                    "customer_creation": customer_creation,
                    "expand": expand,
                    "inactive_message": inactive_message,
                    "invoice_creation": invoice_creation,
                    "metadata": metadata,
                    "name_collection": name_collection,
                    "on_behalf_of": on_behalf_of,
                    "optional_items": optional_items,
                    "payment_intent_data": payment_intent_data,
                    "payment_method_collection": payment_method_collection,
                    "payment_method_types": payment_method_types,
                    "phone_number_collection": phone_number_collection,
                    "restrictions": restrictions,
                    "shipping_address_collection": shipping_address_collection,
                    "shipping_options": shipping_options,
                    "submit_type": submit_type,
                    "subscription_data": subscription_data,
                    "tax_id_collection": tax_id_collection,
                    "transfer_data": transfer_data,
                },
                payment_link_create_params.PaymentLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentLinkCreateResponse,
        )


class AsyncPaymentLinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return AsyncPaymentLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        line_items: Iterable[payment_link_create_params.LineItem],
        after_completion: payment_link_create_params.AfterCompletion | Omit = omit,
        allow_promotion_codes: bool | Omit = omit,
        application_fee_amount: int | Omit = omit,
        application_fee_percent: float | Omit = omit,
        automatic_tax: payment_link_create_params.AutomaticTax | Omit = omit,
        billing_address_collection: Literal["auto", "required"] | Omit = omit,
        consent_collection: payment_link_create_params.ConsentCollection | Omit = omit,
        currency: str | Omit = omit,
        custom_fields: Iterable[payment_link_create_params.CustomField] | Omit = omit,
        custom_text: payment_link_create_params.CustomText | Omit = omit,
        customer_creation: Literal["always", "if_required"] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        inactive_message: str | Omit = omit,
        invoice_creation: payment_link_create_params.InvoiceCreation | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        name_collection: payment_link_create_params.NameCollection | Omit = omit,
        on_behalf_of: str | Omit = omit,
        optional_items: Iterable[payment_link_create_params.OptionalItem] | Omit = omit,
        payment_intent_data: payment_link_create_params.PaymentIntentData | Omit = omit,
        payment_method_collection: Literal["always", "if_required"] | Omit = omit,
        payment_method_types: List[
            Literal[
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "billie",
                "blik",
                "boleto",
                "card",
                "cashapp",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "klarna",
                "konbini",
                "link",
                "mb_way",
                "mobilepay",
                "multibanco",
                "oxxo",
                "p24",
                "pay_by_bank",
                "paynow",
                "paypal",
                "payto",
                "pix",
                "promptpay",
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
        | Omit = omit,
        phone_number_collection: payment_link_create_params.PhoneNumberCollection | Omit = omit,
        restrictions: payment_link_create_params.Restrictions | Omit = omit,
        shipping_address_collection: payment_link_create_params.ShippingAddressCollection | Omit = omit,
        shipping_options: Iterable[payment_link_create_params.ShippingOption] | Omit = omit,
        submit_type: Literal["auto", "book", "donate", "pay", "subscribe"] | Omit = omit,
        subscription_data: payment_link_create_params.SubscriptionData | Omit = omit,
        tax_id_collection: payment_link_create_params.TaxIDCollection | Omit = omit,
        transfer_data: payment_link_create_params.TransferData | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentLinkCreateResponse:
        """
        <p>Creates a payment link.</p>

        Args:
          line_items: The line items representing what is being sold. Each line item represents an
              item being sold. Up to 20 line items are supported.

          after_completion: Behavior after the purchase is complete.

          allow_promotion_codes: Enables user redeemable promotion codes.

          application_fee_amount: The amount of the application fee (if any) that will be requested to be applied
              to the payment and transferred to the application owner's Stripe account. Can
              only be applied when there are no line items with recurring prices.

          application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This
              represents the percentage of the subscription invoice total that will be
              transferred to the application owner's Stripe account. There must be at least 1
              line item with a recurring price to use this field.

          automatic_tax: Configuration for automatic tax collection.

          billing_address_collection: Configuration for collecting the customer's billing address. Defaults to `auto`.

          consent_collection: Configure fields to gather active consent from customers.

          currency: Three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
              lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)
              and supported by each line item's price.

          custom_fields: Collect additional information from your customer using custom fields. Up to 3
              fields are supported. You can't set this parameter if `ui_mode` is `custom`.

          custom_text: Display additional text for your customers using custom text. You can't set this
              parameter if `ui_mode` is `custom`.

          customer_creation: Configures whether
              [checkout sessions](https://docs.stripe.com/api/checkout/sessions) created by
              this payment link create a [Customer](https://docs.stripe.com/api/customers).

          expand: Specifies which fields in the response should be expanded.

          inactive_message: The custom message to be displayed to a customer when a payment link is no
              longer active.

          invoice_creation: Generate a post-purchase Invoice for one-time payments.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`. Metadata associated with this Payment Link will automatically be
              copied to [checkout sessions](https://docs.stripe.com/api/checkout/sessions)
              created by this payment link.

          name_collection: Controls settings applied for collecting the customer's name.

          on_behalf_of: The account on behalf of which to charge.

          optional_items: A list of optional items the customer can add to their order at checkout. Use
              this parameter to pass one-time or recurring
              [Prices](https://docs.stripe.com/api/prices). There is a maximum of 10 optional
              items allowed on a payment link, and the existing limits on the number of line
              items allowed on a payment link apply to the combined number of line items and
              optional items. There is a maximum of 20 combined line items and optional items.

          payment_intent_data: A subset of parameters to be passed to PaymentIntent creation for Checkout
              Sessions in `payment` mode.

          payment_method_collection: Specify whether Checkout should collect a payment method. When set to
              `if_required`, Checkout will not collect a payment method when the total due for
              the session is 0.This may occur if the Checkout Session includes a free trial or
              a discount.

              Can only be set in `subscription` mode. Defaults to `always`.

              If you'd like information on how to collect a payment method outside of
              Checkout, read the guide on
              [configuring subscriptions with a free trial](https://docs.stripe.com/payments/checkout/free-trials).

          payment_method_types: The list of payment method types that customers can use. If no value is passed,
              Stripe will dynamically show relevant payment methods from your
              [payment method settings](https://dashboard.stripe.com/settings/payment_methods)
              (20+ payment methods
              [supported](https://docs.stripe.com/payments/payment-methods/integration-options#payment-method-product-support)).

          phone_number_collection: Controls phone number collection settings during checkout.

              We recommend that you review your privacy policy and check with your legal
              contacts.

          restrictions: Settings that restrict the usage of a payment link.

          shipping_address_collection: Configuration for collecting the customer's shipping address.

          shipping_options: The shipping rate options to apply to
              [checkout sessions](https://docs.stripe.com/api/checkout/sessions) created by
              this payment link.

          submit_type: Describes the type of transaction being performed in order to customize relevant
              text on the page, such as the submit button. Changing this value will also
              affect the hostname in the
              [url](https://docs.stripe.com/api/payment_links/payment_links/object#url)
              property (example: `donate.stripe.com`).

          subscription_data: When creating a subscription, the specified configuration data will be used.
              There must be at least one line item with a recurring price to use
              `subscription_data`.

          tax_id_collection: Controls tax ID collection during checkout.

          transfer_data: The account (if any) the payments will be attributed to for tax reporting, and
              where funds from each payment will be transferred to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/payment_links",
            body=await async_maybe_transform(
                {
                    "line_items": line_items,
                    "after_completion": after_completion,
                    "allow_promotion_codes": allow_promotion_codes,
                    "application_fee_amount": application_fee_amount,
                    "application_fee_percent": application_fee_percent,
                    "automatic_tax": automatic_tax,
                    "billing_address_collection": billing_address_collection,
                    "consent_collection": consent_collection,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "custom_text": custom_text,
                    "customer_creation": customer_creation,
                    "expand": expand,
                    "inactive_message": inactive_message,
                    "invoice_creation": invoice_creation,
                    "metadata": metadata,
                    "name_collection": name_collection,
                    "on_behalf_of": on_behalf_of,
                    "optional_items": optional_items,
                    "payment_intent_data": payment_intent_data,
                    "payment_method_collection": payment_method_collection,
                    "payment_method_types": payment_method_types,
                    "phone_number_collection": phone_number_collection,
                    "restrictions": restrictions,
                    "shipping_address_collection": shipping_address_collection,
                    "shipping_options": shipping_options,
                    "submit_type": submit_type,
                    "subscription_data": subscription_data,
                    "tax_id_collection": tax_id_collection,
                    "transfer_data": transfer_data,
                },
                payment_link_create_params.PaymentLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentLinkCreateResponse,
        )


class PaymentLinksResourceWithRawResponse:
    def __init__(self, payment_links: PaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = to_raw_response_wrapper(
            payment_links.create,
        )


class AsyncPaymentLinksResourceWithRawResponse:
    def __init__(self, payment_links: AsyncPaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = async_to_raw_response_wrapper(
            payment_links.create,
        )


class PaymentLinksResourceWithStreamingResponse:
    def __init__(self, payment_links: PaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = to_streamed_response_wrapper(
            payment_links.create,
        )


class AsyncPaymentLinksResourceWithStreamingResponse:
    def __init__(self, payment_links: AsyncPaymentLinksResource) -> None:
        self._payment_links = payment_links

        self.create = async_to_streamed_response_wrapper(
            payment_links.create,
        )
