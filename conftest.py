# Global fixtures and configuration
import pytest
from utils.driver_factory import get_driver

@pytest.fixture(scope='function')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()