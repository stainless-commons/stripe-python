# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainless_commons_stripe import Stripe, AsyncStripe
from stainless_commons_stripe.types import Refund

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRefunds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Stripe) -> None:
        refund = client.refunds.create()
        assert_matches_type(Refund, refund, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stripe) -> None:
        refund = client.refunds.create(
            amount=0,
            charge="charge",
            currency="currency",
            customer="customer",
            expand=["string"],
            instructions_email="instructions_email",
            metadata={"foo": "string"},
            origin="customer_balance",
            payment_intent="payment_intent",
            reason="duplicate",
            refund_application_fee=True,
            reverse_transfer=True,
        )
        assert_matches_type(Refund, refund, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stripe) -> None:
        response = client.refunds.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        refund = response.parse()
        assert_matches_type(Refund, refund, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stripe) -> None:
        with client.refunds.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            refund = response.parse()
            assert_matches_type(Refund, refund, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRefunds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStripe) -> None:
        refund = await async_client.refunds.create()
        assert_matches_type(Refund, refund, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStripe) -> None:
        refund = await async_client.refunds.create(
            amount=0,
            charge="charge",
            currency="currency",
            customer="customer",
            expand=["string"],
            instructions_email="instructions_email",
            metadata={"foo": "string"},
            origin="customer_balance",
            payment_intent="payment_intent",
            reason="duplicate",
            refund_application_fee=True,
            reverse_transfer=True,
        )
        assert_matches_type(Refund, refund, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStripe) -> None:
        response = await async_client.refunds.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        refund = await response.parse()
        assert_matches_type(Refund, refund, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStripe) -> None:
        async with async_client.refunds.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            refund = await response.parse()
            assert_matches_type(Refund, refund, path=["response"])

        assert cast(Any, response.is_closed) is True
