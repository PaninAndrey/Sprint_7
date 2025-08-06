import requests

from data import Url

class OrderMethods:
    @staticmethod
    def get_order_list():
        response = requests.get(f'{Url.BASE_URL}{Url.ORDER_URL}')
        return response


