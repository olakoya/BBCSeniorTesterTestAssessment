import requests # Imports the requests library, which is used to send HTTP requests (e.g. GET, POST).
import os # Imports the os module, which helps handle file paths and directories.
from pytest_bdd import scenarios, given, then # Imports functions from pytest-bdd, a BDD plugin for pytest (scenarios loads .feature files, and given and then define steps that map to Gherkin steps).
from datetime import datetime #  Imports the datetime class to help parse and compare date/time values (e.g., checking start vs end time).

# Load the .feature file
scenarios(os.path.join(os.path.dirname(__file__), "../features/schedule_api_steps.feature")) # Loads the Gherkin feature file located at ../features/schedule_api_steps.feature.

# Shared variable
response = None # Declares a global response variable to store the API response, so it can be reused across step functions.

# This Given step sends a GET request to the test API endpoint and stores the response.
@given('I make a GET request to "https://testapi.io/api/RMSTest/ibltest"')
def make_valid_request():
    global response
    response = requests.get("https://testapi.io/api/RMSTest/ibltest")

# This Given step sends a GET request to a deliberately invalid URL to trigger an error (like 404).
@given("I make a GET request to an invalid schedule date")
def make_invalid_request():
    global response
    response = requests.get("https://testapi.io/api/RMSTest/ibltest/invalid")

# This verifies that the HTTP status code is 200 OK.
@then("the response status code should be 200")
def check_status_code_ok():
    assert response.status_code == 200

# This checks that the response time is less than 1000 milliseconds (1 second).
@then("the response time should be below 1000 milliseconds")
def check_response_time():
    assert response.elapsed.total_seconds() * 1000 < 1000

# This confirms that every object in the schedule list has a non-empty id.
@then("each item should have a non-empty id")
def check_ids():
    data = response.json()
    for item in data.get("schedule", []):
        assert item.get("id")

# This checks that each item in the schedule has a type field equal to "episode".
@then('each item should have type set to "episode"')
def check_types():
    data = response.json()
    for item in data.get("schedule", []):
        assert item.get("type") == "episode"

# This makes sure each episode has a title that is not empty or just spaces.
@then("each episode should have a non-empty title")
def check_titles():
    data = response.json()
    for item in data.get("schedule", []):
        title = item.get("episode", {}).get("title")
        assert title and title.strip()

# This checks that only one episode has "live": true.
@then("only one episode should have live set to true")
def check_only_one_live():
    data = response.json()
    lives = [item.get("episode", {}).get("live") for item in data.get("schedule", [])]
    assert lives.count(True) == 1

# This verifies that each episode’s transmission_start time is before the transmission_end.
@then("transmission_start must be before transmission_end")
def check_transmission_dates():
    data = response.json()
    for item in data.get("schedule", []):
        start = item.get("transmission_start")
        end = item.get("transmission_end")
        assert datetime.fromisoformat(start) < datetime.fromisoformat(end)

# This confirms that the HTTP response headers include a standard Date field.
@then("the response headers should contain a Date")
def check_date_header():
    assert "Date" in response.headers

# This used in error-handling scenarios, expects the response to return HTTP 404 Not Found.
@then("the status code should be 404")
def check_404():
    assert response.status_code == 404

# This is for invalid responses: ensures the response body contains a JSON details field and http_response_code.
@then("the error object should contain details and http_response_code")
def check_error_object():
    data = response.json()
    assert "details" in data
    assert "http_response_code" in data
