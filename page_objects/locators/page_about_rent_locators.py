from selenium.webdriver.common.by import By

class AboutRent:
    ORDER_HEADER = [By.CLASS_NAME, ".Order_Header__BZXOb"]
    DATE_FIELD = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    RENT_PERIOD = [By.XPATH, ".//div[@class='Dropdown-placeholder' and text()='* Срок аренды']"]
    DROP_MENU = [By.XPATH, ".//div[@class='Dropdown-menu']"]
    CALENDAR_DATE_WORKDAY = [By.XPATH, ".//div[@class='react-datepicker__day react-datepicker__day--019 react-datepicker__day--selected']"]
    CALENDAR_DATE_WEEKEND = [By.XPATH, ".//div[@class='react-datepicker__day react-datepicker__day--003 react-datepicker__day--weekend']"]
    OWN_DAY = [By.XPATH, ".//div[@class='Dropdown-option' and text()='сутки']"]
    BLACK_SCOOTER = [By.XPATH, ".//input[@id='black']"]
    COMMENT_FOR_COURIER = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"]
    BUTTON_ORDER = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]