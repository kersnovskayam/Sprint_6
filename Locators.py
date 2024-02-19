class Locators:
    # Локаторы вкладок
    button1_xpath = '//div[@id="accordion__heading-0"]'
    button2_xpath = '//div[@id="accordion__heading-1"]'
    button3_xpath = '//div[@id="accordion__heading-2"]'
    button4_xpath = '//div[@id="accordion__heading-3"]'
    button5_xpath = '//div[@id="accordion__heading-4"]'
    button6_xpath = '//div[@id="accordion__heading-5"]'
    button7_xpath = '//div[@id="accordion__heading-6"]'
    button8_xpath = '//div[@id="accordion__heading-7"]'

    # локаторы текста
    hidden_text1_xpath = '//div[@id="accordion__panel-0"]'
    hidden_text2_xpath = '//div[@id="accordion__panel-1"]'
    hidden_text3_xpath = '//div[@id="accordion__panel-2"]'
    hidden_text4_xpath = '//div[@id="accordion__panel-3"]'
    hidden_text5_xpath = '//div[@id="accordion__panel-4"]'
    hidden_text6_xpath = '//div[@id="accordion__panel-5"]'
    hidden_text7_xpath = '//div[@id="accordion__panel-6"]'
    hidden_text8_xpath = '//div[@id="accordion__panel-7"]'

    # Локаторы кнопок заказать
    order_xpath1 = '//button[@class="Button_Button__ra12g"]'
    order_xpath2 = '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'

    # локаторы форм нажатия и ввода оформления заказа
    order_name = "//input[@placeholder='* Имя']"
    order_surname = "//input[@placeholder='* Фамилия']"
    order_address = "//input[@placeholder='* Адрес: куда привезти заказ']"
    order_metro = "//input[@placeholder='* Станция метро']"
    select_metro = "//*[@id='root']/div/div[2]/div[2]/div[4]/div/div[2]"
    order_phone = "//input[@placeholder='* Телефон: на него позвонит курьер']"
    button_next = "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    order_date = "//input[@placeholder='* Когда привезти самокат']"
    dropdown_date = "//span[@class='Dropdown-arrow']"
    dropdown_date_select = "//*[@id='root']/div/div[2]/div[2]/div[2]/div[2]/div[1]"
    color_grey_scooter = "// input[ @ id = 'grey']"
    color_black_scooter = "//label[@for='black']"
    comment_courier = "//input[@placeholder='Комментарий для курьера']"
    button_approve = "//button[contains(text(),'Да')]"
    button_check_status = "//button[contains(text(),'Посмотреть статус')]"

    # Локаторы логотипов
    button_dzen = "//img[@alt='Yandex']"
    button_scooter = "//img[@alt='Scooter']"
    button_approve_cookie = "//button[@id='rcc-confirm-button']"