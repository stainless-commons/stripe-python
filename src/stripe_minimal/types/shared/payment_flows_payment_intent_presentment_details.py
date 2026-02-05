# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["PaymentFlowsPaymentIntentPresentmentDetails"]


class PaymentFlowsPaymentIntentPresentmentDetails(BaseModel):
    presentment_amount: int
    """
    Amount intended to be collected by this payment, denominated in
    `presentment_currency`.
    """

    presentment_currency: str
    """Currency presented to the customer during payment."""
