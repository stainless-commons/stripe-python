# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainless_commons_stripe import Stripe, AsyncStripe
from stainless_commons_stripe.types import Customer
from stainless_commons_stripe.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Stripe) -> None:
        customer = client.customers.create()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Stripe) -> None:
        customer = client.customers.create(
            address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            balance=0,
            business_name="string",
            cash_balance={"settings": {"reconciliation_mode": "automatic"}},
            description="description",
            email="email",
            expand=["string"],
            individual_name="string",
            invoice_prefix="invoice_prefix",
            invoice_settings={
                "custom_fields": [
                    {
                        "name": "name",
                        "value": "value",
                    }
                ],
                "default_payment_method": "default_payment_method",
                "footer": "footer",
                "rendering_options": {
                    "amount_tax_display": "",
                    "template": "template",
                },
            },
            metadata={"foo": "string"},
            name="name",
            next_invoice_sequence=0,
            payment_method="payment_method",
            phone="phone",
            preferred_locales=["string"],
            shipping={
                "address": {
                    "city": "city",
                    "country": "country",
                    "line1": "line1",
                    "line2": "line2",
                    "postal_code": "postal_code",
                    "state": "state",
                },
                "name": "name",
                "phone": "phone",
            },
            source="source",
            tax={
                "ip_address": "string",
                "validate_location": "deferred",
            },
            tax_exempt="",
            tax_id_data=[
                {
                    "type": "ad_nrt",
                    "value": "value",
                }
            ],
            test_clock="test_clock",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Stripe) -> None:
        response = client.customers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Stripe) -> None:
        with client.customers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Stripe) -> None:
        customer = client.customers.list()
        assert_matches_type(SyncMyCursorIDPage[Customer], customer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Stripe) -> None:
        customer = client.customers.list(
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            email="email",
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            starting_after="starting_after",
            test_clock="test_clock",
        )
        assert_matches_type(SyncMyCursorIDPage[Customer], customer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Stripe) -> None:
        response = client.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(SyncMyCursorIDPage[Customer], customer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Stripe) -> None:
        with client.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(SyncMyCursorIDPage[Customer], customer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStripe) -> None:
        customer = await async_client.customers.create()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStripe) -> None:
        customer = await async_client.customers.create(
            address={
                "city": "city",
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "postal_code": "postal_code",
                "state": "state",
            },
            balance=0,
            business_name="string",
            cash_balance={"settings": {"reconciliation_mode": "automatic"}},
            description="description",
            email="email",
            expand=["string"],
            individual_name="string",
            invoice_prefix="invoice_prefix",
            invoice_settings={
                "custom_fields": [
                    {
                        "name": "name",
                        "value": "value",
                    }
                ],
                "default_payment_method": "default_payment_method",
                "footer": "footer",
                "rendering_options": {
                    "amount_tax_display": "",
                    "template": "template",
                },
            },
            metadata={"foo": "string"},
            name="name",
            next_invoice_sequence=0,
            payment_method="payment_method",
            phone="phone",
            preferred_locales=["string"],
            shipping={
                "address": {
                    "city": "city",
                    "country": "country",
                    "line1": "line1",
                    "line2": "line2",
                    "postal_code": "postal_code",
                    "state": "state",
                },
                "name": "name",
                "phone": "phone",
            },
            source="source",
            tax={
                "ip_address": "string",
                "validate_location": "deferred",
            },
            tax_exempt="",
            tax_id_data=[
                {
                    "type": "ad_nrt",
                    "value": "value",
                }
            ],
            test_clock="test_clock",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStripe) -> None:
        response = await async_client.customers.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStripe) -> None:
        async with async_client.customers.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStripe) -> None:
        customer = await async_client.customers.list()
        assert_matches_type(AsyncMyCursorIDPage[Customer], customer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStripe) -> None:
        customer = await async_client.customers.list(
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            email="email",
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            starting_after="starting_after",
            test_clock="test_clock",
        )
        assert_matches_type(AsyncMyCursorIDPage[Customer], customer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStripe) -> None:
        response = await async_client.customers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[Customer], customer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStripe) -> None:
        async with async_client.customers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[Customer], customer, path=["response"])

        assert cast(Any, response.is_closed) is True
