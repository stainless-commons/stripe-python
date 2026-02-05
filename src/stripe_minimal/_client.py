# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        prices,
        balance,
        coupons,
        refunds,
        accounts,
        disputes,
        invoices,
        products,
        customers,
        invoiceitems,
        payment_links,
        subscriptions,
        payment_intents,
    )
    from .resources.prices import PricesResource, AsyncPricesResource
    from .resources.balance import BalanceResource, AsyncBalanceResource
    from .resources.coupons import CouponsResource, AsyncCouponsResource
    from .resources.refunds import RefundsResource, AsyncRefundsResource
    from .resources.accounts import AccountsResource, AsyncAccountsResource
    from .resources.disputes import DisputesResource, AsyncDisputesResource
    from .resources.invoices import InvoicesResource, AsyncInvoicesResource
    from .resources.products import ProductsResource, AsyncProductsResource
    from .resources.customers import CustomersResource, AsyncCustomersResource
    from .resources.invoiceitems import InvoiceitemsResource, AsyncInvoiceitemsResource
    from .resources.payment_links import PaymentLinksResource, AsyncPaymentLinksResource
    from .resources.subscriptions import SubscriptionsResource, AsyncSubscriptionsResource
    from .resources.payment_intents import PaymentIntentsResource, AsyncPaymentIntentsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Stripe", "AsyncStripe", "Client", "AsyncClient"]


