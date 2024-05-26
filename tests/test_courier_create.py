import pytest
from helpers import *


class TestCreateCourier:
    @allure.title('Корректная регистрация курьера')
    @allure.description('При запросе с валидными данными - создается курьер, ответ 201')
    def test_create_new_courier(self, generate_courier_then_delete):
        payload = {
            'login': generate_courier_then_delete[0],
            'password': generate_courier_then_delete[1],
            'firstName': generate_courier_then_delete[2]
        }
        response = post_create_courier(payload)
        assert response.status_code == 201 and response.json() == data.SUCCESSFUL_CREATE_COURIER

    @allure.title('Нельзя создать дублирующего курьера')
    @allure.description('При запросе на создание курьера с данными уже существующего курьера - ответ 409')
    def test_create_duplicate_courier(self, generate_courier_register_then_delete):
        payload = {
            'login': generate_courier_register_then_delete[0],
            'password': generate_courier_register_then_delete[1],
            'firstName': generate_courier_register_then_delete[2]
        }
        response = post_create_courier(payload)
        assert response.status_code == 409 and response.json()['message'] == data.DUPLICATE_COURIER

    @allure.title('Проверка обязательности полей')
    @allure.description('При запросе без обязательных полей - ответ 400')
    @pytest.mark.parametrize('payload', [({'password': generate_random_string(10), 'firstName': generate_random_string(10)}),
                                         ({'login': generate_random_string(10), 'firstName': generate_random_string(10)}),
                                         ({'firstName': generate_random_string(10)})])
    def test_not_enough_data_to_create(self, payload):
        response = post_create_courier(payload)
        assert response.status_code == 400 and response.json()['message'] == data.NOT_ENOUGH_DATA_CREATE_COURIER
