# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["IssuingCardholderCompany"]


class IssuingCardholderCompany(BaseModel):
    tax_id_provided: bool
    """Whether the company's business ID number was provided."""
