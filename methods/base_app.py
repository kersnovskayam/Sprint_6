from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def get_page(self, url):
        return self.driver.get(url)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def check_element_to_be_clickable(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))

    def check_visibility_of_element_located(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        self.driver.main_window_handle = self.driver.current_window_handle
        new_window_handle = [h for h in self.driver.window_handles if h != self.driver.main_window_handle][0]
        self.driver.switch_to.window(new_window_handle)

    @staticmethod
    def click_on_element(element):
        element.click()

    @staticmethod
    def enter_text(element, text):
        element.send_keys(text)