import allure
from page_objects.pages.page_main import MainPage
from page_objects.pages.page_order_for_someone import WhoWouldLikeScooter
from page_objects.pages.page_about_rent import RentAbout
from page_objects.pages.page_order_popup_confirm import ConfirmPopup
from page_objects.pages.page_order_popup_order_placed import PopupOrderPlaced

class TestOrderScooter:
    driver = None

    @allure.title('Проверка заказа по клику на кнопку "Заказать" в хедере главной страницы')
    def test_order_scooter_from_button_header(self, get_driver):
        main_page = MainPage(get_driver)

        main_page.button_cookie_click()

        main_page.click_button_order_header()

        page_order = WhoWouldLikeScooter(get_driver)

        page_order.check_url_page_order()

        page_order.correct_complete_form_order("Ксения", "Кутикова", "ул.Мира, д.1", "79876543210")

        page_order.click_button_next()

        about_rent = RentAbout(get_driver)

        about_rent.check_url_page_about_rent()

        about_rent.correct_complete_order_form("10.03.2023", "стучи сильнее")

        about_rent.click_button_order()

        popup_confirm = ConfirmPopup(get_driver)

        popup_confirm.check_url_page_about_rent()

        popup_confirm.press_button_yes()

        popup_order_placed = PopupOrderPlaced(get_driver)

        popup_order_placed.check_url_page_about_rent()

        popup_order_placed.click_view_status_button()

        popup_order_placed.check_click_logo_scooter_open_page_scooter()

        popup_order_placed.check_click_yandex_open_window_dzen()

    @allure.title('Проверка заказа по клику на кнопку "Заказать" в теле главной страницы')
    def test_order_scooter_from_button_body_page(self, get_driver):
        main_page = MainPage(get_driver)

        main_page.button_cookie_click()

        main_page.click_button_order_body()

        page_order = WhoWouldLikeScooter(get_driver)

        page_order.check_url_page_order()

        page_order.correct_complete_form_order("Ксенияя", "Кутикова", "ул.Мира, д.111", "79876543210")

        page_order.click_button_next()

        about_rent = RentAbout(get_driver)

        about_rent.check_url_page_about_rent()

        about_rent.correct_complete_order_form_weekend("10.06.2023", "")

        about_rent.click_button_order()

        popup_confirm = ConfirmPopup(get_driver)

        popup_confirm.check_url_page_about_rent()

        popup_confirm.press_button_yes()

        popup_order_placed = PopupOrderPlaced(get_driver)

        popup_order_placed.check_url_page_about_rent()

        popup_order_placed.click_view_status_button()

        popup_order_placed.check_click_logo_scooter_open_page_scooter()

        popup_order_placed.check_click_yandex_open_window_dzen()













