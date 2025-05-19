import pytest
from selenium.webdriver.common.by import By
import time

def test_invalid_login(driver):
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("wrong@example.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    assert "Your email or password is incorrect!" in driver.page_source