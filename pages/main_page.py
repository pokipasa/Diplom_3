import allure

from pages.base_page import BasePage
from data import CommonData


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на страницу заказов')
    def redirect_to_feed(self, locator_feed):
        self.click_on_element(locator_feed)

    @allure.step('Переход на страницу конструктора')
    def redirect_to_constructor(self, locator_feed, locator_cons):
        self.click_on_element(locator_feed)
        self.click_on_element(locator_cons)

    @allure.step('Открытие нового окна')
    def open_new_window(self, locator_element, locator_text):
        self.click_on_element(locator_element)
        return self.get_text_from_element(locator_text)

    @allure.step('Закрытие нового окна')
    def close_new_window(self, locator_element, locator_close):
        self.click_on_element(locator_element)
        self.click_on_element(locator_close)

    @allure.step('Добавление ингредиента')
    def add_ingredient(self, locator_object, locator_base):
        self.drag_and_drop_element(locator_object, locator_base)

    @allure.step('Создание заказа')
    def create_order(self, locator_button_cabinet, locator_email, locator_password, locator_button_entrance,
                     locator_object, locator_base, locator_create_order):
        self.click_on_element(locator_button_cabinet)
        self.enter_text_into_element(locator_email, CommonData.test_email)
        self.enter_text_into_element(locator_password, CommonData.test_user_password)
        self.click_on_element(locator_button_entrance)
        self.add_ingredient(locator_object, locator_base)
        self.click_on_element(locator_create_order)
