# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainless_commons_stripe import Stripe, AsyncStripe
from stainless_commons_stripe.types import Dispute
from stainless_commons_stripe.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDisputes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Stripe) -> None:
        dispute = client.disputes.update(
            dispute="dispute",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Stripe) -> None:
        dispute = client.disputes.update(
            dispute="dispute",
            evidence={
                "access_activity_log": "access_activity_log",
                "billing_address": "billing_address",
                "cancellation_policy": "cancellation_policy",
                "cancellation_policy_disclosure": "cancellation_policy_disclosure",
                "cancellation_rebuttal": "cancellation_rebuttal",
                "customer_communication": "customer_communication",
                "customer_email_address": "customer_email_address",
                "customer_name": "customer_name",
                "customer_purchase_ip": "customer_purchase_ip",
                "customer_signature": "customer_signature",
                "duplicate_charge_documentation": "duplicate_charge_documentation",
                "duplicate_charge_explanation": "duplicate_charge_explanation",
                "duplicate_charge_id": "duplicate_charge_id",
                "enhanced_evidence": {
                    "visa_compelling_evidence_3": {
                        "disputed_transaction": {
                            "customer_account_id": "string",
                            "customer_device_fingerprint": "string",
                            "customer_device_id": "string",
                            "customer_email_address": "string",
                            "customer_purchase_ip": "string",
                            "merchandise_or_services": "merchandise",
                            "product_description": "string",
                            "shipping_address": {
                                "city": "string",
                                "country": "string",
                                "line1": "string",
                                "line2": "string",
                                "postal_code": "string",
                                "state": "string",
                            },
                        },
                        "prior_undisputed_transactions": [
                            {
                                "charge": "charge",
                                "customer_account_id": "string",
                                "customer_device_fingerprint": "string",
                                "customer_device_id": "string",
                                "customer_email_address": "string",
                                "customer_purchase_ip": "string",
                                "product_description": "string",
                                "shipping_address": {
                                    "city": "string",
                                    "country": "string",
                                    "line1": "string",
                                    "line2": "string",
                                    "postal_code": "string",
                                    "state": "string",
                                },
                            }
                        ],
                    },
                    "visa_compliance": {"fee_acknowledged": True},
                },
                "product_description": "product_description",
                "receipt": "receipt",
                "refund_policy": "refund_policy",
                "refund_policy_disclosure": "refund_policy_disclosure",
                "refund_refusal_explanation": "refund_refusal_explanation",
                "service_date": "service_date",
                "service_documentation": "service_documentation",
                "shipping_address": "shipping_address",
                "shipping_carrier": "shipping_carrier",
                "shipping_date": "shipping_date",
                "shipping_documentation": "shipping_documentation",
                "shipping_tracking_number": "shipping_tracking_number",
                "uncategorized_file": "uncategorized_file",
                "uncategorized_text": "uncategorized_text",
            },
            expand=["string"],
            metadata={"foo": "string"},
            submit=True,
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stripe) -> None:
        response = client.disputes.with_raw_response.update(
            dispute="dispute",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stripe) -> None:
        with client.disputes.with_streaming_response.update(
            dispute="dispute",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stripe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute` but received ''"):
            client.disputes.with_raw_response.update(
                dispute="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Stripe) -> None:
        dispute = client.disputes.list()
        assert_matches_type(SyncMyCursorIDPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stripe) -> None:
        dispute = client.disputes.list(
            charge="charge",
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            payment_intent="payment_intent",
            starting_after="starting_after",
        )
        assert_matches_type(SyncMyCursorIDPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stripe) -> None:
        response = client.disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(SyncMyCursorIDPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stripe) -> None:
        with client.disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(SyncMyCursorIDPage[Dispute], dispute, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDisputes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStripe) -> None:
        dispute = await async_client.disputes.update(
            dispute="dispute",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStripe) -> None:
        dispute = await async_client.disputes.update(
            dispute="dispute",
            evidence={
                "access_activity_log": "access_activity_log",
                "billing_address": "billing_address",
                "cancellation_policy": "cancellation_policy",
                "cancellation_policy_disclosure": "cancellation_policy_disclosure",
                "cancellation_rebuttal": "cancellation_rebuttal",
                "customer_communication": "customer_communication",
                "customer_email_address": "customer_email_address",
                "customer_name": "customer_name",
                "customer_purchase_ip": "customer_purchase_ip",
                "customer_signature": "customer_signature",
                "duplicate_charge_documentation": "duplicate_charge_documentation",
                "duplicate_charge_explanation": "duplicate_charge_explanation",
                "duplicate_charge_id": "duplicate_charge_id",
                "enhanced_evidence": {
                    "visa_compelling_evidence_3": {
                        "disputed_transaction": {
                            "customer_account_id": "string",
                            "customer_device_fingerprint": "string",
                            "customer_device_id": "string",
                            "customer_email_address": "string",
                            "customer_purchase_ip": "string",
                            "merchandise_or_services": "merchandise",
                            "product_description": "string",
                            "shipping_address": {
                                "city": "string",
                                "country": "string",
                                "line1": "string",
                                "line2": "string",
                                "postal_code": "string",
                                "state": "string",
                            },
                        },
                        "prior_undisputed_transactions": [
                            {
                                "charge": "charge",
                                "customer_account_id": "string",
                                "customer_device_fingerprint": "string",
                                "customer_device_id": "string",
                                "customer_email_address": "string",
                                "customer_purchase_ip": "string",
                                "product_description": "string",
                                "shipping_address": {
                                    "city": "string",
                                    "country": "string",
                                    "line1": "string",
                                    "line2": "string",
                                    "postal_code": "string",
                                    "state": "string",
                                },
                            }
                        ],
                    },
                    "visa_compliance": {"fee_acknowledged": True},
                },
                "product_description": "product_description",
                "receipt": "receipt",
                "refund_policy": "refund_policy",
                "refund_policy_disclosure": "refund_policy_disclosure",
                "refund_refusal_explanation": "refund_refusal_explanation",
                "service_date": "service_date",
                "service_documentation": "service_documentation",
                "shipping_address": "shipping_address",
                "shipping_carrier": "shipping_carrier",
                "shipping_date": "shipping_date",
                "shipping_documentation": "shipping_documentation",
                "shipping_tracking_number": "shipping_tracking_number",
                "uncategorized_file": "uncategorized_file",
                "uncategorized_text": "uncategorized_text",
            },
            expand=["string"],
            metadata={"foo": "string"},
            submit=True,
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStripe) -> None:
        response = await async_client.disputes.with_raw_response.update(
            dispute="dispute",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStripe) -> None:
        async with async_client.disputes.with_streaming_response.update(
            dispute="dispute",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStripe) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute` but received ''"):
            await async_client.disputes.with_raw_response.update(
                dispute="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStripe) -> None:
        dispute = await async_client.disputes.list()
        assert_matches_type(AsyncMyCursorIDPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStripe) -> None:
        dispute = await async_client.disputes.list(
            charge="charge",
            created={
                "gt": 0,
                "gte": 0,
                "lt": 0,
                "lte": 0,
            },
            ending_before="ending_before",
            expand=["string"],
            limit=0,
            payment_intent="payment_intent",
            starting_after="starting_after",
        )
        assert_matches_type(AsyncMyCursorIDPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStripe) -> None:
        response = await async_client.disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[Dispute], dispute, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStripe) -> None:
        async with async_client.disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[Dispute], dispute, path=["response"])

        assert cast(Any, response.is_closed) is True
