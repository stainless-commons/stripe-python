# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import invoice_list_params, invoice_create_params, invoice_finalize_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.invoice import Invoice

__all__ = ["InvoicesResource", "AsyncInvoicesResource"]


class InvoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-commons/stripe-python#accessing-raw-response-data-eg-headers
        """
        return InvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-commons/stripe-python#with_streaming_response
        """
        return InvoicesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_tax_ids: Union[SequenceNotStr[str], Literal[""]] | Omit = omit,
        application_fee_amount: int | Omit = omit,
        auto_advance: bool | Omit = omit,
        automatic_tax: invoice_create_params.AutomaticTax | Omit = omit,
        automatically_finalizes_at: int | Omit = omit,
        collection_method: Literal["charge_automatically", "send_invoice"] | Omit = omit,
        currency: str | Omit = omit,
        custom_fields: Union[Iterable[invoice_create_params.CustomFieldsCustomFieldsList], Literal[""]] | Omit = omit,
        customer: str | Omit = omit,
        customer_account: str | Omit = omit,
        days_until_due: int | Omit = omit,
        default_payment_method: str | Omit = omit,
        default_source: str | Omit = omit,
        default_tax_rates: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        discounts: Union[Iterable[invoice_create_params.DiscountsDiscountsList], Literal[""]] | Omit = omit,
        due_date: int | Omit = omit,
        effective_at: int | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        footer: str | Omit = omit,
        from_invoice: invoice_create_params.FromInvoice | Omit = omit,
        issuer: invoice_create_params.Issuer | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        number: str | Omit = omit,
        on_behalf_of: str | Omit = omit,
        payment_settings: invoice_create_params.PaymentSettings | Omit = omit,
        pending_invoice_items_behavior: Literal["exclude", "include"] | Omit = omit,
        rendering: invoice_create_params.Rendering | Omit = omit,
        shipping_cost: invoice_create_params.ShippingCost | Omit = omit,
        shipping_details: invoice_create_params.ShippingDetails | Omit = omit,
        statement_descriptor: str | Omit = omit,
        subscription: str | Omit = omit,
        transfer_data: invoice_create_params.TransferData | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """<p>This endpoint creates a draft invoice for a given customer.

        The invoice remains a draft until you <a href="#finalize_invoice">finalize</a> the invoice, which allows you to <a href="/api/invoices/pay">pay</a> or <a href="/api/invoices/send">send</a> the invoice to your customers.</p>

        Args:
          account_tax_ids: The account tax IDs associated with the invoice. Only editable when the invoice
              is a draft.

          application_fee_amount: A fee in cents (or local equivalent) that will be applied to the invoice and
              transferred to the application owner's Stripe account. The request must be made
              with an OAuth key or the Stripe-Account header in order to take an application
              fee. For more information, see the application fees
              [documentation](https://docs.stripe.com/billing/invoices/connect#collecting-fees).

          auto_advance: Controls whether Stripe performs
              [automatic collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
              of the invoice. If `false`, the invoice's state doesn't automatically advance
              without an explicit action. Defaults to false.

          automatic_tax: Settings for automatic tax lookup for this invoice.

          automatically_finalizes_at: The time when this invoice should be scheduled to finalize (up to 5 years in the
              future). The invoice is finalized at this time if it's still in draft state.

          collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically,
              Stripe will attempt to pay this invoice using the default source attached to the
              customer. When sending an invoice, Stripe will email this invoice to the
              customer with payment instructions. Defaults to `charge_automatically`.

          currency: The currency to create this invoice in. Defaults to that of `customer` if not
              specified.

          custom_fields: A list of up to 4 custom fields to be displayed on the invoice.

          customer: The ID of the customer to bill.

          customer_account: The ID of the account to bill.

          days_until_due: The number of days from when the invoice is created until it is due. Valid only
              for invoices where `collection_method=send_invoice`.

          default_payment_method: ID of the default payment method for the invoice. It must belong to the customer
              associated with the invoice. If not set, defaults to the subscription's default
              payment method, if any, or to the default payment method in the customer's
              invoice settings.

          default_source: ID of the default payment source for the invoice. It must belong to the customer
              associated with the invoice and be in a chargeable state. If not set, defaults
              to the subscription's default source, if any, or to the customer's default
              source.

          default_tax_rates: The tax rates that will apply to any line item that does not have `tax_rates`
              set.

          description: An arbitrary string attached to the object. Often useful for displaying to
              users. Referenced as 'memo' in the Dashboard.

          discounts: The coupons and promotion codes to redeem into discounts for the invoice. If not
              specified, inherits the discount from the invoice's customer. Pass an empty
              string to avoid inheriting any discounts.

          due_date: The date on which payment for this invoice is due. Valid only for invoices where
              `collection_method=send_invoice`.

          effective_at: The date when this invoice is in effect. Same as `finalized_at` unless
              overwritten. When defined, this value replaces the system-generated 'Date of
              issue' printed on the invoice PDF and receipt.

          expand: Specifies which fields in the response should be expanded.

          footer: Footer to be displayed on the invoice.

          from_invoice: Revise an existing invoice. The new invoice will be created in `status=draft`.
              See the
              [revision documentation](https://docs.stripe.com/invoicing/invoice-revisions)
              for more details.

          issuer: The connected account that issues the invoice. The invoice is presented with the
              branding and support information of the specified account.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          number: Set the number for this invoice. If no number is present then a number will be
              assigned automatically when the invoice is finalized. In many markets,
              regulations require invoices to be unique, sequential and / or gapless. You are
              responsible for ensuring this is true across all your different invoicing
              systems in the event that you edit the invoice number using our API. If you use
              only Stripe for your invoices and do not change invoice numbers, Stripe handles
              this aspect of compliance for you automatically.

          on_behalf_of: The account (if any) for which the funds of the invoice payment are intended. If
              set, the invoice will be presented with the branding and support information of
              the specified account. See the
              [Invoices with Connect](https://docs.stripe.com/billing/invoices/connect)
              documentation for details.

          payment_settings: Configuration settings for the PaymentIntent that is generated when the invoice
              is finalized.

          pending_invoice_items_behavior: How to handle pending invoice items on invoice creation. Defaults to `exclude`
              if the parameter is omitted.

          rendering: The rendering-related settings that control how the invoice is displayed on
              customer-facing surfaces such as PDF and Hosted Invoice Page.

          shipping_cost: Settings for the cost of shipping for this invoice.

          shipping_details: Shipping details for the invoice. The Invoice PDF will use the
              `shipping_details` value if it is set, otherwise the PDF will render the
              shipping address from the customer.

          statement_descriptor: Extra information about a charge for the customer's credit card statement. It
              must contain at least one letter. If not specified and this invoice is part of a
              subscription, the default `statement_descriptor` will be set to the first
              subscription item's product's `statement_descriptor`.

          subscription: The ID of the subscription to invoice, if any. If set, the created invoice will
              only include pending invoice items for that subscription. The subscription's
              billing cycle and regular subscription events won't be affected.

          transfer_data: If specified, the funds from the invoice will be transferred to the destination
              and the ID of the resulting transfer will be found on the invoice's charge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/invoices",
            body=maybe_transform(
                {
                    "account_tax_ids": account_tax_ids,
                    "application_fee_amount": application_fee_amount,
                    "auto_advance": auto_advance,
                    "automatic_tax": automatic_tax,
                    "automatically_finalizes_at": automatically_finalizes_at,
                    "collection_method": collection_method,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "customer": customer,
                    "customer_account": customer_account,
                    "days_until_due": days_until_due,
                    "default_payment_method": default_payment_method,
                    "default_source": default_source,
                    "default_tax_rates": default_tax_rates,
                    "description": description,
                    "discounts": discounts,
                    "due_date": due_date,
                    "effective_at": effective_at,
                    "expand": expand,
                    "footer": footer,
                    "from_invoice": from_invoice,
                    "issuer": issuer,
                    "metadata": metadata,
                    "number": number,
                    "on_behalf_of": on_behalf_of,
                    "payment_settings": payment_settings,
                    "pending_invoice_items_behavior": pending_invoice_items_behavior,
                    "rendering": rendering,
                    "shipping_cost": shipping_cost,
                    "shipping_details": shipping_details,
                    "statement_descriptor": statement_descriptor,
                    "subscription": subscription,
                    "transfer_data": transfer_data,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def list(
        self,
        *,
        collection_method: Literal["charge_automatically", "send_invoice"] | Omit = omit,
        created: invoice_list_params.Created | Omit = omit,
        customer: str | Omit = omit,
        customer_account: str | Omit = omit,
        due_date: invoice_list_params.DueDate | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        status: Literal["draft", "open", "paid", "uncollectible", "void"] | Omit = omit,
        subscription: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[Invoice]:
        """<p>You can list all invoices, or list the invoices for a specific customer.

        The invoices are returned sorted by creation date, with the most recently created invoices appearing first.</p>

        Args:
          collection_method: The collection method of the invoice to retrieve. Either `charge_automatically`
              or `send_invoice`.

          created: Only return invoices that were created during the given date interval.

          customer: Only return invoices for the customer specified by this customer ID.

          customer_account: Only return invoices for the account representing the customer specified by this
              account ID.

          ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, starting with `obj_bar`, your subsequent call can include
              `ending_before=obj_bar` in order to fetch the previous page of the list.

          expand: Specifies which fields in the response should be expanded.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 10.

          starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, ending with `obj_foo`, your subsequent call can include
              `starting_after=obj_foo` in order to fetch the next page of the list.

          status: The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or
              `void`.
              [Learn more](https://docs.stripe.com/billing/invoices/workflow#workflow-overview)

          subscription: Only return invoices for the subscription specified by this subscription ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/invoices",
            page=SyncMyCursorIDPage[Invoice],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_method": collection_method,
                        "created": created,
                        "customer": customer,
                        "customer_account": customer_account,
                        "due_date": due_date,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "starting_after": starting_after,
                        "status": status,
                        "subscription": subscription,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=Invoice,
        )

    def finalize(
        self,
        invoice: str,
        *,
        auto_advance: bool | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        <p>Stripe automatically finalizes drafts before sending and attempting payment on invoices. However, if you’d like to finalize a draft invoice manually, you can do so using this method.</p>

        Args:
          auto_advance: Controls whether Stripe performs
              [automatic collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
              of the invoice. If `false`, the invoice's state doesn't automatically advance
              without an explicit action.

          expand: Specifies which fields in the response should be expanded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice:
            raise ValueError(f"Expected a non-empty value for `invoice` but received {invoice!r}")
        return self._post(
            path_template("/v1/invoices/{invoice}/finalize", invoice=invoice),
            body=maybe_transform(
                {
                    "auto_advance": auto_advance,
                    "expand": expand,
                },
                invoice_finalize_params.InvoiceFinalizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )


class AsyncInvoicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-commons/stripe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-commons/stripe-python#with_streaming_response
        """
        return AsyncInvoicesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_tax_ids: Union[SequenceNotStr[str], Literal[""]] | Omit = omit,
        application_fee_amount: int | Omit = omit,
        auto_advance: bool | Omit = omit,
        automatic_tax: invoice_create_params.AutomaticTax | Omit = omit,
        automatically_finalizes_at: int | Omit = omit,
        collection_method: Literal["charge_automatically", "send_invoice"] | Omit = omit,
        currency: str | Omit = omit,
        custom_fields: Union[Iterable[invoice_create_params.CustomFieldsCustomFieldsList], Literal[""]] | Omit = omit,
        customer: str | Omit = omit,
        customer_account: str | Omit = omit,
        days_until_due: int | Omit = omit,
        default_payment_method: str | Omit = omit,
        default_source: str | Omit = omit,
        default_tax_rates: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        discounts: Union[Iterable[invoice_create_params.DiscountsDiscountsList], Literal[""]] | Omit = omit,
        due_date: int | Omit = omit,
        effective_at: int | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        footer: str | Omit = omit,
        from_invoice: invoice_create_params.FromInvoice | Omit = omit,
        issuer: invoice_create_params.Issuer | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        number: str | Omit = omit,
        on_behalf_of: str | Omit = omit,
        payment_settings: invoice_create_params.PaymentSettings | Omit = omit,
        pending_invoice_items_behavior: Literal["exclude", "include"] | Omit = omit,
        rendering: invoice_create_params.Rendering | Omit = omit,
        shipping_cost: invoice_create_params.ShippingCost | Omit = omit,
        shipping_details: invoice_create_params.ShippingDetails | Omit = omit,
        statement_descriptor: str | Omit = omit,
        subscription: str | Omit = omit,
        transfer_data: invoice_create_params.TransferData | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """<p>This endpoint creates a draft invoice for a given customer.

        The invoice remains a draft until you <a href="#finalize_invoice">finalize</a> the invoice, which allows you to <a href="/api/invoices/pay">pay</a> or <a href="/api/invoices/send">send</a> the invoice to your customers.</p>

        Args:
          account_tax_ids: The account tax IDs associated with the invoice. Only editable when the invoice
              is a draft.

          application_fee_amount: A fee in cents (or local equivalent) that will be applied to the invoice and
              transferred to the application owner's Stripe account. The request must be made
              with an OAuth key or the Stripe-Account header in order to take an application
              fee. For more information, see the application fees
              [documentation](https://docs.stripe.com/billing/invoices/connect#collecting-fees).

          auto_advance: Controls whether Stripe performs
              [automatic collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
              of the invoice. If `false`, the invoice's state doesn't automatically advance
              without an explicit action. Defaults to false.

          automatic_tax: Settings for automatic tax lookup for this invoice.

          automatically_finalizes_at: The time when this invoice should be scheduled to finalize (up to 5 years in the
              future). The invoice is finalized at this time if it's still in draft state.

          collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically,
              Stripe will attempt to pay this invoice using the default source attached to the
              customer. When sending an invoice, Stripe will email this invoice to the
              customer with payment instructions. Defaults to `charge_automatically`.

          currency: The currency to create this invoice in. Defaults to that of `customer` if not
              specified.

          custom_fields: A list of up to 4 custom fields to be displayed on the invoice.

          customer: The ID of the customer to bill.

          customer_account: The ID of the account to bill.

          days_until_due: The number of days from when the invoice is created until it is due. Valid only
              for invoices where `collection_method=send_invoice`.

          default_payment_method: ID of the default payment method for the invoice. It must belong to the customer
              associated with the invoice. If not set, defaults to the subscription's default
              payment method, if any, or to the default payment method in the customer's
              invoice settings.

          default_source: ID of the default payment source for the invoice. It must belong to the customer
              associated with the invoice and be in a chargeable state. If not set, defaults
              to the subscription's default source, if any, or to the customer's default
              source.

          default_tax_rates: The tax rates that will apply to any line item that does not have `tax_rates`
              set.

          description: An arbitrary string attached to the object. Often useful for displaying to
              users. Referenced as 'memo' in the Dashboard.

          discounts: The coupons and promotion codes to redeem into discounts for the invoice. If not
              specified, inherits the discount from the invoice's customer. Pass an empty
              string to avoid inheriting any discounts.

          due_date: The date on which payment for this invoice is due. Valid only for invoices where
              `collection_method=send_invoice`.

          effective_at: The date when this invoice is in effect. Same as `finalized_at` unless
              overwritten. When defined, this value replaces the system-generated 'Date of
              issue' printed on the invoice PDF and receipt.

          expand: Specifies which fields in the response should be expanded.

          footer: Footer to be displayed on the invoice.

          from_invoice: Revise an existing invoice. The new invoice will be created in `status=draft`.
              See the
              [revision documentation](https://docs.stripe.com/invoicing/invoice-revisions)
              for more details.

          issuer: The connected account that issues the invoice. The invoice is presented with the
              branding and support information of the specified account.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          number: Set the number for this invoice. If no number is present then a number will be
              assigned automatically when the invoice is finalized. In many markets,
              regulations require invoices to be unique, sequential and / or gapless. You are
              responsible for ensuring this is true across all your different invoicing
              systems in the event that you edit the invoice number using our API. If you use
              only Stripe for your invoices and do not change invoice numbers, Stripe handles
              this aspect of compliance for you automatically.

          on_behalf_of: The account (if any) for which the funds of the invoice payment are intended. If
              set, the invoice will be presented with the branding and support information of
              the specified account. See the
              [Invoices with Connect](https://docs.stripe.com/billing/invoices/connect)
              documentation for details.

          payment_settings: Configuration settings for the PaymentIntent that is generated when the invoice
              is finalized.

          pending_invoice_items_behavior: How to handle pending invoice items on invoice creation. Defaults to `exclude`
              if the parameter is omitted.

          rendering: The rendering-related settings that control how the invoice is displayed on
              customer-facing surfaces such as PDF and Hosted Invoice Page.

          shipping_cost: Settings for the cost of shipping for this invoice.

          shipping_details: Shipping details for the invoice. The Invoice PDF will use the
              `shipping_details` value if it is set, otherwise the PDF will render the
              shipping address from the customer.

          statement_descriptor: Extra information about a charge for the customer's credit card statement. It
              must contain at least one letter. If not specified and this invoice is part of a
              subscription, the default `statement_descriptor` will be set to the first
              subscription item's product's `statement_descriptor`.

          subscription: The ID of the subscription to invoice, if any. If set, the created invoice will
              only include pending invoice items for that subscription. The subscription's
              billing cycle and regular subscription events won't be affected.

          transfer_data: If specified, the funds from the invoice will be transferred to the destination
              and the ID of the resulting transfer will be found on the invoice's charge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/invoices",
            body=await async_maybe_transform(
                {
                    "account_tax_ids": account_tax_ids,
                    "application_fee_amount": application_fee_amount,
                    "auto_advance": auto_advance,
                    "automatic_tax": automatic_tax,
                    "automatically_finalizes_at": automatically_finalizes_at,
                    "collection_method": collection_method,
                    "currency": currency,
                    "custom_fields": custom_fields,
                    "customer": customer,
                    "customer_account": customer_account,
                    "days_until_due": days_until_due,
                    "default_payment_method": default_payment_method,
                    "default_source": default_source,
                    "default_tax_rates": default_tax_rates,
                    "description": description,
                    "discounts": discounts,
                    "due_date": due_date,
                    "effective_at": effective_at,
                    "expand": expand,
                    "footer": footer,
                    "from_invoice": from_invoice,
                    "issuer": issuer,
                    "metadata": metadata,
                    "number": number,
                    "on_behalf_of": on_behalf_of,
                    "payment_settings": payment_settings,
                    "pending_invoice_items_behavior": pending_invoice_items_behavior,
                    "rendering": rendering,
                    "shipping_cost": shipping_cost,
                    "shipping_details": shipping_details,
                    "statement_descriptor": statement_descriptor,
                    "subscription": subscription,
                    "transfer_data": transfer_data,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def list(
        self,
        *,
        collection_method: Literal["charge_automatically", "send_invoice"] | Omit = omit,
        created: invoice_list_params.Created | Omit = omit,
        customer: str | Omit = omit,
        customer_account: str | Omit = omit,
        due_date: invoice_list_params.DueDate | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        status: Literal["draft", "open", "paid", "uncollectible", "void"] | Omit = omit,
        subscription: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Invoice, AsyncMyCursorIDPage[Invoice]]:
        """<p>You can list all invoices, or list the invoices for a specific customer.

        The invoices are returned sorted by creation date, with the most recently created invoices appearing first.</p>

        Args:
          collection_method: The collection method of the invoice to retrieve. Either `charge_automatically`
              or `send_invoice`.

          created: Only return invoices that were created during the given date interval.

          customer: Only return invoices for the customer specified by this customer ID.

          customer_account: Only return invoices for the account representing the customer specified by this
              account ID.

          ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, starting with `obj_bar`, your subsequent call can include
              `ending_before=obj_bar` in order to fetch the previous page of the list.

          expand: Specifies which fields in the response should be expanded.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 10.

          starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, ending with `obj_foo`, your subsequent call can include
              `starting_after=obj_foo` in order to fetch the next page of the list.

          status: The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or
              `void`.
              [Learn more](https://docs.stripe.com/billing/invoices/workflow#workflow-overview)

          subscription: Only return invoices for the subscription specified by this subscription ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/invoices",
            page=AsyncMyCursorIDPage[Invoice],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "collection_method": collection_method,
                        "created": created,
                        "customer": customer,
                        "customer_account": customer_account,
                        "due_date": due_date,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "starting_after": starting_after,
                        "status": status,
                        "subscription": subscription,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=Invoice,
        )

    async def finalize(
        self,
        invoice: str,
        *,
        auto_advance: bool | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Invoice:
        """
        <p>Stripe automatically finalizes drafts before sending and attempting payment on invoices. However, if you’d like to finalize a draft invoice manually, you can do so using this method.</p>

        Args:
          auto_advance: Controls whether Stripe performs
              [automatic collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
              of the invoice. If `false`, the invoice's state doesn't automatically advance
              without an explicit action.

          expand: Specifies which fields in the response should be expanded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice:
            raise ValueError(f"Expected a non-empty value for `invoice` but received {invoice!r}")
        return await self._post(
            path_template("/v1/invoices/{invoice}/finalize", invoice=invoice),
            body=await async_maybe_transform(
                {
                    "auto_advance": auto_advance,
                    "expand": expand,
                },
                invoice_finalize_params.InvoiceFinalizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )


class InvoicesResourceWithRawResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_raw_response_wrapper(
            invoices.create,
        )
        self.list = to_raw_response_wrapper(
            invoices.list,
        )
        self.finalize = to_raw_response_wrapper(
            invoices.finalize,
        )


class AsyncInvoicesResourceWithRawResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_raw_response_wrapper(
            invoices.create,
        )
        self.list = async_to_raw_response_wrapper(
            invoices.list,
        )
        self.finalize = async_to_raw_response_wrapper(
            invoices.finalize,
        )


class InvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.create = to_streamed_response_wrapper(
            invoices.create,
        )
        self.list = to_streamed_response_wrapper(
            invoices.list,
        )
        self.finalize = to_streamed_response_wrapper(
            invoices.finalize,
        )


class AsyncInvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.create = async_to_streamed_response_wrapper(
            invoices.create,
        )
        self.list = async_to_streamed_response_wrapper(
            invoices.list,
        )
        self.finalize = async_to_streamed_response_wrapper(
            invoices.finalize,
        )
