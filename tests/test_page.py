import allure

from constants import URLS
from page_object import PageObject


class Test:

    @allure.title("Проверка работы нажатии кнопки 'Самокат'")
    def test_1(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            test_page = PageObject(set_up_browser)
            test_page.open_main_page(URLS.MAIN)
        with allure.step("Нажимаем кнопку 'Заказать'"):
            test_page.order_button()
        with allure.step("Нажимаем кнопку 'Самокат'"):
            test_page.click_scooter_button()
        with allure.step("Проверка что открытая страница совпадает с ожидаемой"):
            test_page.assert_current_url(URLS.MAIN)

    @allure.title("Проверка работы нажатии кнопки 'Яндекс'")
    def test_2(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            test_page = PageObject(set_up_browser)
            test_page.open_main_page(URLS.MAIN)
        with allure.step("Нажимаем кнопку 'Яндекс'"):
            test_page.click_dzen_button()
        with allure.step("Проверка что открытая страница совпадает с ожидаемой"):
            test_page.switch_to_new_tab()