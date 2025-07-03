from api.app_api import App
import pytest
import requests
import config


@pytest.fixture()
def app(challenger):
    app = App(challenger)
    return app


@pytest.fixture(scope='session')
def challenger():
    response = requests.post(f'{config.URL}/challenger')
    x_challenger = response.headers['X-Challenger']
    return x_challenger