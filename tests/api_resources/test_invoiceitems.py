# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainless_commons_stripe import Stripe, AsyncStripe
from stainless_commons_stripe.types import InvoiceitemCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoiceitems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Stripe) -> None:
        invoiceitem = client.invoiceitems.create()
        assert_matches_type(InvoiceitemCreateResponse, invoiceitem, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stripe) -> None:
        invoiceitem = client.invoiceitems.create(
            amount=0,
            currency="currency",
            customer="customer",
            customer_account="customer_account",
            description="description",
            discountable=True,
            discounts=[
                {
                    "coupon": "coupon",
                    "discount": "discount",
                    "promotion_code": "promotion_code",
                }
            ],
            expand=["string"],
            invoice="invoice",
            metadata={"foo": "string"},
            period={
                "end": 0,
                "start": 0,
            },
            price_data={
                "currency": "currency",
                "product": "product",
                "tax_behavior": "exclusive",
                "unit_amount": 0,
                "unit_amount_decimal": "unit_amount_decimal",
            },
            pricing={"price": "price"},
            quantity=0,
            subscription="subscription",
            tax_behavior="exclusive",
            tax_code="string",
            tax_rates=["string"],
            unit_amount_decimal="unit_amount_decimal",
        )
        assert_matches_type(InvoiceitemCreateResponse, invoiceitem, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stripe) -> None:
        response = client.invoiceitems.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoiceitem = response.parse()
        assert_matches_type(InvoiceitemCreateResponse, invoiceitem, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stripe) -> None:
        with client.invoiceitems.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoiceitem = response.parse()
            assert_matches_type(InvoiceitemCreateResponse, invoiceitem, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvoiceitems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStripe) -> None:
        invoiceitem = await async_client.invoiceitems.create()
        assert_matches_type(InvoiceitemCreateResponse, invoiceitem, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStripe) -> None:
        invoiceitem = await async_client.invoiceitems.create(
            amount=0,
            currency="currency",
            customer="customer",
            customer_account="customer_account",
            description="description",
            discountable=True,
            discounts=[
                {
                    "coupon": "coupon",
                    "discount": "discount",
                    "promotion_code": "promotion_code",
                }
            ],
            expand=["string"],
            invoice="invoice",
            metadata={"foo": "string"},
            period={
                "end": 0,
                "start": 0,
            },
            price_data={
                "currency": "currency",
                "product": "product",
                "tax_behavior": "exclusive",
                "unit_amount": 0,
                "unit_amount_decimal": "unit_amount_decimal",
            },
            pricing={"price": "price"},
            quantity=0,
            subscription="subscription",
            tax_behavior="exclusive",
            tax_code="string",
            tax_rates=["string"],
            unit_amount_decimal="unit_amount_decimal",
        )
        assert_matches_type(InvoiceitemCreateResponse, invoiceitem, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStripe) -> None:
        response = await async_client.invoiceitems.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoiceitem = await response.parse()
        assert_matches_type(InvoiceitemCreateResponse, invoiceitem, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStripe) -> None:
        async with async_client.invoiceitems.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoiceitem = await response.parse()
            assert_matches_type(InvoiceitemCreateResponse, invoiceitem, path=["response"])

        assert cast(Any, response.is_closed) is True
