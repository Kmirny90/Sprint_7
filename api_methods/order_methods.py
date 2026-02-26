import requests
import allure

from url import URL

class OrderMethods:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(order_data: dict):

        return requests.post(URL.ORDERS_CREATE, json=order_data)

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders(params=None):

        return requests.get(URL.ORDERS_GET, params=params)

    @staticmethod
    @allure.step("Отмена заказа")
    def cancel_order(track):

        payload = {"track": track}
        return requests.put(URL.ORDERS_CANCEL, json=payload)

    @staticmethod
    @allure.step("Получение заказа по номеру")
    def get_order_by_track(track):

        params = {"t": track}
        return requests.get(URL.ORDERS_TRACK, params=params)