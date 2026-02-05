# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["InvoiceSettingCustomField"]


class InvoiceSettingCustomField(BaseModel):
    name: str
    """The name of the custom field."""

    value: str
    """The value of the custom field."""
