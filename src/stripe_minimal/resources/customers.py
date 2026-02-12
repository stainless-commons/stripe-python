# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import customer_list_params, customer_create_params
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
from ..pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.customer import Customer

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-commons/stripe-python#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-commons/stripe-python#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address: customer_create_params.Address | Omit = omit,
        balance: int | Omit = omit,
        business_name: Union[str, Literal[""]] | Omit = omit,
        cash_balance: customer_create_params.CashBalance | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        individual_name: Union[str, Literal[""]] | Omit = omit,
        invoice_prefix: str | Omit = omit,
        invoice_settings: customer_create_params.InvoiceSettings | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        name: str | Omit = omit,
        next_invoice_sequence: int | Omit = omit,
        payment_method: str | Omit = omit,
        phone: str | Omit = omit,
        preferred_locales: SequenceNotStr[str] | Omit = omit,
        shipping: customer_create_params.Shipping | Omit = omit,
        source: str | Omit = omit,
        tax: customer_create_params.Tax | Omit = omit,
        tax_exempt: Literal["", "exempt", "none", "reverse"] | Omit = omit,
        tax_id_data: Iterable[customer_create_params.TaxIDData] | Omit = omit,
        test_clock: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
        """<p>Creates a new customer object.</p>

        Args:
          address: The customer's address.

        Learn about
              [country-specific requirements for calculating tax](https://docs.stripe.com/invoicing/taxes?dashboard-or-api=dashboard#set-up-customer).

          balance: An integer amount in cents (or local equivalent) that represents the customer's
              current balance, which affect the customer's future invoices. A negative amount
              represents a credit that decreases the amount due on an invoice; a positive
              amount increases the amount due on an invoice.

          business_name: The customer's business name. This may be up to _150 characters_.

          cash_balance: Balance information and default balance settings for this customer.

          description: An arbitrary string that you can attach to a customer object. It is displayed
              alongside the customer in the dashboard.

          email: Customer's email address. It's displayed alongside the customer in your
              dashboard and can be useful for searching and tracking. This may be up to _512
              characters_.

          expand: Specifies which fields in the response should be expanded.

          individual_name: The customer's full name. This may be up to _150 characters_.

          invoice_prefix: The prefix for the customer used to generate unique invoice numbers. Must be
              3–12 uppercase letters or numbers.

          invoice_settings: Default invoice settings for this customer.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          name: The customer's full name or business name.

          next_invoice_sequence: The sequence to be used on the customer's next invoice. Defaults to 1.

          phone: The customer's phone number.

          preferred_locales: Customer's preferred languages, ordered by preference.

          shipping: The customer's shipping information. Appears on invoices emailed to this
              customer.

          tax: Tax details about the customer.

          tax_exempt: The customer's tax exemption. One of `none`, `exempt`, or `reverse`.

          tax_id_data: The customer's tax IDs.

          test_clock: ID of the test clock to attach to the customer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/customers",
            body=maybe_transform(
                {
                    "address": address,
                    "balance": balance,
                    "business_name": business_name,
                    "cash_balance": cash_balance,
                    "description": description,
                    "email": email,
                    "expand": expand,
                    "individual_name": individual_name,
                    "invoice_prefix": invoice_prefix,
                    "invoice_settings": invoice_settings,
                    "metadata": metadata,
                    "name": name,
                    "next_invoice_sequence": next_invoice_sequence,
                    "payment_method": payment_method,
                    "phone": phone,
                    "preferred_locales": preferred_locales,
                    "shipping": shipping,
                    "source": source,
                    "tax": tax,
                    "tax_exempt": tax_exempt,
                    "tax_id_data": tax_id_data,
                    "test_clock": test_clock,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def list(
        self,
        *,
        created: customer_list_params.Created | Omit = omit,
        email: str | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        test_clock: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[Customer]:
        """<p>Returns a list of your customers.

        The customers are returned sorted by creation date, with the most recent customers appearing first.</p>

        Args:
          created: Only return customers that were created during the given date interval.

          email: A case-sensitive filter on the list based on the customer's `email` field. The
              value must be a string.

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

          test_clock: Provides a list of customers that are associated with the specified test clock.
              The response will not include customers with test clocks if this parameter is
              not set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/customers",
            page=SyncMyCursorIDPage[Customer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "email": email,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "starting_after": starting_after,
                        "test_clock": test_clock,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=Customer,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-commons/stripe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-commons/stripe-python#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address: customer_create_params.Address | Omit = omit,
        balance: int | Omit = omit,
        business_name: Union[str, Literal[""]] | Omit = omit,
        cash_balance: customer_create_params.CashBalance | Omit = omit,
        description: str | Omit = omit,
        email: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        individual_name: Union[str, Literal[""]] | Omit = omit,
        invoice_prefix: str | Omit = omit,
        invoice_settings: customer_create_params.InvoiceSettings | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        name: str | Omit = omit,
        next_invoice_sequence: int | Omit = omit,
        payment_method: str | Omit = omit,
        phone: str | Omit = omit,
        preferred_locales: SequenceNotStr[str] | Omit = omit,
        shipping: customer_create_params.Shipping | Omit = omit,
        source: str | Omit = omit,
        tax: customer_create_params.Tax | Omit = omit,
        tax_exempt: Literal["", "exempt", "none", "reverse"] | Omit = omit,
        tax_id_data: Iterable[customer_create_params.TaxIDData] | Omit = omit,
        test_clock: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Customer:
        """<p>Creates a new customer object.</p>

        Args:
          address: The customer's address.

        Learn about
              [country-specific requirements for calculating tax](https://docs.stripe.com/invoicing/taxes?dashboard-or-api=dashboard#set-up-customer).

          balance: An integer amount in cents (or local equivalent) that represents the customer's
              current balance, which affect the customer's future invoices. A negative amount
              represents a credit that decreases the amount due on an invoice; a positive
              amount increases the amount due on an invoice.

          business_name: The customer's business name. This may be up to _150 characters_.

          cash_balance: Balance information and default balance settings for this customer.

          description: An arbitrary string that you can attach to a customer object. It is displayed
              alongside the customer in the dashboard.

          email: Customer's email address. It's displayed alongside the customer in your
              dashboard and can be useful for searching and tracking. This may be up to _512
              characters_.

          expand: Specifies which fields in the response should be expanded.

          individual_name: The customer's full name. This may be up to _150 characters_.

          invoice_prefix: The prefix for the customer used to generate unique invoice numbers. Must be
              3–12 uppercase letters or numbers.

          invoice_settings: Default invoice settings for this customer.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          name: The customer's full name or business name.

          next_invoice_sequence: The sequence to be used on the customer's next invoice. Defaults to 1.

          phone: The customer's phone number.

          preferred_locales: Customer's preferred languages, ordered by preference.

          shipping: The customer's shipping information. Appears on invoices emailed to this
              customer.

          tax: Tax details about the customer.

          tax_exempt: The customer's tax exemption. One of `none`, `exempt`, or `reverse`.

          tax_id_data: The customer's tax IDs.

          test_clock: ID of the test clock to attach to the customer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/customers",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "balance": balance,
                    "business_name": business_name,
                    "cash_balance": cash_balance,
                    "description": description,
                    "email": email,
                    "expand": expand,
                    "individual_name": individual_name,
                    "invoice_prefix": invoice_prefix,
                    "invoice_settings": invoice_settings,
                    "metadata": metadata,
                    "name": name,
                    "next_invoice_sequence": next_invoice_sequence,
                    "payment_method": payment_method,
                    "phone": phone,
                    "preferred_locales": preferred_locales,
                    "shipping": shipping,
                    "source": source,
                    "tax": tax,
                    "tax_exempt": tax_exempt,
                    "tax_id_data": tax_id_data,
                    "test_clock": test_clock,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def list(
        self,
        *,
        created: customer_list_params.Created | Omit = omit,
        email: str | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        test_clock: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Customer, AsyncMyCursorIDPage[Customer]]:
        """<p>Returns a list of your customers.

        The customers are returned sorted by creation date, with the most recent customers appearing first.</p>

        Args:
          created: Only return customers that were created during the given date interval.

          email: A case-sensitive filter on the list based on the customer's `email` field. The
              value must be a string.

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

          test_clock: Provides a list of customers that are associated with the specified test clock.
              The response will not include customers with test clocks if this parameter is
              not set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/customers",
            page=AsyncMyCursorIDPage[Customer],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "email": email,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "starting_after": starting_after,
                        "test_clock": test_clock,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=Customer,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
