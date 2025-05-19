from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(driver):
    driver.get("https://automationexercise.com")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Signup / Login"))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("automationtestuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("test123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Logout"))).click()
