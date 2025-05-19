import pytest
from selenium.webdriver.common.by import By
import time

def test_add_to_cart(driver):
    driver.get("https://automationexercise.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//u[contains(text(),'View Cart')]").click()
    assert "Shopping Cart" in driver.title or "Cart" in driver.title