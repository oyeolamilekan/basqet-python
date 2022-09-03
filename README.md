
# Basqet Python SDK

The Official Python library for the Basqet API.

## Installation

Install Python

```bash
     pip install basqet-python
```

## Usage/Examples

#### Fetch Available currency

```python
from basqet import BasqetClient

basqet = BasqetClient("pub_test_Y4oKBXgfTU1JbJiHeGFc66rc1FFivg-",
                    "sec_test_eOX9Tp7z-EgK6sw9ijghAWqC9xR_rP0",)

# Fetch all fiat currency
currencies = basqet.fetch_all_currency("FIAT")

```


#### Initialize transaction


```python
from basqet import BasqetClient

basqet = BasqetClient("pub_test_Y4oKBXgfTU1JbJiHeGFc66rc1FFivg-",
                    "sec_test_eOX9Tp7z-EgK6sw9ijghAWqC9xR_rP0",)

payment_data = {
     "customer": {
          "name": "tunde",
          "email": "customer@example.com"
     },
     "amount": "1000",
     "currency": "NGN",
     "meta": {
          "reference": "bghggbbvv"
     }
}

transaction_obj = basqet.initialize_transaction(payment_data);

```


#### Initiate transaction

```python
from basqet import BasqetClient

basqet = BasqetClient("pub_test_Y4oKBXgfTU1JbJiHeGFc66rc1FFivg-",
                    "sec_test_eOX9Tp7z-EgK6sw9ijghAWqC9xR_rP0",)

transaction_obj = basqet.initiate_transaction(<transactionId>, {'currency_id': <currency_id>})

```


#### Verify transaction

```javascript
from basqet import BasqetClient

basqet = BasqetClient("pub_test_Y4oKBXgfTU1JbJiHeGFc66rc1FFivg-",
                    "sec_test_eOX9Tp7z-EgK6sw9ijghAWqC9xR_rP0",)

transaction_obj = basqet.verify_transaction(<transactionId>)

```

#### Mock webhook events

```javascript
from basqet import BasqetClient

basqet = BasqetClient("pub_test_Y4oKBXgfTU1JbJiHeGFc66rc1FFivg-",
                    "sec_test_eOX9Tp7z-EgK6sw9ijghAWqC9xR_rP0",)

transaction_obj = basqet.mock_webhook_event(<transactionId>, { status: 'SUCCESSFUL' })

```

## Documentation/API reference

[Documentation](https://docs.basqet.com/docs)