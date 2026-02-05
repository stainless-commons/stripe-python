# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["File", "Links"]


class Links(BaseModel):
    """
    A list of [file links](https://api.stripe.com#file_links) that point at this file.
    """

    data: List["FileLink"]
    """Details about each object."""

    has_more: bool
    """True if this list has another page of items after this one that can be fetched."""

    object: Literal["list"]
    """String representing the object's type.

    Objects of the same type share the same value. Always has the value `list`.
    """

    url: str
    """The URL where this list can be accessed."""


class File(BaseModel):
    """This object represents files hosted on Stripe's servers.

    You can upload
    files with the [create file](https://api.stripe.com#create_file) request
    (for example, when uploading dispute evidence). Stripe also
    creates files independently (for example, the results of a [Sigma scheduled
    query](#scheduled_queries)).

    Related guide: [File upload guide](https://docs.stripe.com/file-upload)
    """

    id: str
    """Unique identifier for the object."""

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    object: Literal["file"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    purpose: Literal[
        "account_requirement",
        "additional_verification",
        "business_icon",
        "business_logo",
        "customer_signature",
        "dispute_evidence",
        "document_provider_identity_document",
        "finance_report_run",
        "financial_account_statement",
        "identity_document",
        "identity_document_downloadable",
        "issuing_regulatory_reporting",
        "pci_document",
        "platform_terms_of_service",
        "selfie",
        "sigma_scheduled_query",
        "tax_document_user_upload",
        "terminal_android_apk",
        "terminal_reader_splashscreen",
    ]
    """
    The [purpose](https://docs.stripe.com/file-upload#uploading-a-file) of the
    uploaded file.
    """

    size: int
    """The size of the file object in bytes."""

    expires_at: Optional[int] = None
    """The file expires and isn't available at this time in epoch seconds."""

    filename: Optional[str] = None
    """The suitable name for saving the file to a filesystem."""

    links: Optional[Links] = None
    """
    A list of [file links](https://api.stripe.com#file_links) that point at this
    file.
    """

    title: Optional[str] = None
    """A suitable title for the document."""

    type: Optional[str] = None
    """The returned file type (for example, `csv`, `pdf`, `jpg`, or `png`)."""

    url: Optional[str] = None
    """Use your live secret API key to download the file from this URL."""


from .file_link import FileLink
