from selenium.webdriver.common.by import By

class WhoNeedsScooter:
    ORDER_FORM = [By.XPATH, ".//div[@class='App_App__15LM-']"]
    LAST_NAME_FIELD = [By.XPATH, ".//input[@placeholder='* Имя']"]
    FIRST_NAME_FIELD = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    STATION_METRO_FIELD = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    PHONE_FIELD = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_NEXT = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    SELECT_FORM = [By.XPATH, ".//div[@class='select-search_select']"]
    CHEKHOVSKAYA_STATION = [By.XPATH, ".//div[@class='Order_Text__2broi' and text()='Чеховская']"]
