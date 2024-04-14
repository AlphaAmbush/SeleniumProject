import json
import os
import time
import pytest
from datetime import datetime as dt

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from SeleniumProject.conftest import get_pass
from SeleniumProject.objects.login_page import loginPage
from SeleniumProject.objects.inventory_page import inventoryPage


def check_exists_by_xpath(xpath, driver):
    try:
        driver.find_element(
            By.XPATH, xpath)
    except:
        return False
    return True


def return_cost_name_list(driver):
    name_list = []
    cost_list = []
    listSize = 1
    xpath = inventoryPage['inventory_list'] + f"/div[{listSize}]"
    while (check_exists_by_xpath(xpath, driver)):
        cost = float((driver.find_element(
            By.XPATH, xpath+"/div[2]/div[2]/div").text).split('$')[1])
        cost_list.append(cost)
        name = driver.find_element(
            By.XPATH, xpath+"/div[2]/div[1]/a/div").text
        name_list.append(name)
        listSize += 1
        xpath = inventoryPage['inventory_list'] + f"/div[{listSize}]"
    return name_list, cost_list


def descendingTest(A):
    for i in range(len(A) - 1):
        if A[i] < A[i+1]:
            return False
        return True


def ascendingTest(A):
    previous = A[0]
    for number in A:
        if number < previous:
            return False
        previous = number
    return True


@pytest.mark.integration
def test_add_remove_to_cart(loggedIn):
    driver = loggedIn
    driver.get('https://www.saucedemo.com/inventory.html')
    driver.find_element(By.XPATH, inventoryPage['back_pack_add_xpath']).click()
    cartText = driver.find_element(By.XPATH, inventoryPage['cart_logo']).text
    assert cartText == '1'
    driver.find_element(By.XPATH, inventoryPage['jacket_add_xpath']).click()
    cartText = driver.find_element(By.XPATH, inventoryPage['cart_logo']).text
    assert cartText == '2'
    driver.find_element(By.XPATH, inventoryPage['jacket_remove_xpath']).click()
    cartText = driver.find_element(By.XPATH, inventoryPage['cart_logo']).text
    assert cartText == '1'


@pytest.mark.integration
def test_check_sorting_name_ascending(loggedIn):
    driver = loggedIn
    driver.get('https://www.saucedemo.com/inventory.html')
    Select(driver.find_element(
        By.XPATH, inventoryPage['sorting_select_xpath'])).select_by_value('az')
    name_list, cost_list = return_cost_name_list(driver)
    if (ascendingTest(name_list) == False):
        raise Exception('Names of items not ascending')


@pytest.mark.integration
def test_check_sorting_name_descending(loggedIn):
    driver = loggedIn
    driver.get('https://www.saucedemo.com/inventory.html')
    Select(driver.find_element(
        By.XPATH, inventoryPage['sorting_select_xpath'])).select_by_value('za')
    name_list, cost_list = return_cost_name_list(driver)
    if (descendingTest(name_list) == False):
        raise Exception('Names of items not descending')


@pytest.mark.integration
def test_check_sorting_cost_ascending(loggedIn):
    driver = loggedIn
    driver.get('https://www.saucedemo.com/inventory.html')
    Select(driver.find_element(
        By.XPATH, inventoryPage['sorting_select_xpath'])).select_by_value('lohi')
    name_list, cost_list = return_cost_name_list(driver)
    if (ascendingTest(cost_list) == False):
        raise Exception('Costs of items not ascending')


@pytest.mark.integration
def test_check_sorting_cost_descending(loggedIn):
    driver = loggedIn
    driver.get('https://www.saucedemo.com/inventory.html')
    Select(driver.find_element(
        By.XPATH, inventoryPage['sorting_select_xpath'])).select_by_value('hilo')
    name_list, cost_list = return_cost_name_list(driver)
    if (descendingTest(cost_list) == False):
        raise Exception('Costs of items not descending')
