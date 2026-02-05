# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.payment_method_details_card_installments_plan import PaymentMethodDetailsCardInstallmentsPlan

__all__ = ["PaymentFlowsInstallmentOptions"]


class PaymentFlowsInstallmentOptions(BaseModel):
    enabled: bool

    plan: Optional[PaymentMethodDetailsCardInstallmentsPlan] = None
