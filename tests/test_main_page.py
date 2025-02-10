import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from data import Urls


class TestMainPage:

    @allure.title('Переход по клику на «Лента заказов»,')
    def test_transfer_to_feed(self, browser_driver):
        main_page = MainPage(browser_driver)
        main_page.transfer_to_feed(MainPageLocators.feed_button)
        result = browser_driver.current_url
        assert result == Urls.feed_url

    @allure.title('Переход по клику на «Конструктор»')
    def test_transfer_to_cons(self, browser_driver):
        main_page = MainPage(browser_driver)
        main_page.transfer_to_constructor(MainPageLocators.feed_button, MainPageLocators.constructor_button)
        result = browser_driver.current_url
        assert result == Urls.main_url

    @allure.title('Проверка открытия поп-апа с информацией об ингредиенте')
    def test_new_window(self, browser_driver):
        main_page = MainPage(browser_driver)
        result = main_page.new_window(MainPageLocators.object_order, MainPageLocators.ingredient_details)
        assert result == "Детали ингредиента"

    @allure.title('Проверка закрытия поп-апа с информацией об ингредиенте')
    def test_close_new_window(self, browser_driver):
        main_page = MainPage(browser_driver)
        main_page.close_new_window(MainPageLocators.object_order, MainPageLocators.window_button_class)
        element = browser_driver.find_element(*MainPageLocators.section_class)
        element_class = element.get_attribute("class")
        assert element_class == 'Modal_modal__P3_V5'

    @allure.title('Проверка увеличения счетчика ингредиента')
    def test_add_ingredient(self, browser_driver):
        main_page = MainPage(browser_driver)
        main_page.add_ingredient(MainPageLocators.object_order, MainPageLocators.base_order_button)
        element = browser_driver.find_element(*MainPageLocators.total_price)
        assert element.text != "0"

    @allure.title('Проверка, что авторизованный пользователь может сделать заказ')
    def test_create_order(self, browser_driver):
        main_page = MainPage(browser_driver)
        main_page.create_order(
            MainPageLocators.account_button, LoginPageLocators.email_input_field,
            LoginPageLocators.password_input_field, LoginPageLocators.sign_in_button,
            MainPageLocators.object_order, MainPageLocators.base_order_button,
            MainPageLocators.place_order_button
        )
        element = browser_driver.find_element(*MainPageLocators.order_number)
        assert element.text != ''
