import allure
import pytest


@pytest.mark.smoke
@pytest.mark.regression
@allure.tag('smoke', 'regression')
@allure.severity(allure.severity_level.NORMAL)
@allure.sub_suite('Todos')
@allure.suite('Todos')
@allure.title('Получение всех задач')
def test_create_todos(app):
    with allure.step('Отправка запроса'):
        app.todos_api.create_todos('/todos')

    with allure.step('Проверка статуса кода'):
        app.todos_api.check_status_code(201)
    
    with allure.step('Проверка тела ответа'):
        app.todos_api.validate_res_body_create()