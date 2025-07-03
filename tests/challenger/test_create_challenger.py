import allure
import pytest

@pytest.mark.smoke
@pytest.mark.regression
@allure.tag('smoke', 'regression')
@allure.severity(allure.severity_level.NORMAL)
@allure.parent_suite("Challenger")
@allure.suite("Challenger")
@allure.title('Проверка создания нового токена x-challenger')
def test_create_challenger(app):
    """
    Проверка создания нового токена x-challenger 
    """
    with allure.step('Создание'):
        app.challenger_api.create_x_challenger()

    with allure.step('Проверка статус кода'):
        app.challenger_api.check_status_code_ok()

    with allure.step('Проверка есть ли в заголовках x-challenger'):
        app.challenger_api.check_x_challenger()