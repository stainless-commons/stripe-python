# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .issuing_cardholder_card_issuing import IssuingCardholderCardIssuing
from .issuing_cardholder_individual_dob import IssuingCardholderIndividualDob

__all__ = ["IssuingCardholderIndividual"]


class IssuingCardholderIndividual(BaseModel):
    card_issuing: Optional[IssuingCardholderCardIssuing] = None

    dob: Optional[IssuingCardholderIndividualDob] = None

    first_name: Optional[str] = None
    """The first name of this cardholder.

    Required before activating Cards. This field cannot contain any numbers, special
    characters (except periods, commas, hyphens, spaces and apostrophes) or
    non-latin letters.
    """

    last_name: Optional[str] = None
    """The last name of this cardholder.

    Required before activating Cards. This field cannot contain any numbers, special
    characters (except periods, commas, hyphens, spaces and apostrophes) or
    non-latin letters.
    """

    verification: Optional["IssuingCardholderVerification"] = None


from .issuing_cardholder_verification import IssuingCardholderVerification
