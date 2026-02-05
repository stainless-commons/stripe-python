# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal

import httpx

from ..types import coupon_list_params, coupon_create_params
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
from ..types.coupon import Coupon

__all__ = ["CouponsResource", "AsyncCouponsResource"]


class CouponsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CouponsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return CouponsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CouponsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return CouponsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str | Omit = omit,
        amount_off: int | Omit = omit,
        applies_to: coupon_create_params.AppliesTo | Omit = omit,
        currency: str | Omit = omit,
        currency_options: Dict[str, coupon_create_params.CurrencyOptions] | Omit = omit,
        duration: Literal["forever", "once", "repeating"] | Omit = omit,
        duration_in_months: int | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        max_redemptions: int | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        name: str | Omit = omit,
        percent_off: float | Omit = omit,
        redeem_by: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Coupon:
        """
        <p>You can create coupons easily via the <a href="https://dashboard.stripe.com/coupons">coupon management</a> page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.</p>

        <p>A coupon has either a <code>percent_off</code> or an <code>amount_off</code> and <code>currency</code>. If you set an <code>amount_off</code>, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of <currency>100</currency> will have a final total of <currency>0</currency> if a coupon with an <code>amount_off</code> of <amount>200</amount> is applied to it and an invoice with a subtotal of <currency>300</currency> will have a final total of <currency>100</currency> if a coupon with an <code>amount_off</code> of <amount>200</amount> is applied to it.</p>

        Args:
          id: Unique string of your choice that will be used to identify this coupon when
              applying it to a customer. If you don't want to specify a particular code, you
              can leave the ID blank and we'll generate a random code for you.

          amount_off: A positive integer representing the amount to subtract from an invoice total
              (required if `percent_off` is not passed).

          applies_to: A hash containing directions for what this Coupon will apply discounts to.

          currency: Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of
              the `amount_off` parameter (required if `amount_off` is passed).

          currency_options: Coupons defined in each available currency option (only supported if
              `amount_off` is passed). Each key must be a three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a
              [supported currency](https://stripe.com/docs/currencies).

          duration: Specifies how long the discount will be in effect if used on a subscription.
              Defaults to `once`.

          duration_in_months: Required only if `duration` is `repeating`, in which case it must be a positive
              integer that specifies the number of months the discount will be in effect.

          expand: Specifies which fields in the response should be expanded.

          max_redemptions: A positive integer specifying the number of times the coupon can be redeemed
              before it's no longer valid. For example, you might have a 50% off coupon that
              the first 20 readers of your blog can use.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          name: Name of the coupon displayed to customers on, for instance invoices, or
              receipts. By default the `id` is shown if `name` is not set.

          percent_off: A positive float larger than 0, and smaller or equal to 100, that represents the
              discount the coupon will apply (required if `amount_off` is not passed).

          redeem_by: Unix timestamp specifying the last time at which the coupon can be redeemed
              (cannot be set to more than 5 years in the future). After the redeem_by date,
              the coupon can no longer be applied to new customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/coupons",
            body=maybe_transform(
                {
                    "id": id,
                    "amount_off": amount_off,
                    "applies_to": applies_to,
                    "currency": currency,
                    "currency_options": currency_options,
                    "duration": duration,
                    "duration_in_months": duration_in_months,
                    "expand": expand,
                    "max_redemptions": max_redemptions,
                    "metadata": metadata,
                    "name": name,
                    "percent_off": percent_off,
                    "redeem_by": redeem_by,
                },
                coupon_create_params.CouponCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Coupon,
        )

    def list(
        self,
        *,
        created: coupon_list_params.Created | Omit = omit,
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
    ) -> SyncMyCursorIDPage[Coupon]:
        """
        <p>Returns a list of your coupons.</p>

        Args:
          created: A filter on the list, based on the object `created` field. The value can be a
              string with an integer Unix timestamp, or it can be a dictionary with a number
              of different query options.

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
        return self._get_api_list(
            "/v1/coupons",
            page=SyncMyCursorIDPage[Coupon],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    coupon_list_params.CouponListParams,
                ),
            ),
            model=Coupon,
        )


class AsyncCouponsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCouponsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCouponsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCouponsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return AsyncCouponsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str | Omit = omit,
        amount_off: int | Omit = omit,
        applies_to: coupon_create_params.AppliesTo | Omit = omit,
        currency: str | Omit = omit,
        currency_options: Dict[str, coupon_create_params.CurrencyOptions] | Omit = omit,
        duration: Literal["forever", "once", "repeating"] | Omit = omit,
        duration_in_months: int | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        max_redemptions: int | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        name: str | Omit = omit,
        percent_off: float | Omit = omit,
        redeem_by: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Coupon:
        """
        <p>You can create coupons easily via the <a href="https://dashboard.stripe.com/coupons">coupon management</a> page of the Stripe dashboard. Coupon creation is also accessible via the API if you need to create coupons on the fly.</p>

        <p>A coupon has either a <code>percent_off</code> or an <code>amount_off</code> and <code>currency</code>. If you set an <code>amount_off</code>, that amount will be subtracted from any invoice’s subtotal. For example, an invoice with a subtotal of <currency>100</currency> will have a final total of <currency>0</currency> if a coupon with an <code>amount_off</code> of <amount>200</amount> is applied to it and an invoice with a subtotal of <currency>300</currency> will have a final total of <currency>100</currency> if a coupon with an <code>amount_off</code> of <amount>200</amount> is applied to it.</p>

        Args:
          id: Unique string of your choice that will be used to identify this coupon when
              applying it to a customer. If you don't want to specify a particular code, you
              can leave the ID blank and we'll generate a random code for you.

          amount_off: A positive integer representing the amount to subtract from an invoice total
              (required if `percent_off` is not passed).

          applies_to: A hash containing directions for what this Coupon will apply discounts to.

          currency: Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of
              the `amount_off` parameter (required if `amount_off` is passed).

          currency_options: Coupons defined in each available currency option (only supported if
              `amount_off` is passed). Each key must be a three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a
              [supported currency](https://stripe.com/docs/currencies).

          duration: Specifies how long the discount will be in effect if used on a subscription.
              Defaults to `once`.

          duration_in_months: Required only if `duration` is `repeating`, in which case it must be a positive
              integer that specifies the number of months the discount will be in effect.

          expand: Specifies which fields in the response should be expanded.

          max_redemptions: A positive integer specifying the number of times the coupon can be redeemed
              before it's no longer valid. For example, you might have a 50% off coupon that
              the first 20 readers of your blog can use.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          name: Name of the coupon displayed to customers on, for instance invoices, or
              receipts. By default the `id` is shown if `name` is not set.

          percent_off: A positive float larger than 0, and smaller or equal to 100, that represents the
              discount the coupon will apply (required if `amount_off` is not passed).

          redeem_by: Unix timestamp specifying the last time at which the coupon can be redeemed
              (cannot be set to more than 5 years in the future). After the redeem_by date,
              the coupon can no longer be applied to new customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/coupons",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "amount_off": amount_off,
                    "applies_to": applies_to,
                    "currency": currency,
                    "currency_options": currency_options,
                    "duration": duration,
                    "duration_in_months": duration_in_months,
                    "expand": expand,
                    "max_redemptions": max_redemptions,
                    "metadata": metadata,
                    "name": name,
                    "percent_off": percent_off,
                    "redeem_by": redeem_by,
                },
                coupon_create_params.CouponCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Coupon,
        )

    def list(
        self,
        *,
        created: coupon_list_params.Created | Omit = omit,
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
    ) -> AsyncPaginator[Coupon, AsyncMyCursorIDPage[Coupon]]:
        """
        <p>Returns a list of your coupons.</p>

        Args:
          created: A filter on the list, based on the object `created` field. The value can be a
              string with an integer Unix timestamp, or it can be a dictionary with a number
              of different query options.

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
        return self._get_api_list(
            "/v1/coupons",
            page=AsyncMyCursorIDPage[Coupon],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    coupon_list_params.CouponListParams,
                ),
            ),
            model=Coupon,
        )


class CouponsResourceWithRawResponse:
    def __init__(self, coupons: CouponsResource) -> None:
        self._coupons = coupons

        self.create = to_raw_response_wrapper(
            coupons.create,
        )
        self.list = to_raw_response_wrapper(
            coupons.list,
        )


class AsyncCouponsResourceWithRawResponse:
    def __init__(self, coupons: AsyncCouponsResource) -> None:
        self._coupons = coupons

        self.create = async_to_raw_response_wrapper(
            coupons.create,
        )
        self.list = async_to_raw_response_wrapper(
            coupons.list,
        )


class CouponsResourceWithStreamingResponse:
    def __init__(self, coupons: CouponsResource) -> None:
        self._coupons = coupons

        self.create = to_streamed_response_wrapper(
            coupons.create,
        )
        self.list = to_streamed_response_wrapper(
            coupons.list,
        )


class AsyncCouponsResourceWithStreamingResponse:
    def __init__(self, coupons: AsyncCouponsResource) -> None:
        self._coupons = coupons

        self.create = async_to_streamed_response_wrapper(
            coupons.create,
        )
        self.list = async_to_streamed_response_wrapper(
            coupons.list,
        )
