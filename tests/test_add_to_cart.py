import time
from selenium.webdriver.common.by import By

def test_add_to_cart(driver):
    driver.get("https://automationexercise.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Products')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//u[contains(text(),'View Cart')]").click()
    time.sleep(2)
    assert 'Cart' in driver.title or 'Shopping Cart' in driver.page_source