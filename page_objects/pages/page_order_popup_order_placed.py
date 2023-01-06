import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page_objects.locators.popup_order_placed import OrderPlaced

class PopupOrderPlaced:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("проверка URL страницы - должен быть https://qa-scooter.praktikum-services.ru/order")
    def check_url_page_about_rent(self):
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    @allure.step("в поп-ап нажать кнопку 'Посмотреть статус'")
    def click_view_status_button(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(OrderPlaced.VIEW_STATUS_BUTTON))
        self.driver.find_element(*OrderPlaced.VIEW_STATUS_BUTTON).click()

    @allure.step("клик по лого Яндекс открывает страницу Дзен в новом окне")
    def check_click_yandex_open_window_dzen(self):
        self.driver.find_element(*OrderPlaced.LOGO_YANDEX).click()
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        WebDriverWait(self.driver, 7).until(expected_conditions.url_contains("https://dzen.ru/?yredirect=true"))



    @allure.step("клик по лого Самокат открывает главную страницу Самокат")
    def check_click_logo_scooter_open_page_scooter(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(OrderPlaced.LOGO_SCOOTER))
        self.driver.find_element(*OrderPlaced.LOGO_SCOOTER).click()
        WebDriverWait(self.driver, 7).until(expected_conditions.url_contains("https://qa-scooter.praktikum-services.ru/"))
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"



