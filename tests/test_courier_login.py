import pytest
from helpers import *


class TestLoginCourier:
    @allure.title('Корректный логин курьера')
    @allure.description('При валидном запросе - ответ 200')
    def test_login_courier_return_id(self, generate_courier_register_then_delete):
        payload = {
            'login': generate_courier_register_then_delete[0],
            'password': generate_courier_register_then_delete[1]
        }
        response = post_login_courier(payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка обязательности полей')
    @allure.description('При запросе без обязательных полей - ответ 400')
    @pytest.mark.parametrize('payload', [({'login': '', 'password': generate_random_string(10)}),
                                         ({'login': generate_random_string(10), 'password': ''})])
    def test_not_enough_data_to_login(self, payload):
        response = post_login_courier(payload)
        assert response.status_code == 400 and response.json()['message'] == data.NOT_ENOUGH_DATA_LOGIN_COURIER

    @allure.title('Авторизация под несуществующим пользователем')
    @allure.description('При авторизации под несуществующим пользователем - ответ 404')
    def test_nonexistent_courier_error(self):
        payload = {
            'login': generate_random_string(10),
            'password': generate_random_string(10)
        }
        response = post_login_courier(payload)
        assert response.status_code == 404 and response.json()['message'] == data.NOT_FOUND_COURIER

    @allure.title('Авторизация при некорректном пароле')
    @allure.description('Если отправить некорректный пароль для существующего курьера - ответ 404')
    def test_incorrect_password_error(self, generate_courier_register_then_delete):
        payload = {
            'login': generate_courier_register_then_delete[0],
            'password': generate_random_string(10)
        }
        response = post_login_courier(payload)
        assert response.status_code == 404 and response.json()['message'] == data.NOT_FOUND_COURIER

    @allure.title('Авторизация при некорректном логине')
    @allure.description('Если отправить некорректный логин для существующего курьера - ответ 404')
    def test_incorrect_login_error(self, generate_courier_register_then_delete):
        payload = {
            'login': f'{generate_courier_register_then_delete[0]}{1}',
            'password': generate_courier_register_then_delete[1]
        }
        response = post_login_courier(payload)
        assert response.status_code == 404 and response.json()['message'] == data.NOT_FOUND_COURIER
