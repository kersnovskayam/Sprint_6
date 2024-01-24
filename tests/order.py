from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from tests.constants import URLS


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(URLS.MAIN)

    def get_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Заказать']")

    def click_button(self):
        button = self.get_button()
        button.click()

    def wait_for_modal(self):
        modal = self.driver.find_element(By.XPATH, "modal")
        WebDriverWait(self.driver, 10).until(EC.visibility_of(modal))

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://example.com/form")

    def get_input(self, input_id):
        return self.driver.find_element(By.XPATH, input_id)

    def fill_text_input(self, input_xpath, text):
        input_element = self.get_input(input_xpath)
        input_element.send_keys(text)

    def get_dropdown(self):
        return Select(self.driver.find_element(By.ID, dropdown_xpath))

    def select_dropdown_value(self, value):
        dropdown = self.get_dropdown()
        dropdown.select_by_visible_text(value)

    def get_date_input(self):
        return self.driver.find_element(By.XPATH, date_xpath)

    def fill_date_input(self, date):
        date_input = self.get_date_input()
        date_input.send_keys(date)

    def get_checkbox(self):
        return self.driver.find_element(By.XPATH, checkbox_xpath)

    def click_checkbox(self):
        checkbox = self.get_checkbox()
        checkbox.click()

    def get_input(self):
        return self.driver.find_element(By.XPATH, )

    def fill_get_input(self, text):
        get_input = self.get_input()
        get_input.send_keys(text)

    def get_order_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Заказать']")

    def click_order_button(self):
        order_button = self.get_order_button()
        order_button.click()

    def wait_for_success_modal(self):
        success_modal = self.driver.find_element(By.XPATH, success_modal)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(success_modal))

    def close_modal(self):
        modal_close_button = self.driver.find_element(By.XPATH, "//button[text()='Да']")
        modal_close_button.click()

# Пример использования
driver = webdriver.Firefox()
main_page = MainPage(driver)
main_page.open()
main_page.click_button()

form_page = FormPage(driver)
form_page.open()
form_page.fill_text_input(name, "Текст1")
form_page.fill_text_input(surname, "Текст2")
form_page.fill_text_input(adress, "Текст3")
form_page.fill_text_input(phone, "89671111111")
form_page.select_dropdown_value("Option 1")
form_page.click_order_button()

# Проверка модального окна об успешном заказе
form_page.wait_for_success_modal()
form_page.close_modal()

