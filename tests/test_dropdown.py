import allure
from constants import OPTIONS, URLS
from locators.dropdown_locators import LocatorsHiddenButton, LocatorsHiddenText
from methods.dropdown_methods import DropdownMethods


class Tests:
    @allure.title("Нажимаем на вопрос 'Сколько это стоит? И как оплатить?' и проверяем что открывается нужный текст")
    def test_check_hidden_question_text_1(self, browser):
        with allure.step("Открываем страницу и проверяем отображение скрытого текста"):
            page = DropdownMethods(browser)
            page.open_main_page(URLS.MAIN)
            page.approve_cookie()
            page.scroll_page(5000)
            page.click_button_and_verify_hidden_text(LocatorsHiddenButton.faq_hidden_question1_xpath,
                                                     LocatorsHiddenText.faq_hidden_text1_xpath,
                                                     OPTIONS.ANSWER_DESCRIPTION_1)

    @allure.title("Нажимаем на вопрос 'Можно ли заказать самокат прямо на сегодня?' и проверяем что открывается нужный текст")
    def test_check_hidden_question_text_2(self, browser):
        page = DropdownMethods(browser)
        page.open_main_page(URLS.MAIN)
        page.approve_cookie()
        page.scroll_page(5000)
        page.click_button_and_verify_hidden_text(LocatorsHiddenButton.faq_hidden_question2_xpath,
                                                 LocatorsHiddenText.faq_hidden_text2_xpath,
                                                 OPTIONS.ANSWER_DESCRIPTION_2)

    @allure.title("Нажимаем на вопрос 'Хочу сразу несколько самокатов! Так можно?' и проверяем что открывается нужный текст")
    def test_check_hidden_question_text_3(self, browser):
        page = DropdownMethods(browser)
        page.open_main_page(URLS.MAIN)
        page.approve_cookie()
        page.scroll_page(5000)
        page.click_button_and_verify_hidden_text(LocatorsHiddenButton.faq_hidden_question3_xpath,
                                                 LocatorsHiddenText.faq_hidden_text3_xpath,
                                                 OPTIONS.ANSWER_DESCRIPTION_3)


    @allure.title("Нажимаем на вопрос 'Как рассчитывается время аренды?' и проверяем что открывается нужный текст")
    def test_check_hidden_question_text_4(self, browser):
        page = DropdownMethods(browser)
        page.open_main_page(URLS.MAIN)
        page.approve_cookie()
        page.scroll_page(5000)
        page.click_button_and_verify_hidden_text(LocatorsHiddenButton.faq_hidden_question4_xpath,
                                                 LocatorsHiddenText.faq_hidden_text4_xpath,
                                                 OPTIONS.ANSWER_DESCRIPTION_4)

    @allure.title("Нажимаем на вопрос 'Можно ли продлить заказ или вернуть самокат раньше?' и проверяем что открывается нужный текст")
    def test_check_hidden_question_text_5(self, browser):
        page = DropdownMethods(browser)
        page.open_main_page(URLS.MAIN)
        page.approve_cookie()
        page.scroll_page(5000)
        page.click_button_and_verify_hidden_text(LocatorsHiddenButton.faq_hidden_question5_xpath,
                                                 LocatorsHiddenText.faq_hidden_text5_xpath,
                                                 OPTIONS.ANSWER_DESCRIPTION_5)


    @allure.title("Нажимаем на вопрос 'Вы привозите зарядку вместе с самокатом?' и проверяем что открывается нужный текст")
    def test_check_hidden_question_text_6(self, browser):
        page = DropdownMethods(browser)
        page.open_main_page(URLS.MAIN)
        page.approve_cookie()
        page.scroll_page(5000)
        page.click_button_and_verify_hidden_text(LocatorsHiddenButton.faq_hidden_question6_xpath,
                                                 LocatorsHiddenText.faq_hidden_text6_xpath,
                                                 OPTIONS.ANSWER_DESCRIPTION_6)


    @allure.title("Нажимаем на вопрос 'Можно ли отменить заказ?' и проверяем что открывается нужный текст")
    def test_check_hidden_question_text_7(self, browser):
        page = DropdownMethods(browser)
        page.open_main_page(URLS.MAIN)
        page.approve_cookie()
        page.scroll_page(5000)
        page.click_button_and_verify_hidden_text(LocatorsHiddenButton.faq_hidden_question7_xpath,
                                                 LocatorsHiddenText.faq_hidden_text7_xpath,
                                                 OPTIONS.ANSWER_DESCRIPTION_7)


    @allure.title("Нажимаем на вопрос 'Я жизу за МКАДом, привезёте?' и проверяем что открывается нужный текст")
    def test_check_hidden_question_text_8(self, browser):
        page = DropdownMethods(browser)
        page.open_main_page(URLS.MAIN)
        page.approve_cookie()
        page.scroll_page(6000)
        page.click_button_and_verify_hidden_text(LocatorsHiddenButton.faq_hidden_question8_xpath,
                                                 LocatorsHiddenText.faq_hidden_text8_xpath,
                                                 OPTIONS.ANSWER_DESCRIPTION_8)