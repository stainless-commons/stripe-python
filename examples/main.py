import os
from stripe_minimal import Stripe

client = Stripe(
    api_key="sk_test_51Sy0NhELd4ERPg8AvPDZIWNSWXVy3t5ODTl4ZauMCH1ZXLElyErHSS25XqECZjwtYWOgJoxqk9ecBiKntPh9sYeL00fXrvd9aL",  # This is the default and can be omitted
)

account = client.accounts.retrieve()
print(account.id)