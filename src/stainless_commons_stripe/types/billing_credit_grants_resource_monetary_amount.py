# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BillingCreditGrantsResourceMonetaryAmount"]


class BillingCreditGrantsResourceMonetaryAmount(BaseModel):
    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    value: int
    """A positive integer representing the amount."""
