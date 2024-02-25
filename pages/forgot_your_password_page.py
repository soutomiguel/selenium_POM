from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.signin_page import SigninPage
from utilities.test_data import TestData


class ForgotYourPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.URL)

        global base_page
        base_page = BasePage(self.driver)

        self.click_on_back_button = (By.XPATH, "(//a[@href='#'][contains(.,'< Back')])[1]")
        self.signin_register_button = (By.XPATH, "(//a[@href='#'][contains(.,'Sign In/Register')])[1]")
        self.forgot_your_password_button = (By.XPATH, "(//a[@href='#'][contains(.,'forgot your password?')])[1]")
        self.recover_button_field = (By.XPATH, "(//input[contains(@name,'user[email]')])[2]")
        self.reset_my_password_button = (By.XPATH, "(//input[contains(@type,'submit')])[4]")
        self.toast_after_click_on_recover_password = (By.XPATH, "//div[@class='toast-message']")

    def click_signin_register_button(self):
        base_page.click_on(self.signin_register_button)

    def click_on_forgot_your_password_button(self):
        base_page.click_on(self.forgot_your_password_button)

    def click_on_back(self):
        base_page.click_on(self.click_on_back_button)

    def set_email_for_recovery(self, email):
        base_page.set(self.recover_button_field, email)

    def click_on_reset_my_password(self):
        base_page.click_on(self.reset_my_password_button)

    def get_recover_success_message(self):
        return base_page.get_text(self.toast_after_click_on_recover_password)
