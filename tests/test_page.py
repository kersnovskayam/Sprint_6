import allure
from constants import URLS
from methods.page_methods import PageMethods


class Test:

    @allure.title("Проверка работы нажатия кнопки 'Самокат'")
    def test_check_scooter_url(self, browser):
        test_page = PageMethods(browser)
        test_page.open_main_page(URLS.MAIN)
        test_page.click_order_button()
        test_page.click_scooter_button()
        test_page.assert_current_url(URLS.MAIN)

    @allure.title("Проверка работы нажатия кнопки 'Яндекс'")
    def test_check_yandex_url(self, browser):
        test_page = PageMethods(browser)
        test_page.open_main_page(URLS.MAIN)
        test_page.click_dzen_button()
        test_page.check_new_tab()
