# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet"]


class PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet(BaseModel):
    type: Literal["apple_pay", "google_pay", "samsung_pay", "unknown"]
    """
    The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or
    `unknown`.
    """
