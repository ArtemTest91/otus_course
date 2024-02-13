import pytest
import requests

BASE_URL_JSON = "https://jsonplaceholder.typicode.com"


def test_get_users():
    response = requests.get(f"{BASE_URL_JSON}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    assert "id" in response.json()[0]


def test_get_posts():
    response = requests.get(f"{BASE_URL_JSON}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    assert "title" in response.json()[0]


@pytest.mark.parametrize("user_id", [1, 2])
def test_user_posts(user_id):
    response = requests.get(f"{BASE_URL_JSON}/users/{user_id}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(post["userId"] == user_id for post in response.json())


@pytest.mark.parametrize("post_id", [1, 2])
def test_post_comments(post_id):
    response = requests.get(f"{BASE_URL_JSON}/posts/{post_id}/comments")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(comment["postId"] == post_id for comment in response.json())


@pytest.mark.parametrize("user_id", [1, 2])
def test_user_albums(user_id):
    response = requests.get(f"{BASE_URL_JSON}/users/{user_id}/albums")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert all(album["userId"] == user_id for album in response.json())
