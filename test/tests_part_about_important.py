import allure
from page_objects.pages.page_main import MainPage
from page_objects.locators.page_main_locators import PageMain

class TestPartAboutImportant:
    driver = None

    @allure.title('Проверка текста ответа на вопрос "Сколько это стоит? И как оплатить?"')
    def test_question_how_much_is_it(self, get_driver):
        main_page = MainPage(get_driver)

        main_page.button_cookie_click()

        main_page.hidden_img_and_scroll()

        main_page.click_question_how_much_is_it()

        main_page.wait_load_answer_how_much_is_it()

        answer_how_much_is_it = get_driver.find_element(*PageMain.ANSWER_HOW_MUCH_IS_IT)

        text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

        assert answer_how_much_is_it.text == text

    @allure.title('Проверка текста ответа на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    def test_question_would_like_some_scooters(self, get_driver):

        main_page = MainPage(get_driver)

        main_page.button_cookie_click()

        main_page.hidden_img_and_scroll()

        main_page.click_question_would_like_some_scooters()

        main_page.wait_load_answer_would_like_some_scooters()

        answer_would_like_some_scooters = get_driver.find_element(*PageMain.ANSWER_WOULD_LIKE_SOME_SCOOTERS)

        text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто ' \
               'сделать несколько заказов — один за другим.'

        assert answer_would_like_some_scooters.text == text

    @allure.title('Проверка текста ответа на вопрос "Как рассчитывается время аренды?"')
    def test_question_rental_time_is_calculated(self, get_driver):
        main_page = MainPage(get_driver)

        main_page.button_cookie_click()

        main_page.hidden_img_and_scroll()

        main_page.click_question_rental_time_is_calculated()

        main_page.wait_load_answer_rental_time_is_calculated()

        answer_rental_time_is_calculated = get_driver.find_element(*PageMain.ANSWER_RENTAL_TIME_IS_CALCULATED)

        text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды' \
               ' начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, ' \
               'суточная аренда закончится 9 мая в 20:30.'

        assert answer_rental_time_is_calculated.text == text

    @allure.title('Проверка текста ответа на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    def test_question_order_today(self, get_driver):
        main_page = MainPage(get_driver)

        main_page.button_cookie_click()

        main_page.hidden_img_and_scroll()

        main_page.click_question_order_today()

        main_page.wait_load_answer_order_today()

        answer_order_today = get_driver.find_element(*PageMain.ANSWER_ORDER_TODAY)

        text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

        assert answer_order_today.text == text

    @allure.title('Проверка текста ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    def test_question_extend_order(self, get_driver):
        main_page = MainPage(get_driver)

        main_page.button_cookie_click()

        main_page.hidden_img_and_scroll()

        main_page.click_question_extend_order()

        main_page.wait_load_answer_extend_order()

        answer_extend_order = get_driver.find_element(*PageMain.ANSWER_EXTEND_ORDER)

        text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

        assert answer_extend_order.text == text

    @allure.title('Проверка текста ответа на вопрос "Вы привозите зарядку вместе с самокатом?"')
    def test_question_bring_changing_with_scooter(self, get_driver):
        main_page = MainPage(get_driver)

        main_page.button_cookie_click()

        main_page.hidden_img_and_scroll()

        main_page.click_question_bring_changing_with_scooter()

        main_page.wait_load_answer_bring_changing_with_scooter()

        answer_bring_changing_with_scooter = get_driver.find_element(*PageMain.ANSWER_BRING_CHANGING_WITH_SCOOTER)

        text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься ' \
               'без передышек и во сне. Зарядка не понадобится.'

        assert answer_bring_changing_with_scooter.text == text

    @allure.title('Проверка текста ответа на вопрос "Можно ли отменить заказ?"')
    def test_question_cancel_order(self, get_driver):
        main_page = MainPage(get_driver)

        main_page.button_cookie_click()

        main_page.hidden_img_and_scroll()

        main_page.click_question_cancel_order()

        main_page.wait_load_answer_cancel_order()

        answer_cancel_order = get_driver.find_element(*PageMain.ANSWER_CANCEL_ORDER)

        text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

        assert answer_cancel_order.text == text

    @allure.title('Проверка текста ответа на вопрос "Я жизу за МКАДом, привезёте?"')
    def test_question_i_from_mkad(self, get_driver):
        main_page = MainPage(get_driver)

        main_page.button_cookie_click()

        main_page.hidden_img_and_scroll()

        main_page.click_question_i_from_mkad()

        main_page.wait_load_answer_i_from_mkad()

        answer_i_from_mkad = get_driver.find_element(*PageMain.ANSWER_I_FROM_MKAD)

        text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

        assert answer_i_from_mkad.text == text


