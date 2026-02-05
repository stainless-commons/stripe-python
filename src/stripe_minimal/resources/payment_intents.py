# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import payment_intent_list_params
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
from ..types.payment_intent_list_response import PaymentIntentListResponse

__all__ = ["PaymentIntentsResource", "AsyncPaymentIntentsResource"]


class PaymentIntentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentIntentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return PaymentIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentIntentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return PaymentIntentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        created: payment_intent_list_params.Created | Omit = omit,
        customer: str | Omit = omit,
        customer_account: str | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentIntentListResponse:
        """
        <p>Returns a list of PaymentIntents.</p>

        Args:
          created: A filter on the list, based on the object `created` field. The value can be a
              string with an integer Unix timestamp or a dictionary with a number of different
              query options.

          customer: Only return PaymentIntents for the customer that this customer ID specifies.

          customer_account: Only return PaymentIntents for the account representing the customer that this
              ID specifies.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/payment_intents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "customer": customer,
                        "customer_account": customer_account,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    payment_intent_list_params.PaymentIntentListParams,
                ),
            ),
            cast_to=PaymentIntentListResponse,
        )


class AsyncPaymentIntentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentIntentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentIntentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return AsyncPaymentIntentsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        created: payment_intent_list_params.Created | Omit = omit,
        customer: str | Omit = omit,
        customer_account: str | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentIntentListResponse:
        """
        <p>Returns a list of PaymentIntents.</p>

        Args:
          created: A filter on the list, based on the object `created` field. The value can be a
              string with an integer Unix timestamp or a dictionary with a number of different
              query options.

          customer: Only return PaymentIntents for the customer that this customer ID specifies.

          customer_account: Only return PaymentIntents for the account representing the customer that this
              ID specifies.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/payment_intents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created": created,
                        "customer": customer,
                        "customer_account": customer_account,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    payment_intent_list_params.PaymentIntentListParams,
                ),
            ),
            cast_to=PaymentIntentListResponse,
        )


class PaymentIntentsResourceWithRawResponse:
    def __init__(self, payment_intents: PaymentIntentsResource) -> None:
        self._payment_intents = payment_intents

        self.list = to_raw_response_wrapper(
            payment_intents.list,
        )


class AsyncPaymentIntentsResourceWithRawResponse:
    def __init__(self, payment_intents: AsyncPaymentIntentsResource) -> None:
        self._payment_intents = payment_intents

        self.list = async_to_raw_response_wrapper(
            payment_intents.list,
        )


class PaymentIntentsResourceWithStreamingResponse:
    def __init__(self, payment_intents: PaymentIntentsResource) -> None:
        self._payment_intents = payment_intents

        self.list = to_streamed_response_wrapper(
            payment_intents.list,
        )


class AsyncPaymentIntentsResourceWithStreamingResponse:
    def __init__(self, payment_intents: AsyncPaymentIntentsResource) -> None:
        self._payment_intents = payment_intents

        self.list = async_to_streamed_response_wrapper(
            payment_intents.list,
        )
