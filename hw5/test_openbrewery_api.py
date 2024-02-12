import pytest
import requests

BASE_URL_BREW = "https://api.openbrewerydb.org/v1"


def test_get_breweries():
    response = requests.get(f"{BASE_URL_BREW}/breweries")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    assert "id" in response.json()[0]


def test_search_breweries_by_name():
    response = requests.get(f"{BASE_URL_BREW}/breweries?by_name=dog")
    assert response.status_code == 200
    assert "dog" in response.text.lower()
    assert len(response.json()) > 0
    assert "name" in response.json()[0]


@pytest.mark.parametrize("state", ["California", "New York"])
def test_breweries_in_state(state):
    response = requests.get(f"{BASE_URL_BREW}/breweries?by_state={state}")
    assert response.status_code == 200
    assert "state" in response.json()[0]
    assert all(brewery["state"] == state for brewery in response.json())


@pytest.mark.parametrize("brewery_type", ["micro", "bar"])
def test_breweries_by_type(brewery_type):
    response = requests.get(f"{BASE_URL_BREW}/breweries?by_type={brewery_type}")
    assert response.status_code == 200
    assert "brewery_type" in response.json()[0]
    assert all(brewery["brewery_type"] == brewery_type for brewery in response.json())


@pytest.mark.parametrize("city", ["san_diego", "new_york"])
def test_breweries_in_city(city):
    response = requests.get(f"{BASE_URL_BREW}/breweries?by_city={city}")
    assert response.status_code == 200
    assert "city" in response.json()[0]
    assert all(brewery["city"] == city for brewery in response.json())
