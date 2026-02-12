# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .issuing_cardholder_user_terms_acceptance import IssuingCardholderUserTermsAcceptance

__all__ = ["IssuingCardholderCardIssuing"]


class IssuingCardholderCardIssuing(BaseModel):
    user_terms_acceptance: Optional[IssuingCardholderUserTermsAcceptance] = None
