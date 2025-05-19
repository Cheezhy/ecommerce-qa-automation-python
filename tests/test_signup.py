from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_signup(driver):
    driver.get("https://automationexercise.com")
    wait = WebDriverWait(driver, 20)

    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Signup / Login"))).click()
    wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Test User")
    driver.find_element(By.NAME, "email").send_keys("testuser7@example.com")
    driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()

    # Broaden condition with better timeout
    wait.until(
        EC.presence_of_element_located((
            By.XPATH,
            "//*[contains(text(),'Enter Account Information') or contains(text(),'Account Information')]"
        ))
    )