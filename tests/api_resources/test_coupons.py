# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainless_commons_stripe import Stripe, AsyncStripe
from stainless_commons_stripe.types import Coupon
from stainless_commons_stripe.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCoupons:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Stripe) -> None:
        coupon = client.coupons.create()
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Stripe) -> None:
        coupon = client.coupons.create(
            id="id",
            amount_off=0,
            applies_to={"products": ["string"]},
            currency="currency",
            currency_options={"foo": {"amount_off": 0}},
            duration="forever",
            duration_in_months=0,
            expand=["string"],
            max_redemptions=0,
            metadata={"foo": "string"},
            name="name",
            percent_off=0,
            redeem_by=0,
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Stripe) -> None:
        response = client.coupons.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Stripe) -> None:
        with client.coupons.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Stripe) -> None:
        coupon = client.coupons.list()
        assert_matches_type(SyncMyCursorIDPage[Coupon], coupon, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Stripe) -> None:
        coupon = client.coupons.list(
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            starting_after="starting_after",
        )
        assert_matches_type(SyncMyCursorIDPage[Coupon], coupon, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Stripe) -> None:
        response = client.coupons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(SyncMyCursorIDPage[Coupon], coupon, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Stripe) -> None:
        with client.coupons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(SyncMyCursorIDPage[Coupon], coupon, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCoupons:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStripe) -> None:
        coupon = await async_client.coupons.create()
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStripe) -> None:
        coupon = await async_client.coupons.create(
            id="id",
            amount_off=0,
            applies_to={"products": ["string"]},
            currency="currency",
            currency_options={"foo": {"amount_off": 0}},
            duration="forever",
            duration_in_months=0,
            expand=["string"],
            max_redemptions=0,
            metadata={"foo": "string"},
            name="name",
            percent_off=0,
            redeem_by=0,
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStripe) -> None:
        response = await async_client.coupons.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStripe) -> None:
        async with async_client.coupons.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStripe) -> None:
        coupon = await async_client.coupons.list()
        assert_matches_type(AsyncMyCursorIDPage[Coupon], coupon, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStripe) -> None:
        coupon = await async_client.coupons.list(
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncMyCursorIDPage[Coupon], coupon, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStripe) -> None:
        response = await async_client.coupons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[Coupon], coupon, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStripe) -> None:
        async with async_client.coupons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[Coupon], coupon, path=["response"])

        assert cast(Any, response.is_closed) is True
