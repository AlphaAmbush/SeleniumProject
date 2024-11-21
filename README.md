# Selenium UI Testing Project for https://www.saucedemo.com

This project automates UI testing for the website https://www.saucedemo.com using Python, Selenium and pytest.

## Requirements

To run the tests, ensure that you have the following installed on your system:

- Google Chrome
- Python
- Pip

## Getting Started

1. Clone the repository.
2. Open a terminal and navigate to the project directory.
3. Install all dependencies by running:

    ```
    pip install -r requirements.txt
    ```

## Running the Tests

To run the test cases, execute the following command:

    ```
    pytest
    
    ```


The test report will be generated and stored in the `report.html` file in the project's base folder.

### Headless Mode

To run the tests in headless mode, use the `--head` flag followed by `headless`:


## Features

1. End-to-end tests covering all UI scenarios.
2. Uses pytest with Selenium for test automation.
3. Passwords are encrypted using a secret key, which is provided by default in the `conftest.py` file.
4. Automatically installs ChromeDriver using `chromedriver_autoinstaller` package.
5. Test fixture creates browser instances for test execution.
6. Fixture captures screenshots automatically when tests fail, stored in the `screenshots` folder.
7. Generates test reports using the `pytest-html` module.
8. Organized into separate modules for test cases, page objects, and helper classes.
9. Supports headless mode for running tests without GUI.


![image](https://github.com/AlphaAmbush/SeleniumProject/assets/89270361/999286e0-3f53-45d0-a15b-e480be1b1c2f)

