import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from fixtures.conftest import browser
from fixtures.login_fixture import login_with_params
from fixtures.element_fixtures import is_visible
from fixtures.wait_fixture import create_wait

from testdata.credentials import EMAIL, PASSWORD

custom_login = login_with_params(EMAIL, PASSWORD)


# Testing the basic login functionality of the website to check if a user can login with the correct credentials.
@pytest.mark.usefixtures("browser", "custom_login")
def test_valid_login(browser, is_visible, create_wait):
    try:
        browser.maximize_window()
        wait = create_wait
        profile_area = wait.until(is_visible(By.XPATH, "//div[@class='hui-globaluseritem__display-name']"))
        actions = ActionChains(browser)
        actions.move_to_element(profile_area).perform()

        email_element = wait.until(is_visible(By.XPATH, "//div[@class='hui-globaluseritem__email']"))

        email_check = email_element.text

        # This assertion checks the email in the top right corner after hovering over the user's name and compares it to
        # the login email used.
        assert email_check == EMAIL, "Valid login test failed."

    except Exception as e:
        pytest.fail(f"An error occurred: {str(e)}")
