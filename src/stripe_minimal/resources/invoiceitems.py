# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import invoiceitem_create_params
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
from ..types.invoiceitem_create_response import InvoiceitemCreateResponse

__all__ = ["InvoiceitemsResource", "AsyncInvoiceitemsResource"]


class InvoiceitemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoiceitemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return InvoiceitemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoiceitemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return InvoiceitemsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int | Omit = omit,
        currency: str | Omit = omit,
        customer: str | Omit = omit,
        customer_account: str | Omit = omit,
        description: str | Omit = omit,
        discountable: bool | Omit = omit,
        discounts: Union[Iterable[invoiceitem_create_params.DiscountsUnionMember0], Literal[""]] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        invoice: str | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        period: invoiceitem_create_params.Period | Omit = omit,
        price_data: invoiceitem_create_params.PriceData | Omit = omit,
        pricing: invoiceitem_create_params.Pricing | Omit = omit,
        quantity: int | Omit = omit,
        subscription: str | Omit = omit,
        tax_behavior: Literal["exclusive", "inclusive", "unspecified"] | Omit = omit,
        tax_code: Union[str, Literal[""]] | Omit = omit,
        tax_rates: SequenceNotStr[str] | Omit = omit,
        unit_amount_decimal: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceitemCreateResponse:
        """<p>Creates an item to be added to a draft invoice (up to 250 items per invoice).

        If no invoice is specified, the item will be on the next invoice created for the customer specified.</p>

        Args:
          amount: The integer amount in cents (or local equivalent) of the charge to be applied to
              the upcoming invoice. Passing in a negative `amount` will reduce the
              `amount_due` on the invoice.

          currency: Three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
              lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          customer: The ID of the customer to bill for this invoice item.

          customer_account: The ID of the account representing the customer to bill for this invoice item.

          description: An arbitrary string which you can attach to the invoice item. The description is
              displayed in the invoice for easy tracking.

          discountable: Controls whether discounts apply to this invoice item. Defaults to false for
              prorations or negative invoice items, and true for all other invoice items.

          discounts: The coupons and promotion codes to redeem into discounts for the invoice item or
              invoice line item.

          expand: Specifies which fields in the response should be expanded.

          invoice: The ID of an existing invoice to add this invoice item to. For subscription
              invoices, when left blank, the invoice item will be added to the next upcoming
              scheduled invoice. For standalone invoices, the invoice item won't be
              automatically added unless you pass `pending_invoice_item_behavior: 'include'`
              when creating the invoice. This is useful when adding invoice items in response
              to an invoice.created webhook. You can only add invoice items to draft invoices
              and there is a maximum of 250 items per invoice.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          period: The period associated with this invoice item. When set to different values, the
              period will be rendered on the invoice. If you have
              [Stripe Revenue Recognition](https://docs.stripe.com/revenue-recognition)
              enabled, the period will be used to recognize and defer revenue. See the
              [Revenue Recognition documentation](https://docs.stripe.com/revenue-recognition/methodology/subscriptions-and-invoicing)
              for details.

          price_data: Data used to generate a new [Price](https://docs.stripe.com/api/prices) object
              inline.

          pricing: The pricing information for the invoice item.

          quantity: Non-negative integer. The quantity of units for the invoice item.

          subscription: The ID of a subscription to add this invoice item to. When left blank, the
              invoice item is added to the next upcoming scheduled invoice. When set,
              scheduled invoices for subscriptions other than the specified subscription will
              ignore the invoice item. Use this when you want to express that an invoice item
              has been accrued within the context of a particular subscription.

          tax_behavior: Only required if a
              [default tax behavior](<https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)>)
              was not provided in the Stripe Tax settings. Specifies whether the price is
              considered inclusive of taxes or exclusive of taxes. One of `inclusive`,
              `exclusive`, or `unspecified`. Once specified as either `inclusive` or
              `exclusive`, it cannot be changed.

          tax_code: A [tax code](https://docs.stripe.com/tax/tax-categories) ID.

          tax_rates: The tax rates which apply to the invoice item. When set, the `default_tax_rates`
              on the invoice do not apply to this invoice item.

          unit_amount_decimal: The decimal unit amount in cents (or local equivalent) of the charge to be
              applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied
              by the quantity to get the full amount. Passing in a negative
              `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at
              most 12 decimal places.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/invoiceitems",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "customer": customer,
                    "customer_account": customer_account,
                    "description": description,
                    "discountable": discountable,
                    "discounts": discounts,
                    "expand": expand,
                    "invoice": invoice,
                    "metadata": metadata,
                    "period": period,
                    "price_data": price_data,
                    "pricing": pricing,
                    "quantity": quantity,
                    "subscription": subscription,
                    "tax_behavior": tax_behavior,
                    "tax_code": tax_code,
                    "tax_rates": tax_rates,
                    "unit_amount_decimal": unit_amount_decimal,
                },
                invoiceitem_create_params.InvoiceitemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceitemCreateResponse,
        )


class AsyncInvoiceitemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvoiceitemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoiceitemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoiceitemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return AsyncInvoiceitemsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int | Omit = omit,
        currency: str | Omit = omit,
        customer: str | Omit = omit,
        customer_account: str | Omit = omit,
        description: str | Omit = omit,
        discountable: bool | Omit = omit,
        discounts: Union[Iterable[invoiceitem_create_params.DiscountsUnionMember0], Literal[""]] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        invoice: str | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        period: invoiceitem_create_params.Period | Omit = omit,
        price_data: invoiceitem_create_params.PriceData | Omit = omit,
        pricing: invoiceitem_create_params.Pricing | Omit = omit,
        quantity: int | Omit = omit,
        subscription: str | Omit = omit,
        tax_behavior: Literal["exclusive", "inclusive", "unspecified"] | Omit = omit,
        tax_code: Union[str, Literal[""]] | Omit = omit,
        tax_rates: SequenceNotStr[str] | Omit = omit,
        unit_amount_decimal: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceitemCreateResponse:
        """<p>Creates an item to be added to a draft invoice (up to 250 items per invoice).

        If no invoice is specified, the item will be on the next invoice created for the customer specified.</p>

        Args:
          amount: The integer amount in cents (or local equivalent) of the charge to be applied to
              the upcoming invoice. Passing in a negative `amount` will reduce the
              `amount_due` on the invoice.

          currency: Three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
              lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          customer: The ID of the customer to bill for this invoice item.

          customer_account: The ID of the account representing the customer to bill for this invoice item.

          description: An arbitrary string which you can attach to the invoice item. The description is
              displayed in the invoice for easy tracking.

          discountable: Controls whether discounts apply to this invoice item. Defaults to false for
              prorations or negative invoice items, and true for all other invoice items.

          discounts: The coupons and promotion codes to redeem into discounts for the invoice item or
              invoice line item.

          expand: Specifies which fields in the response should be expanded.

          invoice: The ID of an existing invoice to add this invoice item to. For subscription
              invoices, when left blank, the invoice item will be added to the next upcoming
              scheduled invoice. For standalone invoices, the invoice item won't be
              automatically added unless you pass `pending_invoice_item_behavior: 'include'`
              when creating the invoice. This is useful when adding invoice items in response
              to an invoice.created webhook. You can only add invoice items to draft invoices
              and there is a maximum of 250 items per invoice.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          period: The period associated with this invoice item. When set to different values, the
              period will be rendered on the invoice. If you have
              [Stripe Revenue Recognition](https://docs.stripe.com/revenue-recognition)
              enabled, the period will be used to recognize and defer revenue. See the
              [Revenue Recognition documentation](https://docs.stripe.com/revenue-recognition/methodology/subscriptions-and-invoicing)
              for details.

          price_data: Data used to generate a new [Price](https://docs.stripe.com/api/prices) object
              inline.

          pricing: The pricing information for the invoice item.

          quantity: Non-negative integer. The quantity of units for the invoice item.

          subscription: The ID of a subscription to add this invoice item to. When left blank, the
              invoice item is added to the next upcoming scheduled invoice. When set,
              scheduled invoices for subscriptions other than the specified subscription will
              ignore the invoice item. Use this when you want to express that an invoice item
              has been accrued within the context of a particular subscription.

          tax_behavior: Only required if a
              [default tax behavior](<https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)>)
              was not provided in the Stripe Tax settings. Specifies whether the price is
              considered inclusive of taxes or exclusive of taxes. One of `inclusive`,
              `exclusive`, or `unspecified`. Once specified as either `inclusive` or
              `exclusive`, it cannot be changed.

          tax_code: A [tax code](https://docs.stripe.com/tax/tax-categories) ID.

          tax_rates: The tax rates which apply to the invoice item. When set, the `default_tax_rates`
              on the invoice do not apply to this invoice item.

          unit_amount_decimal: The decimal unit amount in cents (or local equivalent) of the charge to be
              applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied
              by the quantity to get the full amount. Passing in a negative
              `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at
              most 12 decimal places.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/invoiceitems",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "customer": customer,
                    "customer_account": customer_account,
                    "description": description,
                    "discountable": discountable,
                    "discounts": discounts,
                    "expand": expand,
                    "invoice": invoice,
                    "metadata": metadata,
                    "period": period,
                    "price_data": price_data,
                    "pricing": pricing,
                    "quantity": quantity,
                    "subscription": subscription,
                    "tax_behavior": tax_behavior,
                    "tax_code": tax_code,
                    "tax_rates": tax_rates,
                    "unit_amount_decimal": unit_amount_decimal,
                },
                invoiceitem_create_params.InvoiceitemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceitemCreateResponse,
        )


class InvoiceitemsResourceWithRawResponse:
    def __init__(self, invoiceitems: InvoiceitemsResource) -> None:
        self._invoiceitems = invoiceitems

        self.create = to_raw_response_wrapper(
            invoiceitems.create,
        )


class AsyncInvoiceitemsResourceWithRawResponse:
    def __init__(self, invoiceitems: AsyncInvoiceitemsResource) -> None:
        self._invoiceitems = invoiceitems

        self.create = async_to_raw_response_wrapper(
            invoiceitems.create,
        )


class InvoiceitemsResourceWithStreamingResponse:
    def __init__(self, invoiceitems: InvoiceitemsResource) -> None:
        self._invoiceitems = invoiceitems

        self.create = to_streamed_response_wrapper(
            invoiceitems.create,
        )


class AsyncInvoiceitemsResourceWithStreamingResponse:
    def __init__(self, invoiceitems: AsyncInvoiceitemsResource) -> None:
        self._invoiceitems = invoiceitems

        self.create = async_to_streamed_response_wrapper(
            invoiceitems.create,
        )
