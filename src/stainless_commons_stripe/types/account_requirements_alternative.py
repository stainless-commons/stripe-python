# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AccountRequirementsAlternative"]


class AccountRequirementsAlternative(BaseModel):
    alternative_fields_due: List[str]
    """Fields that can be provided to resolve all fields in `original_fields_due`."""

    original_fields_due: List[str]
    """
    Fields that are due and can be resolved by providing all fields in
    `alternative_fields_due`.
    """
