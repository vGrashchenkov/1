import random

import pytest

from pages.openbrewerydb import Breweries


@pytest.fixture()
def random_brewery():
    """Получение случайной пивоварни из списка всех пивоварен"""
    return random.choice(Breweries().get_all_breweries().json())


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="URL for test_status_code")
    parser.addoption("--status_code", action="store", default=200, help="expected status code")


@pytest.fixture
def param(request):
    return {"url": request.config.getoption("--url"),
            "status_code": int(request.config.getoption("--status_code"))}
