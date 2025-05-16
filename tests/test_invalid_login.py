
import time
import pytest
from selenium.webdriver.common.by import By

def test_invalid_login(driver):
    driver.get("https://automationexercise.com")
    time.sleep(2)

    # Close cookie overlay if it appears
    try:
        driver.find_element(By.CLASS_NAME, "fc-button").click()
        time.sleep(1)
    except:
        pass

    # Navigate to login page
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)

    # Enter invalid credentials
    driver.find_element(By.NAME, "email").send_keys("invaliduser@example.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpassword")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)

    # Assert that login failed message appears
    assert "Your email or password is incorrect!" in driver.page_source
