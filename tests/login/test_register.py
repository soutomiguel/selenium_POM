from selenium import webdriver
from utilities.clear_cache import delete_all_cookies


class TestRegister:
    def setup_method(self):
        delete_all_cookies()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_populate_all_data(self):
        pass

