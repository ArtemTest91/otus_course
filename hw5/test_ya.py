import requests


def test_check_status_code(url, status_code):
    response = requests.get(url)
    if 400 <= response.status_code < 500:
        assert response.status_code == 404
    else:
        assert response.status_code == status_code
