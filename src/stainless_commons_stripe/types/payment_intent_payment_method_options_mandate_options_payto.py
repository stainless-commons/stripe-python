# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentIntentPaymentMethodOptionsMandateOptionsPayto"]


class PaymentIntentPaymentMethodOptionsMandateOptionsPayto(BaseModel):
    amount: Optional[int] = None
    """Amount that will be collected. It is required when `amount_type` is `fixed`."""

    amount_type: Optional[Literal["fixed", "maximum"]] = None
    """The type of amount that will be collected.

    The amount charged must be exact or up to the value of `amount` param for
    `fixed` or `maximum` type respectively. Defaults to `maximum`.
    """

    end_date: Optional[str] = None
    """Date, in YYYY-MM-DD format, after which payments will not be collected.

    Defaults to no end date.
    """

    payment_schedule: Optional[
        Literal["adhoc", "annual", "daily", "fortnightly", "monthly", "quarterly", "semi_annual", "weekly"]
    ] = None
    """The periodicity at which payments will be collected. Defaults to `adhoc`."""

    payments_per_period: Optional[int] = None
    """The number of payments that will be made during a payment period.

    Defaults to 1 except for when `payment_schedule` is `adhoc`. In that case, it
    defaults to no limit.
    """

    purpose: Optional[
        Literal[
            "dependant_support",
            "government",
            "loan",
            "mortgage",
            "other",
            "pension",
            "personal",
            "retail",
            "salary",
            "tax",
            "utility",
        ]
    ] = None
    """The purpose for which payments are made.

    Has a default value based on your merchant category code.
    """
