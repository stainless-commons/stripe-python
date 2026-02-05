# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .source_order import SourceOrder
from .source_owner import SourceOwner
from .source_type_eps import SourceTypeEps
from .source_type_p24 import SourceTypeP24
from .source_type_card import SourceTypeCard
from .source_type_ideal import SourceTypeIdeal
from .source_type_alipay import SourceTypeAlipay
from .source_type_klarna import SourceTypeKlarna
from .source_type_sofort import SourceTypeSofort
from .source_type_wechat import SourceTypeWechat
from .source_type_giropay import SourceTypeGiropay
from .source_receiver_flow import SourceReceiverFlow
from .source_redirect_flow import SourceRedirectFlow
from .source_type_ach_debit import SourceTypeACHDebit
from .source_type_acss_debit import SourceTypeAcssDebit
from .source_type_bancontact import SourceTypeBancontact
from .source_type_multibanco import SourceTypeMultibanco
from .source_type_sepa_debit import SourceTypeSepaDebit
from .source_type_card_present import SourceTypeCardPresent
from .source_type_au_becs_debit import SourceTypeAuBecsDebit
from .source_type_three_d_secure import SourceTypeThreeDSecure
from .source_code_verification_flow import SourceCodeVerificationFlow
from .source_type_ach_credit_transfer import SourceTypeACHCreditTransfer

__all__ = ["Source"]


class Source(BaseModel):
    """`Source` objects allow you to accept a variety of payment methods.

    They
    represent a customer's payment instrument, and can be used with the Stripe API
    just like a `Card` object: once chargeable, they can be charged, or can be
    attached to customers.

    Stripe doesn't recommend using the deprecated [Sources API](https://docs.stripe.com/api/sources).
    We recommend that you adopt the [PaymentMethods API](https://docs.stripe.com/api/payment_methods).
    This newer API provides access to our latest features and payment method types.

    Related guides: [Sources API](https://docs.stripe.com/sources) and [Sources & Customers](https://docs.stripe.com/sources/customers).
    """

    id: str
    """Unique identifier for the object."""

    client_secret: str
    """The client secret of the source.

    Used for client-side retrieval using a publishable key.
    """

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    flow: str
    """The authentication `flow` of the source.

    `flow` is one of `redirect`, `receiver`, `code_verification`, `none`.
    """

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    object: Literal["source"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    status: str
    """
    The status of the source, one of `canceled`, `chargeable`, `consumed`, `failed`,
    or `pending`. Only `chargeable` sources can be used to create a charge.
    """

    type: Literal[
        "ach_credit_transfer",
        "ach_debit",
        "acss_debit",
        "alipay",
        "au_becs_debit",
        "bancontact",
        "card",
        "card_present",
        "eps",
        "giropay",
        "ideal",
        "klarna",
        "multibanco",
        "p24",
        "sepa_debit",
        "sofort",
        "three_d_secure",
        "wechat",
    ]
    """The `type` of the source.

    The `type` is a payment method, one of `ach_credit_transfer`, `ach_debit`,
    `alipay`, `bancontact`, `card`, `card_present`, `eps`, `giropay`, `ideal`,
    `multibanco`, `klarna`, `p24`, `sepa_debit`, `sofort`, `three_d_secure`, or
    `wechat`. An additional hash is included on the source with a name matching this
    value. It contains additional information specific to the
    [payment method](https://docs.stripe.com/sources) used.
    """

    ach_credit_transfer: Optional[SourceTypeACHCreditTransfer] = None

    ach_debit: Optional[SourceTypeACHDebit] = None

    acss_debit: Optional[SourceTypeAcssDebit] = None

    alipay: Optional[SourceTypeAlipay] = None

    allow_redisplay: Optional[Literal["always", "limited", "unspecified"]] = None
    """
    This field indicates whether this payment method can be shown again to its
    customer in a checkout flow. Stripe products such as Checkout and Elements use
    this field to determine whether a payment method can be shown as a saved payment
    method in a checkout flow. The field defaults to “unspecified”.
    """

    amount: Optional[int] = None
    """
    A positive integer in the smallest currency unit (that is, 100 cents for $1.00,
    or 1 for ¥1, Japanese Yen being a zero-decimal currency) representing the total
    amount associated with the source. This is the amount for which the source will
    be chargeable once ready. Required for `single_use` sources.
    """

    au_becs_debit: Optional[SourceTypeAuBecsDebit] = None

    bancontact: Optional[SourceTypeBancontact] = None

    card: Optional[SourceTypeCard] = None

    card_present: Optional[SourceTypeCardPresent] = None

    code_verification: Optional[SourceCodeVerificationFlow] = None

    currency: Optional[str] = None
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies)
    associated with the source. This is the currency for which the source will be
    chargeable once ready. Required for `single_use` sources.
    """

    customer: Optional[str] = None
    """The ID of the customer to which this source is attached.

    This will not be present when the source has not been attached to a customer.
    """

    eps: Optional[SourceTypeEps] = None

    giropay: Optional[SourceTypeGiropay] = None

    ideal: Optional[SourceTypeIdeal] = None

    klarna: Optional[SourceTypeKlarna] = None

    metadata: Optional[Dict[str, str]] = None
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    multibanco: Optional[SourceTypeMultibanco] = None

    owner: Optional[SourceOwner] = None

    p24: Optional[SourceTypeP24] = None

    receiver: Optional[SourceReceiverFlow] = None

    redirect: Optional[SourceRedirectFlow] = None

    sepa_debit: Optional[SourceTypeSepaDebit] = None

    sofort: Optional[SourceTypeSofort] = None

    source_order: Optional[SourceOrder] = None

    statement_descriptor: Optional[str] = None
    """Extra information about a source.

    This will appear on your customer's statement every time you charge the source.
    """

    three_d_secure: Optional[SourceTypeThreeDSecure] = None

    usage: Optional[str] = None
    """Either `reusable` or `single_use`.

    Whether this source should be reusable or not. Some source types may or may not
    be reusable by construction, while others may leave the option at creation. If
    an incompatible value is passed, an error will be returned.
    """

    wechat: Optional[SourceTypeWechat] = None
