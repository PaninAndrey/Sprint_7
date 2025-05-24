import requests

from data import Url


class LoginMethods:
    @staticmethod
    def login(login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}', data=payload)


    @staticmethod
    def get_courier_id(login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}', data=payload)
        return response.json()['id']
