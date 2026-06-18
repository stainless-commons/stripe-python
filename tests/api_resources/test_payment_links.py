# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from stainless_commons_stripe import Stripe, AsyncStripe
from stainless_commons_stripe.types import PaymentLinkCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Stripe) -> None:
        payment_link = client.payment_links.create(
            line_items=[{"quantity": 0}],
        )
        assert_matches_type(PaymentLinkCreateResponse, payment_link, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Stripe) -> None:
        payment_link = client.payment_links.create(
            line_items=[
                {
                    "quantity": 0,
                    "adjustable_quantity": {
                        "enabled": True,
                        "maximum": 0,
                        "minimum": 0,
                    },
                    "price": "price",
                    "price_data": {
                        "currency": "currency",
                        "product": "product",
                        "product_data": {
                            "name": "name",
                            "description": "description",
                            "images": ["string"],
                            "metadata": {"foo": "string"},
                            "tax_code": "tax_code",
                            "unit_label": "unit_label",
                        },
                        "recurring": {
                            "interval": "day",
                            "interval_count": 0,
                        },
                        "tax_behavior": "exclusive",
                        "unit_amount": 0,
                        "unit_amount_decimal": "unit_amount_decimal",
                    },
                }
            ],
            after_completion={
                "type": "hosted_confirmation",
                "hosted_confirmation": {"custom_message": "custom_message"},
                "redirect": {"url": "url"},
            },
            allow_promotion_codes=True,
            application_fee_amount=0,
            application_fee_percent=0,
            automatic_tax={
                "enabled": True,
                "liability": {
                    "type": "account",
                    "account": "account",
                },
            },
            billing_address_collection="auto",
            consent_collection={
                "payment_method_reuse_agreement": {"position": "auto"},
                "promotions": "auto",
                "terms_of_service": "none",
            },
            currency="currency",
            custom_fields=[
                {
                    "key": "key",
                    "label": {
                        "custom": "custom",
                        "type": "custom",
                    },
                    "type": "dropdown",
                    "dropdown": {
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                            }
                        ],
                        "default_value": "default_value",
                    },
                    "numeric": {
                        "default_value": "default_value",
                        "maximum_length": 0,
                        "minimum_length": 0,
                    },
                    "optional": True,
                    "text": {
                        "default_value": "default_value",
                        "maximum_length": 0,
                        "minimum_length": 0,
                    },
                }
            ],
            custom_text={
                "after_submit": "",
                "shipping_address": "",
                "submit": "",
                "terms_of_service_acceptance": "",
            },
            customer_creation="always",
            expand=["string"],
            inactive_message="inactive_message",
            invoice_creation={
                "enabled": True,
                "invoice_data": {
                    "account_tax_ids": "",
                    "custom_fields": "",
                    "description": "description",
                    "footer": "footer",
                    "issuer": {
                        "type": "account",
                        "account": "account",
                    },
                    "metadata": "",
                    "rendering_options": "",
                },
            },
            metadata={"foo": "string"},
            name_collection={
                "business": {
                    "enabled": True,
                    "optional": True,
                },
                "individual": {
                    "enabled": True,
                    "optional": True,
                },
            },
            on_behalf_of="on_behalf_of",
            optional_items=[
                {
                    "price": "price",
                    "quantity": 0,
                    "adjustable_quantity": {
                        "enabled": True,
                        "maximum": 0,
                        "minimum": 0,
                    },
                }
            ],
            payment_intent_data={
                "capture_method": "automatic",
                "description": "description",
                "metadata": {"foo": "string"},
                "setup_future_usage": "off_session",
                "statement_descriptor": "statement_descriptor",
                "statement_descriptor_suffix": "statement_descriptor_suffix",
                "transfer_group": "transfer_group",
            },
            payment_method_collection="always",
            payment_method_types=["affirm"],
            phone_number_collection={"enabled": True},
            restrictions={"completed_sessions": {"limit": 0}},
            shipping_address_collection={"allowed_countries": ["AC"]},
            shipping_options=[{"shipping_rate": "shipping_rate"}],
            submit_type="auto",
            subscription_data={
                "description": "description",
                "invoice_settings": {
                    "issuer": {
                        "type": "account",
                        "account": "account",
                    }
                },
                "metadata": {"foo": "string"},
                "trial_period_days": 0,
                "trial_settings": {"end_behavior": {"missing_payment_method": "cancel"}},
            },
            tax_id_collection={
                "enabled": True,
                "required": "if_supported",
            },
            transfer_data={
                "destination": "destination",
                "amount": 0,
            },
        )
        assert_matches_type(PaymentLinkCreateResponse, payment_link, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Stripe) -> None:
        response = client.payment_links.with_raw_response.create(
            line_items=[{"quantity": 0}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = response.parse()
        assert_matches_type(PaymentLinkCreateResponse, payment_link, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Stripe) -> None:
        with client.payment_links.with_streaming_response.create(
            line_items=[{"quantity": 0}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = response.parse()
            assert_matches_type(PaymentLinkCreateResponse, payment_link, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStripe) -> None:
        payment_link = await async_client.payment_links.create(
            line_items=[{"quantity": 0}],
        )
        assert_matches_type(PaymentLinkCreateResponse, payment_link, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStripe) -> None:
        payment_link = await async_client.payment_links.create(
            line_items=[
                {
                    "quantity": 0,
                    "adjustable_quantity": {
                        "enabled": True,
                        "maximum": 0,
                        "minimum": 0,
                    },
                    "price": "price",
                    "price_data": {
                        "currency": "currency",
                        "product": "product",
                        "product_data": {
                            "name": "name",
                            "description": "description",
                            "images": ["string"],
                            "metadata": {"foo": "string"},
                            "tax_code": "tax_code",
                            "unit_label": "unit_label",
                        },
                        "recurring": {
                            "interval": "day",
                            "interval_count": 0,
                        },
                        "tax_behavior": "exclusive",
                        "unit_amount": 0,
                        "unit_amount_decimal": "unit_amount_decimal",
                    },
                }
            ],
            after_completion={
                "type": "hosted_confirmation",
                "hosted_confirmation": {"custom_message": "custom_message"},
                "redirect": {"url": "url"},
            },
            allow_promotion_codes=True,
            application_fee_amount=0,
            application_fee_percent=0,
            automatic_tax={
                "enabled": True,
                "liability": {
                    "type": "account",
                    "account": "account",
                },
            },
            billing_address_collection="auto",
            consent_collection={
                "payment_method_reuse_agreement": {"position": "auto"},
                "promotions": "auto",
                "terms_of_service": "none",
            },
            currency="currency",
            custom_fields=[
                {
                    "key": "key",
                    "label": {
                        "custom": "custom",
                        "type": "custom",
                    },
                    "type": "dropdown",
                    "dropdown": {
                        "options": [
                            {
                                "label": "label",
                                "value": "value",
                            }
                        ],
                        "default_value": "default_value",
                    },
                    "numeric": {
                        "default_value": "default_value",
                        "maximum_length": 0,
                        "minimum_length": 0,
                    },
                    "optional": True,
                    "text": {
                        "default_value": "default_value",
                        "maximum_length": 0,
                        "minimum_length": 0,
                    },
                }
            ],
            custom_text={
                "after_submit": "",
                "shipping_address": "",
                "submit": "",
                "terms_of_service_acceptance": "",
            },
            customer_creation="always",
            expand=["string"],
            inactive_message="inactive_message",
            invoice_creation={
                "enabled": True,
                "invoice_data": {
                    "account_tax_ids": "",
                    "custom_fields": "",
                    "description": "description",
                    "footer": "footer",
                    "issuer": {
                        "type": "account",
                        "account": "account",
                    },
                    "metadata": "",
                    "rendering_options": "",
                },
            },
            metadata={"foo": "string"},
            name_collection={
                "business": {
                    "enabled": True,
                    "optional": True,
                },
                "individual": {
                    "enabled": True,
                    "optional": True,
                },
            },
            on_behalf_of="on_behalf_of",
            optional_items=[
                {
                    "price": "price",
                    "quantity": 0,
                    "adjustable_quantity": {
                        "enabled": True,
                        "maximum": 0,
                        "minimum": 0,
                    },
                }
            ],
            payment_intent_data={
                "capture_method": "automatic",
                "description": "description",
                "metadata": {"foo": "string"},
                "setup_future_usage": "off_session",
                "statement_descriptor": "statement_descriptor",
                "statement_descriptor_suffix": "statement_descriptor_suffix",
                "transfer_group": "transfer_group",
            },
            payment_method_collection="always",
            payment_method_types=["affirm"],
            phone_number_collection={"enabled": True},
            restrictions={"completed_sessions": {"limit": 0}},
            shipping_address_collection={"allowed_countries": ["AC"]},
            shipping_options=[{"shipping_rate": "shipping_rate"}],
            submit_type="auto",
            subscription_data={
                "description": "description",
                "invoice_settings": {
                    "issuer": {
                        "type": "account",
                        "account": "account",
                    }
                },
                "metadata": {"foo": "string"},
                "trial_period_days": 0,
                "trial_settings": {"end_behavior": {"missing_payment_method": "cancel"}},
            },
            tax_id_collection={
                "enabled": True,
                "required": "if_supported",
            },
            transfer_data={
                "destination": "destination",
                "amount": 0,
            },
        )
        assert_matches_type(PaymentLinkCreateResponse, payment_link, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStripe) -> None:
        response = await async_client.payment_links.with_raw_response.create(
            line_items=[{"quantity": 0}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_link = await response.parse()
        assert_matches_type(PaymentLinkCreateResponse, payment_link, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStripe) -> None:
        async with async_client.payment_links.with_streaming_response.create(
            line_items=[{"quantity": 0}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_link = await response.parse()
            assert_matches_type(PaymentLinkCreateResponse, payment_link, path=["response"])

        assert cast(Any, response.is_closed) is True
