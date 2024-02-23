from methods.base_app import BasePage
from allure_decorator import allure_step_decorator
from locators.order_locators import OrderLocators
from locators.page_locators import LogoLocators

class PageMethods(BasePage):

    @allure_step_decorator("Открываем страницу Яндекс Самокат учебный тренажер")
    def open_main_page(self, url):
        self.get_page(url)

    @allure_step_decorator("Производим прокрутку страницы вниз")
    def scroll_page(self, pixels):
        self.execute_script(f"window.scrollTo(0, {pixels})")

    @allure_step_decorator("Нажимаем кнопку 'Заказать'")
    def click_order_button(self):
        button = self.check_element_to_be_clickable('xpath', OrderLocators.button_order_xpath1)
        self.click_on_element(button)

    @allure_step_decorator("Нажимаем на кнопку 'Самокат'")
    def click_scooter_button(self):
        button = self.find_element('xpath', LogoLocators.button_scooter)
        assert button is not None
        self.click_on_element(button)

    @allure_step_decorator("Проверка что открытая страница совпадает с ожидаемой")
    def assert_current_url(self, expected_url):
        current_url = self.get_current_url()
        assert current_url == expected_url

    @allure_step_decorator("Нажимаем на кнопку 'Яндекс'")
    def click_dzen_button(self):
        button = self.find_element('xpath', LogoLocators.button_dzen)
        self.click_on_element(button)

    @allure_step_decorator("Производим проверку что открытая новая страница совпадает с ожидаемой")
    def check_new_tab(self):
        self.switch_to_new_window()
