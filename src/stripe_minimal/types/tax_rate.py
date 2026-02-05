# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TaxRate", "FlatAmount"]


class FlatAmount(BaseModel):
    """The amount of the tax rate when the `rate_type`` is `flat_amount`.

    Tax rates with `rate_type` `percentage` can vary based on the transaction, resulting in this field being `null`. This field exposes the amount and currency of the flat tax rate.
    """

    amount: int
    """Amount of the tax when the `rate_type` is `flat_amount`.

    This positive integer represents how much to charge in the smallest currency
    unit (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal
    currency). The amount value supports up to eight digits (e.g., a value of
    99999999 for a USD charge of $999,999.99).
    """

    currency: str
    """Three-letter ISO currency code, in lowercase."""


class TaxRate(BaseModel):
    """
    Tax rates can be applied to [invoices](/invoicing/taxes/tax-rates), [subscriptions](/billing/taxes/tax-rates) and [Checkout Sessions](/payments/checkout/use-manual-tax-rates) to collect tax.

    Related guide: [Tax rates](/billing/taxes/tax-rates)
    """

    id: str
    """Unique identifier for the object."""

    active: bool
    """Defaults to `true`.

    When set to `false`, this tax rate cannot be used with new applications or
    Checkout Sessions, but will still work for subscriptions and invoices that
    already have it set.
    """

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    display_name: str
    """
    The display name of the tax rates as it will appear to your customer on their
    receipt email, PDF, and the hosted invoice page.
    """

    inclusive: bool
    """This specifies if the tax rate is inclusive or exclusive."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["tax_rate"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    percentage: float
    """Tax rate percentage out of 100.

    For tax calculations with automatic_tax[enabled]=true, this percentage includes
    the statutory tax rate of non-taxable jurisdictions.
    """

    country: Optional[str] = None
    """
    Two-letter country code
    ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """

    description: Optional[str] = None
    """An arbitrary string attached to the tax rate for your internal use only.

    It will not be visible to your customers.
    """

    effective_percentage: Optional[float] = None
    """Actual/effective tax rate percentage out of 100.

    For tax calculations with automatic_tax[enabled]=true, this percentage reflects
    the rate actually used to calculate tax based on the product's taxability and
    whether the user is registered to collect taxes in the corresponding
    jurisdiction.
    """

    flat_amount: Optional[FlatAmount] = None
    """The amount of the tax rate when the ` rate_type`` is  `flat_amount`.

    Tax rates with `rate_type` `percentage` can vary based on the transaction,
    resulting in this field being `null`. This field exposes the amount and currency
    of the flat tax rate.
    """

    jurisdiction: Optional[str] = None
    """The jurisdiction for the tax rate.

    You can use this label field for tax reporting purposes. It also appears on your
    customer’s invoice.
    """

    jurisdiction_level: Optional[Literal["city", "country", "county", "district", "multiple", "state"]] = None
    """The level of the jurisdiction that imposes this tax rate.

    Will be `null` for manually defined tax rates.
    """

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    rate_type: Optional[Literal["flat_amount", "percentage"]] = None
    """Indicates the type of tax rate applied to the taxable amount.

    This value can be `null` when no tax applies to the location. This field is only
    present for TaxRates created by Stripe Tax.
    """

    state: Optional[str] = None
    """
    [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without
    country prefix. For example, "NY" for New York, United States.
    """

    tax_type: Optional[
        Literal[
            "amusement_tax",
            "communications_tax",
            "gst",
            "hst",
            "igst",
            "jct",
            "lease_tax",
            "pst",
            "qst",
            "retail_delivery_fee",
            "rst",
            "sales_tax",
            "service_tax",
            "vat",
        ]
    ] = None
    """The high-level tax type, such as `vat` or `sales_tax`."""
