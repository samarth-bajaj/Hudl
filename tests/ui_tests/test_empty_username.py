import pytest

from selenium.webdriver.common.by import By

from fixtures.conftest import browser
from fixtures.login_fixture import login_with_params
from fixtures.element_fixtures import is_visible
from fixtures.wait_fixture import create_wait

from testdata.credentials import PASSWORD

custom_login = login_with_params("", PASSWORD)


# Testing that pressing the login button shows an error if the username field is empty.
@pytest.mark.usefixtures("custom_login")
def test_empty_username(is_visible, create_wait):
    try:
        wait = create_wait

        error_message_element = wait.until(is_visible(By.XPATH, "//p[@data-qa-id='undefined-text']"))
        error_message_element_under_field = wait.until(
            is_visible(By.XPATH, "//div[@id='username-container']/p/span[@id='uniName_947Help']")
        )

        error_message_element_text = error_message_element.text
        expected_error_message = "Please fill in all of the required fields"

        # These tests check whether the two error messages show up and if the text on the error message is correct.
        assert error_message_element.is_displayed(), "Empty username test failed (no error message)."
        assert error_message_element_under_field.is_displayed(), "Empty password test failed " \
                                                                 "(no error message under empty field)."
        assert error_message_element_text == expected_error_message, f"Text value does not match. " \
                                                                     f"Expected: {expected_error_message}, " \
                                                                     f"Actual: {error_message_element_text}"

    except Exception as e:
        pytest.fail(f"An error occurred: {str(e)}")
