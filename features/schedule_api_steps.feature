Feature: Schedule API Testing

  Scenario: Verify status code and response time
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then the response status code should be 200
    And the response time should be below 1000 milliseconds

  Scenario: Verify every item has a non-empty id and type is always episode
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then each item should have a non-empty id
    And each item should have type set to "episode"

  Scenario: Verify every episode title is never null or empty
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then each episode should have a non-empty title

  Scenario: Verify only one episode is live
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then only one episode should have live set to true

  Scenario: Verify start date is before end date
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then transmission_start must be before transmission_end

  Scenario: Verify Date in response headers
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then the response headers should contain a Date

  Scenario: Verify 404 and error object for invalid date
    Given I make a GET request to an invalid schedule date
    Then the status code should be 404
    And the error object should contain details and http_response_code
