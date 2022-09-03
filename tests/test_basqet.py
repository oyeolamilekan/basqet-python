from unittest import TestCase

from basqet.basqet_client import BasqetClient



class BasqetTest(TestCase):
    def setUp(self) -> None:
        self.basqet_client = BasqetClient("pub_test_Y4oKBXgfTU1JbJiHeGFc66rc1FFivg-",
                                          "sec_test_eOX9Tp7z-EgK6sw9ijghAWqC9xR_rP0",)
        self.transaction_reference = 'bq_gLIKZImiud4ELLrWV'

    def test_fetch_all_currency(self):
        all_currency = self.basqet_client.fetch_all_currency("FIAT")
        self.assertEqual(
            type(all_currency),
            list
        )

    def test_initialize_transaction(self):
        transaction_data = {
            "customer": {
                "name": "tunde",
                "email": "customer@example.com"
            },
            "amount": "1000",
            "currency": "NGN",
            "meta": {
                "reference": "f"
            }
        }

        transaction_response = self.basqet_client.initialize_transaction(
            **transaction_data)

        transaction_id = transaction_response.data.id

        transaction_payload = {
            "currency_id": 3
        }

        initiate_transaction_response = self.basqet_client.initiate_transaction(
            transaction_id, **transaction_payload)
        
        self.assertEqual(
            transaction_response.status,
            'success'
        )

        self.assertEqual(
            transaction_response.data.status,
            'INITIATED'
        )

        self.assertEqual(
            transaction_response.data.initialized_amount,
            int(transaction_data["amount"])
        )

        self.assertEqual(
            initiate_transaction_response.data.payment_currency,
            'USDT'
        )

        self.assertEqual(
            type(initiate_transaction_response.data.payment_amount),
            float
        )
    
    def test_verify_transaction(self):
        transaction_response = self.basqet_client.verify_transaction(self.transaction_reference)

        self.assertEqual(
            transaction_response.status,
            'success'
        )

        self.assertEqual(
            transaction_response.data.status,
            'PENDING'
        )
    
    def test_mock_webhook_event(self):
        transaction_response = self.basqet_client.mock_webhook_event(self.transaction_reference, **{'status': 'SUCCESSFUL'})

        self.assertEqual(
            transaction_response.status,
            'success'
        )

        self.assertEqual(
            transaction_response.data.status,
            'SUCCESSFUL'
        )