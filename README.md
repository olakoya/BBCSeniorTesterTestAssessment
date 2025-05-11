# BBC SENIOR TESTER TEST ASSESSMENT

**This project is a solution for the BBC Senior Tester Technical Assessment, covering both functional manual testing and automated testing of a public schedule API.**

**The automated tests are written in Python using pytest-bdd to enable behavior-driven development (BDD) for a schedule-based API. These tests are part of the overall technical assessment submission.**

---
## *Part 1: Automation Testing*

Tech Stack
-----------
1. Language: Python version 3.9+

2. Test Framework: pytest, pytest-bdd

3. HTTP Requests: requests

4. IDE: PyCharm 

5. Runner: CLI with pytest


Project Structure
------------------
1. features/ (Directory)
   - schedule_api_steps.feature (file) # Gherkin scenarios for API testing
2. tests/ (Package)
   - test_schedule_api_steps.py (file) # Step definitions using pytest-bdd
3. .github/workflows/
   - python-tests.yml # GitHub Actions workflow to run tests on push
   - requirements.txt # Python dependencies
   - README.md # Project documentation


---

## API Under Test

This test suite interacts with a mock schedule API endpoint hosted on [testapi.io](https://testapi.io):

Testapi.io is a free tool that allows user to easily mock up API endpoints and mock databases and make requests.

1. Valid Endpoint: `https://testapi.io/api/RMSTest/ibltest`
2. Invalid Endpoint: `https://testapi.io/api/RMSTest/ibltest/invalid`

---

## Features Tested

The suite includes test coverage for the following:

1. **Status Code & Response Time**
   - Valid endpoint returns `200 OK`
   - Invalid endpoint returns `404 Not Found`
   - Response time is less than 1000 ms


2. **Schedule Data Validations**
   - Each item has a non-empty ID
   - Each item has type `broadcast` and episode type `episode`
   - Each episode has a non-empty title
   - Only one episode is marked as `live`
   - `transmission_start` is before `transmission_end`


3. **Headers & Error Handling**
   - Response headers contain a `Date`
   - Error object contains `http_response_code` and `details` (or appropriate message)

---

## *How to Run Tests Locally:*

## *Dependencies*
1. pytest
2. pytest-bdd
3. requests

Setup Instructions And Running of  Automated Tests
----------------------------------------------------
### 1. Clone the Repository
     - git clone https://github.com/olakoya/BBCSeniorTesterTestAssessment.git
     - cd bbc-senior-tester-assessment

### 2. Create and Activate Virtual Environment
     - python -m venv .venv
     - source .venv/bin/activate  # (For Windows: .venv\Scripts\activate)

### 3. Install Dependencies via:
     - pip install -r requirements.txt

### 4. Run all Tests Scenarios:
    - pytest

### 5. Run with detailed output:
      - pytest -v

---

## *Part 2: Functional Manual Testing*

Test Cases Overview
--------------------
### *Test Case ID: TC_API_001*

Test Objective: Verify successful API response and performance

Test Steps: Send GET to /schedules/bbc_one_london/<valid-date>	

Expected Result: HTTP 200 OK, response time < 1000ms


### *Test Case ID: TC_API_002*	

Test Objective: Verify data fields and episode structure

Test Steps: Check each schedule item for id, type, title, transmission times	

Expected Result: All fields valid, type = "episode", correct order


### *Test Case ID: TC_API_003*

Test Objective: Validate 404 and error message for invalid date request	

Test Steps: Send GET to /schedules/bbc_one_london/invalid-date

Expected Result:	HTTP 404, JSON body with details, code


Run Manual Tests in Postman
----------------------------
1. Open Postman (https://web.postman.co/workspace/My-Workspace~185a1c3a-8d6d-4eeb-82db-2a0bd64fb53f/request/create?requestId=c8366ae4-f6fd-4fca-b66d-9de73d7bf5b9)

2. Create a new GET request to the following endpoint: https://testapi.io/api/RMSTest/ibltest

3. Click Send

4. Inspect the response:

   - Check status code

   - Validate response body structure

   - Confirm response time is less than 1000 millisecond
    

Troubleshooting
----------------
1. Couldn't resolve host

      - Use the Desktop Agent in Postman.

      - Check internet connection or try testapi.io fallback endpoint.


2. Python version mismatch

    - Ensure you're using Python 3.9 or higher.

## GitHub Actions CI
This repository includes a GitHub Actions workflow that:

1. Installs dependencies

2. Runs pytest on every push to main

It can be found in: .github/workflows/python-tests.yml

## Screenshots
1. Passing Test in Postman can be found in (https://github.com/olakoya/BBCSeniorTesterTestAssessment.git)

2. Failing Test in Postman can be found in (https://github.com/olakoya/BBCSeniorTesterTestAssessment.git)











