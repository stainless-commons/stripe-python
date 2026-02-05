# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeMultibanco"]


class SourceTypeMultibanco(BaseModel):
    entity: Optional[str] = None

    reference: Optional[str] = None

    refund_account_holder_address_city: Optional[str] = None

    refund_account_holder_address_country: Optional[str] = None

    refund_account_holder_address_line1: Optional[str] = None

    refund_account_holder_address_line2: Optional[str] = None

    refund_account_holder_address_postal_code: Optional[str] = None

    refund_account_holder_address_state: Optional[str] = None

    refund_account_holder_name: Optional[str] = None

    refund_iban: Optional[str] = None
