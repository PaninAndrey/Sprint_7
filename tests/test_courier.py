import allure

from courier_methods import CourierMethods


class TestCreateCourier:
    @allure.title('Successful courier creation')
    def test_successful_create_courier(self, generate_courier_data):
        with allure.step('Create new courier'):
            courier = CourierMethods.create_new_courier(generate_courier_data[0])
        assert courier.status_code == 201 and courier.json() == {'ok': True}

    @allure.title('Impossible to create identical couriers')
    def test_unsuccessful_create_identical_couriers(self, generate_courier_data):
        with allure.step('Create identical courier'):
            courier = CourierMethods.impossible_to_create_two_identical_couriers(generate_courier_data[0])
        assert courier.status_code == 409 and courier.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Impossible to create courier without login')
    def test_unsuccessful_create_courier_without_login(self):
        with allure.step('Create courier without login'):
            courier = CourierMethods.impossible_to_create_courier_without_login()
        assert courier.status_code == 400 and courier.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Impossible to create courier without password')
    def test_unsuccessful_create_courier_without_password(self):
        with allure.step('Create courier without password'):
            courier = CourierMethods.impossible_to_create_courier_without_password()
        assert courier.status_code == 400 and courier.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    

