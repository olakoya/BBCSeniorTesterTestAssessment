Feature: Hello World Test

  Scenario: Just test parsing
    Given I make a GET request to "https://testapi.io/api/RMSTest/ibltest"
    Then the response status code should be 200

