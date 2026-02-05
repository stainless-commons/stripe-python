# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .setup_intent_payment_method_options_mandate_options_payto import (
    SetupIntentPaymentMethodOptionsMandateOptionsPayto,
)

__all__ = ["SetupIntentTypeSpecificPaymentMethodOptionsClient"]


class SetupIntentTypeSpecificPaymentMethodOptionsClient(BaseModel):
    mandate_options: Optional[SetupIntentPaymentMethodOptionsMandateOptionsPayto] = None

    verification_method: Optional[Literal["automatic", "instant", "microdeposits"]] = None
    """Bank account verification method."""
