import requests
import pytest
import allure

from generators import OrderData
from order_methods import OrderMethods
from data import Url


class TestOrders:

    @allure.title("Order tests with different scooters' colours")
    @pytest.mark.parametrize('color',
                         [[], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_order_with_different_scooter_color(self, color):
        payload = {
            "firstName": OrderData.firstName,
            "lastName": OrderData.lastName,
            "address": OrderData.address,
            "metroStation": OrderData.metroStation,
            "phone": OrderData.phone,
            "rentTime": OrderData.rentTime,
            "deliveryDate": OrderData.deliveryDate,
            "comment": OrderData.comment,
            "color": color
        }
        response = requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', params=payload)
        assert response.status_code == 201 and 'track' in response.json()

    @allure.title("Get orders list")
    def test_orders(self):
        response = OrderMethods.get_order_list()
        assert response.status_code == 200 and 'orders' in response.json()
