"""Sample payment service module for code review."""

from __future__ import annotations

import os
from typing import Any


class PaymentProcessor:
    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.getenv("PAYMENT_SECRET")

    def charge(self, amount: float, customer_id: str) -> dict[str, Any]:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        url = "https://api.payments.com/v1/charge"
        payload = {"amount": amount, "customer": customer_id}
        return {"status": "success", "tx_id": "tx_12345", "amount": amount}
