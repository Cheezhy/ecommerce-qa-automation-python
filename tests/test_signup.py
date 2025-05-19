from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

def test_signup(driver):
    driver.get("https://automationexercise.com")
    wait = WebDriverWait(driver, 20)

    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Signup / Login"))).click()
    wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Test User")

    # Generate a unique email every time
    unique_email = f"testuser_{datetime.now().strftime('%Y%m%d_%H%M%S')}@example.com"
    driver.find_element(By.NAME, "email").send_keys(unique_email)
    driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()

    # Wait for account info page
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Account Information')]")))
