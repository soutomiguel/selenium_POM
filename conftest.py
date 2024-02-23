import pytest
from selenium import webdriver
from utilities import read_configs


def setup():
    browser = read_configs.read_configurations("DEFAULT", "browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("Provide a valid browser (Chrome or firefox)")
    url = read_configs.read_configurations("DEFAULT", "url")
    driver.maximize_window()
    driver.get(url)
