import allure
from data.courier_data import ERROR_MESSAGES
from api_methods.courier_methods import CourierMethods


class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    @allure.description("Проверка, что курьер может авторизоваться с валидными данными")
    def test_login_courier_success(self, created_courier):
        with allure.step(f"Авторизуемся под логином {created_courier['login']}"):
            response = CourierMethods.login_courier(
                created_courier["login"],
                created_courier["password"]
            )

        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Логин без логина")
    @allure.description("Проверка, что без логина запрос возвращает ошибку")
    def test_login_missing_login_fails(self, created_courier):
        with allure.step("Отправляем запрос только с паролем"):
            response = CourierMethods.login_courier("", created_courier["password"])

        assert response.status_code == 400
        assert response.json()["message"] == ERROR_MESSAGES["auth_missing_data"]

    @allure.title("Логин без пароля")
    @allure.description("Проверка, что без пароля запрос возвращает ошибку")
    def test_login_missing_password_fails(self, created_courier):
        with allure.step("Отправляем запрос только с логином"):
            response = CourierMethods.login_courier(created_courier["login"], "")

        assert response.status_code == 400
        assert response.json()["message"] == ERROR_MESSAGES["auth_missing_data"]

    @allure.title("Логин с неправильным логином")
    @allure.description("Проверка, что с неверным логином запрос возвращает ошибку")
    def test_login_wrong_login_fails(self, created_courier):
        with allure.step("Авторизуемся с неправильным логином"):
            response = CourierMethods.login_courier(
                "wrong_login_12345",
                created_courier["password"]
            )

        assert response.status_code == 404
        assert response.json()["message"] == ERROR_MESSAGES["auth_not_found"]

    @allure.title("Логин с неправильным паролем")
    @allure.description("Проверка, что с неверным паролем запрос возвращает ошибку")
    def test_login_wrong_password_fails(self, created_courier):
        with allure.step("Авторизуемся с неправильным паролем"):
            response = CourierMethods.login_courier(
                created_courier["login"],
                "wrong_password_12345"
            )

        assert response.status_code == 404
        assert response.json()["message"] == ERROR_MESSAGES["auth_not_found"]

    @allure.title("Логин несуществующего курьера")
    @allure.description("Проверка, что авторизация под несуществующим пользователем возвращает ошибку")
    def test_login_nonexistent_courier_fails(self, random_courier_data):
        with allure.step("Пытаемся авторизоваться под несуществующим курьером"):
            response = CourierMethods.login_courier(
                random_courier_data["login"],
                random_courier_data["password"]
            )

        assert response.status_code == 404
        assert response.json()["message"] == ERROR_MESSAGES["auth_not_found"]