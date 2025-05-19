from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

def test_checkout(driver):
    driver.get("https://automationexercise.com")
    wait = WebDriverWait(driver, 20)

    # 🔐 Log in before checkout
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("automationtestuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("test123")
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

    # 🛒 Add item to cart
    add_to_cart = wait.until(EC.presence_of_element_located((By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")))
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'Add to cart')])[1]"))).click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", add_to_cart)

    view_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//u[contains(text(),'View Cart')]")))
    view_cart.click()

    checkout = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed To Checkout")))
    checkout.click()

    assert "Address Details" in driver.page_source or "Review Your Order" in driver.page_source
