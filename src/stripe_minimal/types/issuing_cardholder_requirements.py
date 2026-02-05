# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IssuingCardholderRequirements"]


class IssuingCardholderRequirements(BaseModel):
    disabled_reason: Optional[Literal["listed", "rejected.listed", "requirements.past_due", "under_review"]] = None
    """
    If `disabled_reason` is present, all cards will decline authorizations with
    `cardholder_verification_required` reason.
    """

    past_due: Optional[
        List[
            Literal[
                "company.tax_id",
                "individual.card_issuing.user_terms_acceptance.date",
                "individual.card_issuing.user_terms_acceptance.ip",
                "individual.dob.day",
                "individual.dob.month",
                "individual.dob.year",
                "individual.first_name",
                "individual.last_name",
                "individual.verification.document",
            ]
        ]
    ] = None
    """
    Array of fields that need to be collected in order to verify and re-enable the
    cardholder.
    """
