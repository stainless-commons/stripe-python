# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PaymentMethodDetailsPassthroughCard"]


class PaymentMethodDetailsPassthroughCard(BaseModel):
    brand: Optional[str] = None
    """Card brand.

    Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`,
    `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
    """

    country: Optional[str] = None
    """Two-letter ISO code representing the country of the card.

    You could use this attribute to get a sense of the international breakdown of
    cards you've collected.
    """

    exp_month: Optional[int] = None
    """Two-digit number representing the card's expiration month."""

    exp_year: Optional[int] = None
    """Four-digit number representing the card's expiration year."""

    funding: Optional[str] = None
    """Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`."""

    last4: Optional[str] = None
    """The last four digits of the card."""
