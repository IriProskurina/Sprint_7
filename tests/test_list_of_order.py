import allure

from methods.order_methods import OrdersMethods


class TestOrdersRetrieval:

    @allure.title('Тест на успешное получение списка заказов')
    def test_successful_order_retrieval(self):
        response = OrdersMethods.git_list_order()  # Исправлено на правильное имя метода

        assert response.status_code == 200 and "orders" in response.json()