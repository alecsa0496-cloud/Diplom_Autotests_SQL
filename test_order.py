# Александра Муратова, 39-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_create_and_fetch_order():
    create_response = sender_stand_request.create_order(data.order_body)

    if create_response.status_code == 201:
        tracker_id = create_response.json().get("track")
        print(f"Заказ успешно создан. Номер трекера: {tracker_id}")
    else:
        print(f"Ошибка при создании заказа: {create_response.status_code}")
        return

    fetch_response = sender_stand_request.get_order(tracker_id)

    if fetch_response.status_code == 200:
        order_details = fetch_response.json()
        print("Информация о заказе:")
        print(order_details)
    else:
        print(f"Ошибка: получен статус-код {fetch_response.status_code}")
    
    assert fetch_response.status_code == 200, f"Ошибка при получении данных заказа: {fetch_response.status_code}"

if __name__ == "__main__":
    test_create_and_fetch_order()