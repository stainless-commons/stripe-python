# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stripe_minimal import Stripe, AsyncStripe
from stripe_minimal.types import PaymentIntentListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentIntents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Stripe) -> None:
        payment_intent = client.payment_intents.list()
        assert_matches_type(PaymentIntentListResponse, payment_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stripe) -> None:
        payment_intent = client.payment_intents.list(
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            customer="customer",
            customer_account="customer_account",
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            starting_after="starting_after",
        )
        assert_matches_type(PaymentIntentListResponse, payment_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stripe) -> None:
        response = client.payment_intents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_intent = response.parse()
        assert_matches_type(PaymentIntentListResponse, payment_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stripe) -> None:
        with client.payment_intents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_intent = response.parse()
            assert_matches_type(PaymentIntentListResponse, payment_intent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentIntents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStripe) -> None:
        payment_intent = await async_client.payment_intents.list()
        assert_matches_type(PaymentIntentListResponse, payment_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStripe) -> None:
        payment_intent = await async_client.payment_intents.list(
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            customer="customer",
            customer_account="customer_account",
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            starting_after="starting_after",
        )
        assert_matches_type(PaymentIntentListResponse, payment_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStripe) -> None:
        response = await async_client.payment_intents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_intent = await response.parse()
        assert_matches_type(PaymentIntentListResponse, payment_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStripe) -> None:
        async with async_client.payment_intents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_intent = await response.parse()
            assert_matches_type(PaymentIntentListResponse, payment_intent, path=["response"])

        assert cast(Any, response.is_closed) is True
