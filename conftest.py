from datetime import datetime
import json
import os
import pytest
import chromedriver_autoinstaller
import time

from cryptography.fernet import Fernet
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from .objects.Enpasswords import passW
from SeleniumProject.objects.login_page import loginPage


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    chromedriver_autoinstaller.install()

# this is used to add options while running the tests from command line


def pytest_addoption(parser):
    parser.addoption('--head', action='store', default='headed',
                     help='Specify for "headless" or "headed" mode')
    parser.addoption('--key', action='store', default='vTPPw-kknNKQogckY3V942H4FwcN5ZQUvWtlP7cZ4Qw=',  # key is added by default for convenience
                     help='Specify the key to decode the password')


# start the browser
@pytest.fixture(scope="session")
def unLoggedIn(request):
    head = request.config.getoption('--head')

    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    if (head == "headless"):
        options.add_argument('--headless')
    global driver  # making driver global to be able to use it to take screenshot
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # timeout for all selenium options
    return driver


@pytest.fixture(scope='session')
def loggedIn(request):
    head = request.config.getoption('--head')

    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    if (head == "headless"):
        options.add_argument('--headless')
    global driver
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(
        by="id", value=loginPage['userName']).send_keys("standard_user")
    driver.find_element(by="id", value=loginPage['passWord']).send_keys(
        get_pass("standard_user") + Keys.RETURN)
    return driver

# We are taking a screenshot if any test fail


@pytest.fixture(scope='function', autouse=True)
def screenshot_on_fail(request):
    yield
    testname = request.node.name.split('.py')[0]
    if request.session.testsfailed:
        driver.save_screenshot(f'screenshots/fail_{testname}.png')


# this fixture runs at start of session and makes the decryption key avaiable for the function
@pytest.fixture(scope='session', autouse=True)
def get_key(request):
    global key
    key = request.config.getoption('--key')


# this fixture takes encrypted password from objects and decrypts it using the key provided by user
def get_pass(user):
    f = Fernet(key)
    password = f.decrypt(passW[user]).decode()
    return password


def pytest_sessionfinish(session, exitstatus):
    total_tests = session.testscollected
    failed_tests = session.testsfailed
    passed_test = total_tests - failed_tests


# pytest --html=report.html --self-contained-html --head headless
