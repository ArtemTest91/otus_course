import requests
import pytest

BASE_URL_DOG = 'https://dog.ceo/api'


def test_random_dog():
    response = requests.get(f"{BASE_URL_DOG}/breeds/image/random")
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["status"] == "success"


def test_list_all_breeds():
    response = requests.get(f"{BASE_URL_DOG}/breeds/list/all")
    assert response.status_code == 200
    assert "message" in response.json()
    assert isinstance(response.json()["message"], dict)
    assert "bulldog" in response.json()["message"]


@pytest.mark.parametrize("breed", ["english bulldog", "akita"])
def test_specific_breed_images(breed):
    response = requests.get(f"{BASE_URL_DOG}/breed/{breed}/images/random")
    assert response.status_code == 200
    assert "message" in response.json()
    assert isinstance(response.json()["message"], list)


@pytest.mark.parametrize("sub_breed", ["french Bulldog", "beagle"])
def test_sub_breed_images(sub_breed):
    response = requests.get(f"{BASE_URL_DOG}/breed/hound/{sub_breed}/images")
    assert response.status_code == 200
    assert "message" in response.json()
    assert isinstance(response.json()["message"], list)


@pytest.mark.parametrize("count", [1, 5])
def test_random_dogs(count):
    response = requests.get(f"{BASE_URL_DOG}/breed/images/random/{count}")
    assert response.status_code == 200
    assert "message" in response.json()
    assert isinstance(response.json()["message"], list)
    assert len(response.json()["message"]) == count
