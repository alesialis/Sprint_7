import pytest
from helpers import *


@allure.step('Генерация данных для курьера, логин, удаление курьера')
@pytest.fixture
def generate_courier_then_delete():
    # Данные для создания курьера
    new_courier_data = generate_new_courier_data()
    login_pass = [new_courier_data[0], new_courier_data[1], new_courier_data[2]]

    yield login_pass

    # Логин курьера
    payload = {
        'login': new_courier_data[0],
        'password': new_courier_data[1]
    }
    login_response = post_login_courier(payload)
    # Удалить курьера
    user_id = login_response.json()['id']
    delete_courier(user_id)


@allure.step('Генерация данных для курьера, регистрация, удаление курьера')
@pytest.fixture
def generate_courier_register_then_delete():
    new_courier_data = generate_new_courier_data()
    payload = {
        "login": new_courier_data[0],
        "password": new_courier_data[1],
        "firstName": new_courier_data[2]
    }
    registration_response = post_create_courier(payload)
    login_pass = []
    if registration_response.status_code == 201:
        login_pass.append(new_courier_data[0])
        login_pass.append(new_courier_data[1])
        login_pass.append(new_courier_data[2])

    yield login_pass

    payload = {
        'login': new_courier_data[0],
        'password': new_courier_data[1]
    }
    login_response = post_login_courier(payload)
    user_id = login_response.json()['id']
    delete_courier(user_id)
