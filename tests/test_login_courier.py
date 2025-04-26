import random
import allure

from generators import generate_courier_body
from methods.courier_methods import CourierMethods


class TestCourierAuthorization:

    @allure.title('Тест на успешную авторизацию курьера с корректными данными')
    @allure.description('Создаем курьера и проверяем, что с правильным логином и паролем курьер может авторизоваться, ожидаем код 200 и наличие id в ответе.')
    def test_successful_courier_login(self, generate_courier_data):
        CourierMethods.create_courier(generate_courier_data[0])
        login_response = CourierMethods.login_courier(generate_courier_data[1], generate_courier_data[2])

        assert login_response.status_code == 200 and "id" in login_response.json()

    @allure.title('Тест на неудачу авторизации с неполными данными')
    @allure.description('Проверяем авторизацию с отсутствующим логином и ожидаем ошибку 400 с сообщением "Недостаточно данных для входа".')
    def test_auth_without_login(self):
        courier_body = generate_courier_body()
        password = courier_body['password']
        login_response = CourierMethods.login_courier(None, password)

        assert (login_response.status_code == 400
                and login_response.json().get("message") == "Недостаточно данных для входа")

    @allure.title('Тест на неуспешную авторизацию курьера с некорректным логином')
    @allure.description('Создаем курьера и пробуем авторизоваться с неправильным логином и получаем код 404 с сообщением "Учетная запись не найдена".')
    def test_auth_with_invalid_login(self):
        courier_body = generate_courier_body()
        invalid_login = "invalid_login"
        courier_login = CourierMethods.login_courier(invalid_login, courier_body['password'])

        assert (courier_login.status_code == 404
                and courier_login.json().get("message") == "Учетная запись не найдена")

    @allure.title('Тест на попытку авторизации с пустым паролем')
    @allure.description('Делаем попытку авторизации с корректным логином, но без пароля. Ожидаем код 400 и сообщение "Недостаточно данных для входа".')
    def test_auth_without_password(self, generate_courier_data):
        CourierMethods.create_courier(generate_courier_data[0])
        login_response = CourierMethods.login_courier(generate_courier_data[1], None)

        assert (login_response.status_code == 400
                and login_response.json().get("message") == "Недостаточно данных для входа")

    @allure.title('Тест на неудачную авторизацию с неправильным паролем')
    @allure.description('Создаем курьера и используем неправильный пароль, ожидая получить код 404 и сообщение "Учетная запись не найдена".')
    def test_auth_with_wrong_password(self, generate_courier_data):
        CourierMethods.create_courier(generate_courier_data[0])
        wrong_password = random.randint(1000, 9999)
        login_response = CourierMethods.login_courier(generate_courier_data[1], wrong_password)

        assert (login_response.status_code == 404
                and login_response.json().get("message") == "Учетная запись не найдена")