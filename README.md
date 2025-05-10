# BBCSeniorTesterTestAssessment

This project is a solution for the BBC Senior Tester Technical Assessment, covering both functional manual testing and automated testing of a public schedule API.

Part 1: Automation Testing
Tech Stack
----------
1. Language: Python version 3.9+

2. Test Framework: pytest, pytest-bdd

3. HTTP Requests: requests

4. IDE: PyCharm 

5. Runner: CLI with pytest


Project Structure
------------------
.
├── features/
│   └── schedule_api_steps.feature   # Gherkin scenarios
├── tests/
│   └── test_schedule_api_steps.py   # Step definitions
├── requirements.txt                 # Dependencies
└── README.md


Setup Instructions
-------------------
1. Clone the Repository
     - git clone https://github.com/your-username/bbc-senior-tester-assessment.git
     - cd bbc-senior-tester-assessment

2. Create and Activate Virtual Environment
     - python -m venv .venv
     - source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install Dependencies
     - pip install -r requirements.txt

How to Run Automated Tests
---------------------------
Run all scenarios:
  - pytest
Run with detailed output:
  - pytest -v


Part 2: Functional Manual Testing
Test Cases Overview
--------------------
Test Case ID: TC01		

Test Objective: Verify successful API response and performance

Test Steps: Send GET to /schedules/bbc_one_london/<valid-date>	

Expected Result: HTTP 200 OK, response time < 1000ms


Test Case ID: TC02		

Test Objective: Verify data fields and episode structure

Test Steps: Check each schedule item for id, type, title, transmission times	

Expected Result: All fields valid, type = "episode", correct order


Test Case ID: TC03	

Test Objective: Validate 404 and error message for invalid date request	

Test Steps: Send GET to /schedules/bbc_one_london/invalid-date

Expected Result:	HTTP 404, JSON body with details, code


How to Run Manual Tests in Postman
-----------------------------------
1. Open Postman

2. Create a new GET request to the following endpoint:
     https://api.schedules.bbc.com/schedules/bbc_one_london/2024-05-06

3. Click Send

4. Inspect the response:

  - Check status code

  - Validate response body structure

  - Confirm response time is < 1 second
    

Troubleshooting
---------------
1. "Couldn't resolve host"

      - Use the Desktop Agent in Postman.

      - Check internet connection or try testapi.io fallback endpoint.

2. Python version mismatch

    - Ensure you're using Python 3.9 or higher.














