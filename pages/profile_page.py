from data import CommonData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
import allure
from data import Urls


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход в личный кабинет')
    def redirect_to_dashboard(self, locator_button_cabinet):
        self.click_on_element(locator_button_cabinet)

    @allure.step('Открытие истории заказов')
    def orders_history(self, locator_button_cabinet, locator_email, locator_password, locator_button_entrance,
                       locator_history):
        self.click_on_element(locator_button_cabinet)
        self.enter_text_into_element(locator_email, CommonData.test_email)
        self.enter_text_into_element(locator_password, CommonData.test_user_password)
        self.click_on_element(locator_button_entrance)
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(Urls.main_url))
        self.click_on_element(locator_button_cabinet)
        self.click_on_element(locator_history)

    @allure.step('Авторизация и разлогин пользователя')
    def authorization_and_exit(self, locator_button_cabinet, locator_email, locator_password,
                               locator_button_entrance,
                               locator_exit):
        self.click_on_element(locator_button_cabinet)
        self.enter_text_into_element(locator_email, CommonData.test_email)
        self.enter_text_into_element(locator_password, CommonData.test_user_password)
        self.click_on_element(locator_button_entrance)
        WebDriverWait(self.driver, 100).until(expected_conditions.url_to_be(Urls.main_url))
        self.click_on_element(locator_button_cabinet)
        self.click_on_element(locator_exit)
