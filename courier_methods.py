import requests

from data import Url
from generators import CourierData


class CourierMethods:

    @staticmethod
    def create_new_courier(body):
       return requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', data=body)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.COURIER_URL}/{courier_id}')

    @staticmethod
    def impossible_to_create_two_identical_couriers(body):
        requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', data=body)
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', data=body)

    @staticmethod
    def impossible_to_create_courier_without_login():
        courier_data = CourierData.new_courier_data()
        payload = {
            "login": '',
            "password": courier_data.get('password'),
            "firstName": courier_data.get('firstName')
        }
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', data=payload)

    @staticmethod
    def impossible_to_create_courier_without_password():
        courier_data = CourierData.new_courier_data()
        payload = {
            "login": courier_data.get('login'),
            "password": '',
            "firstName": courier_data.get('firstName')
        }
        return requests.post(f'{Url.BASE_URL}{Url.COURIER_URL}', data=payload)
