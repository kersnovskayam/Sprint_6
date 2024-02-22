import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    options = Options()
    options.headless = False
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
