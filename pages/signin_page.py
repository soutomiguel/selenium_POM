from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.test_data import TestData


class SigninPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.URL)

        global base_page
        base_page = BasePage(self.driver)

        self.signin_register_button = (By.XPATH, "(//a[@href='#'][contains(.,'Sign In/Register')])[1]")
        self.close_popup_button = (By.XPATH, "/html/body/div[22]/div/div[2]/div/div/div/div/div/button/svg/circle")
        self.email_field = (By.XPATH, "(//input[contains(@id,'email')])[1]")
        self.password_field = (By.XPATH, "(//input[contains(@id,'password')])[1]")
        self.login_button = (By.XPATH, "//input[@data-target='sign-in.button']")
        self.login_success_message = (By.XPATH, "//div[@class='toast-message']")
        self.login_invalid_format_credential_error = (By.XPATH, "(//span[contains(.,'Invalid email or password.')])[1]")

    def close_popup(self):
        base_page.click_on(self.close_popup_button)

    def click_signin_register_button(self):
        base_page.click_on(self.signin_register_button)

    def set_email_address(self, email_address):
        base_page.set(self.email_field, email_address)

    def set_passwd(self, password):
        base_page.set(self.password_field, password)

    def click_on_login(self):
        base_page.click_on(self.login_button)

    def click_on_forgot_your_password(self):
        base_page.click_on(self.forgot_your_password_button)

    def get_login_success_text(self):
        return base_page.get_text(self.login_success_message)

    def get_login_invalid_credential_format_text(self):
        return base_page.get_text(self.login_invalid_format_credential_error)
