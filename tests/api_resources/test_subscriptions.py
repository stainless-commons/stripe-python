# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainless_commons_stripe import Stripe, AsyncStripe
from stainless_commons_stripe.types import (
    Subscription,
)
from stainless_commons_stripe.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Stripe) -> None:
        subscription = client.subscriptions.update(
            subscription_exposed_id="subscription_exposed_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Stripe) -> None:
        subscription = client.subscriptions.update(
            subscription_exposed_id="subscription_exposed_id",
            add_invoice_items=[
                {
                    "discounts": [
                        {
                            "coupon": "coupon",
                            "discount": "discount",
                            "promotion_code": "promotion_code",
                        }
                    ],
                    "metadata": {"foo": "string"},
                    "period": {
                        "end": {
                            "type": "min_item_period_end",
                            "timestamp": 0,
                        },
                        "start": {
                            "type": "max_item_period_start",
                            "timestamp": 0,
                        },
                    },
                    "price": "price",
                    "price_data": {
                        "currency": "currency",
                        "product": "product",
                        "tax_behavior": "exclusive",
                        "unit_amount": 0,
                        "unit_amount_decimal": "unit_amount_decimal",
                    },
                    "quantity": 0,
                    "tax_rates": ["string"],
                }
            ],
            application_fee_percent=0,
            automatic_tax={
                "enabled": True,
                "liability": {
                    "type": "account",
                    "account": "account",
                },
            },
            billing_cycle_anchor="now",
            billing_thresholds={
                "amount_gte": 0,
                "reset_billing_cycle_anchor": True,
            },
            cancel_at="",
            cancel_at_period_end=True,
            cancellation_details={
                "comment": "string",
                "feedback": "",
            },
            collection_method="charge_automatically",
            days_until_due=0,
            default_payment_method="default_payment_method",
            default_source="string",
            default_tax_rates=["string"],
            description="string",
            discounts=[
                {
                    "coupon": "coupon",
                    "discount": "discount",
                    "promotion_code": "promotion_code",
                }
            ],
            expand=["string"],
            invoice_settings={
                "account_tax_ids": ["string"],
                "issuer": {
                    "type": "account",
                    "account": "account",
                },
            },
            items=[
                {
                    "id": "id",
                    "billing_thresholds": {"usage_gte": 0},
                    "clear_usage": True,
                    "deleted": True,
                    "discounts": [
                        {
                            "coupon": "coupon",
                            "discount": "discount",
                            "promotion_code": "promotion_code",
                        }
                    ],
                    "metadata": {"foo": "string"},
                    "price": "price",
                    "price_data": {
                        "currency": "currency",
                        "product": "product",
                        "recurring": {
                            "interval": "day",
                            "interval_count": 0,
                        },
                        "tax_behavior": "exclusive",
                        "unit_amount": 0,
                        "unit_amount_decimal": "unit_amount_decimal",
                    },
                    "quantity": 0,
                    "tax_rates": ["string"],
                }
            ],
            metadata={"foo": "string"},
            off_session=True,
            on_behalf_of="string",
            pause_collection={
                "behavior": "keep_as_draft",
                "resumes_at": 0,
            },
            payment_behavior="allow_incomplete",
            payment_settings={
                "payment_method_options": {
                    "acss_debit": {
                        "mandate_options": {"transaction_type": "business"},
                        "verification_method": "automatic",
                    },
                    "bancontact": {"preferred_language": "de"},
                    "card": {
                        "mandate_options": {
                            "amount": 0,
                            "amount_type": "fixed",
                            "description": "description",
                        },
                        "network": "amex",
                        "request_three_d_secure": "any",
                    },
                    "customer_balance": {
                        "bank_transfer": {
                            "eu_bank_transfer": {"country": "country"},
                            "type": "type",
                        },
                        "funding_type": "funding_type",
                    },
                    "konbini": "",
                    "payto": {
                        "mandate_options": {
                            "amount": 0,
                            "purpose": "dependant_support",
                        }
                    },
                    "sepa_debit": "",
                    "us_bank_account": {
                        "financial_connections": {
                            "filters": {"account_subcategories": ["checking"]},
                            "permissions": ["balances"],
                            "prefetch": ["balances"],
                        },
                        "verification_method": "automatic",
                    },
                },
                "payment_method_types": ["ach_credit_transfer"],
                "save_default_payment_method": "off",
            },
            pending_invoice_item_interval={
                "interval": "day",
                "interval_count": 0,
            },
            proration_behavior="always_invoice",
            proration_date=0,
            transfer_data={
                "destination": "destination",
                "amount_percent": 0,
            },
            trial_end="now",
            trial_from_plan=True,
            trial_settings={"end_behavior": {"missing_payment_method": "cancel"}},
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stripe) -> None:
        response = client.subscriptions.with_raw_response.update(
            subscription_exposed_id="subscription_exposed_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stripe) -> None:
        with client.subscriptions.with_streaming_response.update(
            subscription_exposed_id="subscription_exposed_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stripe) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_exposed_id` but received ''"
        ):
            client.subscriptions.with_raw_response.update(
                subscription_exposed_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Stripe) -> None:
        subscription = client.subscriptions.list()
        assert_matches_type(SyncMyCursorIDPage[Subscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stripe) -> None:
        subscription = client.subscriptions.list(
            automatic_tax={"enabled": True},
            collection_method="charge_automatically",
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            current_period_end={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            current_period_start={
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
            price="price",
            starting_after="starting_after",
            status="active",
            test_clock="test_clock",
        )
        assert_matches_type(SyncMyCursorIDPage[Subscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stripe) -> None:
        response = client.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncMyCursorIDPage[Subscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stripe) -> None:
        with client.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncMyCursorIDPage[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Stripe) -> None:
        subscription = client.subscriptions.cancel(
            subscription_exposed_id="subscription_exposed_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: Stripe) -> None:
        subscription = client.subscriptions.cancel(
            subscription_exposed_id="subscription_exposed_id",
            cancellation_details={
                "comment": "string",
                "feedback": "",
            },
            expand=["string"],
            invoice_now=True,
            prorate=True,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Stripe) -> None:
        response = client.subscriptions.with_raw_response.cancel(
            subscription_exposed_id="subscription_exposed_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Stripe) -> None:
        with client.subscriptions.with_streaming_response.cancel(
            subscription_exposed_id="subscription_exposed_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Stripe) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_exposed_id` but received ''"
        ):
            client.subscriptions.with_raw_response.cancel(
                subscription_exposed_id="",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStripe) -> None:
        subscription = await async_client.subscriptions.update(
            subscription_exposed_id="subscription_exposed_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStripe) -> None:
        subscription = await async_client.subscriptions.update(
            subscription_exposed_id="subscription_exposed_id",
            add_invoice_items=[
                {
                    "discounts": [
                        {
                            "coupon": "coupon",
                            "discount": "discount",
                            "promotion_code": "promotion_code",
                        }
                    ],
                    "metadata": {"foo": "string"},
                    "period": {
                        "end": {
                            "type": "min_item_period_end",
                            "timestamp": 0,
                        },
                        "start": {
                            "type": "max_item_period_start",
                            "timestamp": 0,
                        },
                    },
                    "price": "price",
                    "price_data": {
                        "currency": "currency",
                        "product": "product",
                        "tax_behavior": "exclusive",
                        "unit_amount": 0,
                        "unit_amount_decimal": "unit_amount_decimal",
                    },
                    "quantity": 0,
                    "tax_rates": ["string"],
                }
            ],
            application_fee_percent=0,
            automatic_tax={
                "enabled": True,
                "liability": {
                    "type": "account",
                    "account": "account",
                },
            },
            billing_cycle_anchor="now",
            billing_thresholds={
                "amount_gte": 0,
                "reset_billing_cycle_anchor": True,
            },
            cancel_at="",
            cancel_at_period_end=True,
            cancellation_details={
                "comment": "string",
                "feedback": "",
            },
            collection_method="charge_automatically",
            days_until_due=0,
            default_payment_method="default_payment_method",
            default_source="string",
            default_tax_rates=["string"],
            description="string",
            discounts=[
                {
                    "coupon": "coupon",
                    "discount": "discount",
                    "promotion_code": "promotion_code",
                }
            ],
            expand=["string"],
            invoice_settings={
                "account_tax_ids": ["string"],
                "issuer": {
                    "type": "account",
                    "account": "account",
                },
            },
            items=[
                {
                    "id": "id",
                    "billing_thresholds": {"usage_gte": 0},
                    "clear_usage": True,
                    "deleted": True,
                    "discounts": [
                        {
                            "coupon": "coupon",
                            "discount": "discount",
                            "promotion_code": "promotion_code",
                        }
                    ],
                    "metadata": {"foo": "string"},
                    "price": "price",
                    "price_data": {
                        "currency": "currency",
                        "product": "product",
                        "recurring": {
                            "interval": "day",
                            "interval_count": 0,
                        },
                        "tax_behavior": "exclusive",
                        "unit_amount": 0,
                        "unit_amount_decimal": "unit_amount_decimal",
                    },
                    "quantity": 0,
                    "tax_rates": ["string"],
                }
            ],
            metadata={"foo": "string"},
            off_session=True,
            on_behalf_of="string",
            pause_collection={
                "behavior": "keep_as_draft",
                "resumes_at": 0,
            },
            payment_behavior="allow_incomplete",
            payment_settings={
                "payment_method_options": {
                    "acss_debit": {
                        "mandate_options": {"transaction_type": "business"},
                        "verification_method": "automatic",
                    },
                    "bancontact": {"preferred_language": "de"},
                    "card": {
                        "mandate_options": {
                            "amount": 0,
                            "amount_type": "fixed",
                            "description": "description",
                        },
                        "network": "amex",
                        "request_three_d_secure": "any",
                    },
                    "customer_balance": {
                        "bank_transfer": {
                            "eu_bank_transfer": {"country": "country"},
                            "type": "type",
                        },
                        "funding_type": "funding_type",
                    },
                    "konbini": "",
                    "payto": {
                        "mandate_options": {
                            "amount": 0,
                            "purpose": "dependant_support",
                        }
                    },
                    "sepa_debit": "",
                    "us_bank_account": {
                        "financial_connections": {
                            "filters": {"account_subcategories": ["checking"]},
                            "permissions": ["balances"],
                            "prefetch": ["balances"],
                        },
                        "verification_method": "automatic",
                    },
                },
                "payment_method_types": ["ach_credit_transfer"],
                "save_default_payment_method": "off",
            },
            pending_invoice_item_interval={
                "interval": "day",
                "interval_count": 0,
            },
            proration_behavior="always_invoice",
            proration_date=0,
            transfer_data={
                "destination": "destination",
                "amount_percent": 0,
            },
            trial_end="now",
            trial_from_plan=True,
            trial_settings={"end_behavior": {"missing_payment_method": "cancel"}},
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStripe) -> None:
        response = await async_client.subscriptions.with_raw_response.update(
            subscription_exposed_id="subscription_exposed_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStripe) -> None:
        async with async_client.subscriptions.with_streaming_response.update(
            subscription_exposed_id="subscription_exposed_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStripe) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_exposed_id` but received ''"
        ):
            await async_client.subscriptions.with_raw_response.update(
                subscription_exposed_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStripe) -> None:
        subscription = await async_client.subscriptions.list()
        assert_matches_type(AsyncMyCursorIDPage[Subscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStripe) -> None:
        subscription = await async_client.subscriptions.list(
            automatic_tax={"enabled": True},
            collection_method="charge_automatically",
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            current_period_end={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            current_period_start={
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
            price="price",
            starting_after="starting_after",
            status="active",
            test_clock="test_clock",
        )
        assert_matches_type(AsyncMyCursorIDPage[Subscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStripe) -> None:
        response = await async_client.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[Subscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStripe) -> None:
        async with async_client.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncStripe) -> None:
        subscription = await async_client.subscriptions.cancel(
            subscription_exposed_id="subscription_exposed_id",
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncStripe) -> None:
        subscription = await async_client.subscriptions.cancel(
            subscription_exposed_id="subscription_exposed_id",
            cancellation_details={
                "comment": "string",
                "feedback": "",
            },
            expand=["string"],
            invoice_now=True,
            prorate=True,
        )
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncStripe) -> None:
        response = await async_client.subscriptions.with_raw_response.cancel(
            subscription_exposed_id="subscription_exposed_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(Subscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncStripe) -> None:
        async with async_client.subscriptions.with_streaming_response.cancel(
            subscription_exposed_id="subscription_exposed_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(Subscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncStripe) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `subscription_exposed_id` but received ''"
        ):
            await async_client.subscriptions.with_raw_response.cancel(
                subscription_exposed_id="",
            )
