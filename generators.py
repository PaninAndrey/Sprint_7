import random
import string
from faker import Faker


class CourierData:

# метод генерации данных для создания нового курьера
    @staticmethod
    def new_courier_data():
        # метод генерирует строку, состоящую только из букв нижнего регистра,
        # в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
        "login": login,
        "password": password,
        "firstName": first_name
        }
        # Возвращаем словарь с логином, паролем и именем курьера
        return payload

class OrderData:

        fake = Faker()
        firstName = fake.first_name()
        lastName = fake.last_name()
        address = fake.address()
        metroStation = random.randint(1, 10)
        phone = fake.phone_number()
        rentTime = random.randint(1, 10)
        deliveryDate = fake.date_between(start_date='today', end_date='+3d').isoformat()
        comment = fake.text(30)

