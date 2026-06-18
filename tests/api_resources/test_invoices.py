# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainless_commons_stripe import Stripe, AsyncStripe
from stainless_commons_stripe.types import Invoice
from stainless_commons_stripe.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Stripe) -> None:
        invoice = client.invoices.create()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Stripe) -> None:
        invoice = client.invoices.create(
            account_tax_ids="",
            application_fee_amount=0,
            auto_advance=True,
            automatic_tax={
                "enabled": True,
                "liability": {
                    "type": "account",
                    "account": "account",
                },
            },
            automatically_finalizes_at=0,
            collection_method="charge_automatically",
            currency="currency",
            custom_fields="",
            customer="customer",
            customer_account="customer_account",
            days_until_due=0,
            default_payment_method="default_payment_method",
            default_source="default_source",
            default_tax_rates=["string"],
            description="description",
            discounts="",
            due_date=0,
            effective_at=0,
            expand=["string"],
            footer="footer",
            from_invoice={
                "action": "revision",
                "invoice": "invoice",
            },
            issuer={
                "type": "account",
                "account": "account",
            },
            metadata="",
            number="number",
            on_behalf_of="on_behalf_of",
            payment_settings={
                "default_mandate": "",
                "payment_method_options": {
                    "acss_debit": "",
                    "bancontact": "",
                    "card": "",
                    "customer_balance": "",
                    "konbini": "",
                    "payto": "",
                    "sepa_debit": "",
                    "us_bank_account": "",
                },
                "payment_method_types": "",
            },
            pending_invoice_items_behavior="exclude",
            rendering={
                "amount_tax_display": "",
                "pdf": {"page_size": "a4"},
                "template": "template",
                "template_version": "",
            },
            shipping_cost={
                "shipping_rate": "shipping_rate",
                "shipping_rate_data": {
                    "display_name": "display_name",
                    "delivery_estimate": {
                        "maximum": {
                            "unit": "business_day",
                            "value": 0,
                        },
                        "minimum": {
                            "unit": "business_day",
                            "value": 0,
                        },
                    },
                    "fixed_amount": {
                        "amount": 0,
                        "currency": "currency",
                        "currency_options": {
                            "foo": {
                                "amount": 0,
                                "tax_behavior": "exclusive",
                            }
                        },
                    },
                    "metadata": {"foo": "string"},
                    "tax_behavior": "exclusive",
                    "tax_code": "tax_code",
                    "type": "fixed_amount",
                },
            },
            shipping_details={
                "address": {
                    "city": "city",
                    "country": "country",
                    "line1": "line1",
                    "line2": "line2",
                    "postal_code": "postal_code",
                    "state": "state",
                },
                "name": "name",
                "phone": "",
            },
            statement_descriptor="statement_descriptor",
            subscription="subscription",
            transfer_data={
                "destination": "destination",
                "amount": 0,
            },
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Stripe) -> None:
        response = client.invoices.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Stripe) -> None:
        with client.invoices.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Stripe) -> None:
        invoice = client.invoices.list()
        assert_matches_type(SyncMyCursorIDPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Stripe) -> None:
        invoice = client.invoices.list(
            collection_method="charge_automatically",
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            customer="customer",
            customer_account="customer_account",
            due_date={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            starting_after="starting_after",
            status="draft",
            subscription="subscription",
        )
        assert_matches_type(SyncMyCursorIDPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Stripe) -> None:
        response = client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(SyncMyCursorIDPage[Invoice], invoice, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Stripe) -> None:
        with client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(SyncMyCursorIDPage[Invoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_finalize(self, client: Stripe) -> None:
        invoice = client.invoices.finalize(
            invoice="invoice",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_method_finalize_with_all_params(self, client: Stripe) -> None:
        invoice = client.invoices.finalize(
            invoice="invoice",
            auto_advance=True,
            expand=["string"],
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_raw_response_finalize(self, client: Stripe) -> None:
        response = client.invoices.with_raw_response.finalize(
            invoice="invoice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    def test_streaming_response_finalize(self, client: Stripe) -> None:
        with client.invoices.with_streaming_response.finalize(
            invoice="invoice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_finalize(self, client: Stripe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice` but received ''"):
            client.invoices.with_raw_response.finalize(
                invoice="",
            )


class TestAsyncInvoices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStripe) -> None:
        invoice = await async_client.invoices.create()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStripe) -> None:
        invoice = await async_client.invoices.create(
            account_tax_ids="",
            application_fee_amount=0,
            auto_advance=True,
            automatic_tax={
                "enabled": True,
                "liability": {
                    "type": "account",
                    "account": "account",
                },
            },
            automatically_finalizes_at=0,
            collection_method="charge_automatically",
            currency="currency",
            custom_fields="",
            customer="customer",
            customer_account="customer_account",
            days_until_due=0,
            default_payment_method="default_payment_method",
            default_source="default_source",
            default_tax_rates=["string"],
            description="description",
            discounts="",
            due_date=0,
            effective_at=0,
            expand=["string"],
            footer="footer",
            from_invoice={
                "action": "revision",
                "invoice": "invoice",
            },
            issuer={
                "type": "account",
                "account": "account",
            },
            metadata="",
            number="number",
            on_behalf_of="on_behalf_of",
            payment_settings={
                "default_mandate": "",
                "payment_method_options": {
                    "acss_debit": "",
                    "bancontact": "",
                    "card": "",
                    "customer_balance": "",
                    "konbini": "",
                    "payto": "",
                    "sepa_debit": "",
                    "us_bank_account": "",
                },
                "payment_method_types": "",
            },
            pending_invoice_items_behavior="exclude",
            rendering={
                "amount_tax_display": "",
                "pdf": {"page_size": "a4"},
                "template": "template",
                "template_version": "",
            },
            shipping_cost={
                "shipping_rate": "shipping_rate",
                "shipping_rate_data": {
                    "display_name": "display_name",
                    "delivery_estimate": {
                        "maximum": {
                            "unit": "business_day",
                            "value": 0,
                        },
                        "minimum": {
                            "unit": "business_day",
                            "value": 0,
                        },
                    },
                    "fixed_amount": {
                        "amount": 0,
                        "currency": "currency",
                        "currency_options": {
                            "foo": {
                                "amount": 0,
                                "tax_behavior": "exclusive",
                            }
                        },
                    },
                    "metadata": {"foo": "string"},
                    "tax_behavior": "exclusive",
                    "tax_code": "tax_code",
                    "type": "fixed_amount",
                },
            },
            shipping_details={
                "address": {
                    "city": "city",
                    "country": "country",
                    "line1": "line1",
                    "line2": "line2",
                    "postal_code": "postal_code",
                    "state": "state",
                },
                "name": "name",
                "phone": "",
            },
            statement_descriptor="statement_descriptor",
            subscription="subscription",
            transfer_data={
                "destination": "destination",
                "amount": 0,
            },
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStripe) -> None:
        response = await async_client.invoices.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStripe) -> None:
        async with async_client.invoices.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncStripe) -> None:
        invoice = await async_client.invoices.list()
        assert_matches_type(AsyncMyCursorIDPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStripe) -> None:
        invoice = await async_client.invoices.list(
            collection_method="charge_automatically",
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            customer="customer",
            customer_account="customer_account",
            due_date={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            starting_after="starting_after",
            status="draft",
            subscription="subscription",
        )
        assert_matches_type(AsyncMyCursorIDPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStripe) -> None:
        response = await async_client.invoices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[Invoice], invoice, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStripe) -> None:
        async with async_client.invoices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[Invoice], invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_finalize(self, async_client: AsyncStripe) -> None:
        invoice = await async_client.invoices.finalize(
            invoice="invoice",
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_method_finalize_with_all_params(self, async_client: AsyncStripe) -> None:
        invoice = await async_client.invoices.finalize(
            invoice="invoice",
            auto_advance=True,
            expand=["string"],
        )
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_raw_response_finalize(self, async_client: AsyncStripe) -> None:
        response = await async_client.invoices.with_raw_response.finalize(
            invoice="invoice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(Invoice, invoice, path=["response"])

    @parametrize
    async def test_streaming_response_finalize(self, async_client: AsyncStripe) -> None:
        async with async_client.invoices.with_streaming_response.finalize(
            invoice="invoice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(Invoice, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_finalize(self, async_client: AsyncStripe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice` but received ''"):
            await async_client.invoices.with_raw_response.finalize(
                invoice="",
            )
