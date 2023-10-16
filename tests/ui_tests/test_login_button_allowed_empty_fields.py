import pytest

from selenium.webdriver.common.by import By

from fixtures.conftest import browser
from fixtures.login_fixture import login_with_params

from testdata.credentials import EMAIL, PASSWORD

custom_login = login_with_params(EMAIL, "")
password = PASSWORD


# Testing if the login button is allowed to be clicked if there are empty fields in the sign in box.
@pytest.mark.usefixtures("browser", "custom_login")
def test_login_button_allowed_empty_fields(browser):
    try:
        username_field = browser.find_element(By.ID, "email")
        password_field = browser.find_element(By.ID, "password")
        login_button = browser.find_element(By.ID, "logIn")

        # The two checks below check that the login button is still visible but not clickable.
        assert not login_button.is_enabled(), "Login button is still clickable."
        assert login_button.is_displayed(), "Login button is not visible."

        username_field.clear()
        password_field.send_keys(password)

        assert not login_button.is_enabled(), "Login button is still clickable."
        assert login_button.is_displayed(), "Login button is not visible."

    except Exception as e:
        pytest.fail(f"An error occurred: {str(e)}")
