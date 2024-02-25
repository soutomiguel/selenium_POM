from selenium import webdriver
from pages.forgot_your_password_page import ForgotYourPasswordPage
from utilities.clear_cache import delete_all_cookies
from utilities.test_data import TestData


class TestForgotYourPassword:
    def setup_method(self):
        delete_all_cookies()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_recover_password(self):
        forgot_you_password_page = ForgotYourPasswordPage(self.driver)
        # signin_page.close_popup()
        forgot_you_password_page.click_signin_register_button()
        forgot_you_password_page.click_on_forgot_your_password_button()
        forgot_you_password_page.set_email_for_recovery(TestData.EMAIL)
        forgot_you_password_page.click_on_reset_my_password()
        assert (
                forgot_you_password_page.get_recover_success_message() == TestData.SUCCESS_MESSAGES[1]
        )

