import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from fixtures.conftest import browser
from fixtures.login_fixture import login_with_params
from fixtures.element_fixtures import is_visible, is_clickable, is_present
from fixtures.wait_fixture import create_wait

from testdata.credentials import EMAIL, PASSWORD

custom_login = login_with_params(EMAIL, PASSWORD)


# Testing the logout functionality of the website
@pytest.mark.usefixtures("browser", "custom_login")
def test_logout_functionality(browser, is_visible, is_clickable, is_present, create_wait):
    try:
        wait = create_wait
        profile_area = wait.until(is_visible(By.XPATH, "//div[@class='hui-globaluseritem__display-name']"))
        actions = ActionChains(browser)
        actions.move_to_element(profile_area).perform()

        logout_button = wait.until(
            is_clickable(By.XPATH, "//div[@class='hui-globalusermenu']//a[@data-qa-id='webnav-usermenu-logout']")
        )

        logout_button.click()

        login_button = wait.until(is_present(By.XPATH, "//a[@data-qa-id='login-select']"))

        # This assert checks if the login button is displayed after logging out, which indicates a successful logout.
        assert login_button.is_displayed(), "Logout test failed. User is not redirected to the login page."

    except Exception as e:
        pytest.fail(f"An error occurred: {str(e)}")
