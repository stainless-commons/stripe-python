# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal

import httpx

from ..types import refund_create_params
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
from ..types.refund import Refund

__all__ = ["RefundsResource", "AsyncRefundsResource"]


class RefundsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RefundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return RefundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RefundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return RefundsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int | Omit = omit,
        charge: str | Omit = omit,
        currency: str | Omit = omit,
        customer: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        instructions_email: str | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        origin: Literal["customer_balance"] | Omit = omit,
        payment_intent: str | Omit = omit,
        reason: Literal["duplicate", "fraudulent", "requested_by_customer"] | Omit = omit,
        refund_application_fee: bool | Omit = omit,
        reverse_transfer: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Refund:
        """
        <p>When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.</p>

        <p>Creating a new refund will refund a charge that has previously been created but not yet refunded.
        Funds will be refunded to the credit or debit card that was originally charged.</p>

        <p>You can optionally refund only part of a charge.
        You can do so multiple times, until the entire charge has been refunded.</p>

        <p>Once entirely refunded, a charge can’t be refunded again.
        This method will raise an error when called on an already-refunded charge,
        or when trying to refund more money than is left on a charge.</p>

        Args:
          charge: The identifier of the charge to refund.

          currency: Three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
              lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          customer: Customer whose customer balance to refund from.

          expand: Specifies which fields in the response should be expanded.

          instructions_email: For payment methods without native refund support (e.g., Konbini, PromptPay),
              use this email from the customer to receive refund instructions.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          origin: Origin of the refund

          payment_intent: The identifier of the PaymentIntent to refund.

          reason: String indicating the reason for the refund. If set, possible values are
              `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the
              charge to be fraudulent, specifying `fraudulent` as the reason will add the
              associated card and email to your
              [block lists](https://docs.stripe.com/radar/lists), and will also help us
              improve our fraud detection algorithms.

          refund_application_fee: Boolean indicating whether the application fee should be refunded when refunding
              this charge. If a full charge refund is given, the full application fee will be
              refunded. Otherwise, the application fee will be refunded in an amount
              proportional to the amount of the charge refunded. An application fee can be
              refunded only by the application that created the charge.

          reverse_transfer: Boolean indicating whether the transfer should be reversed when refunding this
              charge. The transfer will be reversed proportionally to the amount being
              refunded (either the entire or partial amount).

              A transfer can be reversed only by the application that created the charge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/refunds",
            body=maybe_transform(
                {
                    "amount": amount,
                    "charge": charge,
                    "currency": currency,
                    "customer": customer,
                    "expand": expand,
                    "instructions_email": instructions_email,
                    "metadata": metadata,
                    "origin": origin,
                    "payment_intent": payment_intent,
                    "reason": reason,
                    "refund_application_fee": refund_application_fee,
                    "reverse_transfer": reverse_transfer,
                },
                refund_create_params.RefundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Refund,
        )


class AsyncRefundsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRefundsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRefundsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRefundsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return AsyncRefundsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int | Omit = omit,
        charge: str | Omit = omit,
        currency: str | Omit = omit,
        customer: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        instructions_email: str | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        origin: Literal["customer_balance"] | Omit = omit,
        payment_intent: str | Omit = omit,
        reason: Literal["duplicate", "fraudulent", "requested_by_customer"] | Omit = omit,
        refund_application_fee: bool | Omit = omit,
        reverse_transfer: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Refund:
        """
        <p>When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.</p>

        <p>Creating a new refund will refund a charge that has previously been created but not yet refunded.
        Funds will be refunded to the credit or debit card that was originally charged.</p>

        <p>You can optionally refund only part of a charge.
        You can do so multiple times, until the entire charge has been refunded.</p>

        <p>Once entirely refunded, a charge can’t be refunded again.
        This method will raise an error when called on an already-refunded charge,
        or when trying to refund more money than is left on a charge.</p>

        Args:
          charge: The identifier of the charge to refund.

          currency: Three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
              lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          customer: Customer whose customer balance to refund from.

          expand: Specifies which fields in the response should be expanded.

          instructions_email: For payment methods without native refund support (e.g., Konbini, PromptPay),
              use this email from the customer to receive refund instructions.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          origin: Origin of the refund

          payment_intent: The identifier of the PaymentIntent to refund.

          reason: String indicating the reason for the refund. If set, possible values are
              `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the
              charge to be fraudulent, specifying `fraudulent` as the reason will add the
              associated card and email to your
              [block lists](https://docs.stripe.com/radar/lists), and will also help us
              improve our fraud detection algorithms.

          refund_application_fee: Boolean indicating whether the application fee should be refunded when refunding
              this charge. If a full charge refund is given, the full application fee will be
              refunded. Otherwise, the application fee will be refunded in an amount
              proportional to the amount of the charge refunded. An application fee can be
              refunded only by the application that created the charge.

          reverse_transfer: Boolean indicating whether the transfer should be reversed when refunding this
              charge. The transfer will be reversed proportionally to the amount being
              refunded (either the entire or partial amount).

              A transfer can be reversed only by the application that created the charge.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/refunds",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "charge": charge,
                    "currency": currency,
                    "customer": customer,
                    "expand": expand,
                    "instructions_email": instructions_email,
                    "metadata": metadata,
                    "origin": origin,
                    "payment_intent": payment_intent,
                    "reason": reason,
                    "refund_application_fee": refund_application_fee,
                    "reverse_transfer": reverse_transfer,
                },
                refund_create_params.RefundCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Refund,
        )


class RefundsResourceWithRawResponse:
    def __init__(self, refunds: RefundsResource) -> None:
        self._refunds = refunds

        self.create = to_raw_response_wrapper(
            refunds.create,
        )


class AsyncRefundsResourceWithRawResponse:
    def __init__(self, refunds: AsyncRefundsResource) -> None:
        self._refunds = refunds

        self.create = async_to_raw_response_wrapper(
            refunds.create,
        )


class RefundsResourceWithStreamingResponse:
    def __init__(self, refunds: RefundsResource) -> None:
        self._refunds = refunds

        self.create = to_streamed_response_wrapper(
            refunds.create,
        )


class AsyncRefundsResourceWithStreamingResponse:
    def __init__(self, refunds: AsyncRefundsResource) -> None:
        self._refunds = refunds

        self.create = async_to_streamed_response_wrapper(
            refunds.create,
        )
