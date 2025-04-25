import allure
import pytest

from data import color_scooter
from generators import generate_order_body
from methods.order_methods import OrdersMethods


class TestCreateOrder:

    @allure.title('Тест на успешное создание заказа')
    @allure.description('Создаем заказ с рандомными параметрами и перебираем варинты цвета самоката, код 201 и в теле ответа присутсвует "track"')
    @pytest.mark.parametrize("color", color_scooter)
    def test_create_order(self,color):
        order = OrdersMethods.create_order(generate_order_body(color))

        assert order.status_code == 201 and "track" in order.json()

