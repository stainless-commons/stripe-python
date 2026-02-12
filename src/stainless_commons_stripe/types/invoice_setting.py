# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .shared.invoice_setting_custom_field import InvoiceSettingCustomField

__all__ = ["InvoiceSetting", "DefaultPaymentMethod", "RenderingOptions"]

if TYPE_CHECKING or not PYDANTIC_V1:
    DefaultPaymentMethod = TypeAliasType("DefaultPaymentMethod", Union[str, "PaymentMethod", None])
else:
    DefaultPaymentMethod: TypeAlias = Union[str, "PaymentMethod", None]


class RenderingOptions(BaseModel):
    amount_tax_display: Optional[str] = None
    """
    How line-item prices and amounts will be displayed with respect to tax on
    invoice PDFs.
    """

    template: Optional[str] = None
    """ID of the invoice rendering template to be used for this customer's invoices.

    If set, the template will be used on all invoices for this customer unless a
    template is set directly on the invoice.
    """


class InvoiceSetting(BaseModel):
    custom_fields: Optional[List[InvoiceSettingCustomField]] = None
    """Default custom fields to be displayed on invoices for this customer."""

    default_payment_method: Optional[DefaultPaymentMethod] = None
    """
    ID of a payment method that's attached to the customer, to be used as the
    customer's default payment method for subscriptions and invoices.
    """

    footer: Optional[str] = None
    """Default footer to be displayed on invoices for this customer."""

    rendering_options: Optional[RenderingOptions] = None


from .payment_method import PaymentMethod
