import random
import string

import pytest

from pages.openbrewerydb import Breweries


class Test:
    data_city = ['Abington', 'Anoka', 'South Bend', 'Boise', 'Castle Rock', 'Denver', 'Gilbert', 'Houston',
                 'John Day', 'Killeshin', 'Knoxville', 'Costa Mesa', 'Petaluma', 'Portland', 'Quilcene', 'El Reno',
                 'San Diego', 'Williamsville']

    data_search = ['micro', 'Dodge', 'Barrel', 'Brew']

    def test_all_breweries(self):
        response = Breweries().get_all_breweries()

        assert response.json() \
               and response.status_code == 200 \
               and response.reason == 'OK'

    @pytest.mark.parametrize("city", data_city)
    def test_find_breweries_by_city_positive(self, city):
        response = Breweries().get_all_breweries(param=f'by_city={city}').json()

        for brewery in response:
            assert brewery.get('city') == city

    @pytest.mark.parametrize("city", [''.join(random.choices(string.ascii_letters, k=10))])
    def test_find_breweries_by_city_negative(self, city):
        response = Breweries().get_all_breweries(param=f'by_city={city}')

        assert not response.json() and \
               response.status_code == 200 \
               and response.reason == 'OK'

    @pytest.mark.parametrize("per_page", [random.randint(1, 50)])
    def test_breweries_per_page(self, per_page):
        response = Breweries().get_all_breweries(param=f'per_page={per_page}').json()

        assert len(response) == per_page

    @pytest.mark.parametrize("search", data_search)
    def test_search_breweries_positive(self, search):
        response = Breweries().search_breweries(search)

        assert response.json() \
               and response.status_code == 200 \
               and response.reason == 'OK'

    @pytest.mark.parametrize("search", [''.join(random.choices(string.ascii_letters, k=10))])
    def test_search_breweries_negative(self, search):
        response = Breweries().search_breweries(search)

        assert not response.json() and \
               response.status_code == 200 \
               and response.reason == 'OK'

    def test_get_brewery(self, random_brewery):
        brewery_id = random_brewery.get('id')

        response = Breweries().get_brewery(brewery_id)

        assert response.status_code == 200 and response.reason == 'OK'
        assert random_brewery == response.json()
