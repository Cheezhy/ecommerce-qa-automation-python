from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkout(driver):
    driver.get("https://automationexercise.com")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'Add to cart')])[1]"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//u[contains(text(),'View Cart')]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed To Checkout"))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Address Details') or contains(text(),'Review Your Order')]")))
