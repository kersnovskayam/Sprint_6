from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import Locators


class PageObject:

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self, url):
        self.driver.get(url)

    def approve_cookie(self):
        button = self.driver.find_element(By.XPATH, Locators.button_approve_cookie)
        button.click()

    def scroll_page(self, pixels):
        self.driver.execute_script(f"window.scrollTo(0, {pixels})")

    def click_button_and_verify_hidden_text(self, button_xpath, hidden_text_xpath, expected_text):
        button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, button_xpath)))
        button.click()
        hidden_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, hidden_text_xpath)))
        assert hidden_text.text == expected_text

    def enter_order_name(self, name):
        self.driver.find_element(By.XPATH, Locators.order_name).send_keys(name)

    def enter_order_surname(self, surname):
        self.driver.find_element(By.XPATH, Locators.order_surname).send_keys(surname)

    def enter_order_address(self, address):
        self.driver.find_element(By.XPATH, Locators.order_address).send_keys(address)

    def enter_order_metro(self, metro):
        self.driver.find_element(By.XPATH, Locators.order_metro).send_keys(metro)
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.select_metro))
        )
        button.click()

    def enter_order_phone(self, phone):
        self.driver.find_element(By.XPATH, Locators.order_phone).send_keys(phone)

    def enter_order_date(self, date):
        self.driver.find_element(By.XPATH, Locators.order_date).send_keys(date)

    def enter_comment_courier(self, comment):
        self.driver.find_element(By.XPATH, Locators.comment_courier).send_keys(comment)

    def order_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.order_xpath1))
        )
        button.click()

    def order_button2(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.order_xpath2))
        )
        button.click()

    def button_next(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.button_next))
        )
        button.click()

    def dropdown_date(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.dropdown_date))
        )
        button.click()
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.dropdown_date_select))
        )
        button.click()

    def color_black_scooter(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.color_black_scooter))
        )
        button.click()

    def color_grey_scooter(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.color_grey_scooter))
        )
        button.click()

    def button_approve_order(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.button_approve))
        )
        button.click()

    def button_approve(self):
        button_approve = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.button_approve))
        )
        button_approve.click()

    def button_check_status(self):
        button_check_status = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.button_check_status))
        )
        button_check_status.click()

    def click_scooter_button(self):
        button = self.driver.find_element(By.XPATH, Locators.button_scooter)
        button.click()

    def assert_current_url(self, expected_url):
        assert self.driver.current_url == expected_url

    def click_dzen_button(self):
        button = self.driver.find_element(By.XPATH, Locators.button_dzen)
        button.click()

    def switch_to_new_tab(self):
        self.main_window_handle = self.driver.current_window_handle
        new_window_handle = [h for h in self.driver.window_handles if h != self.main_window_handle][0]
        self.driver.switch_to.window(new_window_handle)