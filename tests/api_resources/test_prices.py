# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stripe_minimal import Stripe, AsyncStripe
from stripe_minimal.types import Price, PriceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Stripe) -> None:
        price = client.prices.create(
            currency="currency",
        )
        assert_matches_type(Price, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stripe) -> None:
        price = client.prices.create(
            currency="currency",
            active=True,
            billing_scheme="per_unit",
            currency_options={
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
            custom_unit_amount={
                "enabled": True,
                "maximum": 0,
                "minimum": 0,
                "preset": 0,
            },
            expand=["string"],
            lookup_key="lookup_key",
            metadata={"foo": "string"},
            nickname="nickname",
            product="product",
            product_data={
                "name": "name",
                "id": "id",
                "active": True,
                "metadata": {"foo": "string"},
                "statement_descriptor": "statement_descriptor",
                "tax_code": "tax_code",
                "unit_label": "unit_label",
            },
            recurring={
                "interval": "day",
                "interval_count": 0,
                "meter": "meter",
                "usage_type": "licensed",
            },
            tax_behavior="exclusive",
            tiers=[
                {
                    "up_to": "inf",
                    "flat_amount": 0,
                    "flat_amount_decimal": "flat_amount_decimal",
                    "unit_amount": 0,
                    "unit_amount_decimal": "unit_amount_decimal",
                }
            ],
            tiers_mode="graduated",
            transfer_lookup_key=True,
            transform_quantity={
                "divide_by": 0,
                "round": "down",
            },
            unit_amount=0,
            unit_amount_decimal="unit_amount_decimal",
        )
        assert_matches_type(Price, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stripe) -> None:
        response = client.prices.with_raw_response.create(
            currency="currency",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(Price, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stripe) -> None:
        with client.prices.with_streaming_response.create(
            currency="currency",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Stripe) -> None:
        price = client.prices.list()
        assert_matches_type(PriceListResponse, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stripe) -> None:
        price = client.prices.list(
            active=True,
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            currency="currency",
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            lookup_keys=["string"],
            product="product",
            recurring={
                "interval": "day",
                "meter": "meter",
                "usage_type": "licensed",
            },
            starting_after="starting_after",
            type="one_time",
        )
        assert_matches_type(PriceListResponse, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stripe) -> None:
        response = client.prices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceListResponse, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stripe) -> None:
        with client.prices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(PriceListResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStripe) -> None:
        price = await async_client.prices.create(
            currency="currency",
        )
        assert_matches_type(Price, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStripe) -> None:
        price = await async_client.prices.create(
            currency="currency",
            active=True,
            billing_scheme="per_unit",
            currency_options={
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
            custom_unit_amount={
                "enabled": True,
                "maximum": 0,
                "minimum": 0,
                "preset": 0,
            },
            expand=["string"],
            lookup_key="lookup_key",
            metadata={"foo": "string"},
            nickname="nickname",
            product="product",
            product_data={
                "name": "name",
                "id": "id",
                "active": True,
                "metadata": {"foo": "string"},
                "statement_descriptor": "statement_descriptor",
                "tax_code": "tax_code",
                "unit_label": "unit_label",
            },
            recurring={
                "interval": "day",
                "interval_count": 0,
                "meter": "meter",
                "usage_type": "licensed",
            },
            tax_behavior="exclusive",
            tiers=[
                {
                    "up_to": "inf",
                    "flat_amount": 0,
                    "flat_amount_decimal": "flat_amount_decimal",
                    "unit_amount": 0,
                    "unit_amount_decimal": "unit_amount_decimal",
                }
            ],
            tiers_mode="graduated",
            transfer_lookup_key=True,
            transform_quantity={
                "divide_by": 0,
                "round": "down",
            },
            unit_amount=0,
            unit_amount_decimal="unit_amount_decimal",
        )
        assert_matches_type(Price, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStripe) -> None:
        response = await async_client.prices.with_raw_response.create(
            currency="currency",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = await response.parse()
        assert_matches_type(Price, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStripe) -> None:
        async with async_client.prices.with_streaming_response.create(
            currency="currency",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(Price, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStripe) -> None:
        price = await async_client.prices.list()
        assert_matches_type(PriceListResponse, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStripe) -> None:
        price = await async_client.prices.list(
            active=True,
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            currency="currency",
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            lookup_keys=["string"],
            product="product",
            recurring={
                "interval": "day",
                "meter": "meter",
                "usage_type": "licensed",
            },
            starting_after="starting_after",
            type="one_time",
        )
        assert_matches_type(PriceListResponse, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStripe) -> None:
        response = await async_client.prices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = await response.parse()
        assert_matches_type(PriceListResponse, price, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStripe) -> None:
        async with async_client.prices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(PriceListResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True
