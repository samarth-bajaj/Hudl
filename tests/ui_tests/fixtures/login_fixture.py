import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login_with_params(username, password):
    @pytest.fixture(scope="module")
    def login(browser):
        try:
            browser.get("https://www.hudl.com/")
            browser.find_element(By.XPATH, "//a[@data-qa-id='login-select']").click()
            browser.find_element(By.XPATH, "//a[@data-qa-id='login-hudl']").click()

            username_field = browser.find_element(By.ID, "email")
            password_field = browser.find_element(By.ID, "password")
            login_button = browser.find_element(By.ID, "logIn")

            username_field.send_keys(username)
            password_field.send_keys(password)

            login_button.click()

            yield browser

        except Exception as e:
            pytest.fail(f"An error occurred during login: {str(e)}")

    return login
