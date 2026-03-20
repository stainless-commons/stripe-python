# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal

import httpx

from ..types import dispute_list_params, dispute_update_params
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
from ..types.dispute import Dispute

__all__ = ["DisputesResource", "AsyncDisputesResource"]


class DisputesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-commons/stripe-python#accessing-raw-response-data-eg-headers
        """
        return DisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-commons/stripe-python#with_streaming_response
        """
        return DisputesResourceWithStreamingResponse(self)

    def update(
        self,
        dispute: str,
        *,
        evidence: dispute_update_params.Evidence | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        submit: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dispute:
        """
        <p>When you get a dispute, contacting your customer is always the best first step. If that doesn’t work, you can submit evidence to help us resolve the dispute in your favor. You can do this in your <a href="https://dashboard.stripe.com/disputes">dashboard</a>, but if you prefer, you can use the API to submit evidence programmatically.</p>

        <p>Depending on your dispute type, different evidence fields will give you a better chance of winning your dispute. To figure out which evidence fields to provide, see our <a href="/docs/disputes/categories">guide to dispute types</a>.</p>

        Args:
          evidence: Evidence to upload, to respond to a dispute. Updating any field in the hash will
              submit all fields in the hash for review. The combined character count of all
              fields is limited to 150,000.

          expand: Specifies which fields in the response should be expanded.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          submit: Whether to immediately submit evidence to the bank. If `false`, evidence is
              staged on the dispute. Staged evidence is visible in the API and Dashboard, and
              can be submitted to the bank by making another request with this attribute set
              to `true` (the default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute:
            raise ValueError(f"Expected a non-empty value for `dispute` but received {dispute!r}")
        return self._post(
            path_template("/v1/disputes/{dispute}", dispute=dispute),
            body=maybe_transform(
                {
                    "evidence": evidence,
                    "expand": expand,
                    "metadata": metadata,
                    "submit": submit,
                },
                dispute_update_params.DisputeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def list(
        self,
        *,
        charge: str | Omit = omit,
        created: dispute_list_params.Created | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        payment_intent: str | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[Dispute]:
        """
        <p>Returns a list of your disputes.</p>

        Args:
          charge: Only return disputes associated to the charge specified by this charge ID.

          created: Only return disputes that were created during the given date interval.

          ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, starting with `obj_bar`, your subsequent call can include
              `ending_before=obj_bar` in order to fetch the previous page of the list.

          expand: Specifies which fields in the response should be expanded.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 10.

          payment_intent: Only return disputes associated to the PaymentIntent specified by this
              PaymentIntent ID.

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
            "/v1/disputes",
            page=SyncMyCursorIDPage[Dispute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "charge": charge,
                        "created": created,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "payment_intent": payment_intent,
                        "starting_after": starting_after,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            model=Dispute,
        )


class AsyncDisputesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDisputesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-commons/stripe-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDisputesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDisputesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-commons/stripe-python#with_streaming_response
        """
        return AsyncDisputesResourceWithStreamingResponse(self)

    async def update(
        self,
        dispute: str,
        *,
        evidence: dispute_update_params.Evidence | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        submit: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Dispute:
        """
        <p>When you get a dispute, contacting your customer is always the best first step. If that doesn’t work, you can submit evidence to help us resolve the dispute in your favor. You can do this in your <a href="https://dashboard.stripe.com/disputes">dashboard</a>, but if you prefer, you can use the API to submit evidence programmatically.</p>

        <p>Depending on your dispute type, different evidence fields will give you a better chance of winning your dispute. To figure out which evidence fields to provide, see our <a href="/docs/disputes/categories">guide to dispute types</a>.</p>

        Args:
          evidence: Evidence to upload, to respond to a dispute. Updating any field in the hash will
              submit all fields in the hash for review. The combined character count of all
              fields is limited to 150,000.

          expand: Specifies which fields in the response should be expanded.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          submit: Whether to immediately submit evidence to the bank. If `false`, evidence is
              staged on the dispute. Staged evidence is visible in the API and Dashboard, and
              can be submitted to the bank by making another request with this attribute set
              to `true` (the default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute:
            raise ValueError(f"Expected a non-empty value for `dispute` but received {dispute!r}")
        return await self._post(
            path_template("/v1/disputes/{dispute}", dispute=dispute),
            body=await async_maybe_transform(
                {
                    "evidence": evidence,
                    "expand": expand,
                    "metadata": metadata,
                    "submit": submit,
                },
                dispute_update_params.DisputeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Dispute,
        )

    def list(
        self,
        *,
        charge: str | Omit = omit,
        created: dispute_list_params.Created | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        payment_intent: str | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Dispute, AsyncMyCursorIDPage[Dispute]]:
        """
        <p>Returns a list of your disputes.</p>

        Args:
          charge: Only return disputes associated to the charge specified by this charge ID.

          created: Only return disputes that were created during the given date interval.

          ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, starting with `obj_bar`, your subsequent call can include
              `ending_before=obj_bar` in order to fetch the previous page of the list.

          expand: Specifies which fields in the response should be expanded.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 10.

          payment_intent: Only return disputes associated to the PaymentIntent specified by this
              PaymentIntent ID.

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
            "/v1/disputes",
            page=AsyncMyCursorIDPage[Dispute],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "charge": charge,
                        "created": created,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "payment_intent": payment_intent,
                        "starting_after": starting_after,
                    },
                    dispute_list_params.DisputeListParams,
                ),
            ),
            model=Dispute,
        )


class DisputesResourceWithRawResponse:
    def __init__(self, disputes: DisputesResource) -> None:
        self._disputes = disputes

        self.update = to_raw_response_wrapper(
            disputes.update,
        )
        self.list = to_raw_response_wrapper(
            disputes.list,
        )


class AsyncDisputesResourceWithRawResponse:
    def __init__(self, disputes: AsyncDisputesResource) -> None:
        self._disputes = disputes

        self.update = async_to_raw_response_wrapper(
            disputes.update,
        )
        self.list = async_to_raw_response_wrapper(
            disputes.list,
        )


class DisputesResourceWithStreamingResponse:
    def __init__(self, disputes: DisputesResource) -> None:
        self._disputes = disputes

        self.update = to_streamed_response_wrapper(
            disputes.update,
        )
        self.list = to_streamed_response_wrapper(
            disputes.list,
        )


class AsyncDisputesResourceWithStreamingResponse:
    def __init__(self, disputes: AsyncDisputesResource) -> None:
        self._disputes = disputes

        self.update = async_to_streamed_response_wrapper(
            disputes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            disputes.list,
        )
