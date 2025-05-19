from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

def test_add_to_cart(driver):
    driver.set_window_size(1920, 1080)
    driver.get("https://automationexercise.com")
    wait = WebDriverWait(driver, 20)

    add_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//a[contains(text(),'Add to cart')])[1]"))
    )
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'Add to cart')])[1]"))).click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", add_button)

    view_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//u[contains(text(),'View Cart')]")))
    view_cart.click()

    # Assert we are on the cart page
    assert "Shopping Cart" in driver.page_source
