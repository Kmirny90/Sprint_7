import pytest
import allure
from api_methods.order_methods import OrderMethods
from data.order_data import *


class TestCreateOrder:
    @pytest.mark.parametrize("color_data", [
        [],
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"]
    ])
    @allure.title("Создание заказа с цветом {color}")
    def test_create_order_with_different_colors(self, color_data, created_order):
        with allure.step("Подготовка данных заказа"):
            order_data = ORDER_BODY.copy()
            order_data["color"] = color_data

        with allure.step("Отправка запроса на создание заказа"):
            response = OrderMethods.create_order(order_data)

        with allure.step("Проверка ответа"):
            assert response.status_code == 201
            assert "track" in response.json()

        created_order.append(response.json()["track"])


