import allure
import time
from Locators import Locators
from constants import OPTIONS, URLS
from page_object import PageObject

class Tests:
    @allure.title("Проверка скрытого текста в Option_1")
    def test_1(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            page = PageObject(set_up_browser)
            page.open_main_page(URLS.MAIN)

        with allure.step("Нажимаем на кнопку подтвердить куки"):
            page.approve_cookie()

        with allure.step("Прокрутка страницы"):
            page.scroll_page(5000)

        with allure.step("Нажатие кнопки и проверка скрытого текста"):
            page.click_button_and_verify_hidden_text(Locators.button1_xpath,
                                                     Locators.hidden_text1_xpath,
                                                     OPTIONS.Option_1)

    @allure.title("Проверка скрытого текста в Option_2")
    def test_2(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            page = PageObject(set_up_browser)
            page.open_main_page(URLS.MAIN)

        with allure.step("Прокрутка страницы"):
            page.scroll_page(5000)

        with allure.step("Нажатие кнопки и проверка скрытого текста"):
            page.click_button_and_verify_hidden_text(Locators.button2_xpath,
                                                     Locators.hidden_text2_xpath,
                                                     OPTIONS.Option_2)

    @allure.title("Проверка скрытого текста в Option_3")
    def test_3(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            page = PageObject(set_up_browser)
            page.open_main_page(URLS.MAIN)

        with allure.step("Прокрутка страницы"):
            page.scroll_page(5000)

        with allure.step("Нажатие кнопки и проверка скрытого текста"):
            page.click_button_and_verify_hidden_text(Locators.button3_xpath,
                                                     Locators.hidden_text3_xpath,
                                                     OPTIONS.Option_3)

    @allure.title("Проверка скрытого текста в Option_4")
    def test_4(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            page = PageObject(set_up_browser)
            page.open_main_page(URLS.MAIN)

        with allure.step("Прокрутка страницы"):
            page.scroll_page(5000)

        with allure.step("Нажатие кнопки и проверка скрытого текста"):
            page.click_button_and_verify_hidden_text(Locators.button4_xpath,
                                                     Locators.hidden_text4_xpath,
                                                     OPTIONS.Option_4)

    @allure.title("Проверка скрытого текста в Option_5")
    def test_5(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            page = PageObject(set_up_browser)
            page.open_main_page(URLS.MAIN)

        with allure.step("Прокрутка страницы"):
            page.scroll_page(5000)

        with allure.step("Нажатие кнопки и проверка скрытого текста"):
            page.click_button_and_verify_hidden_text(Locators.button5_xpath,
                                                     Locators.hidden_text5_xpath,
                                                     OPTIONS.Option_5)

    @allure.title("Проверка скрытого текста в Option_6")
    def test_6(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            page = PageObject(set_up_browser)
            page.open_main_page(URLS.MAIN)

        with allure.step("Прокрутка страницы"):
            page.scroll_page(6000)

        with allure.step("Нажатие кнопки и проверка скрытого текста"):
            page.click_button_and_verify_hidden_text(Locators.button6_xpath,
                                                     Locators.hidden_text6_xpath,
                                                     OPTIONS.Option_6)

    @allure.title("Проверка скрытого текста в Option_7")
    def test_7(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            page = PageObject(set_up_browser)
            page.open_main_page(URLS.MAIN)

        with allure.step("Прокрутка страницы"):
            page.scroll_page(7000)

        with allure.step("Нажатие кнопки и проверка скрытого текста"):
            page.click_button_and_verify_hidden_text(Locators.button7_xpath,
                                                     Locators.hidden_text7_xpath,
                                                     OPTIONS.Option_7)

    @allure.title("Проверка скрытого текста в Option_8")
    def test_8(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            page = PageObject(set_up_browser)
            page.open_main_page(URLS.MAIN)

        with allure.step("Прокрутка страницы"):
            page.scroll_page(7000)

        with allure.step("Нажатие кнопки и проверка скрытого текста"):
            page.click_button_and_verify_hidden_text(Locators.button8_xpath,
                                                     Locators.hidden_text8_xpath,
                                                     OPTIONS.Option_8)