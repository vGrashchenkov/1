import requests


class Breweries:

    def __init__(self):
        self.URL = 'https://api.openbrewerydb.org'

    def get_all_breweries(self, param=None):
        path = '/breweries'

        if param:
            path = f'{path}?{param}'

        return requests.request("GET", self.URL + path)

    def get_brewery(self, brewery_id):
        path = f'/breweries/{brewery_id}'

        return requests.request("GET", self.URL + path)

    def search_breweries(self, query):
        path = f'/breweries/search?query={query}'

        return requests.request("GET", self.URL + path)
