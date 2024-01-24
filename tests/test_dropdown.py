from selenium.webdriver.common.by import By
from tests.constants import OPTIONS, URLS

from tests import Locators

class Tests():
    def test_4(self, set_up_browser):
        driver = set_up_browser

        driver.get(URLS.MAIN)
        driver.execute_script("window.scrollTo(0, 1980)")
        button = driver.find_element(By.XPATH, Locators.Locators.button1_xpath)
        button.click()
        hidden_text = driver.find_element(By.XPATH, Locators.Locators.hidden_text1_xpath)
        assert hidden_text.is_displayed() is True
        assert hidden_text.text == OPTIONS.Option_1

    def test_2(self, set_up_browser):
        driver = set_up_browser

        driver.get(URLS.MAIN)
        driver.execute_script("window.scrollTo(0, 1980)")
        button = driver.find_element(By.XPATH, Locators.Locators.button2_xpath)
        button.click()
        hidden_text = driver.find_element(By.XPATH, Locators.Locators.hidden_text2_xpath)
        assert hidden_text.is_displayed() is True
        assert hidden_text.text == OPTIONS.Option_2

    def test_3(self, set_up_browser):
        driver = set_up_browser

        driver.get(URLS.MAIN)
        driver.execute_script("window.scrollTo(0, 1980)")
        button = driver.find_element(By.XPATH, Locators.Locators.button3_xpath)
        button.click()
        hidden_text = driver.find_element(By.XPATH, Locators.Locators.hidden_text3_xpath)
        assert hidden_text.is_displayed() is True
        assert hidden_text.text == OPTIONS.Option_3

    def test_4(self, set_up_browser):
        driver = set_up_browser

        driver.get(URLS.MAIN)
        driver.execute_script("window.scrollTo(0, 1980)")
        button = driver.find_element(By.XPATH, Locators.Locators.button4_xpath)
        button.click()
        hidden_text = driver.find_element(By.XPATH, Locators.Locators.hidden_text4_xpath)
        assert hidden_text.is_displayed() is True
        assert hidden_text.text == OPTIONS.Option_4

    def test_5(self, set_up_browser):
        driver = set_up_browser

        driver.get(URLS.MAIN)
        driver.execute_script("window.scrollTo(0, 1980)")
        button = driver.find_element(By.XPATH, Locators.Locators.button5_xpath)
        button.click()
        hidden_text = driver.find_element(By.XPATH, Locators.Locators.hidden_text5_xpath)
        assert hidden_text.is_displayed() is True
        assert hidden_text.text == OPTIONS.Option_5

    def test_6(self, set_up_browser):
        driver = set_up_browser

        driver.get(URLS.MAIN)
        driver.execute_script("window.scrollTo(0, 1980)")
        button = driver.find_element(By.XPATH, Locators.Locators.button6_xpath)
        button.click()
        hidden_text = driver.find_element(By.XPATH, Locators.Locators.hidden_text6_xpath)
        assert hidden_text.is_displayed() is True
        assert hidden_text.text == OPTIONS.Option_6


    def test_7(self, set_up_browser):
        driver = set_up_browser

        driver.get(URLS.MAIN)
        driver.execute_script("window.scrollTo(0, 1980)")
        button = driver.find_element(By.XPATH, Locators.Locators.button7_xpath)
        button.click()
        hidden_text = driver.find_element(By.XPATH, Locators.Locators.hidden_text7_xpath)
        assert hidden_text.is_displayed() is True
        assert hidden_text.text == OPTIONS.Option_7