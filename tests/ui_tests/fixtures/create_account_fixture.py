import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def create_account_with_params(firstname, lastname, email, password):
    @pytest.fixture(scope="module")
    def create_account(browser):
        try:
            browser.get("https://www.hudl.com/")
            browser.find_element(By.XPATH, "//a[@data-qa-id='login-select']").click()
            browser.find_element(By.XPATH, "//a[@data-qa-id='login-hudl']").click()
            browser.find_element(By.ID, "nav-btn-page").click()

            fname_field = browser.find_element(By.ID, "first-name")
            lname_field = browser.find_element(By.ID, "last-name")
            email_field = browser.find_element(By.ID, "email-signup")
            passwd_field = browser.find_element(By.ID, "password-signup")
            confpasswd_field = browser.find_element(By.ID, "password-confirm")
            create_account_button = browser.find_element(By.ID, "btn-signup")

            fname_field.send_keys(firstname)
            lname_field.send_keys(lastname)
            email_field.send_keys(email)
            passwd_field.send_keys(password)
            confpasswd_field.send_keys(password)

            create_account_button.click()

            yield browser

        except Exception as e:
            pytest.fail(f"An error occurred during login: {str(e)}")

    return create_account
