# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "DisputeUpdateParams",
    "Evidence",
    "EvidenceEnhancedEvidence",
    "EvidenceEnhancedEvidenceEnhancedEvidence",
    "EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3",
    "EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransaction",
    "EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransactionShippingAddress",
    "EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransaction",
    "EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransactionShippingAddress",
    "EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompliance",
]


class DisputeUpdateParams(TypedDict, total=False):
    evidence: Evidence
    """Evidence to upload, to respond to a dispute.

    Updating any field in the hash will submit all fields in the hash for review.
    The combined character count of all fields is limited to 150,000.
    """

    expand: SequenceNotStr[str]
    """Specifies which fields in the response should be expanded."""

    metadata: Union[Dict[str, str], Literal[""]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Individual keys can be unset by posting an
    empty value to them. All keys can be unset by posting an empty value to
    `metadata`.
    """

    submit: bool
    """Whether to immediately submit evidence to the bank.

    If `false`, evidence is staged on the dispute. Staged evidence is visible in the
    API and Dashboard, and can be submitted to the bank by making another request
    with this attribute set to `true` (the default).
    """


class EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransactionShippingAddress(
    TypedDict, total=False
):
    city: Union[str, Literal[""]]

    country: Union[str, Literal[""]]

    line1: Union[str, Literal[""]]

    line2: Union[str, Literal[""]]

    postal_code: Union[str, Literal[""]]

    state: Union[str, Literal[""]]


class EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransaction(TypedDict, total=False):
    customer_account_id: Union[str, Literal[""]]

    customer_device_fingerprint: Union[str, Literal[""]]

    customer_device_id: Union[str, Literal[""]]

    customer_email_address: Union[str, Literal[""]]

    customer_purchase_ip: Union[str, Literal[""]]

    merchandise_or_services: Literal["merchandise", "services"]

    product_description: Union[str, Literal[""]]

    shipping_address: EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransactionShippingAddress


class EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransactionShippingAddress(
    TypedDict, total=False
):
    city: Union[str, Literal[""]]

    country: Union[str, Literal[""]]

    line1: Union[str, Literal[""]]

    line2: Union[str, Literal[""]]

    postal_code: Union[str, Literal[""]]

    state: Union[str, Literal[""]]


class EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransaction(TypedDict, total=False):
    charge: Required[str]

    customer_account_id: Union[str, Literal[""]]

    customer_device_fingerprint: Union[str, Literal[""]]

    customer_device_id: Union[str, Literal[""]]

    customer_email_address: Union[str, Literal[""]]

    customer_purchase_ip: Union[str, Literal[""]]

    product_description: Union[str, Literal[""]]

    shipping_address: (
        EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransactionShippingAddress
    )


class EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3(TypedDict, total=False):
    disputed_transaction: EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3DisputedTransaction

    prior_undisputed_transactions: Iterable[
        EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3PriorUndisputedTransaction
    ]


class EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompliance(TypedDict, total=False):
    fee_acknowledged: bool


class EvidenceEnhancedEvidenceEnhancedEvidence(TypedDict, total=False):
    visa_compelling_evidence_3: EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompellingEvidence3

    visa_compliance: EvidenceEnhancedEvidenceEnhancedEvidenceVisaCompliance


EvidenceEnhancedEvidence: TypeAlias = Union[EvidenceEnhancedEvidenceEnhancedEvidence, Literal[""]]


class Evidence(TypedDict, total=False):
    """Evidence to upload, to respond to a dispute.

    Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.
    """

    access_activity_log: str

    billing_address: str

    cancellation_policy: str

    cancellation_policy_disclosure: str

    cancellation_rebuttal: str

    customer_communication: str

    customer_email_address: str

    customer_name: str

    customer_purchase_ip: str

    customer_signature: str

    duplicate_charge_documentation: str

    duplicate_charge_explanation: str

    duplicate_charge_id: str

    enhanced_evidence: EvidenceEnhancedEvidence

    product_description: str

    receipt: str

    refund_policy: str

    refund_policy_disclosure: str

    refund_refusal_explanation: str

    service_date: str

    service_documentation: str

    shipping_address: str

    shipping_carrier: str

    shipping_date: str

    shipping_documentation: str

    shipping_tracking_number: str

    uncategorized_file: str

    uncategorized_text: str
