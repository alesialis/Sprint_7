import allure
import requests
import data
import random
import string
from random import randrange
from faker import Faker
from phone_gen import PhoneNumber
import datetime


# Отправление запросов
@allure.step('Генерация рандомной строки')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерация данных login, password, firstName для создания курьера')
def generate_new_courier_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return login, password, first_name


@allure.step('Запрос на создание курьера')
def post_create_courier(payload):
    request = requests.post(f'{data.URL + data.CREATE_COURIER_URL}', json=payload)
    return request


@allure.step('Запрос на логин курьера')
def post_login_courier(payload):
    request = requests.post(f'{data.URL + data.LOGIN_COURIER_URL}', json=payload)
    return request


@allure.step('Запрос на удаление курьера')
def delete_courier(user_id):
    payload = {
        "id": user_id
    }
    request = requests.delete(f'{data.URL + data.DELETE_COURIER_URL}/{user_id}', json=payload)
    return request


@allure.step('Запрос на создание заказа')
def post_create_order(order_params):
    request = requests.post(f'{data.URL + data.CREATE_ORDER_URL}', json=order_params)
    return request


@allure.step('Запрос на получение списка заказов')
def get_list_orders():
    request = requests.get(f'{data.URL + data.GET_ORDERS_URL}')
    return request


# Генерация данных
class Data:
    faker = Faker('ru_RU')
    first_name = faker.first_name()
    last_name = faker.last_name()
    address = faker.street_name()
    metro = randrange(1, 10)
    phone = PhoneNumber('RU')
    phone_number = phone.get_number()
    rent_time = randrange(1, 6)
    delivery_date = datetime.date.today().day
    comment = 'Тестовый комментарий'

