import pytest
import requests

@pytest.fixture
def response():
    url = "https://testapi.io/api/RMSTest/ibltest"
    return requests.get(url)