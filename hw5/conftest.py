import pytest

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="URL для теста")
    parser.addoption("--status_code", action="store", default=200, type=int, help="Ожидаемый код состояния")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
