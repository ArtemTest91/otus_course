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
    assert "bulldog", "bullterrier" in response.json()["message"]


@pytest.mark.parametrize("breed", ["chihuahua", "akita"])
def test_specific_breed_images(breed):
    response = requests.get(f"{BASE_URL_DOG}/breed/{breed}/images/random")
    assert response.status_code == 200
    assert response.json()['status'] == 'success'
    assert "message" in response.json()
    assert isinstance(response.json()["message"], str)


@pytest.mark.parametrize("sub_breed", ["afghan", "blood"])
def test_sub_breed_list(sub_breed):
    response = requests.get(f"{BASE_URL_DOG}/breed/hound/list")
    assert response.status_code == 200
    assert response.json()['status'] == 'success'
    assert "message" in response.json()
    assert isinstance(response.json()["message"], list)


breeds_to_test = ["chihuahua", "poodle", "beagle", "husky", "maltese"]


@pytest.mark.parametrize("breed", breeds_to_test)
def test_random_image_for_breed(breed):
    response = requests.get(f"{BASE_URL_DOG}/breed/{breed}/images/random")
    assert response.status_code == 200
    assert response.json()['status'] == 'success'
    assert "message" in response.json()
    assert isinstance(response.json()["message"], str)
    assert response.json()["message"].endswith(".jpg")
