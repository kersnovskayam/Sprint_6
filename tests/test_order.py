import allure
from constants import URLS, DATA1, DATA2
from page_object import PageObject


class Test:
    @allure.title("Выполнение оформления заказа по нажатию кнопки 'Заказать' ")
    def test1(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            page = PageObject(set_up_browser)
            page.open_main_page(URLS.MAIN)
        with allure.step("Нажимаем на кнопку подтвердить куки"):
            page.approve_cookie()
        with allure.step("Нажатие на кнопку 'Заказать' "):
            page.order_button()
        with allure.step("Ввод имени из первого набора данных"):
            page.enter_order_name(DATA1.name)
        with allure.step("Ввод фамилии из первого набора данных"):
            page.enter_order_surname(DATA1.surname)
        with allure.step("Ввод адреса из первого набора данных"):
            page.enter_order_address(DATA1.address)
        with allure.step("Ввод метро из первого набора данных"):
            page.enter_order_metro(DATA1.metro)
        with allure.step("Ввод номера телефона из первого набора данных"):
            page.enter_order_phone(DATA1.phone)
        with allure.step("Нажатие на кнопку 'Далее'"):
            page.button_next()
        with allure.step("Ввод даты заказа из первого набора данных"):
            page.enter_order_date(DATA1.date)
        with allure.step("Выбор срока аренды самоката"):
            page.dropdown_date()
        with allure.step("Выбор цвета самоката"):
            page.color_grey_scooter()
        with allure.step("Ввод комментария из первого набора данных"):
            page.enter_comment_courier(DATA1.comment)
        with allure.step("Нажатие на кнопку 'Заказать' "):
            page.button_next()
        with allure.step("Нажатие на кнопку 'Да'"):
            page.button_approve()
        with allure.step("Нажатие на кнопку 'Посмотреть статус'"):
            page.button_check_status()

    @allure.title("Выполнение оформления заказа по нажатию кнопки 'Заказать' в середине главной страницы ")
    def test2(self, set_up_browser):
        with allure.step("Открытие основной страницы"):
            page = PageObject(set_up_browser)
            page.open_main_page(URLS.MAIN)
        with allure.step("Прокрутка страницы до кнопки 'Заказать'"):
            page.scroll_page(1980)
        with allure.step("Нажатие на кнопку 'Заказать' "):
            page.order_button2()
        with allure.step("Ввод имени из второго набора данных"):
            page.enter_order_name(DATA2.name)
        with allure.step("Ввод фамилии из второго набора данных"):
            page.enter_order_surname(DATA2.surname)
        with allure.step("Ввод адреса из второго набора данных"):
            page.enter_order_address(DATA2.address)
        with allure.step("Ввод метро из второго набора данных"):
            page.enter_order_metro(DATA2.metro)
        with allure.step("Ввод номера телефона из второго набора данных"):
            page.enter_order_phone(DATA2.phone)
        with allure.step("Нажатие на кнопку 'Далее'"):
            page.button_next()
        with allure.step("Ввод даты заказа из второго набора данных"):
            page.enter_order_date(DATA2.date)
        with allure.step("Выбор срока аренды самоката"):
            page.dropdown_date()
        with allure.step("Выбор цвета самоката"):
            page.color_black_scooter()
        with allure.step("Ввод комментария из второго набора данных"):
            page.enter_comment_courier(DATA2.comment)
        with allure.step("Нажатие на кнопку 'Заказать' "):
            page.button_next()
        with allure.step("Нажатие на кнопку 'Да'"):
            page.button_approve()
        with allure.step("Нажатие на кнопку 'Посмотреть статус'"):
            page.button_check_status()