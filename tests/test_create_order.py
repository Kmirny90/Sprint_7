import pytest
import allure
from api_methods.order_methods import OrderMethods
from data.order_data import *


class TestCreateOrder:
    @pytest.mark.parametrize("color", COLOR_VARIANTS)
    @allure.title("Создание заказа с цветом {color}")
    def test_create_order_with_different_colors(self, color):
        order_data = ORDER_BODY.copy()
        if color:
            order_data["color"] = color

        response = OrderMethods.create_order(order_data)

        assert response.status_code == 201
        assert "track" in response.json()

        OrderMethods.cancel_order(response.json()["track"])