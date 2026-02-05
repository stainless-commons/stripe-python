# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..types import price_list_params, price_create_params
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
from ..types.price import Price
from .._base_client import make_request_options
from ..types.price_list_response import PriceListResponse

__all__ = ["PricesResource", "AsyncPricesResource"]


class PricesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PricesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return PricesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return PricesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        currency: str,
        active: bool | Omit = omit,
        billing_scheme: Literal["per_unit", "tiered"] | Omit = omit,
        currency_options: Dict[str, price_create_params.CurrencyOptions] | Omit = omit,
        custom_unit_amount: price_create_params.CustomUnitAmount | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        lookup_key: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        nickname: str | Omit = omit,
        product: str | Omit = omit,
        product_data: price_create_params.ProductData | Omit = omit,
        recurring: price_create_params.Recurring | Omit = omit,
        tax_behavior: Literal["exclusive", "inclusive", "unspecified"] | Omit = omit,
        tiers: Iterable[price_create_params.Tier] | Omit = omit,
        tiers_mode: Literal["graduated", "volume"] | Omit = omit,
        transfer_lookup_key: bool | Omit = omit,
        transform_quantity: price_create_params.TransformQuantity | Omit = omit,
        unit_amount: int | Omit = omit,
        unit_amount_decimal: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Price:
        """
        <p>Creates a new <a href="https://docs.stripe.com/api/prices">Price</a> for an existing <a href="https://docs.stripe.com/api/products">Product</a>. The Price can be recurring or one-time.</p>

        Args:
          currency: Three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
              lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          active: Whether the price can be used for new purchases. Defaults to `true`.

          billing_scheme: Describes how to compute the price per period. Either `per_unit` or `tiered`.
              `per_unit` indicates that the fixed amount (specified in `unit_amount` or
              `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with
              `usage_type=licensed`), or per unit of total usage (for prices with
              `usage_type=metered`). `tiered` indicates that the unit pricing will be computed
              using a tiering strategy as defined using the `tiers` and `tiers_mode`
              attributes.

          currency_options: Prices defined in each available currency option. Each key must be a
              three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a
              [supported currency](https://stripe.com/docs/currencies).

          custom_unit_amount: When set, provides configuration for the amount to be adjusted by the customer
              during Checkout Sessions and Payment Links.

          expand: Specifies which fields in the response should be expanded.

          lookup_key: A lookup key used to retrieve prices dynamically from a static string. This may
              be up to 200 characters.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          nickname: A brief description of the price, hidden from customers.

          product: The ID of the [Product](https://docs.stripe.com/api/products) that this
              [Price](https://docs.stripe.com/api/prices) will belong to.

          product_data: These fields can be used to create a new product that this price will belong to.

          recurring: The recurring components of a price such as `interval` and `usage_type`.

          tax_behavior: Only required if a
              [default tax behavior](<https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)>)
              was not provided in the Stripe Tax settings. Specifies whether the price is
              considered inclusive of taxes or exclusive of taxes. One of `inclusive`,
              `exclusive`, or `unspecified`. Once specified as either `inclusive` or
              `exclusive`, it cannot be changed.

          tiers: Each element represents a pricing tier. This parameter requires `billing_scheme`
              to be set to `tiered`. See also the documentation for `billing_scheme`.

          tiers_mode: Defines if the tiering price should be `graduated` or `volume` based. In
              `volume`-based tiering, the maximum quantity within a period determines the per
              unit price, in `graduated` tiering pricing can successively change as the
              quantity grows.

          transfer_lookup_key: If set to true, will atomically remove the lookup key from the existing price,
              and assign it to this price.

          transform_quantity: Apply a transformation to the reported usage or set quantity before computing
              the billed price. Cannot be combined with `tiers`.

          unit_amount: A positive integer in cents (or local equivalent) (or 0 for a free price)
              representing how much to charge. One of `unit_amount`, `unit_amount_decimal`, or
              `custom_unit_amount` is required, unless `billing_scheme=tiered`.

          unit_amount_decimal: Same as `unit_amount`, but accepts a decimal value in cents (or local
              equivalent) with at most 12 decimal places. Only one of `unit_amount` and
              `unit_amount_decimal` can be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/prices",
            body=maybe_transform(
                {
                    "currency": currency,
                    "active": active,
                    "billing_scheme": billing_scheme,
                    "currency_options": currency_options,
                    "custom_unit_amount": custom_unit_amount,
                    "expand": expand,
                    "lookup_key": lookup_key,
                    "metadata": metadata,
                    "nickname": nickname,
                    "product": product,
                    "product_data": product_data,
                    "recurring": recurring,
                    "tax_behavior": tax_behavior,
                    "tiers": tiers,
                    "tiers_mode": tiers_mode,
                    "transfer_lookup_key": transfer_lookup_key,
                    "transform_quantity": transform_quantity,
                    "unit_amount": unit_amount,
                    "unit_amount_decimal": unit_amount_decimal,
                },
                price_create_params.PriceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Price,
        )

    def list(
        self,
        *,
        active: bool | Omit = omit,
        created: price_list_params.Created | Omit = omit,
        currency: str | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        lookup_keys: SequenceNotStr[str] | Omit = omit,
        product: str | Omit = omit,
        recurring: price_list_params.Recurring | Omit = omit,
        starting_after: str | Omit = omit,
        type: Literal["one_time", "recurring"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceListResponse:
        """
        <p>Returns a list of your active prices, excluding <a href="/docs/products-prices/pricing-models#inline-pricing">inline prices</a>. For the list of inactive prices, set <code>active</code> to false.</p>

        Args:
          active: Only return prices that are active or inactive (e.g., pass `false` to list all
              inactive prices).

          created: A filter on the list, based on the object `created` field. The value can be a
              string with an integer Unix timestamp, or it can be a dictionary with a number
              of different query options.

          currency: Only return prices for the given currency.

          ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, starting with `obj_bar`, your subsequent call can include
              `ending_before=obj_bar` in order to fetch the previous page of the list.

          expand: Specifies which fields in the response should be expanded.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 10.

          lookup_keys: Only return the price with these lookup_keys, if any exist. You can specify up
              to 10 lookup_keys.

          product: Only return prices for the given product.

          recurring: Only return prices with these recurring fields.

          starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, ending with `obj_foo`, your subsequent call can include
              `starting_after=obj_foo` in order to fetch the next page of the list.

          type: Only return prices of type `recurring` or `one_time`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/prices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "created": created,
                        "currency": currency,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "lookup_keys": lookup_keys,
                        "product": product,
                        "recurring": recurring,
                        "starting_after": starting_after,
                        "type": type,
                    },
                    price_list_params.PriceListParams,
                ),
            ),
            cast_to=PriceListResponse,
        )


class AsyncPricesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPricesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPricesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return AsyncPricesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        currency: str,
        active: bool | Omit = omit,
        billing_scheme: Literal["per_unit", "tiered"] | Omit = omit,
        currency_options: Dict[str, price_create_params.CurrencyOptions] | Omit = omit,
        custom_unit_amount: price_create_params.CustomUnitAmount | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        lookup_key: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        nickname: str | Omit = omit,
        product: str | Omit = omit,
        product_data: price_create_params.ProductData | Omit = omit,
        recurring: price_create_params.Recurring | Omit = omit,
        tax_behavior: Literal["exclusive", "inclusive", "unspecified"] | Omit = omit,
        tiers: Iterable[price_create_params.Tier] | Omit = omit,
        tiers_mode: Literal["graduated", "volume"] | Omit = omit,
        transfer_lookup_key: bool | Omit = omit,
        transform_quantity: price_create_params.TransformQuantity | Omit = omit,
        unit_amount: int | Omit = omit,
        unit_amount_decimal: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Price:
        """
        <p>Creates a new <a href="https://docs.stripe.com/api/prices">Price</a> for an existing <a href="https://docs.stripe.com/api/products">Product</a>. The Price can be recurring or one-time.</p>

        Args:
          currency: Three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
              lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).

          active: Whether the price can be used for new purchases. Defaults to `true`.

          billing_scheme: Describes how to compute the price per period. Either `per_unit` or `tiered`.
              `per_unit` indicates that the fixed amount (specified in `unit_amount` or
              `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with
              `usage_type=licensed`), or per unit of total usage (for prices with
              `usage_type=metered`). `tiered` indicates that the unit pricing will be computed
              using a tiering strategy as defined using the `tiers` and `tiers_mode`
              attributes.

          currency_options: Prices defined in each available currency option. Each key must be a
              three-letter
              [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a
              [supported currency](https://stripe.com/docs/currencies).

          custom_unit_amount: When set, provides configuration for the amount to be adjusted by the customer
              during Checkout Sessions and Payment Links.

          expand: Specifies which fields in the response should be expanded.

          lookup_key: A lookup key used to retrieve prices dynamically from a static string. This may
              be up to 200 characters.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          nickname: A brief description of the price, hidden from customers.

          product: The ID of the [Product](https://docs.stripe.com/api/products) that this
              [Price](https://docs.stripe.com/api/prices) will belong to.

          product_data: These fields can be used to create a new product that this price will belong to.

          recurring: The recurring components of a price such as `interval` and `usage_type`.

          tax_behavior: Only required if a
              [default tax behavior](<https://docs.stripe.com/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)>)
              was not provided in the Stripe Tax settings. Specifies whether the price is
              considered inclusive of taxes or exclusive of taxes. One of `inclusive`,
              `exclusive`, or `unspecified`. Once specified as either `inclusive` or
              `exclusive`, it cannot be changed.

          tiers: Each element represents a pricing tier. This parameter requires `billing_scheme`
              to be set to `tiered`. See also the documentation for `billing_scheme`.

          tiers_mode: Defines if the tiering price should be `graduated` or `volume` based. In
              `volume`-based tiering, the maximum quantity within a period determines the per
              unit price, in `graduated` tiering pricing can successively change as the
              quantity grows.

          transfer_lookup_key: If set to true, will atomically remove the lookup key from the existing price,
              and assign it to this price.

          transform_quantity: Apply a transformation to the reported usage or set quantity before computing
              the billed price. Cannot be combined with `tiers`.

          unit_amount: A positive integer in cents (or local equivalent) (or 0 for a free price)
              representing how much to charge. One of `unit_amount`, `unit_amount_decimal`, or
              `custom_unit_amount` is required, unless `billing_scheme=tiered`.

          unit_amount_decimal: Same as `unit_amount`, but accepts a decimal value in cents (or local
              equivalent) with at most 12 decimal places. Only one of `unit_amount` and
              `unit_amount_decimal` can be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/prices",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "active": active,
                    "billing_scheme": billing_scheme,
                    "currency_options": currency_options,
                    "custom_unit_amount": custom_unit_amount,
                    "expand": expand,
                    "lookup_key": lookup_key,
                    "metadata": metadata,
                    "nickname": nickname,
                    "product": product,
                    "product_data": product_data,
                    "recurring": recurring,
                    "tax_behavior": tax_behavior,
                    "tiers": tiers,
                    "tiers_mode": tiers_mode,
                    "transfer_lookup_key": transfer_lookup_key,
                    "transform_quantity": transform_quantity,
                    "unit_amount": unit_amount,
                    "unit_amount_decimal": unit_amount_decimal,
                },
                price_create_params.PriceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Price,
        )

    async def list(
        self,
        *,
        active: bool | Omit = omit,
        created: price_list_params.Created | Omit = omit,
        currency: str | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        lookup_keys: SequenceNotStr[str] | Omit = omit,
        product: str | Omit = omit,
        recurring: price_list_params.Recurring | Omit = omit,
        starting_after: str | Omit = omit,
        type: Literal["one_time", "recurring"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PriceListResponse:
        """
        <p>Returns a list of your active prices, excluding <a href="/docs/products-prices/pricing-models#inline-pricing">inline prices</a>. For the list of inactive prices, set <code>active</code> to false.</p>

        Args:
          active: Only return prices that are active or inactive (e.g., pass `false` to list all
              inactive prices).

          created: A filter on the list, based on the object `created` field. The value can be a
              string with an integer Unix timestamp, or it can be a dictionary with a number
              of different query options.

          currency: Only return prices for the given currency.

          ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, starting with `obj_bar`, your subsequent call can include
              `ending_before=obj_bar` in order to fetch the previous page of the list.

          expand: Specifies which fields in the response should be expanded.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 10.

          lookup_keys: Only return the price with these lookup_keys, if any exist. You can specify up
              to 10 lookup_keys.

          product: Only return prices for the given product.

          recurring: Only return prices with these recurring fields.

          starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, ending with `obj_foo`, your subsequent call can include
              `starting_after=obj_foo` in order to fetch the next page of the list.

          type: Only return prices of type `recurring` or `one_time`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/prices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active": active,
                        "created": created,
                        "currency": currency,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "lookup_keys": lookup_keys,
                        "product": product,
                        "recurring": recurring,
                        "starting_after": starting_after,
                        "type": type,
                    },
                    price_list_params.PriceListParams,
                ),
            ),
            cast_to=PriceListResponse,
        )


class PricesResourceWithRawResponse:
    def __init__(self, prices: PricesResource) -> None:
        self._prices = prices

        self.create = to_raw_response_wrapper(
            prices.create,
        )
        self.list = to_raw_response_wrapper(
            prices.list,
        )


class AsyncPricesResourceWithRawResponse:
    def __init__(self, prices: AsyncPricesResource) -> None:
        self._prices = prices

        self.create = async_to_raw_response_wrapper(
            prices.create,
        )
        self.list = async_to_raw_response_wrapper(
            prices.list,
        )


class PricesResourceWithStreamingResponse:
    def __init__(self, prices: PricesResource) -> None:
        self._prices = prices

        self.create = to_streamed_response_wrapper(
            prices.create,
        )
        self.list = to_streamed_response_wrapper(
            prices.list,
        )


class AsyncPricesResourceWithStreamingResponse:
    def __init__(self, prices: AsyncPricesResource) -> None:
        self._prices = prices

        self.create = async_to_streamed_response_wrapper(
            prices.create,
        )
        self.list = async_to_streamed_response_wrapper(
            prices.list,
        )
