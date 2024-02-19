import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def set_up_browser():
    options = Options()
    options.headless = False
    driver = webdriver.Firefox()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()
