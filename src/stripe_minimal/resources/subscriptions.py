# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal

import httpx

from ..types import subscription_list_params, subscription_cancel_params, subscription_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.subscription import Subscription
from ..types.subscription_list_response import SubscriptionListResponse

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    def update(
        self,
        subscription_exposed_id: str,
        *,
        add_invoice_items: Iterable[subscription_update_params.AddInvoiceItem] | Omit = omit,
        application_fee_percent: Union[float, Literal[""]] | Omit = omit,
        automatic_tax: subscription_update_params.AutomaticTax | Omit = omit,
        billing_cycle_anchor: Literal["now", "unchanged"] | Omit = omit,
        billing_thresholds: subscription_update_params.BillingThresholds | Omit = omit,
        cancel_at: Union[Literal["", "max_period_end", "min_period_end"], int] | Omit = omit,
        cancel_at_period_end: bool | Omit = omit,
        cancellation_details: subscription_update_params.CancellationDetails | Omit = omit,
        collection_method: Literal["charge_automatically", "send_invoice"] | Omit = omit,
        days_until_due: int | Omit = omit,
        default_payment_method: str | Omit = omit,
        default_source: Union[str, Literal[""]] | Omit = omit,
        default_tax_rates: Union[SequenceNotStr[str], Literal[""]] | Omit = omit,
        description: Union[str, Literal[""]] | Omit = omit,
        discounts: Union[Iterable[subscription_update_params.DiscountsDiscountsList], Literal[""]] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        invoice_settings: subscription_update_params.InvoiceSettings | Omit = omit,
        items: Iterable[subscription_update_params.Item] | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        off_session: bool | Omit = omit,
        on_behalf_of: Union[str, Literal[""]] | Omit = omit,
        pause_collection: subscription_update_params.PauseCollection | Omit = omit,
        payment_behavior: Literal[
            "allow_incomplete", "default_incomplete", "error_if_incomplete", "pending_if_incomplete"
        ]
        | Omit = omit,
        payment_settings: subscription_update_params.PaymentSettings | Omit = omit,
        pending_invoice_item_interval: subscription_update_params.PendingInvoiceItemInterval | Omit = omit,
        proration_behavior: Literal["always_invoice", "create_prorations", "none"] | Omit = omit,
        proration_date: int | Omit = omit,
        transfer_data: subscription_update_params.TransferData | Omit = omit,
        trial_end: Union[Literal["now"], int] | Omit = omit,
        trial_from_plan: bool | Omit = omit,
        trial_settings: subscription_update_params.TrialSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """
        <p>Updates an existing subscription to match the specified parameters.
        When changing prices or quantities, we optionally prorate the price we charge next month to make up for any price changes.
        To preview how the proration is calculated, use the <a href="/docs/api/invoices/create_preview">create preview</a> endpoint.</p>

        <p>By default, we prorate subscription changes. For example, if a customer signs up on May 1 for a <currency>100</currency> price, they’ll be billed <currency>100</currency> immediately. If on May 15 they switch to a <currency>200</currency> price, then on June 1 they’ll be billed <currency>250</currency> (<currency>200</currency> for a renewal of her subscription, plus a <currency>50</currency> prorating adjustment for half of the previous month’s <currency>100</currency> difference). Similarly, a downgrade generates a credit that is applied to the next invoice. We also prorate when you make quantity changes.</p>

        <p>Switching prices does not normally change the billing date or generate an immediate charge unless:</p>

        <ul>
        <li>The billing interval is changed (for example, from monthly to yearly).</li>
        <li>The subscription moves from free to paid.</li>
        <li>A trial starts or ends.</li>
        </ul>

        <p>In these cases, we apply a credit for the unused time on the previous price, immediately charge the customer using the new price, and reset the billing date. Learn about how <a href="/docs/billing/subscriptions/upgrade-downgrade#immediate-payment">Stripe immediately attempts payment for subscription changes</a>.</p>

        <p>If you want to charge for an upgrade immediately, pass <code>proration_behavior</code> as <code>always_invoice</code> to create prorations, automatically invoice the customer for those proration adjustments, and attempt to collect payment. If you pass <code>create_prorations</code>, the prorations are created but not automatically invoiced. If you want to bill the customer for the prorations before the subscription’s renewal date, you need to manually <a href="/docs/api/invoices/create">invoice the customer</a>.</p>

        <p>If you don’t want to prorate, set the <code>proration_behavior</code> option to <code>none</code>. With this option, the customer is billed <currency>100</currency> on May 1 and <currency>200</currency> on June 1. Similarly, if you set <code>proration_behavior</code> to <code>none</code> when switching between different billing intervals (for example, from monthly to yearly), we don’t generate any credits for the old subscription’s unused time. We still reset the billing date and bill immediately for the new subscription.</p>

        <p>Updating the quantity on a subscription many times in an hour may result in <a href="/docs/rate-limits">rate limiting</a>. If you need to bill for a frequently changing quantity, consider integrating <a href="/docs/billing/subscriptions/usage-based">usage-based billing</a> instead.</p>

        Args:
          add_invoice_items: A list of prices and quantities that will generate invoice items appended to the
              next invoice for this subscription. You may pass up to 20 items.

          application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This
              represents the percentage of the subscription invoice total that will be
              transferred to the application owner's Stripe account. The request must be made
              by a platform account on a connected account in order to set an application fee
              percentage. For more information, see the application fees
              [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).

          automatic_tax: Automatic tax settings for this subscription. We recommend you only include this
              parameter when the existing value is being changed.

          billing_cycle_anchor: Either `now` or `unchanged`. Setting the value to `now` resets the
              subscription's billing cycle anchor to the current time (in UTC). For more
              information, see the billing cycle
              [documentation](https://docs.stripe.com/billing/subscriptions/billing-cycle).

          billing_thresholds: Define thresholds at which an invoice will be sent, and the subscription
              advanced to a new billing period. When updating, pass an empty string to remove
              previously-defined thresholds.

          cancel_at: A timestamp at which the subscription should cancel. If set to a date before the
              current period ends, this will cause a proration if prorations have been enabled
              using `proration_behavior`. If set during a future period, this will always
              cause a proration for that period.

          cancel_at_period_end: Indicate whether this subscription should cancel at the end of the current
              period (`current_period_end`). Defaults to `false`.

          cancellation_details: Details about why this subscription was cancelled

          collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically,
              Stripe will attempt to pay this subscription at the end of the cycle using the
              default source attached to the customer. When sending an invoice, Stripe will
              email your customer an invoice with payment instructions and mark the
              subscription as `active`. Defaults to `charge_automatically`.

          days_until_due: Number of days a customer has to pay invoices generated by this subscription.
              Valid only for subscriptions where `collection_method` is set to `send_invoice`.

          default_payment_method: ID of the default payment method for the subscription. It must belong to the
              customer associated with the subscription. This takes precedence over
              `default_source`. If neither are set, invoices will use the customer's
              [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
              or
              [default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source).

          default_source: ID of the default payment source for the subscription. It must belong to the
              customer associated with the subscription and be in a chargeable state. If
              `default_payment_method` is also set, `default_payment_method` will take
              precedence. If neither are set, invoices will use the customer's
              [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
              or
              [default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source).

          default_tax_rates: The tax rates that will apply to any subscription item that does not have
              `tax_rates` set. Invoices created will have their `default_tax_rates` populated
              from the subscription. Pass an empty string to remove previously-defined tax
              rates.

          description: The subscription's description, meant to be displayable to the customer. Use
              this field to optionally store an explanation of the subscription for rendering
              in Stripe surfaces and certain local payment methods UIs.

          discounts: The coupons to redeem into discounts for the subscription. If not specified or
              empty, inherits the discount from the subscription's customer.

          expand: Specifies which fields in the response should be expanded.

          invoice_settings: All invoices will be billed using the specified settings.

          items: A list of up to 20 subscription items, each with an attached price.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          off_session: Indicates if a customer is on or off-session while an invoice payment is
              attempted. Defaults to `false` (on-session).

          on_behalf_of: The account on behalf of which to charge, for each of the subscription's
              invoices.

          pause_collection: If specified, payment collection for this subscription will be paused. Note that
              the subscription status will be unchanged and will not be updated to `paused`.
              Learn more about
              [pausing collection](https://docs.stripe.com/billing/subscriptions/pause-payment).

          payment_behavior: Use `allow_incomplete` to transition the subscription to `status=past_due` if a
              payment is required but cannot be paid. This allows you to manage scenarios
              where additional user actions are needed to pay a subscription's invoice. For
              example, SCA regulation may require 3DS authentication to complete payment. See
              the
              [SCA Migration Guide](https://docs.stripe.com/billing/migration/strong-customer-authentication)
              for Billing to learn more. This is the default behavior.

              Use `default_incomplete` to transition the subscription to `status=past_due`
              when payment is required and await explicit confirmation of the invoice's
              payment intent. This allows simpler management of scenarios where additional
              user actions are needed to pay a subscription’s invoice. Such as failed
              payments,
              [SCA regulation](https://docs.stripe.com/billing/migration/strong-customer-authentication),
              or collecting a mandate for a bank debit payment method.

              Use `pending_if_incomplete` to update the subscription using
              [pending updates](https://docs.stripe.com/billing/subscriptions/pending-updates).
              When you use `pending_if_incomplete` you can only pass the parameters
              [supported by pending updates](https://docs.stripe.com/billing/pending-updates-reference#supported-attributes).

              Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code
              if a subscription's invoice cannot be paid. For example, if a payment method
              requires 3DS authentication due to SCA regulation and further user action is
              needed, this parameter does not update the subscription and returns an error
              instead. This was the default behavior for API versions prior to 2019-03-14. See
              the [changelog](https://docs.stripe.com/changelog/2019-03-14) to learn more.

          payment_settings: Payment settings to pass to invoices created by the subscription.

          pending_invoice_item_interval: Specifies an interval for how often to bill for any pending invoice items. It is
              analogous to calling
              [Create an invoice](https://docs.stripe.com/api#create_invoice) for the given
              subscription at the specified interval.

          proration_behavior: Determines how to handle
              [prorations](https://docs.stripe.com/billing/subscriptions/prorations) when the
              billing cycle changes (e.g., when switching plans, resetting
              `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity`
              changes. The default value is `create_prorations`.

          proration_date: If set, prorations will be calculated as though the subscription was updated at
              the given time. This can be used to apply exactly the same prorations that were
              previewed with the
              [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint.
              `proration_date` can also be used to implement custom proration logic, such as
              prorating by day instead of by second, by providing the time that you wish to
              use for proration calculations.

          transfer_data: If specified, the funds from the subscription's invoices will be transferred to
              the destination and the ID of the resulting transfers will be found on the
              resulting charges. This will be unset if you POST an empty value.

          trial_end: Unix timestamp representing the end of the trial period the customer will get
              before being charged for the first time. This will always overwrite any trials
              that might apply via a subscribed plan. If set, `trial_end` will override the
              default trial period of the plan the customer is being subscribed to. The
              `billing_cycle_anchor` will be updated to the `trial_end` value. The special
              value `now` can be provided to end the customer's trial immediately. Can be at
              most two years from `billing_cycle_anchor`.

          trial_from_plan: Indicates if a plan's `trial_period_days` should be applied to the subscription.
              Setting `trial_end` per subscription is preferred, and this defaults to `false`.
              Setting this flag to `true` together with `trial_end` is not allowed. See
              [Using trial periods on subscriptions](https://docs.stripe.com/billing/subscriptions/trials)
              to learn more.

          trial_settings: Settings related to subscription trials.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_exposed_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_exposed_id` but received {subscription_exposed_id!r}"
            )
        return self._post(
            f"/v1/subscriptions/{subscription_exposed_id}",
            body=maybe_transform(
                {
                    "add_invoice_items": add_invoice_items,
                    "application_fee_percent": application_fee_percent,
                    "automatic_tax": automatic_tax,
                    "billing_cycle_anchor": billing_cycle_anchor,
                    "billing_thresholds": billing_thresholds,
                    "cancel_at": cancel_at,
                    "cancel_at_period_end": cancel_at_period_end,
                    "cancellation_details": cancellation_details,
                    "collection_method": collection_method,
                    "days_until_due": days_until_due,
                    "default_payment_method": default_payment_method,
                    "default_source": default_source,
                    "default_tax_rates": default_tax_rates,
                    "description": description,
                    "discounts": discounts,
                    "expand": expand,
                    "invoice_settings": invoice_settings,
                    "items": items,
                    "metadata": metadata,
                    "off_session": off_session,
                    "on_behalf_of": on_behalf_of,
                    "pause_collection": pause_collection,
                    "payment_behavior": payment_behavior,
                    "payment_settings": payment_settings,
                    "pending_invoice_item_interval": pending_invoice_item_interval,
                    "proration_behavior": proration_behavior,
                    "proration_date": proration_date,
                    "transfer_data": transfer_data,
                    "trial_end": trial_end,
                    "trial_from_plan": trial_from_plan,
                    "trial_settings": trial_settings,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    def list(
        self,
        *,
        automatic_tax: subscription_list_params.AutomaticTax | Omit = omit,
        collection_method: Literal["charge_automatically", "send_invoice"] | Omit = omit,
        created: subscription_list_params.Created | Omit = omit,
        current_period_end: subscription_list_params.CurrentPeriodEnd | Omit = omit,
        current_period_start: subscription_list_params.CurrentPeriodStart | Omit = omit,
        customer: str | Omit = omit,
        customer_account: str | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        price: str | Omit = omit,
        starting_after: str | Omit = omit,
        status: Literal[
            "active",
            "all",
            "canceled",
            "ended",
            "incomplete",
            "incomplete_expired",
            "past_due",
            "paused",
            "trialing",
            "unpaid",
        ]
        | Omit = omit,
        test_clock: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """<p>By default, returns a list of subscriptions that have not been canceled.

        In order to list canceled subscriptions, specify <code>status=canceled</code>.</p>

        Args:
          automatic_tax: Filter subscriptions by their automatic tax settings.

          collection_method: The collection method of the subscriptions to retrieve. Either
              `charge_automatically` or `send_invoice`.

          created: Only return subscriptions that were created during the given date interval.

          current_period_end: Only return subscriptions whose minimum item current_period_end falls within the
              given date interval.

          current_period_start: Only return subscriptions whose maximum item current_period_start falls within
              the given date interval.

          customer: The ID of the customer whose subscriptions you're retrieving.

          customer_account: The ID of the account representing the customer whose subscriptions you're
              retrieving.

          ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, starting with `obj_bar`, your subsequent call can include
              `ending_before=obj_bar` in order to fetch the previous page of the list.

          expand: Specifies which fields in the response should be expanded.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 10.

          price: Filter for subscriptions that contain this recurring price ID.

          starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, ending with `obj_foo`, your subsequent call can include
              `starting_after=obj_foo` in order to fetch the next page of the list.

          status: The status of the subscriptions to retrieve. Passing in a value of `canceled`
              will return all canceled subscriptions, including those belonging to deleted
              customers. Pass `ended` to find subscriptions that are canceled and
              subscriptions that are expired due to
              [incomplete payment](https://docs.stripe.com/billing/subscriptions/overview#subscription-statuses).
              Passing in a value of `all` will return subscriptions of all statuses. If no
              value is supplied, all subscriptions that have not been canceled are returned.

          test_clock: Filter for subscriptions that are associated with the specified test clock. The
              response will not include subscriptions with test clocks if this and the
              customer parameter is not set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "automatic_tax": automatic_tax,
                        "collection_method": collection_method,
                        "created": created,
                        "current_period_end": current_period_end,
                        "current_period_start": current_period_start,
                        "customer": customer,
                        "customer_account": customer_account,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "price": price,
                        "starting_after": starting_after,
                        "status": status,
                        "test_clock": test_clock,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            cast_to=SubscriptionListResponse,
        )

    def cancel(
        self,
        subscription_exposed_id: str,
        *,
        cancellation_details: subscription_cancel_params.CancellationDetails | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        invoice_now: bool | Omit = omit,
        prorate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """<p>Cancels a customer’s subscription immediately.

        The customer won’t be charged again for the subscription. After it’s canceled, you can no longer update the subscription or its <a href="/metadata">metadata</a>.</p>

        <p>Any pending invoice items that you’ve created are still charged at the end of the period, unless manually <a href="#delete_invoiceitem">deleted</a>. If you’ve set the subscription to cancel at the end of the period, any pending prorations are also left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations are removed if <code>invoice_now</code> and <code>prorate</code> are both set to true.</p>

        <p>By default, upon subscription cancellation, Stripe stops automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.</p>

        Args:
          cancellation_details: Details about why this subscription was cancelled

          expand: Specifies which fields in the response should be expanded.

          invoice_now: Will generate a final invoice that invoices for any un-invoiced metered usage
              and new/pending proration invoice items. Defaults to `false`.

          prorate: Will generate a proration invoice item that credits remaining unused time until
              the subscription period end. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_exposed_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_exposed_id` but received {subscription_exposed_id!r}"
            )
        return self._delete(
            f"/v1/subscriptions/{subscription_exposed_id}",
            body=maybe_transform(
                {
                    "cancellation_details": cancellation_details,
                    "expand": expand,
                    "invoice_now": invoice_now,
                    "prorate": prorate,
                },
                subscription_cancel_params.SubscriptionCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stripe-minimal-python#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def update(
        self,
        subscription_exposed_id: str,
        *,
        add_invoice_items: Iterable[subscription_update_params.AddInvoiceItem] | Omit = omit,
        application_fee_percent: Union[float, Literal[""]] | Omit = omit,
        automatic_tax: subscription_update_params.AutomaticTax | Omit = omit,
        billing_cycle_anchor: Literal["now", "unchanged"] | Omit = omit,
        billing_thresholds: subscription_update_params.BillingThresholds | Omit = omit,
        cancel_at: Union[Literal["", "max_period_end", "min_period_end"], int] | Omit = omit,
        cancel_at_period_end: bool | Omit = omit,
        cancellation_details: subscription_update_params.CancellationDetails | Omit = omit,
        collection_method: Literal["charge_automatically", "send_invoice"] | Omit = omit,
        days_until_due: int | Omit = omit,
        default_payment_method: str | Omit = omit,
        default_source: Union[str, Literal[""]] | Omit = omit,
        default_tax_rates: Union[SequenceNotStr[str], Literal[""]] | Omit = omit,
        description: Union[str, Literal[""]] | Omit = omit,
        discounts: Union[Iterable[subscription_update_params.DiscountsDiscountsList], Literal[""]] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        invoice_settings: subscription_update_params.InvoiceSettings | Omit = omit,
        items: Iterable[subscription_update_params.Item] | Omit = omit,
        metadata: Union[Dict[str, str], Literal[""]] | Omit = omit,
        off_session: bool | Omit = omit,
        on_behalf_of: Union[str, Literal[""]] | Omit = omit,
        pause_collection: subscription_update_params.PauseCollection | Omit = omit,
        payment_behavior: Literal[
            "allow_incomplete", "default_incomplete", "error_if_incomplete", "pending_if_incomplete"
        ]
        | Omit = omit,
        payment_settings: subscription_update_params.PaymentSettings | Omit = omit,
        pending_invoice_item_interval: subscription_update_params.PendingInvoiceItemInterval | Omit = omit,
        proration_behavior: Literal["always_invoice", "create_prorations", "none"] | Omit = omit,
        proration_date: int | Omit = omit,
        transfer_data: subscription_update_params.TransferData | Omit = omit,
        trial_end: Union[Literal["now"], int] | Omit = omit,
        trial_from_plan: bool | Omit = omit,
        trial_settings: subscription_update_params.TrialSettings | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """
        <p>Updates an existing subscription to match the specified parameters.
        When changing prices or quantities, we optionally prorate the price we charge next month to make up for any price changes.
        To preview how the proration is calculated, use the <a href="/docs/api/invoices/create_preview">create preview</a> endpoint.</p>

        <p>By default, we prorate subscription changes. For example, if a customer signs up on May 1 for a <currency>100</currency> price, they’ll be billed <currency>100</currency> immediately. If on May 15 they switch to a <currency>200</currency> price, then on June 1 they’ll be billed <currency>250</currency> (<currency>200</currency> for a renewal of her subscription, plus a <currency>50</currency> prorating adjustment for half of the previous month’s <currency>100</currency> difference). Similarly, a downgrade generates a credit that is applied to the next invoice. We also prorate when you make quantity changes.</p>

        <p>Switching prices does not normally change the billing date or generate an immediate charge unless:</p>

        <ul>
        <li>The billing interval is changed (for example, from monthly to yearly).</li>
        <li>The subscription moves from free to paid.</li>
        <li>A trial starts or ends.</li>
        </ul>

        <p>In these cases, we apply a credit for the unused time on the previous price, immediately charge the customer using the new price, and reset the billing date. Learn about how <a href="/docs/billing/subscriptions/upgrade-downgrade#immediate-payment">Stripe immediately attempts payment for subscription changes</a>.</p>

        <p>If you want to charge for an upgrade immediately, pass <code>proration_behavior</code> as <code>always_invoice</code> to create prorations, automatically invoice the customer for those proration adjustments, and attempt to collect payment. If you pass <code>create_prorations</code>, the prorations are created but not automatically invoiced. If you want to bill the customer for the prorations before the subscription’s renewal date, you need to manually <a href="/docs/api/invoices/create">invoice the customer</a>.</p>

        <p>If you don’t want to prorate, set the <code>proration_behavior</code> option to <code>none</code>. With this option, the customer is billed <currency>100</currency> on May 1 and <currency>200</currency> on June 1. Similarly, if you set <code>proration_behavior</code> to <code>none</code> when switching between different billing intervals (for example, from monthly to yearly), we don’t generate any credits for the old subscription’s unused time. We still reset the billing date and bill immediately for the new subscription.</p>

        <p>Updating the quantity on a subscription many times in an hour may result in <a href="/docs/rate-limits">rate limiting</a>. If you need to bill for a frequently changing quantity, consider integrating <a href="/docs/billing/subscriptions/usage-based">usage-based billing</a> instead.</p>

        Args:
          add_invoice_items: A list of prices and quantities that will generate invoice items appended to the
              next invoice for this subscription. You may pass up to 20 items.

          application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This
              represents the percentage of the subscription invoice total that will be
              transferred to the application owner's Stripe account. The request must be made
              by a platform account on a connected account in order to set an application fee
              percentage. For more information, see the application fees
              [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).

          automatic_tax: Automatic tax settings for this subscription. We recommend you only include this
              parameter when the existing value is being changed.

          billing_cycle_anchor: Either `now` or `unchanged`. Setting the value to `now` resets the
              subscription's billing cycle anchor to the current time (in UTC). For more
              information, see the billing cycle
              [documentation](https://docs.stripe.com/billing/subscriptions/billing-cycle).

          billing_thresholds: Define thresholds at which an invoice will be sent, and the subscription
              advanced to a new billing period. When updating, pass an empty string to remove
              previously-defined thresholds.

          cancel_at: A timestamp at which the subscription should cancel. If set to a date before the
              current period ends, this will cause a proration if prorations have been enabled
              using `proration_behavior`. If set during a future period, this will always
              cause a proration for that period.

          cancel_at_period_end: Indicate whether this subscription should cancel at the end of the current
              period (`current_period_end`). Defaults to `false`.

          cancellation_details: Details about why this subscription was cancelled

          collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically,
              Stripe will attempt to pay this subscription at the end of the cycle using the
              default source attached to the customer. When sending an invoice, Stripe will
              email your customer an invoice with payment instructions and mark the
              subscription as `active`. Defaults to `charge_automatically`.

          days_until_due: Number of days a customer has to pay invoices generated by this subscription.
              Valid only for subscriptions where `collection_method` is set to `send_invoice`.

          default_payment_method: ID of the default payment method for the subscription. It must belong to the
              customer associated with the subscription. This takes precedence over
              `default_source`. If neither are set, invoices will use the customer's
              [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
              or
              [default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source).

          default_source: ID of the default payment source for the subscription. It must belong to the
              customer associated with the subscription and be in a chargeable state. If
              `default_payment_method` is also set, `default_payment_method` will take
              precedence. If neither are set, invoices will use the customer's
              [invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
              or
              [default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source).

          default_tax_rates: The tax rates that will apply to any subscription item that does not have
              `tax_rates` set. Invoices created will have their `default_tax_rates` populated
              from the subscription. Pass an empty string to remove previously-defined tax
              rates.

          description: The subscription's description, meant to be displayable to the customer. Use
              this field to optionally store an explanation of the subscription for rendering
              in Stripe surfaces and certain local payment methods UIs.

          discounts: The coupons to redeem into discounts for the subscription. If not specified or
              empty, inherits the discount from the subscription's customer.

          expand: Specifies which fields in the response should be expanded.

          invoice_settings: All invoices will be billed using the specified settings.

          items: A list of up to 20 subscription items, each with an attached price.

          metadata: Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
              attach to an object. This can be useful for storing additional information about
              the object in a structured format. Individual keys can be unset by posting an
              empty value to them. All keys can be unset by posting an empty value to
              `metadata`.

          off_session: Indicates if a customer is on or off-session while an invoice payment is
              attempted. Defaults to `false` (on-session).

          on_behalf_of: The account on behalf of which to charge, for each of the subscription's
              invoices.

          pause_collection: If specified, payment collection for this subscription will be paused. Note that
              the subscription status will be unchanged and will not be updated to `paused`.
              Learn more about
              [pausing collection](https://docs.stripe.com/billing/subscriptions/pause-payment).

          payment_behavior: Use `allow_incomplete` to transition the subscription to `status=past_due` if a
              payment is required but cannot be paid. This allows you to manage scenarios
              where additional user actions are needed to pay a subscription's invoice. For
              example, SCA regulation may require 3DS authentication to complete payment. See
              the
              [SCA Migration Guide](https://docs.stripe.com/billing/migration/strong-customer-authentication)
              for Billing to learn more. This is the default behavior.

              Use `default_incomplete` to transition the subscription to `status=past_due`
              when payment is required and await explicit confirmation of the invoice's
              payment intent. This allows simpler management of scenarios where additional
              user actions are needed to pay a subscription’s invoice. Such as failed
              payments,
              [SCA regulation](https://docs.stripe.com/billing/migration/strong-customer-authentication),
              or collecting a mandate for a bank debit payment method.

              Use `pending_if_incomplete` to update the subscription using
              [pending updates](https://docs.stripe.com/billing/subscriptions/pending-updates).
              When you use `pending_if_incomplete` you can only pass the parameters
              [supported by pending updates](https://docs.stripe.com/billing/pending-updates-reference#supported-attributes).

              Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code
              if a subscription's invoice cannot be paid. For example, if a payment method
              requires 3DS authentication due to SCA regulation and further user action is
              needed, this parameter does not update the subscription and returns an error
              instead. This was the default behavior for API versions prior to 2019-03-14. See
              the [changelog](https://docs.stripe.com/changelog/2019-03-14) to learn more.

          payment_settings: Payment settings to pass to invoices created by the subscription.

          pending_invoice_item_interval: Specifies an interval for how often to bill for any pending invoice items. It is
              analogous to calling
              [Create an invoice](https://docs.stripe.com/api#create_invoice) for the given
              subscription at the specified interval.

          proration_behavior: Determines how to handle
              [prorations](https://docs.stripe.com/billing/subscriptions/prorations) when the
              billing cycle changes (e.g., when switching plans, resetting
              `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity`
              changes. The default value is `create_prorations`.

          proration_date: If set, prorations will be calculated as though the subscription was updated at
              the given time. This can be used to apply exactly the same prorations that were
              previewed with the
              [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint.
              `proration_date` can also be used to implement custom proration logic, such as
              prorating by day instead of by second, by providing the time that you wish to
              use for proration calculations.

          transfer_data: If specified, the funds from the subscription's invoices will be transferred to
              the destination and the ID of the resulting transfers will be found on the
              resulting charges. This will be unset if you POST an empty value.

          trial_end: Unix timestamp representing the end of the trial period the customer will get
              before being charged for the first time. This will always overwrite any trials
              that might apply via a subscribed plan. If set, `trial_end` will override the
              default trial period of the plan the customer is being subscribed to. The
              `billing_cycle_anchor` will be updated to the `trial_end` value. The special
              value `now` can be provided to end the customer's trial immediately. Can be at
              most two years from `billing_cycle_anchor`.

          trial_from_plan: Indicates if a plan's `trial_period_days` should be applied to the subscription.
              Setting `trial_end` per subscription is preferred, and this defaults to `false`.
              Setting this flag to `true` together with `trial_end` is not allowed. See
              [Using trial periods on subscriptions](https://docs.stripe.com/billing/subscriptions/trials)
              to learn more.

          trial_settings: Settings related to subscription trials.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_exposed_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_exposed_id` but received {subscription_exposed_id!r}"
            )
        return await self._post(
            f"/v1/subscriptions/{subscription_exposed_id}",
            body=await async_maybe_transform(
                {
                    "add_invoice_items": add_invoice_items,
                    "application_fee_percent": application_fee_percent,
                    "automatic_tax": automatic_tax,
                    "billing_cycle_anchor": billing_cycle_anchor,
                    "billing_thresholds": billing_thresholds,
                    "cancel_at": cancel_at,
                    "cancel_at_period_end": cancel_at_period_end,
                    "cancellation_details": cancellation_details,
                    "collection_method": collection_method,
                    "days_until_due": days_until_due,
                    "default_payment_method": default_payment_method,
                    "default_source": default_source,
                    "default_tax_rates": default_tax_rates,
                    "description": description,
                    "discounts": discounts,
                    "expand": expand,
                    "invoice_settings": invoice_settings,
                    "items": items,
                    "metadata": metadata,
                    "off_session": off_session,
                    "on_behalf_of": on_behalf_of,
                    "pause_collection": pause_collection,
                    "payment_behavior": payment_behavior,
                    "payment_settings": payment_settings,
                    "pending_invoice_item_interval": pending_invoice_item_interval,
                    "proration_behavior": proration_behavior,
                    "proration_date": proration_date,
                    "transfer_data": transfer_data,
                    "trial_end": trial_end,
                    "trial_from_plan": trial_from_plan,
                    "trial_settings": trial_settings,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    async def list(
        self,
        *,
        automatic_tax: subscription_list_params.AutomaticTax | Omit = omit,
        collection_method: Literal["charge_automatically", "send_invoice"] | Omit = omit,
        created: subscription_list_params.Created | Omit = omit,
        current_period_end: subscription_list_params.CurrentPeriodEnd | Omit = omit,
        current_period_start: subscription_list_params.CurrentPeriodStart | Omit = omit,
        customer: str | Omit = omit,
        customer_account: str | Omit = omit,
        ending_before: str | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        price: str | Omit = omit,
        starting_after: str | Omit = omit,
        status: Literal[
            "active",
            "all",
            "canceled",
            "ended",
            "incomplete",
            "incomplete_expired",
            "past_due",
            "paused",
            "trialing",
            "unpaid",
        ]
        | Omit = omit,
        test_clock: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """<p>By default, returns a list of subscriptions that have not been canceled.

        In order to list canceled subscriptions, specify <code>status=canceled</code>.</p>

        Args:
          automatic_tax: Filter subscriptions by their automatic tax settings.

          collection_method: The collection method of the subscriptions to retrieve. Either
              `charge_automatically` or `send_invoice`.

          created: Only return subscriptions that were created during the given date interval.

          current_period_end: Only return subscriptions whose minimum item current_period_end falls within the
              given date interval.

          current_period_start: Only return subscriptions whose maximum item current_period_start falls within
              the given date interval.

          customer: The ID of the customer whose subscriptions you're retrieving.

          customer_account: The ID of the account representing the customer whose subscriptions you're
              retrieving.

          ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, starting with `obj_bar`, your subsequent call can include
              `ending_before=obj_bar` in order to fetch the previous page of the list.

          expand: Specifies which fields in the response should be expanded.

          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              100, and the default is 10.

          price: Filter for subscriptions that contain this recurring price ID.

          starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines
              your place in the list. For instance, if you make a list request and receive 100
              objects, ending with `obj_foo`, your subsequent call can include
              `starting_after=obj_foo` in order to fetch the next page of the list.

          status: The status of the subscriptions to retrieve. Passing in a value of `canceled`
              will return all canceled subscriptions, including those belonging to deleted
              customers. Pass `ended` to find subscriptions that are canceled and
              subscriptions that are expired due to
              [incomplete payment](https://docs.stripe.com/billing/subscriptions/overview#subscription-statuses).
              Passing in a value of `all` will return subscriptions of all statuses. If no
              value is supplied, all subscriptions that have not been canceled are returned.

          test_clock: Filter for subscriptions that are associated with the specified test clock. The
              response will not include subscriptions with test clocks if this and the
              customer parameter is not set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "automatic_tax": automatic_tax,
                        "collection_method": collection_method,
                        "created": created,
                        "current_period_end": current_period_end,
                        "current_period_start": current_period_start,
                        "customer": customer,
                        "customer_account": customer_account,
                        "ending_before": ending_before,
                        "expand": expand,
                        "limit": limit,
                        "price": price,
                        "starting_after": starting_after,
                        "status": status,
                        "test_clock": test_clock,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            cast_to=SubscriptionListResponse,
        )

    async def cancel(
        self,
        subscription_exposed_id: str,
        *,
        cancellation_details: subscription_cancel_params.CancellationDetails | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        invoice_now: bool | Omit = omit,
        prorate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """<p>Cancels a customer’s subscription immediately.

        The customer won’t be charged again for the subscription. After it’s canceled, you can no longer update the subscription or its <a href="/metadata">metadata</a>.</p>

        <p>Any pending invoice items that you’ve created are still charged at the end of the period, unless manually <a href="#delete_invoiceitem">deleted</a>. If you’ve set the subscription to cancel at the end of the period, any pending prorations are also left in place and collected at the end of the period. But if the subscription is set to cancel immediately, pending prorations are removed if <code>invoice_now</code> and <code>prorate</code> are both set to true.</p>

        <p>By default, upon subscription cancellation, Stripe stops automatic collection of all finalized invoices for the customer. This is intended to prevent unexpected payment attempts after the customer has canceled a subscription. However, you can resume automatic collection of the invoices manually after subscription cancellation to have us proceed. Or, you could check for unpaid invoices before allowing the customer to cancel the subscription at all.</p>

        Args:
          cancellation_details: Details about why this subscription was cancelled

          expand: Specifies which fields in the response should be expanded.

          invoice_now: Will generate a final invoice that invoices for any un-invoiced metered usage
              and new/pending proration invoice items. Defaults to `false`.

          prorate: Will generate a proration invoice item that credits remaining unused time until
              the subscription period end. Defaults to `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_exposed_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_exposed_id` but received {subscription_exposed_id!r}"
            )
        return await self._delete(
            f"/v1/subscriptions/{subscription_exposed_id}",
            body=await async_maybe_transform(
                {
                    "cancellation_details": cancellation_details,
                    "expand": expand,
                    "invoice_now": invoice_now,
                    "prorate": prorate,
                },
                subscription_cancel_params.SubscriptionCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.update = to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.cancel = to_raw_response_wrapper(
            subscriptions.cancel,
        )


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.update = async_to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            subscriptions.cancel,
        )


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.update = to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.cancel = to_streamed_response_wrapper(
            subscriptions.cancel,
        )


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.update = async_to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            subscriptions.cancel,
        )
