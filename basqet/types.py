from typing import NamedTuple


class Currencies(NamedTuple):
    id: str
    name: str
    slug: str
    type: str
    icon_url: str
    created_at: str
    updated_at: int


class TransactionPayload(NamedTuple):
    id: str
    reference: str
    status: str
    initialized_amount: str
    initialized_currency: str
    merchant_id: str = None
    customer_id: str = None
    amount_paid: str = None
    description: str = None
    payment_amount: str = None
    payment_address: str = None
    payment_currency: str = None
    merchant: dict
    fee: str = None
    processor_id: str = None
    expiry_date: str = None
    created_at: str = None
    updated_at: str = None
    description: str = None
    merchant: dict = None
    qrCode: str = None


class ResponseTransaction(NamedTuple):
    status: str
    data: TransactionPayload
    meta: dict

class TransactionStatus(NamedTuple):
    status: str

class VerifyTransaction(NamedTuple):
    status: str
    data: TransactionStatus
    meta: dict
