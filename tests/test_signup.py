import time
from selenium.webdriver.common.by import By

def test_signup(driver):
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)
    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("testsignup_user@example.com")
    driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()
    assert "Enter Account Information" in driver.page_source