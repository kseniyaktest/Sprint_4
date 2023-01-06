import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page_objects.locators.page_main_locators import PageMain


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def wait_for_load_part_about_important(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(PageMain.QUESTION_HOW_MUCH_IS_IT))

    @allure.step("закрыть информационное окно о сборе cookie")
    def button_cookie_click(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(PageMain.BUTTON_COOKIE))
        self.driver.find_element(*PageMain.BUTTON_COOKIE).click()

    @allure.step("функции раскрытия ответа на вопрос")
    def click_question_how_much_is_it(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.presence_of_element_located(PageMain.QUESTION_HOW_MUCH_IS_IT))
        self.driver.find_element(*PageMain.QUESTION_HOW_MUCH_IS_IT).click()

    def click_question_would_like_some_scooters(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.presence_of_element_located(PageMain.QUESTION_WOULD_LIKE_SOME_SCOOTERS))
        self.driver.find_element(*PageMain.QUESTION_WOULD_LIKE_SOME_SCOOTERS).click()

    def click_question_rental_time_is_calculated(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.presence_of_element_located(PageMain.QUESTION_RENTAL_TIME_IS_CALCULATED))
        self.driver.find_element(*PageMain.QUESTION_RENTAL_TIME_IS_CALCULATED).click()

    def click_question_order_today(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.presence_of_element_located(PageMain.QUESTION_ORDER_TODAY))
        self.driver.find_element(*PageMain.QUESTION_ORDER_TODAY).click()

    def click_question_extend_order(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.presence_of_element_located(PageMain.QUESTION_EXTEND_ORDER))
        self.driver.find_element(*PageMain.QUESTION_EXTEND_ORDER).click()

    def click_question_bring_changing_with_scooter(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.presence_of_element_located(
            PageMain.QUESTION_BRING_CHANGING_WITH_SCOOTER))
        self.driver.find_element(*PageMain.QUESTION_BRING_CHANGING_WITH_SCOOTER).click()

    def click_question_cancel_order(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.presence_of_element_located(PageMain.QUESTION_CANCEL_ORDER))
        self.driver.find_element(*PageMain.QUESTION_CANCEL_ORDER).click()

    def click_question_i_from_mkad(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.presence_of_element_located(PageMain.QUESTION_I_FROM_MKAD))
        self.driver.find_element(*PageMain.QUESTION_I_FROM_MKAD).click()

    @allure.step("скрыть мешающий элемент и проскроллить страницу вниз")
    def hidden_img_and_scroll(self):
        element_1 = self.driver.find_element(By.XPATH, ".//img[@src='/assets/scooter.png']")

        self.driver.execute_script("arguments[0].style.visibility='hidden'", element_1)

        element = self.driver.find_element(By.ID, "accordion__heading-7")

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("функции ожидания ответа на вопрос")

    def wait_load_answer_how_much_is_it(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(PageMain.ANSWER_HOW_MUCH_IS_IT))

    def wait_load_answer_would_like_some_scooters(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.visibility_of_element_located(PageMain.ANSWER_WOULD_LIKE_SOME_SCOOTERS))

    def wait_load_answer_rental_time_is_calculated(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.visibility_of_element_located(PageMain.ANSWER_RENTAL_TIME_IS_CALCULATED))

    def wait_load_answer_order_today(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(PageMain.ANSWER_ORDER_TODAY))

    def wait_load_answer_extend_order(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(PageMain.ANSWER_EXTEND_ORDER))

    def wait_load_answer_bring_changing_with_scooter(self):
        WebDriverWait(self.driver, 7).until(
            expected_conditions.visibility_of_element_located(PageMain.ANSWER_BRING_CHANGING_WITH_SCOOTER))

    def wait_load_answer_cancel_order(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(PageMain.ANSWER_CANCEL_ORDER))

    def wait_load_answer_i_from_mkad(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(PageMain.ANSWER_I_FROM_MKAD))

    @allure.step("клик кнопки 'Заказать' в Header")
    def click_button_order_header(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(PageMain.BUTTON_ORDER_HEADER))
        self.driver.find_element(*PageMain.BUTTON_ORDER_HEADER).click()

    @allure.step("клик кнопки 'Заказать' в теле страницы")
    def click_button_order_body(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(PageMain.BUTTON_ORDER_BODY))
        self.driver.find_element(*PageMain.BUTTON_ORDER_BODY).click()
