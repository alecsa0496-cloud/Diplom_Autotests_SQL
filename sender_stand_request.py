import configuration
import requests


def create_order(body):
    """Создание нового заказа."""
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=body
    )


def get_order(track_number):
    """Получение информации о заказе по номеру трека."""
    get_order_url = (
        f"{configuration.URL_SERVICE}"
        f"{configuration.FETCH_ORDER_TRACK}"
        f"?t={track_number}"
    )
    response = requests.get(get_order_url)
    return response
