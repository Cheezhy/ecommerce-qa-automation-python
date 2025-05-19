from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_signup(driver):
    driver.get("https://automationexercise.com")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Signup / Login"))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("testuser2@example.com")
    driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Enter Account Information')]")))
