import allure
import pytest


@pytest.mark.smoke
@pytest.mark.regression
@allure.tag('smoke', 'regression')
@allure.severity(allure.severity_level.NORMAL)
@allure.parent_suite("Challenger")
@allure.suite('Challengers')
@allure.title('Получение всех challengers')
def test_get_challengers(app):
    """
    Проверка метода получения всех испытаний 
    """
    with allure.step('Отправка запроса'):
        app.challengers_api.get_challengers()

    with allure.step('Проверка на статус код'):
        app.challengers_api.check_status_code_ok()

    with allure.step('Проверка тело ответа'):
        app.challengers_api.validate_response_body()
