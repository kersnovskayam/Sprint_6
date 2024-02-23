import allure

from constants import URLS
from locators.order_locators import OrderLocators
from methods.order_methods import OrderMethods
from test_data import PersonalDataUserOne, PersonalDataUserTwo


class Test:
    @allure.title("Выполнение оформления заказа по нажатию кнопки 'Заказать' ")
    def test_order_form_top(self, browser):
        page = OrderMethods(browser)
        page.open_main_page(URLS.MAIN)
        page.approve_cookie()
        page.click_order_button()
        page.enter_order_name(PersonalDataUserOne.NAME)
        page.enter_order_surname(PersonalDataUserOne.SURNAME)
        page.enter_order_address(PersonalDataUserOne.ADDRESS)
        page.enter_order_metro(PersonalDataUserOne.METRO)
        page.enter_order_phone(PersonalDataUserOne.PHONE)
        page.click_button_next()
        page.enter_order_date(PersonalDataUserOne.DATE)
        page.dropdown_date()
        page.choose_color_of_scooter(OrderLocators.order_color_grey_scooter)
        page.enter_comment_courier(PersonalDataUserOne.COMMENT)
        page.click_button_next()
        page.click_button_approve()
        page.click_button_check_status()

    @allure.title("Выполнение оформления заказа по нажатию кнопки 'Заказать' в середине главной страницы ")
    def test_order_form_down(self, browser):
        page = OrderMethods(browser)
        page.open_main_page(URLS.MAIN)
        page.approve_cookie()
        page.scroll_page(1980)
        page.click_order_button2()
        page.enter_order_name(PersonalDataUserTwo.NAME)
        page.enter_order_surname(PersonalDataUserTwo.SURNAME)
        page.enter_order_address(PersonalDataUserTwo.ADDRESS)
        page.enter_order_metro2(PersonalDataUserTwo.METRO)
        page.enter_order_phone(PersonalDataUserTwo.PHONE)
        page.click_button_next()
        page.enter_order_date(PersonalDataUserTwo.DATE)
        page.dropdown_date()
        page.choose_color_of_scooter(OrderLocators.order_color_black_scooter)
        page.enter_comment_courier(PersonalDataUserTwo.COMMENT)
        page.click_button_next()
        page.click_button_approve()
        page.click_button_check_status()