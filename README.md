# Install
First, make sure to install the necessary Python packages. Run the following command to install them:

pip install pytest pytest-html requests Appium-Python-Client

These packages include:
pytest: Test framework
pytest-html: For generating HTML test reports
requests: To send API requests
Appium-Python-Client: For Appium automation tests

Before running the tests, ensure all necessary packages are installed and Appium is properly set up.

# Run Tests and Generate Reports
Use the following command to run the tests and generate an HTML test report:

pytest --maxfail=5 --disable-warnings -q --html=reports/test_report.html

Explanation of the Command:
--maxfail=1: Allow up to 5 test failure before stopping the test run.
--disable-warnings: Disables warning messages from showing.
-q: Quiet mode, reduces output verbosity.
--html=reports/test_report.html: Generates the test report in HTML format and saves it in reports/test_report.html.

# Run a Specific Test
If you only want to run a specific test, use the following command:

pytest tests/test_api.py --maxfail=1 --disable-warnings -q --html=reports/test_report.html
This command runs the tests/test_api.py file and generates an HTML test report.

# Location of Test Reports
After the tests are completed, the report will be saved in the reports/ directory under the filename test_report.html. You can open this file in your browser to view the detailed test results.

# About the Tasks
This project including mobile app automation, basic coding tasks, and API testing.

Task 1: Pyramid Pattern
Test the pyramid pattern output by checking if the correct structure is printed.

Task 2: App UI Verification
Use Appium to automate the UI testing of the app and verify the weather date.

Task 3: API Verification
Confirm that the request is successful and the data meets expectations.