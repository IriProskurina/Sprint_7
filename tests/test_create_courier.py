import allure

from generators import generate_courier_body
from methods.courier_methods import CourierMethods



class TestCreateCourier:
    @allure.title('Проверка успешной регистрации курьера')
    @allure.description('Регистрация нового курьера и проверка, что ответ сервера содержит код 201 и {"ok": True}.')
    def test_success_create_courier(self,generate_courier_data):
      courier_data =generate_courier_data[0]
      response = CourierMethods.create_courier(courier_data)

      assert response.status_code == 201
      assert response.json() == {"ok": True}

    @allure.title('Проверка обработки ошибки создания двух курьеров с одинаковыми данными')
    @allure.description('Пытаемся зарегистрировать двух курьеров с идентичными параметрами и ожидаем ошибку при создании второго.')
    def test_success_create_courier(self, generate_courier_data):
        first_courier = CourierMethods.create_courier(generate_courier_data[0])
        second_courier = CourierMethods.create_courier(generate_courier_data[0])
        assert first_courier.status_code == 201
        assert second_courier.status_code == 409

    @allure.title('Проверка получения ошибки при создании курьера с повторяющимся логином')
    @allure.description('Создаем двух курьеров, заменяя логин второго курьера аналогичным логином первого, и проверяем ошибку.')
    def test_success_create_courier(self, generate_courier_data):
        first_courier = CourierMethods.create_courier(generate_courier_data[0])
        second_courier_body= generate_courier_body()
        second_courier_body ["login"] = generate_courier_data [1]
        # Логин второго курьера совпадает с логином первого
        second_courier = CourierMethods.create_courier(second_courier_body)

        assert first_courier.status_code == 201
        assert second_courier.status_code == 409
        assert second_courier.json().get("message") == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Текст не создает курьера без указания логина')
    @allure.description('Пытаемся зарегистрировать курьера, не указав логин, и проверяем, что возвращается ошибка.')
    def test_success_create_courier(self):
        first_courier_body = generate_courier_body()
        first_courier_body.pop("login")
        first = CourierMethods.create_courier(first_courier_body)

        assert first.status_code == 400
        assert first.json().get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title('Тест на создание курьера без указания пароля')
    @allure.description('Пытаемся зарегистрировать курьера без пароля и проверяем валидность возвращаемого сообщения об ошибке.')
    def test_success_create_courier(self):
        first_courier_body = generate_courier_body()
        first_courier_body.pop("password")
        first = CourierMethods.create_courier(first_courier_body)

        assert first.status_code == 400
        assert first.json().get("message") == "Недостаточно данных для создания учетной записи"
