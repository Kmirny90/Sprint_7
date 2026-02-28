import pytest
import allure
from generators import generate_couriers_body, generate_order_body
from api_methods.courier_methods import CourierMethods
from api_methods.order_methods import OrderMethods


@pytest.fixture
def random_courier_data():
    courier_data = generate_couriers_body()
    yield courier_data

    response = CourierMethods.login_courier(
        courier_data['login'],
        courier_data['password']
    )
    if response.status_code == 200:
        courier_id = response.json()['id']
        CourierMethods.delete_courier(courier_id)

@pytest.fixture
def created_courier(random_courier_data):

    with allure.step("Создание курьера через фикстуру"):

        CourierMethods.create_courier(random_courier_data)

        auth_response = CourierMethods.login_courier(
            random_courier_data['login'],
            random_courier_data['password']
        )
        courier_id = auth_response.json()['id']

        courier_info = {
            "login": random_courier_data['login'],
            "password": random_courier_data['password'],
            "first_name": random_courier_data['firstName'],
            "id": courier_id
        }

        yield courier_info

        with allure.step("Удаление курьера после теста"):
            CourierMethods.delete_courier(courier_id)


@pytest.fixture
def created_order():

    with allure.step("Создание заказа через фикстуру"):
        order_data = generate_order_body()
        response = OrderMethods.create_order(order_data)
        track = response.json()['track']

        yield track

        with allure.step("Отмена заказа после теста"):
            OrderMethods.cancel_order(track)

@pytest.fixture
def order_data_without_color():

    return generate_order_body()

@pytest.fixture
def auth_data(created_courier):

    return {
        "login": created_courier["login"],
        "password": created_courier["password"]
    }
