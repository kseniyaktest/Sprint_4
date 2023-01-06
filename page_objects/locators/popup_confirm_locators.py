from selenium.webdriver.common.by import By

class PopupConfirm:
    MODAL_HEADER = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text()='Хотите оформить заказ?']"]
    YES_BUTTON = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']"]
    