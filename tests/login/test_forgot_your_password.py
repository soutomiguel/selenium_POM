from selenium import webdriver

from pages.base_page import BasePage
from pages.forgot_your_password_page import ForgotYourPassword
from utilities.clear_cache import delete_all_cookies


class TestForgotYourPassword:
    def setup_method(self):
        delete_all_cookies()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_populate_using_valid_email(self):
        forgot_your_password = ForgotYourPassword(self.driver)
        forgot_your_password.click_on_forgot_your_password_button()
