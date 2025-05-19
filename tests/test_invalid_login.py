import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login(driver):
    driver.get("https://automationexercise.com")
    wait = WebDriverWait(driver, 10)

    login_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
    login_btn.click()

    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("wrong@example.com")
    driver.find_element(By.NAME, "password").send_keys("wrongpass")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

    # Wait for error message to show up
    error_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'incorrect')]"))
    )

    assert "incorrect" in error_element.text.lower()
