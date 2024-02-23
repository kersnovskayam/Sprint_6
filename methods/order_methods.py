from locators.page_locators import LogoLocators
from methods.base_app import BasePage
from allure_decorator import allure_step_decorator
from locators.order_locators import OrderLocators


class OrderMethods(BasePage):

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

    @allure_step_decorator("Находим поле ввода 'Имя' и вводим значение из тестового набора данных")
    def enter_order_name(self, name):
        element = self.find_element('xpath', OrderLocators.order_name)
        assert "* Имя" in element.get_attribute("placeholder")
        self.enter_text(element, name)

    @allure_step_decorator("Находим поле ввода 'Фамилия' и вводим значение из тестового набора данных")
    def enter_order_surname(self, surname):
        element = self.find_element('xpath', OrderLocators.order_surname)
        assert "* Фамилия" in element.get_attribute("placeholder")
        self.enter_text(element, surname)

    @allure_step_decorator("Находим поле ввода 'Адрес' и вводим значение из тестового набора данных")
    def enter_order_address(self, address):
        element = self.find_element('xpath', OrderLocators.order_address)
        assert "* Адрес: куда привезти заказ" in element.get_attribute("placeholder")
        self.enter_text(element, address)

    @allure_step_decorator("Находим поле ввода 'Метро' вводим и бывираем значение из тестового набора данных")
    def enter_order_metro(self, metro):
        element = self.find_element('xpath', OrderLocators.order_metro)
        assert "* Станция метро" in element.get_attribute("placeholder")
        self.enter_text(element, metro)
        button = self.check_element_to_be_clickable('xpath', OrderLocators.select_metro)
        self.click_on_element(button)

    @allure_step_decorator("Находим поле ввода 'Метро' вводим и бывираем значение из тестового набора данных")
    def enter_order_metro2(self, metro):
        element = self.find_element('xpath', OrderLocators.order_metro)
        assert "* Станция метро" in element.get_attribute("placeholder")
        self.enter_text(element, metro)
        button = self.check_element_to_be_clickable('xpath', OrderLocators.select_metro2)
        assert button is not None
        self.click_on_element(button)

    @allure_step_decorator("Находим поле ввода 'Номер телефона' и вводим значение из тестового набора данных")
    def enter_order_phone(self, phone):
        element = self.find_element('xpath', OrderLocators.order_phone)
        assert "* Телефон: на него позвонит курьер" in element.get_attribute("placeholder")
        self.enter_text(element, phone)

    @allure_step_decorator("Находим поле ввода '* Когда привезти самокат' и вводим значение из тестового набора данных")
    def enter_order_date(self, date):
        element = self.find_element('xpath', OrderLocators.order_date)
        assert "* Когда привезти самокат" in element.get_attribute("placeholder")
        self.enter_text(element, date)

    @allure_step_decorator("Находим поле '* Срок аренды' и нажимаем на '1 день'")
    def dropdown_date(self):
        button = self.check_element_to_be_clickable('xpath', OrderLocators.order_dropdown_date)
        self.click_on_element(button)
        assert button is not None
        button = self.check_element_to_be_clickable('xpath', OrderLocators.select_dropdown_date)
        assert button is not None
        self.click_on_element(button)

    @allure_step_decorator("Выбираем цвет самоката 'черный жемчуг'/'серая безысходность' ")
    def choose_color_of_scooter(self, locator):
        button = self.check_element_to_be_clickable('xpath', locator)
        assert button is not None
        self.click_on_element(button)

    @allure_step_decorator("Находим поле ввода 'комментарий' и вводим значение из тестового набора данных")
    def enter_comment_courier(self, comment):
        element = self.find_element('xpath', OrderLocators.order_comment_courier)
        assert "Комментарий для курьера" in element.get_attribute("placeholder")
        self.enter_text(element, comment)

    @allure_step_decorator("Нажимаем на кнопку 'Заказать'")
    def click_order_button(self):
        button = self.check_element_to_be_clickable('xpath', OrderLocators.button_order_xpath1)
        assert button is not None
        self.click_on_element(button)

    @allure_step_decorator("Нажатие на кнопку 'Заказать' ")
    def click_order_button2(self):
        button = self.check_element_to_be_clickable('xpath', OrderLocators.button_order_xpath2)
        assert button is not None
        self.click_on_element(button)

    @allure_step_decorator("Нажатие на кнопку 'Далее'")
    def click_button_next(self):
        button = self.check_element_to_be_clickable('xpath', OrderLocators.order_button_next)
        assert button is not None
        self.click_on_element(button)

    @allure_step_decorator("Нажатие на кнопку 'Да'")
    def click_button_approve(self):
        button = self.check_element_to_be_clickable('xpath', OrderLocators.order_button_approve)
        assert button is not None
        self.click_on_element(button)

    @allure_step_decorator("Нажатие на кнопку 'Посмотреть статус'")
    def click_button_check_status(self):
        button = self.check_element_to_be_clickable('xpath', OrderLocators.order_button_check_status)
        assert button is not None
        self.click_on_element(button)