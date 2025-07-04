import allure
import pytest
from schemas import todos_schema
import requests
import config



@pytest.mark.smoke
@pytest.mark.regression
@allure.tag('smoke', 'regression')
@allure.severity(allure.severity_level.NORMAL)
@allure.sub_suite('Todos')
@allure.suite('Todos')
@pytest.mark.parametrize('path, status', [
    ('todos', 200),
    ('/todo', 404)
], ids=['Положительная провека', 'Негативная проверка'])
def test_get_all_todos(app, path, status):
    """
    Получение всех задач
    """
    allure.dynamic.title(f"Получение задач: путь='{path}', ожидаемый статус={status}")
    
    with allure.step('Отправка запроса'):
        app.todos_api.get_todos(path)

    with allure.step('Проверка статус кода'):
        app.todos_api.check_status_code(status)

    if status == 200:
        with allure.step('Проверка тела ответа'):
            app.todos_api.validate_response_body()



