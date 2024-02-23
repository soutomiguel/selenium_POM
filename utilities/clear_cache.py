from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def delete_all_cookies():
    chrome_options = Options()
    chrome_options.add_argument("--disable-cache")
    driver = webdriver.Chrome(options=chrome_options)
    driver.delete_all_cookies()
