# Sprint_7

## Финальный проект 7 спринта
<hr>

## Студент: Андрей Панин

## <h>Когорта: #21</h>
<hr>

## <h>Project: Тестирование API Яндекс.Самокат</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results


<hr>

<h3 align="left" style="color:yellow">Project files and description:</h3>

| Название файла             | Содержание файла                            |
|----------------------------|---------------------------------------------|
| allure-results.dir         | Папка с отчетами Allure                     |                                                               |
| tests                      | Директория с тестами                        |
| conftest.py                | Фикстуры                                    |
| test_additional_task.py    | Тесты к дополнительному заданию             |
| test_courier.py            | Тесты на создание курьера                   |
| test_login.py              | Тесты на логин курьера                      |
| test_orders.py             | Тесты на создание заказа и список заказов   |
| additional_task_methods.py | Методы для тестов к дополнительному заданию |
| courier_methods.py         | Методы для тестов на сооздание курьера      |
| data.py                    | Файл с url-ами                              |
| generators.py              | Файл для генерации тестовых данных          
| login_methods.py           | Файл с методами для тестов при авторизации  |
| order_methods.py           | Файл с методами для тестов заказов          |
| README.md                  | README-файл                                 |
| requirements.txt           | Файл с зависимостями                        |
