# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeKlarna"]


class SourceTypeKlarna(BaseModel):
    background_image_url: Optional[str] = None

    client_token: Optional[str] = None

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    locale: Optional[str] = None

    logo_url: Optional[str] = None

    page_title: Optional[str] = None

    pay_later_asset_urls_descriptive: Optional[str] = None

    pay_later_asset_urls_standard: Optional[str] = None

    pay_later_name: Optional[str] = None

    pay_later_redirect_url: Optional[str] = None

    pay_now_asset_urls_descriptive: Optional[str] = None

    pay_now_asset_urls_standard: Optional[str] = None

    pay_now_name: Optional[str] = None

    pay_now_redirect_url: Optional[str] = None

    pay_over_time_asset_urls_descriptive: Optional[str] = None

    pay_over_time_asset_urls_standard: Optional[str] = None

    pay_over_time_name: Optional[str] = None

    pay_over_time_redirect_url: Optional[str] = None

    payment_method_categories: Optional[str] = None

    purchase_country: Optional[str] = None

    purchase_type: Optional[str] = None

    redirect_url: Optional[str] = None

    shipping_delay: Optional[int] = None

    shipping_first_name: Optional[str] = None

    shipping_last_name: Optional[str] = None
