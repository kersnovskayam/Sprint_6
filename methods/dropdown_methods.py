from methods.base_app import BasePage
from allure_decorator import allure_step_decorator
from locators.page_locators import LogoLocators


class DropdownMethods(BasePage):
    @allure_step_decorator("Открываем страницу Яндекс Самокат учебный тренажер")
    def open_main_page(self, url):
        self.get_page(url)

    @allure_step_decorator("Нажимаем на кнопку подтвердить куки")
    def approve_cookie(self):
        button = self.find_element('xpath', LogoLocators.button_approve_cookie)
        assert button is not None
        self.click_on_element(button)

    @allure_step_decorator("Производим прокрутку страницы вниз")
    def scroll_page(self, pixels):
        self.execute_script(f"window.scrollTo(0, {pixels})")

    @allure_step_decorator("Нажимаем на кнопку раскрытия скрытого текста в вопросе")
    def click_button_and_verify_hidden_text(self, button_xpath, hidden_text_xpath, expected_text):
        button = self.check_visibility_of_element_located('xpath', button_xpath)
        self.click_on_element(button)
        hidden_text = self.check_visibility_of_element_located('xpath', hidden_text_xpath)
        assert hidden_text.is_displayed() is True
        assert hidden_text.text == expected_text