class Stripe(SyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Stripe client instance.

        This automatically infers the `api_key` argument from the `STRIPE_SECRET_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("STRIPE_SECRET_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("STRIPE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.stripe.com/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def accounts(self) -> AccountsResource:
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def balance(self) -> BalanceResource:
        from .resources.balance import BalanceResource

        return BalanceResource(self)

    @cached_property
    def coupons(self) -> CouponsResource:
        from .resources.coupons import CouponsResource

        return CouponsResource(self)

    @cached_property
    def customers(self) -> CustomersResource:
        from .resources.customers import CustomersResource

        return CustomersResource(self)

    @cached_property
    def disputes(self) -> DisputesResource:
        from .resources.disputes import DisputesResource

        return DisputesResource(self)

    @cached_property
    def invoices(self) -> InvoicesResource:
        from .resources.invoices import InvoicesResource

        return InvoicesResource(self)

    @cached_property
    def invoiceitems(self) -> InvoiceitemsResource:
        from .resources.invoiceitems import InvoiceitemsResource

        return InvoiceitemsResource(self)

    @cached_property
    def payment_links(self) -> PaymentLinksResource:
        from .resources.payment_links import PaymentLinksResource

        return PaymentLinksResource(self)

    @cached_property
    def payment_intents(self) -> PaymentIntentsResource:
        from .resources.payment_intents import PaymentIntentsResource

        return PaymentIntentsResource(self)

    @cached_property
    def prices(self) -> PricesResource:
        from .resources.prices import PricesResource

        return PricesResource(self)

    @cached_property
    def products(self) -> ProductsResource:
        from .resources.products import ProductsResource

        return ProductsResource(self)

    @cached_property
    def refunds(self) -> RefundsResource:
        from .resources.refunds import RefundsResource

        return RefundsResource(self)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        from .resources.subscriptions import SubscriptionsResource

        return SubscriptionsResource(self)

    @cached_property
    def with_raw_response(self) -> StripeWithRawResponse:
        return StripeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StripeWithStreamedResponse:
        return StripeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncStripe(AsyncAPIClient):
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncStripe client instance.

        This automatically infers the `api_key` argument from the `STRIPE_SECRET_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("STRIPE_SECRET_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("STRIPE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.stripe.com/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def balance(self) -> AsyncBalanceResource:
        from .resources.balance import AsyncBalanceResource

        return AsyncBalanceResource(self)

    @cached_property
    def coupons(self) -> AsyncCouponsResource:
        from .resources.coupons import AsyncCouponsResource

        return AsyncCouponsResource(self)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        from .resources.customers import AsyncCustomersResource

        return AsyncCustomersResource(self)

    @cached_property
    def disputes(self) -> AsyncDisputesResource:
        from .resources.disputes import AsyncDisputesResource

        return AsyncDisputesResource(self)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        from .resources.invoices import AsyncInvoicesResource

        return AsyncInvoicesResource(self)

    @cached_property
    def invoiceitems(self) -> AsyncInvoiceitemsResource:
        from .resources.invoiceitems import AsyncInvoiceitemsResource

        return AsyncInvoiceitemsResource(self)

    @cached_property
    def payment_links(self) -> AsyncPaymentLinksResource:
        from .resources.payment_links import AsyncPaymentLinksResource

        return AsyncPaymentLinksResource(self)

    @cached_property
    def payment_intents(self) -> AsyncPaymentIntentsResource:
        from .resources.payment_intents import AsyncPaymentIntentsResource

        return AsyncPaymentIntentsResource(self)

    @cached_property
    def prices(self) -> AsyncPricesResource:
        from .resources.prices import AsyncPricesResource

        return AsyncPricesResource(self)

    @cached_property
    def products(self) -> AsyncProductsResource:
        from .resources.products import AsyncProductsResource

        return AsyncProductsResource(self)

    @cached_property
    def refunds(self) -> AsyncRefundsResource:
        from .resources.refunds import AsyncRefundsResource

        return AsyncRefundsResource(self)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        from .resources.subscriptions import AsyncSubscriptionsResource

        return AsyncSubscriptionsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncStripeWithRawResponse:
        return AsyncStripeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStripeWithStreamedResponse:
        return AsyncStripeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class StripeWithRawResponse:
    _client: Stripe

    def __init__(self, client: Stripe) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def balance(self) -> balance.BalanceResourceWithRawResponse:
        from .resources.balance import BalanceResourceWithRawResponse

        return BalanceResourceWithRawResponse(self._client.balance)

    @cached_property
    def coupons(self) -> coupons.CouponsResourceWithRawResponse:
        from .resources.coupons import CouponsResourceWithRawResponse

        return CouponsResourceWithRawResponse(self._client.coupons)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithRawResponse:
        from .resources.customers import CustomersResourceWithRawResponse

        return CustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithRawResponse:
        from .resources.disputes import DisputesResourceWithRawResponse

        return DisputesResourceWithRawResponse(self._client.disputes)

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithRawResponse:
        from .resources.invoices import InvoicesResourceWithRawResponse

        return InvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def invoiceitems(self) -> invoiceitems.InvoiceitemsResourceWithRawResponse:
        from .resources.invoiceitems import InvoiceitemsResourceWithRawResponse

        return InvoiceitemsResourceWithRawResponse(self._client.invoiceitems)

    @cached_property
    def payment_links(self) -> payment_links.PaymentLinksResourceWithRawResponse:
        from .resources.payment_links import PaymentLinksResourceWithRawResponse

        return PaymentLinksResourceWithRawResponse(self._client.payment_links)

    @cached_property
    def payment_intents(self) -> payment_intents.PaymentIntentsResourceWithRawResponse:
        from .resources.payment_intents import PaymentIntentsResourceWithRawResponse

        return PaymentIntentsResourceWithRawResponse(self._client.payment_intents)

    @cached_property
    def prices(self) -> prices.PricesResourceWithRawResponse:
        from .resources.prices import PricesResourceWithRawResponse

        return PricesResourceWithRawResponse(self._client.prices)

    @cached_property
    def products(self) -> products.ProductsResourceWithRawResponse:
        from .resources.products import ProductsResourceWithRawResponse

        return ProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def refunds(self) -> refunds.RefundsResourceWithRawResponse:
        from .resources.refunds import RefundsResourceWithRawResponse

        return RefundsResourceWithRawResponse(self._client.refunds)

    @cached_property
    def subscriptions(self) -> subscriptions.SubscriptionsResourceWithRawResponse:
        from .resources.subscriptions import SubscriptionsResourceWithRawResponse

        return SubscriptionsResourceWithRawResponse(self._client.subscriptions)


class AsyncStripeWithRawResponse:
    _client: AsyncStripe

    def __init__(self, client: AsyncStripe) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def balance(self) -> balance.AsyncBalanceResourceWithRawResponse:
        from .resources.balance import AsyncBalanceResourceWithRawResponse

        return AsyncBalanceResourceWithRawResponse(self._client.balance)

    @cached_property
    def coupons(self) -> coupons.AsyncCouponsResourceWithRawResponse:
        from .resources.coupons import AsyncCouponsResourceWithRawResponse

        return AsyncCouponsResourceWithRawResponse(self._client.coupons)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithRawResponse:
        from .resources.customers import AsyncCustomersResourceWithRawResponse

        return AsyncCustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithRawResponse:
        from .resources.disputes import AsyncDisputesResourceWithRawResponse

        return AsyncDisputesResourceWithRawResponse(self._client.disputes)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithRawResponse:
        from .resources.invoices import AsyncInvoicesResourceWithRawResponse

        return AsyncInvoicesResourceWithRawResponse(self._client.invoices)

    @cached_property
    def invoiceitems(self) -> invoiceitems.AsyncInvoiceitemsResourceWithRawResponse:
        from .resources.invoiceitems import AsyncInvoiceitemsResourceWithRawResponse

        return AsyncInvoiceitemsResourceWithRawResponse(self._client.invoiceitems)

    @cached_property
    def payment_links(self) -> payment_links.AsyncPaymentLinksResourceWithRawResponse:
        from .resources.payment_links import AsyncPaymentLinksResourceWithRawResponse

        return AsyncPaymentLinksResourceWithRawResponse(self._client.payment_links)

    @cached_property
    def payment_intents(self) -> payment_intents.AsyncPaymentIntentsResourceWithRawResponse:
        from .resources.payment_intents import AsyncPaymentIntentsResourceWithRawResponse

        return AsyncPaymentIntentsResourceWithRawResponse(self._client.payment_intents)

    @cached_property
    def prices(self) -> prices.AsyncPricesResourceWithRawResponse:
        from .resources.prices import AsyncPricesResourceWithRawResponse

        return AsyncPricesResourceWithRawResponse(self._client.prices)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithRawResponse:
        from .resources.products import AsyncProductsResourceWithRawResponse

        return AsyncProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def refunds(self) -> refunds.AsyncRefundsResourceWithRawResponse:
        from .resources.refunds import AsyncRefundsResourceWithRawResponse

        return AsyncRefundsResourceWithRawResponse(self._client.refunds)

    @cached_property
    def subscriptions(self) -> subscriptions.AsyncSubscriptionsResourceWithRawResponse:
        from .resources.subscriptions import AsyncSubscriptionsResourceWithRawResponse

        return AsyncSubscriptionsResourceWithRawResponse(self._client.subscriptions)


class StripeWithStreamedResponse:
    _client: Stripe

    def __init__(self, client: Stripe) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def balance(self) -> balance.BalanceResourceWithStreamingResponse:
        from .resources.balance import BalanceResourceWithStreamingResponse

        return BalanceResourceWithStreamingResponse(self._client.balance)

    @cached_property
    def coupons(self) -> coupons.CouponsResourceWithStreamingResponse:
        from .resources.coupons import CouponsResourceWithStreamingResponse

        return CouponsResourceWithStreamingResponse(self._client.coupons)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithStreamingResponse:
        from .resources.customers import CustomersResourceWithStreamingResponse

        return CustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def disputes(self) -> disputes.DisputesResourceWithStreamingResponse:
        from .resources.disputes import DisputesResourceWithStreamingResponse

        return DisputesResourceWithStreamingResponse(self._client.disputes)

    @cached_property
    def invoices(self) -> invoices.InvoicesResourceWithStreamingResponse:
        from .resources.invoices import InvoicesResourceWithStreamingResponse

        return InvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def invoiceitems(self) -> invoiceitems.InvoiceitemsResourceWithStreamingResponse:
        from .resources.invoiceitems import InvoiceitemsResourceWithStreamingResponse

        return InvoiceitemsResourceWithStreamingResponse(self._client.invoiceitems)

    @cached_property
    def payment_links(self) -> payment_links.PaymentLinksResourceWithStreamingResponse:
        from .resources.payment_links import PaymentLinksResourceWithStreamingResponse

        return PaymentLinksResourceWithStreamingResponse(self._client.payment_links)

    @cached_property
    def payment_intents(self) -> payment_intents.PaymentIntentsResourceWithStreamingResponse:
        from .resources.payment_intents import PaymentIntentsResourceWithStreamingResponse

        return PaymentIntentsResourceWithStreamingResponse(self._client.payment_intents)

    @cached_property
    def prices(self) -> prices.PricesResourceWithStreamingResponse:
        from .resources.prices import PricesResourceWithStreamingResponse

        return PricesResourceWithStreamingResponse(self._client.prices)

    @cached_property
    def products(self) -> products.ProductsResourceWithStreamingResponse:
        from .resources.products import ProductsResourceWithStreamingResponse

        return ProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def refunds(self) -> refunds.RefundsResourceWithStreamingResponse:
        from .resources.refunds import RefundsResourceWithStreamingResponse

        return RefundsResourceWithStreamingResponse(self._client.refunds)

    @cached_property
    def subscriptions(self) -> subscriptions.SubscriptionsResourceWithStreamingResponse:
        from .resources.subscriptions import SubscriptionsResourceWithStreamingResponse

        return SubscriptionsResourceWithStreamingResponse(self._client.subscriptions)


class AsyncStripeWithStreamedResponse:
    _client: AsyncStripe

    def __init__(self, client: AsyncStripe) -> None:
        self._client = client

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def balance(self) -> balance.AsyncBalanceResourceWithStreamingResponse:
        from .resources.balance import AsyncBalanceResourceWithStreamingResponse

        return AsyncBalanceResourceWithStreamingResponse(self._client.balance)

    @cached_property
    def coupons(self) -> coupons.AsyncCouponsResourceWithStreamingResponse:
        from .resources.coupons import AsyncCouponsResourceWithStreamingResponse

        return AsyncCouponsResourceWithStreamingResponse(self._client.coupons)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithStreamingResponse:
        from .resources.customers import AsyncCustomersResourceWithStreamingResponse

        return AsyncCustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def disputes(self) -> disputes.AsyncDisputesResourceWithStreamingResponse:
        from .resources.disputes import AsyncDisputesResourceWithStreamingResponse

        return AsyncDisputesResourceWithStreamingResponse(self._client.disputes)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesResourceWithStreamingResponse:
        from .resources.invoices import AsyncInvoicesResourceWithStreamingResponse

        return AsyncInvoicesResourceWithStreamingResponse(self._client.invoices)

    @cached_property
    def invoiceitems(self) -> invoiceitems.AsyncInvoiceitemsResourceWithStreamingResponse:
        from .resources.invoiceitems import AsyncInvoiceitemsResourceWithStreamingResponse

        return AsyncInvoiceitemsResourceWithStreamingResponse(self._client.invoiceitems)

    @cached_property
    def payment_links(self) -> payment_links.AsyncPaymentLinksResourceWithStreamingResponse:
        from .resources.payment_links import AsyncPaymentLinksResourceWithStreamingResponse

        return AsyncPaymentLinksResourceWithStreamingResponse(self._client.payment_links)

    @cached_property
    def payment_intents(self) -> payment_intents.AsyncPaymentIntentsResourceWithStreamingResponse:
        from .resources.payment_intents import AsyncPaymentIntentsResourceWithStreamingResponse

        return AsyncPaymentIntentsResourceWithStreamingResponse(self._client.payment_intents)

    @cached_property
    def prices(self) -> prices.AsyncPricesResourceWithStreamingResponse:
        from .resources.prices import AsyncPricesResourceWithStreamingResponse

        return AsyncPricesResourceWithStreamingResponse(self._client.prices)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithStreamingResponse:
        from .resources.products import AsyncProductsResourceWithStreamingResponse

        return AsyncProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def refunds(self) -> refunds.AsyncRefundsResourceWithStreamingResponse:
        from .resources.refunds import AsyncRefundsResourceWithStreamingResponse

        return AsyncRefundsResourceWithStreamingResponse(self._client.refunds)

    @cached_property
    def subscriptions(self) -> subscriptions.AsyncSubscriptionsResourceWithStreamingResponse:
        from .resources.subscriptions import AsyncSubscriptionsResourceWithStreamingResponse

        return AsyncSubscriptionsResourceWithStreamingResponse(self._client.subscriptions)


Client = Stripe

AsyncClient = AsyncStripe
