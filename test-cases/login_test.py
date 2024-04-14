import time
import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from SeleniumProject.conftest import get_pass
from SeleniumProject.objects.login_page import loginPage
from SeleniumProject.objects.helper import screenshot


# all the sanity tests are marked with a marker to make it easy to run
# only the sanity tests
@pytest.mark.sanity
def test_login_std_user(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    driver.find_element(
        by="id", value=loginPage['userName']).send_keys("standard_user")
    driver.find_element(by="id", value=loginPage['passWord']).send_keys(
        get_pass("standard_user") + Keys.RETURN)
    print(driver.current_url)
    screenshot(driver, "logged_in_page")
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


# this login user generates an error message
@pytest.mark.sanity
def test_login_locked_out(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    driver.find_element(
        by="id", value=loginPage['userName']).send_keys("locked_out_user")
    driver.find_element(by="id", value=loginPage['passWord']).send_keys(
        get_pass("locked_out_user") + Keys.RETURN)

    errorMsg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, loginPage['lockedOutErrMsg'])))
    assert errorMsg.text == "Epic sadface: Sorry, this user has been locked out."

    print(driver.current_url)

    assert driver.current_url == "https://www.saucedemo.com/"
