import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


from SeleniumProject.objects.login_page import loginPage
from SeleniumProject.objects.inventory_page import inventoryPage
from SeleniumProject.objects.checkout_page import checkoutPage
from SeleniumProject.objects.helper import screenshot


@pytest.mark.sanity
def test_checkout(setup):
    driver = setup
    driver.find_element(By.XPATH, inventoryPage['back_pack_add_xpath']).click()
    driver.find_element(By.XPATH, inventoryPage['jacket_add_xpath']).click()
    driver.find_element(
        By.XPATH, inventoryPage['cart_logo']).click()
    driver.find_element(By.XPATH, checkoutPage['checkout_btn']).click()
    driver.find_element(
        By.XPATH, checkoutPage['first_name']).send_keys("xyz")
    driver.find_element(
        By.XPATH, checkoutPage['last_name']).send_keys("yzx")
    driver.find_element(
        By.XPATH, checkoutPage['zip_code']).send_keys("1234")
    driver.find_element(By.XPATH, checkoutPage['continue_btn']).click()
    screenshot(driver, 'final_checkout_page')
    driver.find_element(By.XPATH, checkoutPage['finish_btn']).click()
    succ_message = (driver.find_element(
        By.XPATH, checkoutPage['success_msg'])).text
    assert succ_message == 'Thank you for your order!'
