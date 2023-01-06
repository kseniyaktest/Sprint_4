from selenium.webdriver.common.by import By

class OrderPlaced:
    MODAL_HEADER = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']"]
    VIEW_STATUS_BUTTON = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']"]
    SUCCESSFUL_ORDER = [By.XPATH, ".//div[@class='Order_Text__2broi']"]
    LOGO_YANDEX = [By.XPATH, ".//img[@src='/assets/ya.svg']"]
    LOGO_SCOOTER = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]