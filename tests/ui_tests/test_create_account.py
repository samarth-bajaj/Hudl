import pytest
import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from fixtures.conftest import browser
from fixtures.create_account_fixture import create_account_with_params
from fixtures.element_fixtures import is_visible
from fixtures.wait_fixture import create_wait

from testdata.credentials import PASSWORD

random_number = random.randint(100, 99999999)
firstname = "FnameTest"
lastname = "LnameTest"
email = f"{firstname}{random_number}@{lastname}.com"
password = PASSWORD
create_custom_account = create_account_with_params(firstname, lastname, email, password)


# Testing the create account functionality with a randomly generated email.
@pytest.mark.usefixtures("browser", "create_custom_account")
def test_create_account(browser, is_visible, create_wait):
    try:
        wait = create_wait

        firstname_check = browser.find_element(By.XPATH, "//span[@class='fanWebnav_displayName__GvEDV']").text
        profile_area = wait.until(is_visible(By.XPATH, "//div[@class='fanWebnav_globalUserItemDisplayName__QgQU2']"))
        actions = ActionChains(browser)
        actions.move_to_element(profile_area).perform()
        email_element = wait.until(is_visible(By.XPATH, "//div[@class='fanWebnav_globalUserItemEmail__w6mTM']"))

        email_check = email_element.text.lower()
        expected_firstname = "FnameTest"
        expected_email = email.lower()

        # Tests to make sure that the first name and the email in the top right corner match the ones used to signup.
        assert firstname_check == expected_firstname, "Firstname does not match."
        assert email_check == expected_email, "Email does not match."

    except Exception as e:
        pytest.fail(f"An error occurred: {str(e)}")
