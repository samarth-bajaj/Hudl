import pytest

from selenium.webdriver.common.by import By

from fixtures.conftest import browser
from fixtures.login_fixture import login_with_params
from fixtures.element_fixtures import is_visible
from fixtures.wait_fixture import create_wait

from testdata.credentials import EMAIL

custom_login = login_with_params(EMAIL, "Testpass2!")


# Testing whether an error message shows up if the user uses the wrong password.
@pytest.mark.usefixtures("browser", "custom_login")
def test_invalid_login(is_visible, create_wait):
    try:
        wait = create_wait
        error_message_element = wait.until(is_visible(By.XPATH, "//p[@data-qa-id='undefined-text']"))

        # Checking to see if the error message is displayed.
        assert error_message_element.is_displayed(), "Invalid login test failed."

    except Exception as e:
        pytest.fail(f"An error occurred: {str(e)}")
