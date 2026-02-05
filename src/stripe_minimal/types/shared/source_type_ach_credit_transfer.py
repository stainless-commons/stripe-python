# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeACHCreditTransfer"]


class SourceTypeACHCreditTransfer(BaseModel):
    account_number: Optional[str] = None

    bank_name: Optional[str] = None

    fingerprint: Optional[str] = None

    refund_account_holder_name: Optional[str] = None

    refund_account_holder_type: Optional[str] = None

    refund_routing_number: Optional[str] = None

    routing_number: Optional[str] = None

    swift_code: Optional[str] = None
