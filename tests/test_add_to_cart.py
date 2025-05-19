
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures("driver")
def test_add_to_cart(driver):
    driver.get("https://automationexercise.com")
    driver.maximize_window()
    time.sleep(3)

    # Scroll to first product and hover
    product = driver.find_element(By.XPATH, "(//div[@class='productinfo text-center'])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(product).perform()
    time.sleep(2)

    # Click 'Add to cart' on the first product
    driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[1]").click()
    time.sleep(2)

    # Click 'View Cart' in modal
    driver.find_element(By.XPATH, "//u[text()='View Cart']").click()
    time.sleep(2)

    # Confirm product is in cart
    assert "Shopping Cart" in driver.page_source
    assert "Blue Top" in driver.page_source  # Adjust if product name changes
