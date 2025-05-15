import time
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

def test_valid_login(driver):
    driver.get("https://automationexercise.com")
    time.sleep(2)

    # Dismiss overlay if it appears
    try:
        driver.find_element(By.CLASS_NAME, "fc-button").click()  # Accept cookies
        time.sleep(1)
    except:
        pass  # If not present, continue

    # Try clicking 'Signup / Login' again
    login_link = driver.find_element(By.LINK_TEXT, "Signup / Login")
    try:
        login_link.click()
    except ElementClickInterceptedException:
        time.sleep(1)
        login_link.click()  # Retry after waiting

    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("automationtestuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("test123")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)
    assert "Logged in as" in driver.page_source

