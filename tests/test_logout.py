import pytest
from selenium.webdriver.common.by import By
import time

def test_logout(driver):
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("automationtestuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("test123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    assert "Signup / Login" in driver.page_source