import requests
import allure
import pytest
from data.URLs import url
from data.courier_data import generation_new_data_courier
from data.courier_data import register_new_courier_and_return_login_password
import conftest


class TestCreateCourier:

    @allure.title("Создание курьера")
    @allure.step('Проверка создания курьера (код - 201 и тест - "ok": True)')
    def test_create_courier(self):
        data = generation_new_data_courier()

        payload = data
        response = requests.post(f"{url}/api/v1/courier", json=payload)  # Исправлено data на json

        assert response.status_code == 201
        assert response.json() == {"ok": True}, "Неверное содержимое ответа."

    @allure.title("Создание курьера с дублирующимся логином")
    @allure.description('Проверка создания курьера (код - 409 и текст - "message": "Этот логин уже используется"')
    def test_create_courier_duplicate_login(self):
        login_pass = register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
            "firstName": "test_firstName"  # Добавлено недостающее поле firstName
        }
        response = requests.post(f"{url}/api/v1/courier", json=payload)  # Исправлено data на json

        assert response.status_code == 409
        # Исправлено "massage" на "message" в соответствии с реальным API
        assert response.json() == {"code": 409, "message": "Этот логин уже используется"}, "Неверное содержимое ответа."

    @allure.title("Создание курьера с дублирующимся логином")
    @allure.description('Проверка создания курьера (код - 409 и текст - "message": "Этот логин уже используется"')
    def test_create_courier_duplicate_login(self):
        login_pass = register_new_courier_and_return_login_password()
        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
            "firstName": "test_firstName"
        }
        response = requests.post(f"{url}/api/v1/courier", json=payload)

        assert response.status_code == 409
        response_data = response.json()

        # Вариант 1: Точное совпадение
        assert response_data == {
            "code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."
        }, "Неверное содержимое ответа."

        # ИЛИ Вариант 2: Проверка части сообщения
        assert response_data["code"] == 409
        assert "Этот логин уже используется" in response_data["message"]