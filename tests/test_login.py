import allure

from courier_methods import CourierMethods
from generators import CourierData
from login_methods import LoginMethods


class TestLogins:
    @allure.title('Successful login')
    def test_success_login(self, generate_courier_data):
        with allure.step('Create courier'):
            CourierMethods.create_new_courier(generate_courier_data[0])
            login = generate_courier_data[1]
            password = generate_courier_data[2]
        with allure.step('Successful login'):
            login_response = LoginMethods.login(login, password)
        assert login_response.status_code == 200 and 'id' in login_response.json()

    @allure.title('Unsuccessful login with invalid login')
    def test_no_login_with_invalid_login(self, generate_courier_data):
        with allure.step('Create courier'):
            CourierMethods.create_new_courier(generate_courier_data[0])
            login = generate_courier_data[1] + 'qwerty'
            password = generate_courier_data[2]
        with allure.step('Unsuccessful login'):
            login_response = LoginMethods.login(login, password)
        assert login_response.status_code == 404 and login_response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Unsuccessful login with invalid password')
    def test_no_login_with_invalid_password(self, generate_courier_data):
        with allure.step('Create courier'):
            CourierMethods.create_new_courier(generate_courier_data[0])
            login = generate_courier_data[1]
            password = generate_courier_data[2] + 'qwerty'
        with allure.step('Unsuccessful login'):
            login_response = LoginMethods.login(login, password)
        assert login_response.status_code == 404 and login_response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Unsuccessful login without login')
    def test_no_login_without_login(self, generate_courier_data):
        with allure.step('Create courier'):
            CourierMethods.create_new_courier(generate_courier_data[0])
            login = ''
            password = generate_courier_data[2]
        with allure.step('Unsuccessful login'):
            login_response = LoginMethods.login(login, password)
        assert login_response.status_code == 400 and login_response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Unsuccessful login without password')
    def test_no_login_without_password(self, generate_courier_data):
        with allure.step('Create courier'):
            CourierMethods.create_new_courier(generate_courier_data[0])
            login = generate_courier_data[1]
            password = ''
        with allure.step('Unsuccessful login'):
            login_response = LoginMethods.login(login, password)
        assert login_response.status_code == 400 and login_response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Unsuccessful login with nonexistent login and password')
    def test_no_login_with_nonexistent_data(self):
        with allure.step('Create login and password without previous registration'):
            nonexistent_courier = CourierData.new_courier_data()
            login = nonexistent_courier['login']
            password = nonexistent_courier['password']
        with allure.step('Unsuccessful login'):
            login_response = LoginMethods.login(login, password)
        assert login_response.status_code == 404 and login_response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
