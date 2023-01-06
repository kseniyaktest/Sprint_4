import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from page_objects.locators.page_about_rent_locators import AboutRent

class RentAbout:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step("проверка URL страницы 'Про аренду' - должен быть https://qa-scooter.praktikum-services.ru/order")
    def check_url_page_about_rent(self):
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/order"


    @allure.step("корректное заполнение даты и выбор дня доставки в рабочий день")
    def correct_complete_date_field_workday(self, date):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(AboutRent.DATE_FIELD))
        self.driver.find_element(*AboutRent.DATE_FIELD).send_keys(date)
        self.driver.find_element(*AboutRent.DATE_FIELD).send_keys(Keys.ESCAPE)

    @allure.step("корректное заполнение даты и выбор дня доставки в выходной день")
    def correct_complete_date_field_weekend(self, date):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(AboutRent.DATE_FIELD))
        self.driver.find_element(*AboutRent.DATE_FIELD).send_keys(date)
        self.driver.find_element(*AboutRent.DATE_FIELD).send_keys(Keys.ESCAPE)


    @allure.step("корректное заполнение срока аренды")
    def correct_complete_rent_period(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(AboutRent.RENT_PERIOD))
        self.driver.find_element(*AboutRent.RENT_PERIOD).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(AboutRent.OWN_DAY))
        self.driver.find_element(*AboutRent.OWN_DAY).click()

    @allure.step("выбрать скутер чёрный жемчуг")
    def choose_scooter_color_black(self):
        self.driver.find_element(*AboutRent.BLACK_SCOOTER).click()

    @allure.step("заполнить комментарий для курьера")
    def complete_comment_for_courier(self, message):
        self.driver.find_element(*AboutRent.COMMENT_FOR_COURIER).send_keys(message)

    @allure.step("заполнить форму 'Про аренду' для заказа в рабочий день")
    def correct_complete_order_form(self, date, message):
        self.correct_complete_date_field_workday(date)
        self.correct_complete_rent_period()
        self.choose_scooter_color_black()
        self.complete_comment_for_courier(message)

    @allure.step("заполнить форму 'Про аренду' для заказа в выходной день")
    def correct_complete_order_form_weekend(self, date, message):
        self.correct_complete_date_field_weekend(date)
        self.correct_complete_rent_period()
        self.choose_scooter_color_black()
        self.complete_comment_for_courier(message)

    @allure.step("кликнуть кнопку 'Заказать'")
    def click_button_order(self):
        self.driver.find_element(*AboutRent.BUTTON_ORDER).click()


