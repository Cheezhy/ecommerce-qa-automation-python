import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
def test_signup_new_user(driver):
    driver.get("https://automationexercise.com")

    # Click 'Signup / Login'
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()

    # Fill name and email
    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("signupuser123@example.com")
    driver.find_element(By.XPATH, "//button[text()='Signup']").click()
    time.sleep(2)

    # Fill the registration form
    driver.find_element(By.ID, "id_gender1").click()
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "days").send_keys("15")
    driver.find_element(By.ID, "months").send_keys("May")
    driver.find_element(By.ID, "years").send_keys("1995")

    driver.find_element(By.ID, "first_name").send_keys("Test")
    driver.find_element(By.ID, "last_name").send_keys("User")
    driver.find_element(By.ID, "address1").send_keys("123 Testing St")
    driver.find_element(By.ID, "state").send_keys("Lagos")
    driver.find_element(By.ID, "city").send_keys("Ikeja")
    driver.find_element(By.ID, "zipcode").send_keys("100001")
    driver.find_element(By.ID, "mobile_number").send_keys("08123456789")
    
    driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

    # Assert confirmation message
    assert "ACCOUNT CREATED!" in driver.page_source
