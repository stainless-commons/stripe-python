# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .issuing_cardholder_address import IssuingCardholderAddress
from .issuing_cardholder_company import IssuingCardholderCompany
from .issuing_cardholder_requirements import IssuingCardholderRequirements
from .issuing_cardholder_authorization_controls import IssuingCardholderAuthorizationControls

__all__ = ["IssuingCardholder"]


class IssuingCardholder(BaseModel):
    """
    An Issuing `Cardholder` object represents an individual or business entity who is [issued](https://docs.stripe.com/issuing) cards.

    Related guide: [How to create a cardholder](https://docs.stripe.com/issuing/cards/virtual/issue-cards#create-cardholder)
    """

    id: str
    """Unique identifier for the object."""

    billing: IssuingCardholderAddress

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if
    the object exists in test mode.
    """

    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format.
    """

    name: str
    """The cardholder's name. This will be printed on cards issued to them."""

    object: Literal["issuing.cardholder"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    requirements: IssuingCardholderRequirements

    status: Literal["active", "blocked", "inactive"]
    """Specifies whether to permit authorizations on this cardholder's cards."""

    type: Literal["company", "individual"]
    """One of `individual` or `company`.

    See
    [Choose a cardholder type](https://docs.stripe.com/issuing/other/choose-cardholder)
    for more details.
    """

    company: Optional[IssuingCardholderCompany] = None

    email: Optional[str] = None
    """The cardholder's email address."""

    individual: Optional["IssuingCardholderIndividual"] = None

    phone_number: Optional[str] = None
    """The cardholder's phone number.

    This is required for all cardholders who will be creating EU cards. See the
    [3D Secure documentation](https://docs.stripe.com/issuing/3d-secure#when-is-3d-secure-applied)
    for more details.
    """

    preferred_locales: Optional[List[Literal["de", "en", "es", "fr", "it"]]] = None
    """The cardholder’s preferred locales (languages), ordered by preference.

    Locales can be `de`, `en`, `es`, `fr`, or `it`. This changes the language of the
    [3D Secure flow](https://docs.stripe.com/issuing/3d-secure) and one-time
    password messages sent to the cardholder.
    """

    spending_controls: Optional[IssuingCardholderAuthorizationControls] = None


from .issuing_cardholder_individual import IssuingCardholderIndividual
