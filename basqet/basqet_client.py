from typing import List
from .exceptions.switch_errors import SwitchErrorStates
from .network_client import NetworkClient
from .types import Currencies, ResponseTransaction, TransactionPayload, TransactionStatus, VerifyTransaction


class BasqetClient():

    def __init__(self, pubKey, secretKey) -> None:
        self.request = NetworkClient(
            pubKey=pubKey,
            secretKey=secretKey
        )

    def fetch_all_currency(self, currenyType: str | None) -> List[Currencies]:
        """
        Fetch Available currency

        Args:
            currenyType (string | None)
        Returns:
            List[Currencies]: A list of Currencies
        """

        try:
            data = []

            all_currencies_response = self.request.get(
                f"currency{'?type=' + currenyType if currenyType else ''}")

            all_currencies = all_currencies_response['data']

            for currency in all_currencies:
                currencies = Currencies._make(
                    [
                        currency.get('id', None),
                        currency.get('name', None),
                        currency.get('slug', None),
                        currency.get('icon_url', None),
                        currency.get('type', None),
                        currency.get('created_at', None),
                        currency.get('updated_at', None)
                    ]
                )
                data.append(currencies)
            return data
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def initialize_transaction(self, **data: dict) -> ResponseTransaction:
        """
        Initialize transaction

        Args:
            data: (dict | None)
        Returns:
            ResponseTransaction: Transaction Response
        """
        try:
            response = self.request.post("transaction", data)
            response_transaction = ResponseTransaction(
                status=response['status'],
                data=TransactionPayload(
                    id=response.get('data', None).get('id'),
                    reference=response.get('data', None).get('reference'),
                    amount_paid=response.get('data', None).get('amount_paid'),
                    status=response.get('data', None).get('status'),
                    description=response.get('data', None).get('description'),
                    initialized_amount=response.get(
                        'data', None).get('initialized_amount'),
                    payment_amount=response.get(
                        'data', None).get('payment_amount'),
                    payment_address=response.get(
                        'data', None).get('payment_address'),
                    payment_currency=response.get(
                        'data', None).get('payment_currency'),
                    initialized_currency=response.get(
                        'data', None).get('initialized_currency'),
                ),
                meta=response['meta']
            )
            return response_transaction
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def initiate_transaction(self, transaction_id: str,  **data: dict) -> ResponseTransaction:
        """
        Initiate transaction

        Args:
            transaction_id: str
            data: (dict | None)
        Returns:
            ResponseTransaction: Transaction Response
        """
        try:
            response = self.request.post(
                f"transaction/{transaction_id}/pay", data)
            response_transaction = ResponseTransaction(
                status=response.get('status', None),
                data=TransactionPayload(
                    id=response.get('data', None).get('id'),
                    merchant_id=response.get(
                        'data', None).get('merchant_id', None),
                    customer_id=response.get(
                        'data', None).get('customer_id', None),
                    reference=response.get(
                        'data', None).get('reference', None),
                    amount_paid=response.get(
                        'data', None).get('amount_paid', None),
                    status=response.get('data', None).get('status', None),
                    description=response.get(
                        'data', None).get('description', None),
                    initialized_amount=response.get(
                        'data', None).get('initialized_amount', None),
                    payment_amount=response.get(
                        'data', None).get('payment_amount', None),
                    payment_address=response.get(
                        'data', None).get('payment_address', None),
                    payment_currency=response.get(
                        'data', None).get('payment_currency', None),
                    expiry_date=response.get(
                        'data', None).get('expiry_date', None),
                    fee=response.get('data', None).get('fee', None),
                    initialized_currency=response.get(
                        'data', None).get('initialized_currency', None),
                    merchant=response.get('data', None).get('merchant', None),
                    qrCode=response.get('data', None).get('qrCode', None),
                    processor_id=response.get(
                        'data', None).get('processor_id', None),
                    created_at=response.get(
                        'data', None).get('created_at', None),
                    updated_at=response.get(
                        'data', None).get('updated_at', None),
                ),
                meta=response['meta']
            )
            return response_transaction
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def verify_transaction(self, transaction_id: str) -> VerifyTransaction:
        """
        Verify transaction

        Args:
            transaction_id: str
        Returns:
            VerifyTransaction: Transaction Response
        """
        try:
            response = self.request.get(f"transaction/{transaction_id}/status")
            verify_transaction_response = VerifyTransaction(
                status=response.get('status'), data=TransactionStatus(status=response.get('data').get('status'),), meta=response.get('meta'),)
            return verify_transaction_response
        except Exception as e:
            raise SwitchErrorStates(e).switch()

    def mock_webhook_event(self, transaction_id: str, **data: dict) -> VerifyTransaction:
        """
        Mock webhook events

        Args:
            transaction_id: str
            data: (dict | None)
        Returns:
            ResponseTransaction: Transaction Response
        """
        try:
            response = self.request.post(
                f'transaction/${transaction_id}/trigger', data)
            verify_transaction_response = VerifyTransaction(
                status=response.get('status'), data=TransactionStatus(status=response.get('data').get('status'),), meta=response.get('meta'),)
            return verify_transaction_response
        except Exception as e:
            raise SwitchErrorStates(e).switch()
