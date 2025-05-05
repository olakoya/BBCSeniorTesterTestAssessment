Feature: Schedule API Testing

  Scenario 1: Verify status code and response time
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then the response status code should be 200
    And the response time should be below 1000 milliseconds

  Scenario 2: Verify every id field is never null or empty and type is always "episode"
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then every item should have a non-empty id
    And the type in episode should always be "episode"

  Scenario 3: Verify every episode title is never null or empty
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then each schedule item should have a non-empty title in episode

  Scenario 4: Verify only one episode is live
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then only one episode should have live set to true

  Scenario 5: Verify start date is before end date
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then transmission_start must be before transmission_end

  Scenario 6: Verify Date in response headers
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then the response headers should contain a Date

  Scenario 7: Verify 404 and error object for invalid date
    Given I make a GET request to an invalid schedule date
    Then the status code should be 404
    And the error object should have details and http_response_code
