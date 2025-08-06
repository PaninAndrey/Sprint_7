import requests

from data import Url
from generators import OrderData


class DeleteCourier:
    @staticmethod
    def unsuccessful_delete_courier_with_no_id():
        response = requests.delete(f'{Url.BASE_URL}{Url.COURIER_URL}/')
        return response

    @staticmethod
    def unsuccessful_delete_courier_with_invalid_id():
        courier_id = '9830983'
        response = requests.delete(f'{Url.BASE_URL}{Url.COURIER_URL}/{courier_id}')
        return response


class Orders:
    @staticmethod
    def create_new_order_and_get_track_number():
        payload = {
            "firstName": OrderData.firstName,
            "lastName": OrderData.lastName,
            "address": OrderData.address,
            "metroStation": OrderData.metroStation,
            "phone": OrderData.phone,
            "rentTime": OrderData.rentTime,
            "deliveryDate": OrderData.deliveryDate,
            "comment": OrderData.comment,
            "color": []
        }
        response = requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', params=payload)
        return response.json()['track']

    @staticmethod
    def get_order_id_number(track_number):
        order_response = requests.get(f'{Url.BASE_URL}{Url.TRACK_NUMBER_URL}{track_number}')
        order_id = order_response.json()['order']['id']
        return order_id

    @staticmethod
    def take_order_acception(order_id, courier_id):
        response = requests.put(f'{Url.BASE_URL}{Url.ORDER_ACCEPT_URL}{order_id}{Url.COURIER_ID_PARAMS_URL}{courier_id}')
        return response

    @staticmethod
    def reject_order_without_courier_id(order_id):
        response = requests.put(f'{Url.BASE_URL}{Url.ORDER_ACCEPT_URL}{order_id}{Url.COURIER_ID_PARAMS_URL}')
        return response

    @staticmethod
    def reject_order_with_invalid_courier_id(order_id):
        courier_id = '673493985'
        response = requests.put(f'{Url.BASE_URL}{Url.ORDER_ACCEPT_URL}{order_id}{Url.COURIER_ID_PARAMS_URL}{courier_id}')
        return response

    @staticmethod
    def reject_order_without_order_id(courier_id):
        response = requests.put(f'{Url.BASE_URL}{Url.ORDER_ACCEPT_URL}{Url.COURIER_ID_PARAMS_URL}{courier_id}')
        return response

    @staticmethod
    def reject_order_with_invalid_order_id(courier_id):
        order_id = '8943249'
        response = requests.put(f'{Url.BASE_URL}{Url.ORDER_ACCEPT_URL}{order_id}{Url.COURIER_ID_PARAMS_URL}{courier_id}')
        return response

    @staticmethod
    def get_order_by_track_number(track_number):
        response = requests.get(f'{Url.BASE_URL}{Url.TRACK_NUMBER_URL}{track_number}')
        return response

    @staticmethod
    def reject_order_without_track_number():
        response = requests.get(f'{Url.BASE_URL}{Url.TRACK_NUMBER_URL}')
        return response

    @staticmethod
    def reject_order_with_invalid_track_number():
        track_number = '42424556'
        response = requests.get(f'{Url.BASE_URL}{Url.TRACK_NUMBER_URL}{track_number}')
        return response