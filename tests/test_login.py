import time
from selenium.webdriver.common.by import By

def test_valid_login(driver):
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)
    driver.find_element(By.NAME, "email").send_keys("automationtestuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("test123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    assert "Logged in as" in driver.page_source