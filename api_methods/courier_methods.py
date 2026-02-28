import requests
import allure
from url import  URL

class CourierMethods:

    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(courier_body: dict):
        return requests.post(URL.COURIER_CREATE, json=courier_body)

    @staticmethod
    @allure.step("Логин курьера")
    def login_courier(login, password):
        payload = {"login": login, "password": password}
        return requests.post(URL.COURIER_LOGIN, json=payload)

    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):

        return requests.delete(f"{URL.COURIER_DELETE}{courier_id}")