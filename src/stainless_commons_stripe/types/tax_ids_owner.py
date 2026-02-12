# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .shared import application
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["TaxIDsOwner", "Account", "Application", "Customer"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Account = TypeAliasType("Account", Union[str, "account.Account"])
else:
    Account: TypeAlias = Union[str, "account.Account"]

Application: TypeAlias = Union[str, application.Application]

if TYPE_CHECKING or not PYDANTIC_V1:
    Customer = TypeAliasType("Customer", Union[str, "customer.Customer"])
else:
    Customer: TypeAlias = Union[str, "customer.Customer"]


class TaxIDsOwner(BaseModel):
    type: Literal["account", "application", "customer", "self"]
    """Type of owner referenced."""

    account: Optional[Account] = None
    """The account being referenced when `type` is `account`."""

    application: Optional[Application] = None
    """The Connect Application being referenced when `type` is `application`."""

    customer: Optional[Customer] = None
    """The customer being referenced when `type` is `customer`."""

    customer_account: Optional[str] = None
    """
    The Account representing the customer being referenced when `type` is
    `customer`.
    """


from . import account, customer
