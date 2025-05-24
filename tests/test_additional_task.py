import allure

from additional_task_methods import DeleteCourier, Orders
from courier_methods import CourierMethods
from login_methods import LoginMethods


class TestsAdditionalTask:
    @allure.title('Deleting an existant courier')
    def test_delete_existant_courier(self, generate_courier_for_deleting):
        with allure.step('Create new courier'):
            CourierMethods.create_new_courier(generate_courier_for_deleting[0])
            login = generate_courier_for_deleting[1]
            password = generate_courier_for_deleting[2]
        with allure.step('Get courier id'):
            courier_id = LoginMethods.get_courier_id(login, password)
        with allure.step('Delete courier'):
            delete_courier = CourierMethods.delete_courier(courier_id)
        assert delete_courier.status_code == 200 and delete_courier.json() == {"ok": True}

    @allure.title('Unsuccessful delete courier with no id')
    def test_unsuccessful_delete_courier_without_id(self):
        response = DeleteCourier.unsuccessful_delete_courier_with_no_id()
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Not Found.'}

    @allure.title('Unsuccessful delete courier with invalid id')
    def test_unsuccessful_delete_courier_with_invalid_id(self):
        response = DeleteCourier.unsuccessful_delete_courier_with_invalid_id()
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}

    @allure.title('Accept an order')
    def test_successful_accept_order(self, generate_courier_data):
        with allure.step('Create new courier'):
            CourierMethods.create_new_courier(generate_courier_data[0])
            login = generate_courier_data[1]
            password = generate_courier_data[2]
        with allure.step('Get courier id'):
            courier_id = LoginMethods.get_courier_id(login, password)
        with allure.step('Get track number'):
            track_number = Orders.create_new_order_and_get_track_number()
        with allure.step('Get order id'):
            order_id = Orders.get_order_id_number(track_number)
        with allure.step('Order accepton'):
            response = Orders.take_order_acception(order_id, courier_id )
        assert response.status_code == 200 and response.json() == {'ok': True}

    @allure.title('Rejection an order without courier id')
    def test_rejection_order_without_courier_id(self):
        with allure.step('Get track number'):
            track_number = Orders.create_new_order_and_get_track_number()
        with allure.step('Get order id'):
            order_id = Orders.get_order_id_number(track_number)
        with allure.step('Order rejection'):
            response = Orders.reject_order_without_courier_id(order_id)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure.title('Rejection an order with invalid courier id')
    def test_rejection_order_with_invalid_courier_id(self):
        with allure.step('Get track number'):
            track_number = Orders.create_new_order_and_get_track_number()
        with allure.step('Get order id'):
            order_id = Orders.get_order_id_number(track_number)
        with allure.step('Order rejection'):
            response = Orders.reject_order_with_invalid_courier_id(order_id)
        assert response.status_code == 404 and response.json() == {'code': 404, "message": "Курьера с таким id не существует"}

    @allure.title('Rejection an order without order id')
    def test_rejection_order_without_order_id(self, generate_courier_data):
        with allure.step('Create new courier'):
            CourierMethods.create_new_courier(generate_courier_data[0])
            login = generate_courier_data[1]
            password = generate_courier_data[2]
        with allure.step('Get courier id'):
            courier_id = LoginMethods.get_courier_id(login, password)
        with allure.step('Order rejection'):
            response = Orders.reject_order_without_order_id(courier_id)
        assert response.status_code == 404 and response.json() == {'code': 404, "message": "Not Found."}

    @allure.title('Rejection an order with invalid order id')
    def test_rejection_order_with_invalid_order_id(self, generate_courier_data):
        with allure.step('Create new courier'):
            CourierMethods.create_new_courier(generate_courier_data[0])
            login = generate_courier_data[1]
            password = generate_courier_data[2]
        with allure.step('Get courier id'):
            courier_id = LoginMethods.get_courier_id(login, password)
        with allure.step('Order rejection'):
            response = Orders.reject_order_with_invalid_order_id(courier_id)
        assert response.status_code == 404 and response.json() == {'code': 404, "message": "Заказа с таким id не существует"}

    @allure.title('Get order by track number')
    def test_get_order_by_track_number(self):
        with allure.step('Get track number'):
            track_number = Orders.create_new_order_and_get_track_number()
        with allure.step('Get order data'):
            response = Orders.get_order_by_track_number(track_number)
        assert response.status_code == 200 and response.json()['order']['track'] == track_number

    @allure.title('Impossible to get order without track number')
    def test_no_order_without_track_number(self):
        with allure.step('Impossible to get order'):
            response = Orders.reject_order_without_track_number()
        assert response.status_code == 400 and response.json() == {'code': 400, "message": "Недостаточно данных для поиска"}

    @allure.title('Impossible to get order with invalid track number')
    def test_no_order_with_invalid_track_number(self):
        with allure.step('Impossible to get order'):
            response = Orders.reject_order_with_invalid_track_number()
        assert response.status_code == 404 and response.json() == {'code': 404, "message": "Заказ не найден"}