import requests # This is a library used to make HTTP requests (like GET, POST).
import os # This helps with file and path operations (used here to locate the .feature file).
from datetime import datetime # This is used to parse and compare timestamps.
from pytest_bdd import scenarios, given, then # This imports decorators (scenarios, given, then) to define BDD (Behavior Driven Development) steps.

# Load the feature file
scenarios(os.path.join(os.path.dirname(__file__), "../features/schedule_api_steps.feature"))
# os.path.dirname(__file__): Gets the current directory of the Python file.
# ../features/schedule_api_steps.feature: Relative path to your .feature file.
# scenarios(...): Loads all scenarios from the given .feature file so they are recognized by pytest-bdd.


# ----------------------------------
# Given steps  – Setup API Requests
# -----------------------------------

# 1. Valid request step
@given('I make a GET request to "https://testapi.io/api/RMSTest/ibltest"', target_fixture="response")
def make_valid_request():
    return requests.get("https://testapi.io/api/RMSTest/ibltest")
# The above lines of code tell pytest-bdd that this is a Given step from your Gherkin scenario.
# It makes a GET request to test API endpoint.
# Also, the target_fixture="response" means that the response will be passed into the then steps as a fixture named response.

# 2. Invalid request step
@given("I make a GET request to an invalid schedule date", target_fixture="response")
def make_invalid_request():
    return requests.get("https://testapi.io/api/RMSTest/ibltest/invalid")
# The above lines of code simulate a request with an invalid path or date to trigger error handling.


# ----------------------------------------
# Then steps – Assertions on the Response
# ----------------------------------------

#  1. Status code is 200
@then("the response status code should be 200")
def check_status_code_ok(response):
    assert response.status_code == 200
# The above lines of code verify that the API call was successful (HTTP 200 OK).

# 2. Status code is 404
@then("the status code should be 404")
def check_404(response):
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
# The above lines of code confirm the API correctly returns 404 for invalid URLs.

# 3. Response time check
@then("the response time should be below 1000 milliseconds")
def check_response_time(response):
    assert response.elapsed.total_seconds() * 1000 < 1000
# The above lines of code measure how long the response took.
# Also Ensures it's under 1000 ms (1 second).

# 4. All items must have non-empty ids
@then("each item should have a non-empty id")
def check_ids(response):
    data = response.json()
    elements = data.get("schedule", {}).get("elements", [])
    for item in elements:
        assert item.get("id"), f"Missing or empty ID in item: {item}"
# The above lines of code parse the JSON.
# ALso ensures each schedule item has an id and it's not empty.

# 5. The item "type" is "broadcast", episode "type" is "episode"
@then('each item should have type set to "episode"')
def check_types(response):
    data = response.json()
    elements = data.get("schedule", {}).get("elements", [])
    for item in elements:
        assert item.get("type") == "broadcast", f"Expected 'broadcast', got '{item.get('type')}'"
        episode_type = item.get("episode", {}).get("type")
        assert episode_type == "episode", f"Expected episode type to be 'episode', got '{episode_type}'"
# The above lines of code ensures top-level type is "broadcast" and nested episode type is "episode".

# 6. Each episode has a non-empty title
@then("each episode should have a non-empty title")
def check_titles(response):
    data = response.json()
    elements = data.get("schedule", {}).get("elements", [])
    for item in elements:
        title = item.get("episode", {}).get("title", "")
        assert title.strip(), f"Empty or missing title in item: {item.get('id')}"
# Those lines of code make sure every episode has a non-blank title.

# 7. Only one live episode
@then("only one episode should have live set to true")
def check_only_one_live(response):
    data = response.json()
    elements = data.get("schedule", {}).get("elements", [])
    lives = [item.get("episode", {}).get("live", False) for item in elements]
    assert lives.count(True) == 1, f"Expected exactly one live episode, found {lives.count(True)}"
# Those lines of code extract live flags and asserts that only one is True.

# 8. Check start and end timestamps
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
# The lines of code Check ISO timestamps.
# Also ensures each transmission ends after it starts.

# 9. Check headers for Date
@then("the response headers should contain a Date")
def check_date_header(response):
    assert "Date" in response.headers
# Those lines of code validate that the server sent a Date header (standard for HTTP responses).

# 10. Validate 404 error message
@then("the error object should contain details and http_response_code")
def check_error_object(response):
    # Assert the raw body content
    assert response.status_code == 404
    assert response.text.strip() == "Endpoint not found"
# The above lines of code confirm the error response text is "Endpoint not found" (as expected from your test API).