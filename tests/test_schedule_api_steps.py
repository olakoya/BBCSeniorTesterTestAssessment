import os
import requests
import time
from pytest_bdd import scenarios, given, then, parsers

BASE_URL = "https://testapi.io/api/RMSTest/ibltest"
response = None

# scenarios("../features/schedule_api_steps.feature")
scenarios(os.path.join(os.path.dirname(__file__), "../features/schedule_api_steps.feature"))

@given(parsers.cfparse('I make a GET request to "{url}"'))
def make_get_request(url):
    global response
    start_time = time.time()
    response = requests.get(url)
    response.elapsed_time = (time.time() - start_time) * 1000  # in ms


@then("the response status code should be 200")
def check_status_code():
    assert response.status_code == 200


@then("the response time should be below 1000 milliseconds")
def check_response_time():
    assert response.elapsed_time < 1000


@then("verify every elements:id field is never null or empty (“”)")
def check_id_fields():
    data = response.json()
    for item in data:
        assert item["id"] is not None and item["id"] != ""


@then("verify that the “type” in “episode” for every item is always “episode”")
def check_episode_type():
    data = response.json()
    for item in data:
        assert item["episode"]["type"] == "episode"


@then("verify that every title field in episode is never null or empty")
def check_episode_titles():
    data = response.json()
    for item in data:
        title = item["episode"]["title"]
        assert title is not None and title != ""


@then("verify that only one episode in the list has “live” field in “episode” as true")
def check_only_one_live():
    data = response.json()
    live_count = sum(1 for item in data if item["episode"].get("live") is True)
    assert live_count == 1


@then("verify that the “transmission_start” date value is before the “transmission_end” date")
def check_transmission_dates():
    data = response.json()
    for item in data:
        start = item["transmission_start"]
        end = item["transmission_end"]
        assert start < end


@then("verify in the response headers, verify the “Date” value")
def check_response_header_date():
    date_header = response.headers.get("Date")
    assert date_header is not None and date_header != ""


@then("verify that the HTTP status code of the response is 404")
def check_404_status_code():
    assert response.status_code == 404


@then("verify the error object had the properties ‘details’ and ‘http_response_code’")
def check_error_object_properties():
    error_data = response.json()
    assert "details" in error_data
    assert "http_response_code" in error_data
