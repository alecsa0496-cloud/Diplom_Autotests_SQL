
```python
import configuration
import requests

# Создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}{configuration.FETCH_ORDER_TRACK}?t={track_number}"
    response = requests.get(get_order_url)
    return response