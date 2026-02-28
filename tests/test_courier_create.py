import allure
import pytest
from data.courier_data import ERROR_MESSAGES
from api_methods.courier_methods import CourierMethods
from generators import generate_couriers_body


class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    @allure.description("Проверка, что курьера можно создать с валидными данными")
    def test_create_courier_success(self, random_courier_data):
        response = CourierMethods.create_courier(random_courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Проверка, что повторное создание курьера с теми же данными возвращает ошибку")
    def test_create_duplicate_courier_fails(self, random_courier_data):
        with allure.step("Создаем первого курьера"):
            response1 = CourierMethods.create_courier(random_courier_data)
            assert response1.status_code == 201

        with allure.step("Пытаемся создать такого же курьера повторно"):
            response2 = CourierMethods.create_courier(random_courier_data)

        assert response2.status_code == 409
        assert response2.json()["message"] == ERROR_MESSAGES["login_already_used"]

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Создание курьера без поля {missing_field}")
    def test_create_courier_missing_required_field_fails(self, missing_field):
        courier_body = generate_couriers_body()
        del courier_body[missing_field]

        response = CourierMethods.create_courier(courier_body)
        assert response.status_code == 400

    @allure.title("Создание курьера без firstName — успешно")
    def test_create_courier_without_firstname_success(self):
        courier_body = generate_couriers_body()
        del courier_body["firstName"]

        response = CourierMethods.create_courier(courier_body)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        auth_response = CourierMethods.login_courier(
            courier_body['login'],
            courier_body['password']
        )
        courier_id = auth_response.json()["id"]
        CourierMethods.delete_courier(courier_id)


    @allure.title("Создание курьера с существующим логином")
    @allure.description("Проверка, что нельзя создать курьера с логином, который уже есть в системе")
    def test_create_courier_with_existing_login_fails(self, random_courier_data):
        with allure.step("Создаем первого курьера"):
            response1 = CourierMethods.create_courier(random_courier_data)
            assert response1.status_code == 201

        with allure.step("Пытаемся создать курьера с таким же логином, но другим паролем"):
            duplicate_login_data = random_courier_data.copy()
            duplicate_login_data['password'] = "different_password"
            duplicate_login_data['firstName'] = "Different Name"

            response2 = CourierMethods.create_courier(duplicate_login_data)

        assert response2.status_code == 409
        assert response2.json()["message"] == ERROR_MESSAGES["login_already_used"]

