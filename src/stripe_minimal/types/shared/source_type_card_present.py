# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SourceTypeCardPresent"]


class SourceTypeCardPresent(BaseModel):
    application_cryptogram: Optional[str] = None

    application_preferred_name: Optional[str] = None

    authorization_code: Optional[str] = None

    authorization_response_code: Optional[str] = None

    brand: Optional[str] = None

    country: Optional[str] = None

    cvm_type: Optional[str] = None

    data_type: Optional[str] = None

    dedicated_file_name: Optional[str] = None

    emv_auth_data: Optional[str] = None

    evidence_customer_signature: Optional[str] = None

    evidence_transaction_certificate: Optional[str] = None

    exp_month: Optional[int] = None

    exp_year: Optional[int] = None

    fingerprint: Optional[str] = None

    funding: Optional[str] = None

    last4: Optional[str] = None

    pos_device_id: Optional[str] = None

    pos_entry_mode: Optional[str] = None

    read_method: Optional[str] = None

    reader: Optional[str] = None

    terminal_verification_results: Optional[str] = None

    transaction_status_information: Optional[str] = None
