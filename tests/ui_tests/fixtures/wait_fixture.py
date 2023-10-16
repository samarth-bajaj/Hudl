import pytest

from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def create_wait(browser):
    return WebDriverWait(browser, 10)
