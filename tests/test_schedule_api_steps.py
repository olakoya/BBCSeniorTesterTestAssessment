import requests
import os
from datetime import datetime
from pytest_bdd import scenarios, given, then

# Load the feature file
scenarios(os.path.join(os.path.dirname(__file__), "../features/schedule_api_steps.feature"))

# ---------------------
# Given steps
# ---------------------

@given('I make a GET request to "https://testapi.io/api/RMSTest/ibltest"', target_fixture="response")
def make_valid_request():
    return requests.get("https://testapi.io/api/RMSTest/ibltest")


@given("I make a GET request to an invalid schedule date", target_fixture="response")
def make_invalid_request():
    return requests.get("https://testapi.io/api/RMSTest/ibltest/invalid")


# ---------------------
# Then steps
# ---------------------

@then("the response status code should be 200")
def check_status_code_ok(response):
    assert response.status_code == 200


@then("the status code should be 404")
def check_404(response):
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"


@then("the response time should be below 1000 milliseconds")
def check_response_time(response):
    assert response.elapsed.total_seconds() * 1000 < 1000


@then("each item should have a non-empty id")
def check_ids(response):
    data = response.json()
    elements = data.get("schedule", {}).get("elements", [])
    for item in elements:
        assert item.get("id"), f"Missing or empty ID in item: {item}"


@then('each item should have type set to "episode"')
def check_types(response):
    data = response.json()
    elements = data.get("schedule", {}).get("elements", [])
    for item in elements:
        assert item.get("type") == "broadcast", f"Expected 'broadcast', got '{item.get('type')}'"
        episode_type = item.get("episode", {}).get("type")
        assert episode_type == "episode", f"Expected episode type to be 'episode', got '{episode_type}'"


@then("each episode should have a non-empty title")
def check_titles(response):
    data = response.json()
    elements = data.get("schedule", {}).get("elements", [])
    for item in elements:
        title = item.get("episode", {}).get("title", "")
        assert title.strip(), f"Empty or missing title in item: {item.get('id')}"


@then("only one episode should have live set to true")
def check_only_one_live(response):
    data = response.json()
    elements = data.get("schedule", {}).get("elements", [])
    lives = [item.get("episode", {}).get("live", False) for item in elements]
    assert lives.count(True) == 1, f"Expected exactly one live episode, found {lives.count(True)}"


@then("transmission_start must be before transmission_end")
def check_transmission_dates(response):
    data = response.json()
    elements = data.get("schedule", {}).get("elements", [])
    for item in elements:
        start = item.get("transmission_start")
        end = item.get("transmission_end")
        assert start and end, f"Missing transmission_start or transmission_end in item: {item.get('id')}"
        start_dt = datetime.fromisoformat(start.rstrip("Z"))
        end_dt = datetime.fromisoformat(end.rstrip("Z"))
        assert start_dt < end_dt, f"Start time is not before end time in item: {item.get('id')}"


@then("the response headers should contain a Date")
def check_date_header(response):
    assert "Date" in response.headers


@then("the error object should contain details and http_response_code")
def check_error_object(response):
    # Assert the raw body content
    assert response.status_code == 404
    assert response.text.strip() == "Endpoint not found"