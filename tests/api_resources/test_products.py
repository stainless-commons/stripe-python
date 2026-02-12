# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainless_commons_stripe import Stripe, AsyncStripe
from stainless_commons_stripe.types import Product
from stainless_commons_stripe.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Stripe) -> None:
        product = client.products.create(
            name="name",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stripe) -> None:
        product = client.products.create(
            name="name",
            id="id",
            active=True,
            default_price_data={
                "currency": "currency",
                "currency_options": {
                    "foo": {
                        "custom_unit_amount": {
                            "enabled": True,
                            "maximum": 0,
                            "minimum": 0,
                            "preset": 0,
                        },
                        "tax_behavior": "exclusive",
                        "tiers": [
                            {
                                "up_to": "inf",
                                "flat_amount": 0,
                                "flat_amount_decimal": "flat_amount_decimal",
                                "unit_amount": 0,
                                "unit_amount_decimal": "unit_amount_decimal",
                            }
                        ],
                        "unit_amount": 0,
                        "unit_amount_decimal": "unit_amount_decimal",
                    }
                },
                "custom_unit_amount": {
                    "enabled": True,
                    "maximum": 0,
                    "minimum": 0,
                    "preset": 0,
                },
                "metadata": {"foo": "string"},
                "recurring": {
                    "interval": "day",
                    "interval_count": 0,
                },
                "tax_behavior": "exclusive",
                "unit_amount": 0,
                "unit_amount_decimal": "unit_amount_decimal",
            },
            description="description",
            expand=["string"],
            images=["string"],
            marketing_features=[{"name": "name"}],
            metadata={"foo": "string"},
            package_dimensions={
                "height": 0,
                "length": 0,
                "weight": 0,
                "width": 0,
            },
            shippable=True,
            statement_descriptor="statement_descriptor",
            tax_code="tax_code",
            unit_label="unit_label",
            url="url",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stripe) -> None:
        response = client.products.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stripe) -> None:
        with client.products.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Stripe) -> None:
        product = client.products.list()
        assert_matches_type(SyncMyCursorIDPage[Product], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stripe) -> None:
        product = client.products.list(
            active=True,
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            ending_before="ending_before",
            expand=["string"],
            ids=["string"],
            limit=0,
            shippable=True,
            starting_after="starting_after",
            url="url",
        )
        assert_matches_type(SyncMyCursorIDPage[Product], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stripe) -> None:
        response = client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(SyncMyCursorIDPage[Product], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stripe) -> None:
        with client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(SyncMyCursorIDPage[Product], product, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStripe) -> None:
        product = await async_client.products.create(
            name="name",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStripe) -> None:
        product = await async_client.products.create(
            name="name",
            id="id",
            active=True,
            default_price_data={
                "currency": "currency",
                "currency_options": {
                    "foo": {
                        "custom_unit_amount": {
                            "enabled": True,
                            "maximum": 0,
                            "minimum": 0,
                            "preset": 0,
                        },
                        "tax_behavior": "exclusive",
                        "tiers": [
                            {
                                "up_to": "inf",
                                "flat_amount": 0,
                                "flat_amount_decimal": "flat_amount_decimal",
                                "unit_amount": 0,
                                "unit_amount_decimal": "unit_amount_decimal",
                            }
                        ],
                        "unit_amount": 0,
                        "unit_amount_decimal": "unit_amount_decimal",
                    }
                },
                "custom_unit_amount": {
                    "enabled": True,
                    "maximum": 0,
                    "minimum": 0,
                    "preset": 0,
                },
                "metadata": {"foo": "string"},
                "recurring": {
                    "interval": "day",
                    "interval_count": 0,
                },
                "tax_behavior": "exclusive",
                "unit_amount": 0,
                "unit_amount_decimal": "unit_amount_decimal",
            },
            description="description",
            expand=["string"],
            images=["string"],
            marketing_features=[{"name": "name"}],
            metadata={"foo": "string"},
            package_dimensions={
                "height": 0,
                "length": 0,
                "weight": 0,
                "width": 0,
            },
            shippable=True,
            statement_descriptor="statement_descriptor",
            tax_code="tax_code",
            unit_label="unit_label",
            url="url",
        )
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStripe) -> None:
        response = await async_client.products.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(Product, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStripe) -> None:
        async with async_client.products.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(Product, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStripe) -> None:
        product = await async_client.products.list()
        assert_matches_type(AsyncMyCursorIDPage[Product], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStripe) -> None:
        product = await async_client.products.list(
            active=True,
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            ending_before="ending_before",
            expand=["string"],
            ids=["string"],
            limit=0,
            shippable=True,
            starting_after="starting_after",
            url="url",
        )
        assert_matches_type(AsyncMyCursorIDPage[Product], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStripe) -> None:
        response = await async_client.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[Product], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStripe) -> None:
        async with async_client.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[Product], product, path=["response"])

        assert cast(Any, response.is_closed) is True
