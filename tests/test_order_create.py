import pytest
from helpers import *
from helpers import Data


class TestCreateOrder:
    @allure.title('Корректное создание заказа')
    @allure.description('Поле color необязательное, может принимать одно или два значения - ответ 201')
    @pytest.mark.parametrize('payload', [
        ({
            'firstName': Data.first_name,
            'lastName': Data.last_name,
            'address': Data.address,
            'metroStation': Data.metro,
            'phone': Data.phone_number,
            'rentTime': Data.rent_time,
            'deliveryDate': Data.delivery_date,
            'comment': Data.comment,
            'color': ["BLACK", "GREY"]}),
        ({
            'firstName': Data.first_name,
            'lastName': Data.last_name,
            'address': Data.address,
            'metroStation': Data.metro,
            'phone': Data.phone_number,
            'rentTime': Data.rent_time,
            'deliveryDate': Data.delivery_date,
            'comment': Data.comment,
            'color': ["BLACK"]}),
        ({
            'firstName': Data.first_name,
            'lastName': Data.last_name,
            'address': Data.address,
            'metroStation': Data.metro,
            'phone': Data.phone_number,
            'rentTime': Data.rent_time,
            'deliveryDate': Data.delivery_date,
            'comment': Data.comment,
            'color': ["GREY"]}),
        ({
            'firstName': Data.first_name,
            'lastName': Data.last_name,
            'address': Data.address,
            'metroStation': Data.metro,
            'phone': Data.phone_number,
            'rentTime': Data.rent_time,
            'deliveryDate': Data.delivery_date,
            'comment': Data.comment})
    ])
    def test_create_valid_order(self, payload):
        response = post_create_order(payload)
        assert response.status_code == 201 and 'track' in response.text
