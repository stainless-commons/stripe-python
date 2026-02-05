# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["IssuingCardholderVerification"]


class IssuingCardholderVerification(BaseModel):
    document: Optional["IssuingCardholderIDDocument"] = None


from .issuing_cardholder_id_document import IssuingCardholderIDDocument
