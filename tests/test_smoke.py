def test_site_load(driver):
    driver.get('https://automationexercise.com')
    assert 'Automation Exercise' in driver.title