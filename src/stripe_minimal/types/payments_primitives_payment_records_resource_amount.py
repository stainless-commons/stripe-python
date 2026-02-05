# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PaymentsPrimitivesPaymentRecordsResourceAmount"]


class PaymentsPrimitivesPaymentRecordsResourceAmount(BaseModel):
    """A representation of an amount of money, consisting of an amount and a currency."""

    currency: str
    """
    Three-letter
    [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in
    lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    value: int
    """
    A positive integer representing the amount in the currency's
    [minor unit](https://docs.stripe.com/currencies#zero-decimal). For example,
    `100` can represent 1 USD or 100 JPY.
    """
