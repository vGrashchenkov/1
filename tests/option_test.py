import requests


def test_status_code(param):
    response = requests.request("GET", param.get('url'))

    assert response.status_code == param.get('status_code'), \
        f"url = {param.get('url')}, получили status_code {response.status_code}"



