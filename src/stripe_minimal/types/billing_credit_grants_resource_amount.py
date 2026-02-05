# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .billing_credit_grants_resource_monetary_amount import BillingCreditGrantsResourceMonetaryAmount

__all__ = ["BillingCreditGrantsResourceAmount"]


class BillingCreditGrantsResourceAmount(BaseModel):
    type: Literal["monetary"]
    """The type of this amount. We currently only support `monetary` billing credits."""

    monetary: Optional[BillingCreditGrantsResourceMonetaryAmount] = None
