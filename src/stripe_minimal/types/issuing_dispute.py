# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "IssuingDispute",
    "Evidence",
    "EvidenceCanceled",
    "EvidenceCanceledAdditionalDocumentation",
    "EvidenceDuplicate",
    "EvidenceDuplicateAdditionalDocumentation",
    "EvidenceDuplicateCardStatement",
    "EvidenceDuplicateCashReceipt",
    "EvidenceDuplicateCheckImage",
    "EvidenceFraudulent",
    "EvidenceFraudulentAdditionalDocumentation",
    "EvidenceMerchandiseNotAsDescribed",
    "EvidenceMerchandiseNotAsDescribedAdditionalDocumentation",
    "EvidenceNoValidAuthorization",
    "EvidenceNoValidAuthorizationAdditionalDocumentation",
    "EvidenceNotReceived",
    "EvidenceNotReceivedAdditionalDocumentation",
    "EvidenceOther",
    "EvidenceOtherAdditionalDocumentation",
    "EvidenceServiceNotAsDescribed",
    "EvidenceServiceNotAsDescribedAdditionalDocumentation",
    "Transaction",
    "Treasury",
]

EvidenceCanceledAdditionalDocumentation: TypeAlias = Union[str, "File", None]


class EvidenceCanceled(BaseModel):
    additional_documentation: Optional[EvidenceCanceledAdditionalDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional
    documentation supporting the dispute.
    """

    canceled_at: Optional[int] = None
    """Date when order was canceled."""

    cancellation_policy_provided: Optional[bool] = None
    """Whether the cardholder was provided with a cancellation policy."""

    cancellation_reason: Optional[str] = None
    """Reason for canceling the order."""

    expected_at: Optional[int] = None
    """Date when the cardholder expected to receive the product."""

    explanation: Optional[str] = None
    """Explanation of why the cardholder is disputing this transaction."""

    product_description: Optional[str] = None
    """Description of the merchandise or service that was purchased."""

    product_type: Optional[Literal["merchandise", "service"]] = None
    """Whether the product was a merchandise or service."""

    return_status: Optional[Literal["merchant_rejected", "successful"]] = None
    """Result of cardholder's attempt to return the product."""

    returned_at: Optional[int] = None
    """Date when the product was returned or attempted to be returned."""


EvidenceDuplicateAdditionalDocumentation: TypeAlias = Union[str, "File", None]

EvidenceDuplicateCardStatement: TypeAlias = Union[str, "File", None]

EvidenceDuplicateCashReceipt: TypeAlias = Union[str, "File", None]

EvidenceDuplicateCheckImage: TypeAlias = Union[str, "File", None]


class EvidenceDuplicate(BaseModel):
    additional_documentation: Optional[EvidenceDuplicateAdditionalDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional
    documentation supporting the dispute.
    """

    card_statement: Optional[EvidenceDuplicateCardStatement] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the
    card statement showing that the product had already been paid for.
    """

    cash_receipt: Optional[EvidenceDuplicateCashReceipt] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the
    receipt showing that the product had been paid for in cash.
    """

    check_image: Optional[EvidenceDuplicateCheckImage] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Image of the
    front and back of the check that was used to pay for the product.
    """

    explanation: Optional[str] = None
    """Explanation of why the cardholder is disputing this transaction."""

    original_transaction: Optional[str] = None
    """Transaction (e.g., ipi\\__...) that the disputed transaction is a duplicate of.

    Of the two or more transactions that are copies of each other, this is original
    undisputed one.
    """


EvidenceFraudulentAdditionalDocumentation: TypeAlias = Union[str, "File", None]


class EvidenceFraudulent(BaseModel):
    additional_documentation: Optional[EvidenceFraudulentAdditionalDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional
    documentation supporting the dispute.
    """

    explanation: Optional[str] = None
    """Explanation of why the cardholder is disputing this transaction."""


EvidenceMerchandiseNotAsDescribedAdditionalDocumentation: TypeAlias = Union[str, "File", None]


class EvidenceMerchandiseNotAsDescribed(BaseModel):
    additional_documentation: Optional[EvidenceMerchandiseNotAsDescribedAdditionalDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional
    documentation supporting the dispute.
    """

    explanation: Optional[str] = None
    """Explanation of why the cardholder is disputing this transaction."""

    received_at: Optional[int] = None
    """Date when the product was received."""

    return_description: Optional[str] = None
    """Description of the cardholder's attempt to return the product."""

    return_status: Optional[Literal["merchant_rejected", "successful"]] = None
    """Result of cardholder's attempt to return the product."""

    returned_at: Optional[int] = None
    """Date when the product was returned or attempted to be returned."""


EvidenceNoValidAuthorizationAdditionalDocumentation: TypeAlias = Union[str, "File", None]


class EvidenceNoValidAuthorization(BaseModel):
    additional_documentation: Optional[EvidenceNoValidAuthorizationAdditionalDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional
    documentation supporting the dispute.
    """

    explanation: Optional[str] = None
    """Explanation of why the cardholder is disputing this transaction."""


EvidenceNotReceivedAdditionalDocumentation: TypeAlias = Union[str, "File", None]


class EvidenceNotReceived(BaseModel):
    additional_documentation: Optional[EvidenceNotReceivedAdditionalDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional
    documentation supporting the dispute.
    """

    expected_at: Optional[int] = None
    """Date when the cardholder expected to receive the product."""

    explanation: Optional[str] = None
    """Explanation of why the cardholder is disputing this transaction."""

    product_description: Optional[str] = None
    """Description of the merchandise or service that was purchased."""

    product_type: Optional[Literal["merchandise", "service"]] = None
    """Whether the product was a merchandise or service."""


EvidenceOtherAdditionalDocumentation: TypeAlias = Union[str, "File", None]


class EvidenceOther(BaseModel):
    additional_documentation: Optional[EvidenceOtherAdditionalDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional
    documentation supporting the dispute.
    """

    explanation: Optional[str] = None
    """Explanation of why the cardholder is disputing this transaction."""

    product_description: Optional[str] = None
    """Description of the merchandise or service that was purchased."""

    product_type: Optional[Literal["merchandise", "service"]] = None
    """Whether the product was a merchandise or service."""


EvidenceServiceNotAsDescribedAdditionalDocumentation: TypeAlias = Union[str, "File", None]


class EvidenceServiceNotAsDescribed(BaseModel):
    additional_documentation: Optional[EvidenceServiceNotAsDescribedAdditionalDocumentation] = None
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional
    documentation supporting the dispute.
    """

    canceled_at: Optional[int] = None
    """Date when order was canceled."""

    cancellation_reason: Optional[str] = None
    """Reason for canceling the order."""

    explanation: Optional[str] = None
    """Explanation of why the cardholder is disputing this transaction."""

    received_at: Optional[int] = None
    """Date when the product was received."""


class Evidence(BaseModel):
    reason: Literal[
        "canceled",
        "duplicate",
        "fraudulent",
        "merchandise_not_as_described",
        "no_valid_authorization",
        "not_received",
        "other",
        "service_not_as_described",
    ]
    """The reason for filing the dispute.

    Its value will match the field containing the evidence.
    """

    canceled: Optional[EvidenceCanceled] = None

    duplicate: Optional[EvidenceDuplicate] = None

    fraudulent: Optional[EvidenceFraudulent] = None

    merchandise_not_as_described: Optional[EvidenceMerchandiseNotAsDescribed] = None

    no_valid_authorization: Optional[EvidenceNoValidAuthorization] = None

    not_received: Optional[EvidenceNotReceived] = None

    other: Optional[EvidenceOther] = None

    service_not_as_described: Optional[EvidenceServiceNotAsDescribed] = None


if TYPE_CHECKING or not PYDANTIC_V1:
    Transaction = TypeAliasType("Transaction", Union[str, "IssuingTransaction"])
else:
    Transaction: TypeAlias = Union[str, "IssuingTransaction"]


class Treasury(BaseModel):
    received_debit: str
    """
    The Treasury
    [ReceivedDebit](https://docs.stripe.com/api/treasury/received_debits) that is
    being disputed.
    """

    debit_reversal: Optional[str] = None
    """
    The Treasury
    [DebitReversal](https://docs.stripe.com/api/treasury/debit_reversals)
    representing this Issuing dispute
    """


class IssuingDispute(BaseModel):
    """
    As a [card issuer](https://docs.stripe.com/issuing), you can dispute transactions that the cardholder does not recognize, suspects to be fraudulent, or has other issues with.

    Related guide: [Issuing disputes](https://docs.stripe.com/issuing/purchases/disputes)
    """

    id: str
    """Unique identifier for the object."""

    amount: int
    """
    Disputed amount in the card's currency and in the
    [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    Usually the amount of the `transaction`, but can differ (usually because of
    currency fluctuation).
    """

    created: int
    """Time at which the object was created. Measured in seconds since the Unix epoch."""

    currency: str
    """The currency the `transaction` was made in."""

    evidence: Evidence

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

    object: Literal["issuing.dispute"]
    """String representing the object's type.

    Objects of the same type share the same value.
    """

    status: Literal["expired", "lost", "submitted", "unsubmitted", "won"]
    """Current status of the dispute."""

    transaction: Transaction
    """The transaction being disputed."""

    balance_transactions: Optional[List["BalanceTransaction"]] = None
    """List of balance transactions associated with the dispute."""

    loss_reason: Optional[
        Literal[
            "cardholder_authentication_issuer_liability",
            "eci5_token_transaction_with_tavv",
            "excess_disputes_in_timeframe",
            "has_not_met_the_minimum_dispute_amount_requirements",
            "invalid_duplicate_dispute",
            "invalid_incorrect_amount_dispute",
            "invalid_no_authorization",
            "invalid_use_of_disputes",
            "merchandise_delivered_or_shipped",
            "merchandise_or_service_as_described",
            "not_cancelled",
            "other",
            "refund_issued",
            "submitted_beyond_allowable_time_limit",
            "transaction_3ds_required",
            "transaction_approved_after_prior_fraud_dispute",
            "transaction_authorized",
            "transaction_electronically_read",
            "transaction_qualifies_for_visa_easy_payment_service",
            "transaction_unattended",
        ]
    ] = None
    """The enum that describes the dispute loss outcome.

    If the dispute is not lost, this field will be absent. New enum values may be
    added in the future, so be sure to handle unknown values.
    """

    treasury: Optional[Treasury] = None


from .file import File
from .balance_transaction import BalanceTransaction
from .issuing_transaction import IssuingTransaction
