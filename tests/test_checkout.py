
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures("driver")
def test_checkout_flow(driver):
    driver.get("https://automationexercise.com")
    driver.maximize_window()
    time.sleep(3)

    # Hover and add first product to cart
    product = driver.find_element(By.XPATH, "(//div[@class='productinfo text-center'])[1]")
    ActionChains(driver).move_to_element(product).perform()
    driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[1]").click()
    time.sleep(2)

    # Click 'View Cart'
    driver.find_element(By.XPATH, "//u[text()='View Cart']").click()
    time.sleep(2)

    # Click Proceed To Checkout
    driver.find_element(By.XPATH, "//a[text()='Proceed To Checkout']").click()
    time.sleep(2)

    # If not logged in, login
    if "Login" in driver.page_source:
        driver.find_element(By.NAME, "email").send_keys("automationtestuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("test123")
        driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Cart").click()
        driver.find_element(By.XPATH, "//a[text()='Proceed To Checkout']").click()

    # Confirm address and proceed
    assert "Review Your Order" in driver.page_source
    driver.find_element(By.NAME, "message").send_keys("Automated order message")
    driver.find_element(By.XPATH, "//a[text()='Place Order']").click()
    time.sleep(2)

    # Fill payment details
    driver.find_element(By.NAME, "name_on_card").send_keys("Test User")
    driver.find_element(By.NAME, "card_number").send_keys("4111111111111111")
    driver.find_element(By.NAME, "cvc").send_keys("123")
    driver.find_element(By.NAME, "expiry_month").send_keys("12")
    driver.find_element(By.NAME, "expiry_year").send_keys("2026")

    driver.find_element(By.ID, "submit").click()
    time.sleep(3)

    # Assert order confirmation
    assert "Your order has been placed successfully!" in driver.page_source
