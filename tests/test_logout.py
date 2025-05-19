
import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
def test_logout(driver):
    driver.get("https://automationexercise.com")

    # Login
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    driver.find_element(By.NAME, "email").send_keys("automationtestuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("test123")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)

    # Click logout
    driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(2)

    # Assert redirected to login page
    assert "Login to your account" in driver.page_source
