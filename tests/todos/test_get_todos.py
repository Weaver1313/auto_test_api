import allure
import pytest


@pytest.mark.smoke
@pytest.mark.regression
@allure.tag('smoke', 'regression')
@allure.severity(allure.severity_level.NORMAL)
@allure.sub_suite('Todos')
@allure.suite('Todos')
@allure.title('Получение всех задач')
def test_get_all_todos(app):
    """
    Получение всех задач
    """
    with allure.step('Отправка запроса'):
        app.todos_api.get_todos()

    with allure.step('Проверка статус кода'):
        app.todos_api.check_status_code_ok()

    with allure.step('Проверка тела ответа'):
        app.todos_api.validate_response_body()