import allure
from pages.base_page import BasePage
from data import CommonData


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Восстановление пароля')
    def reset_password(self, locator_button_cabinet, locator_recover_pass, locator_email, locator_button_recover):
        self.click_on_element(locator_button_cabinet)
        self.click_on_element(locator_recover_pass)
        self.enter_text_into_element(locator_email, CommonData.test_email)
        self.click_on_element(locator_button_recover)

    @allure.step('Открытие страницы восстановления пароля')
    def password_recovery_page(self, locator_button_cabinet, locator_recover_pass):
        self.click_on_element(locator_button_cabinet)
        self.click_on_element(locator_recover_pass)

    @allure.step('Показ и скрытие элемента')
    def hide_password(self, locator_button_cabinet, locator_email):
        self.click_on_element(locator_button_cabinet)
        self.click_on_element(locator_email)
