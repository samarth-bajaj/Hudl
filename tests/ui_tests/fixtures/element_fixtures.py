import pytest

from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def is_visible(browser):
    def visibility_condition(by, value):
        return EC.visibility_of_element_located((by, value))

    return visibility_condition


@pytest.fixture(scope="function")
def is_clickable(browser):
    def clickable_condition(by, value):
        return EC.element_to_be_clickable((by, value))

    return clickable_condition


@pytest.fixture(scope="function")
def is_present(browser):
    def presence_condition(by, value):
        return EC.presence_of_element_located((by, value))

    return presence_condition
