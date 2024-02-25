from selenium import webdriver
from pages.signin_page import SigninPage
from utilities.test_data import TestData
from utilities.clear_cache import delete_all_cookies


class TestLogin:

    def setup_method(self):
        delete_all_cookies()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_login_using_valid_credentials(self):
        signin_page = SigninPage(self.driver)
        # signin_page.close_popup()
        signin_page.click_signin_register_button()
        signin_page.set_email_address(TestData.EMAIL)
        signin_page.set_passwd(TestData.PASSWORD)
        signin_page.click_on_login()
        assert (
                signin_page.get_login_success_text() == TestData.SUCCESS_MESSAGES[0]
        )

    def test_login_using_invalid_email_format(self):
        signin_page = SigninPage(self.driver)
        # signin_page.close_popup()
        signin_page.click_signin_register_button()
        signin_page.set_passwd(TestData.PASSWORD)
        signin_page.click_on_login()
        assert (
                signin_page.get_login_invalid_credential_format_text() == TestData.ERROR_MESSAGES[0]
        )

    def test_login_using_invalid_password_format(self):
        signin_page = SigninPage(self.driver)
        # signin_page.close_popup()
        signin_page.click_signin_register_button()
        signin_page.set_email_address(TestData.EMAIL)
        signin_page.click_on_login()
        assert (
                signin_page.get_login_invalid_credential_format_text() == TestData.ERROR_MESSAGES[0]
        )
