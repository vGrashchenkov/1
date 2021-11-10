import pytest
import random

from pages.openbrewerydb.openbrewerydb import Breweries


@pytest.fixture()
def random_brewery():
    """Получение случайной пивоварни из списка всех пивоварен"""

    all_breweries = Breweries().get_all_breweries().json()

    return random.choice(all_breweries)
