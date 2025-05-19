import pytest
from selenium.webdriver.common.by import By
import time
import uuid

def test_signup(driver):
    driver.get("https://automationexercise.com")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)
    unique_email = f"testuser_{uuid.uuid4().hex[:6]}@example.com"
    driver.find_element(By.NAME, "name").send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys(unique_email)
    driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()
    assert "Enter Account Information" in driver.page_source