# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TaxCode"]


class TaxCode(BaseModel):
    """
    [Tax codes](https://stripe.com/docs/tax/tax-categories) classify goods and services for tax purposes.
    """

    id: str
    """Unique identifier for the object."""

    description: str
    """A detailed description of which types of products the tax code represents."""

    name: str
    """A short name for the tax code."""

    object: Literal["tax_code"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """
