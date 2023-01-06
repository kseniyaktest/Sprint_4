import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page_objects.locators.popup_confirm_locators import PopupConfirm


class ConfirmPopup:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("проверка URL страницы - должен быть https://qa-scooter.praktikum-services.ru/order")
    def check_url_page_about_rent(self):
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    @allure.step("в поп-ап нажать кнопку 'Да'")
    def press_button_yes(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(PopupConfirm.YES_BUTTON))
        self.driver.find_element(*PopupConfirm.YES_BUTTON).click()

