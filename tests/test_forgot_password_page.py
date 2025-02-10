import allure
from pages.forgot_password_page import ForgotPasswordPage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from data import Urls
from pages.profile_page import web_driver_wait


class TestForgotPasswordPage:

    @allure.title('Проверка фокуса на поле ввода пароля')
    def test_highlight_pass_entry_field(self, browser_driver):
        forgot_page = ForgotPasswordPage(browser_driver)
        forgot_page.hide_password(MainPageLocators.account_button, ForgotPasswordPageLocators.email_entry_field)
        element = browser_driver.find_element(*ForgotPasswordPageLocators.email_entry_field)
        tab = element.find_element(*LoginPageLocators.email_active_field)
        tab_class = tab.get_attribute("class")
        assert tab_class == 'input pr-6 pl-6 input_type_text input_size_default input_status_active'

    @allure.title('Проверка перехода на страницу "Сброс пароля"')
    def test_input_email_and_click_on_pass_recovery_button_opens_pass_page(self, browser_driver):
        forgot_page = ForgotPasswordPage(browser_driver)
        forgot_page.page_recover(MainPageLocators.account_button, LoginPageLocators.forgot_password_button)
        browser_driver.implicitly_wait(5)
        result = browser_driver.current_url
        assert result == Urls.forgot_password_url

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_click_on_pass_recovery_button_opens_recovery_page(self, browser_driver):
        forgot_page = ForgotPasswordPage(browser_driver)
        forgot_page.recover_password(
            MainPageLocators.account_button, LoginPageLocators.forgot_password_button,
            ForgotPasswordPageLocators.email_entry_field, ForgotPasswordPageLocators.recover_button
        )
        web_driver_wait(browser_driver, Urls.reset_password_url)
        result = browser_driver.current_url
        assert result == Urls.reset_password_url
