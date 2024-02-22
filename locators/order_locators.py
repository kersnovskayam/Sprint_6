class OrderLocators:
    # Локаторы кнопок заказать
    button_order_xpath1 = '//button[@class="Button_Button__ra12g"]'
    button_order_xpath2 = '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'

    # локаторы форм нажатия и ввода оформления заказа
    order_name = "//input[@placeholder='* Имя']"
    order_surname = "//input[@placeholder='* Фамилия']"
    order_address = "//input[@placeholder='* Адрес: куда привезти заказ']"
    order_metro = "//input[@placeholder='* Станция метро']"
    select_metro = ".//div[text()='Беговая']"
    select_metro2 = ".//div[text()='Пушкинская']"
    order_phone = "//input[@placeholder='* Телефон: на него позвонит курьер']"
    order_button_next = "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    order_date = "//input[@placeholder='* Когда привезти самокат']"
    order_dropdown_date = "//span[@class='Dropdown-arrow']"
    select_dropdown_date = "//div[text() = 'сутки']"
    order_color_grey_scooter = "// input[ @ id = 'grey']"
    order_color_black_scooter = "//label[@for='black']"
    order_comment_courier = "//input[@placeholder='Комментарий для курьера']"
    order_button_approve = "//button[contains(text(),'Да')]"
    order_button_check_status = "//button[contains(text(),'Посмотреть статус')]"