import pytest
from selenium.webdriver.common.by import By
import time

def test_checkout(driver):
    driver.get("https://automationexercise.com")
    driver.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//u[contains(text(),'View Cart')]").click()
    driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
    assert "Address Details" in driver.page_source or "Review Your Order" in driver.page_source