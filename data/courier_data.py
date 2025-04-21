import pytest
import requests
import random
import string
from data.URLs import url  # Предполагается, что URL хранится здесь


def generation_new_data_courier():
    letters = string.ascii_lowercase
    login_new = "".join(random.choice(letters) for i in range(10))
    password_new = "".join(random.choice(letters) for i in range(10))
    first_name_new = "".join(random.choice(letters) for i in range(10))

    return {
        "login": login_new,
        "password": password_new,
        "firstName": first_name_new
    }


def register_new_courier_and_return_login_password():
    login_pass = []

    # 1. Исправляем название функции и сохраняем результат
    data = generation_new_data_courier()

    # 2. Получаем данные из словаря
    login = data["login"]
    password = data["password"]
    first_name = data["firstName"]

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # 3. Добавляем обработку ошибок и используем json вместо data
    try:
        response = requests.post(f"{url}/api/v1/courier", json=payload)
        response.raise_for_status()  # Генерирует исключение для статусов 4xx/5xx

        if response.status_code == 201:
            login_pass.extend([login, password, first_name])

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при создании курьера: {e}")

    return login_pass