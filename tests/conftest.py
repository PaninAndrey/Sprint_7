import pytest

from generators import CourierData
from login_methods import LoginMethods
from courier_methods import CourierMethods


@pytest.fixture()
def generate_courier_data():
    courier_data = CourierData.new_courier_data()
    login = courier_data['login']
    password = courier_data['password']
    yield [courier_data, login, password]
    courier_id = LoginMethods.get_courier_id(login, password)
    CourierMethods.delete_courier(courier_id)

@pytest.fixture()
def generate_courier_for_deleting():
    courier_data = CourierData.new_courier_data()
    login = courier_data['login']
    password = courier_data['password']
    yield [courier_data, login, password]


