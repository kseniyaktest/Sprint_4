import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page_objects.locators.page_order_for_someone_locators import WhoNeedsScooter

class WhoWouldLikeScooter:
    #
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("проверка URL страницы заказа самоката - должен быть https://qa-scooter.praktikum-services.ru/order")
    def check_url_page_order(self):
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    @allure.step("ожидание загрузки страницы заказа")
    def wait_load_page_order(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(WhoNeedsScooter.BUTTON_NEXT))

    @allure.step("корректное заполнение поля 'Имя'")
    def correct_complete_last_name_field(self, last_name):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(WhoNeedsScooter.LAST_NAME_FIELD))
        self.driver.find_element(*WhoNeedsScooter.LAST_NAME_FIELD).send_keys(last_name)

    @allure.step("корректное заполнение поля 'Фамилия'")
    def correct_complete_first_name_field(self, first_name):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(WhoNeedsScooter.FIRST_NAME_FIELD))
        self.driver.find_element(*WhoNeedsScooter.FIRST_NAME_FIELD).send_keys(first_name)

    @allure.step("корректное заполнение поля 'Адрес'")
    def correct_complete_address_field(self, address):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(WhoNeedsScooter.ADDRESS_FIELD))
        self.driver.find_element(*WhoNeedsScooter.ADDRESS_FIELD).send_keys(address)

    @allure.step("корректное заполнение поля 'Метро'")
    def click_station_metro_field(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(WhoNeedsScooter.STATION_METRO_FIELD))
        self.driver.find_element(*WhoNeedsScooter.STATION_METRO_FIELD).click()

    @allure.step("выбрать станцию 'Чеховская'")
    def choose_chekhovskaya_station(self):
        self.driver.find_element(*WhoNeedsScooter.CHEKHOVSKAYA_STATION).click()

    @allure.step("проскроллить список станций метро до Чеховская")
    def scroll_station_to_checkovskaya_station_click(self):
        element = self.driver.find_element(*WhoNeedsScooter.CHEKHOVSKAYA_STATION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("корректное заполнение поля 'Телефон'")
    def correct_complete_phone_number(self, phone_number):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(WhoNeedsScooter.PHONE_FIELD))
        self.driver.find_element(*WhoNeedsScooter.PHONE_FIELD).send_keys(phone_number)

    @allure.step("корректное заполнение формы заказа")
    def correct_complete_form_order(self, last_name, first_name, address, phone_number):
        self.correct_complete_last_name_field(last_name)
        self.correct_complete_first_name_field(first_name)
        self.correct_complete_address_field(address)
        self.click_station_metro_field()
        self.choose_chekhovskaya_station()
        self.correct_complete_phone_number(phone_number)


    @allure.step("клик кнопки 'Далее'")
    def click_button_next(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(WhoNeedsScooter.BUTTON_NEXT))
        self.driver.find_element(*WhoNeedsScooter.BUTTON_NEXT).click()
