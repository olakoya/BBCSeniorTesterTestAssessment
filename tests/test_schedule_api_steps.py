import requests
import os
from pytest_bdd import scenarios, given, then
from datetime import datetime

# Load the .feature file
scenarios(os.path.join(os.path.dirname(__file__), "../features/schedule_api_steps.feature"))

# Shared variable
response = None


@given('I make a GET request to "https://testapi.io/api/RMSTest/ibltest"')
def make_valid_request():
    global response
    response = requests.get("https://testapi.io/api/RMSTest/ibltest")


@given("I make a GET request to an invalid schedule date")
def make_invalid_request():
    global response
    response = requests.get("https://testapi.io/api/RMSTest/ibltest/invalid")


@then("the response status code should be 200")
def check_status_code_ok():
    assert response.status_code == 200


@then("the response time should be below 1000 milliseconds")
def check_response_time():
    assert response.elapsed.total_seconds() * 1000 < 1000


@then("each item should have a non-empty id")
def check_ids():
    data = response.json()
    for item in data.get("schedule", []):
        assert item.get("id")


@then('each item should have type set to "episode"')
def check_types():
    data = response.json()
    for item in data.get("schedule", []):
        assert item.get("type") == "episode"


@then("each episode should have a non-empty title")
def check_titles():
    data = response.json()
    for item in data.get("schedule", []):
        title = item.get("episode", {}).get("title")
        assert title and title.strip()


@then("only one episode should have live set to true")
def check_only_one_live():
    data = response.json()
    lives = [item.get("episode", {}).get("live") for item in data.get("schedule", [])]
    assert lives.count(True) == 1


@then("transmission_start must be before transmission_end")
def check_transmission_dates():
    data = response.json()
    for item in data.get("schedule", []):
        start = item.get("transmission_start")
        end = item.get("transmission_end")
        assert datetime.fromisoformat(start) < datetime.fromisoformat(end)


@then("the response headers should contain a Date")
def check_date_header():
    assert "Date" in response.headers


@then("the status code should be 404")
def check_404():
    assert response.status_code == 404


@then("the error object should contain details and http_response_code")
def check_error_object():
    data = response.json()
    assert "details" in data
    assert "http_response_code" in data
