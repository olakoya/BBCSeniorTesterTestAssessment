import os
import requests
import time
from pytest_bdd import scenarios, given, then, parsers

scenarios(os.path.join(os.path.dirname(__file__), "../features/schedule_api_steps.feature"))
# scenarios(os.path.join(os.path.dirname(__file__), "../features/hello_world.feature"))


BASE_URL = "https://testapi.io/api/RMSTest/ibltest"
response = None

@given(parsers.cfparse('I make a GET request to "{url}"'))
def make_get_request(url):
    global response
    start_time = time.time()
    response = requests.get(url)
    response.elapsed_time = (time.time() - start_time) * 1000


@given("I make a GET request to an invalid schedule date")
def make_invalid_get_request():
    global response
    response = requests.get("https://testapi.io/api/RMSTest/invalid-date")


@then("the response status code should be 200")
def check_status_code():
    assert response.status_code == 200


@then("the response time should be below 1000 milliseconds")
def check_response_time():
    assert response.elapsed_time < 1000


@then("every item should have a non-empty id")
def check_id_fields():
    data = response.json()
    for item in data:
        assert item["id"] is not None and item["id"] != ""


@then('the type in episode should always be "episode"')
def check_episode_type():
    data = response.json()
    for item in data:
        assert item["episode"]["type"] == "episode"


@then("each schedule item should have a non-empty title in episode")
def check_episode_titles():
    data = response.json()
    for item in data:
        title = item["episode"]["title"]
        assert title is not None and title != ""


@then("only one episode should have live set to true")
def check_only_one_live():
    data = response.json()
    live_count = sum(1 for item in data if item["episode"].get("live") is True)
    assert live_count == 1


@then("transmission_start must be before transmission_end")
def check_transmission_dates():
    data = response.json()
    for item in data:
        assert item["transmission_start"] < item["transmission_end"]


@then("the response headers should contain a Date")
def check_response_header_date():
    assert "Date" in response.headers
    assert response.headers["Date"] != ""


@then("the status code should be 404")
def check_404_status_code():
    assert response.status_code == 404


@then("the error object should have details and http_response_code")
def check_error_object_properties():
    error_data = response.json()
    assert "details" in error_data
    assert "http_response_code" in error_data
