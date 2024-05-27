from helpers import *


class TestGetListOrders:
    @allure.title('Корректный список заказов')
    @allure.description('При валидном запросе - в ответе список заказов')
    def test_get_list_of_orders(self):
        response = get_list_orders()
        assert response.status_code == 200 and 'orders' in response.text
