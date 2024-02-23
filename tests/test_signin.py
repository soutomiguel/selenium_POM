from time import sleep
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

    def test_valid_credentials(self):
        login_page = SigninPage(self.driver)
        # login_page.close_popup()
        login_page.click_signin_register_button()
        login_page.set_email_address(TestData.EMAIL)
        login_page.set_passwd(TestData.PASSWORD)
        login_page.click_on_login()
        assert login_page.get_login_success_text() == "Signed in successfully."
