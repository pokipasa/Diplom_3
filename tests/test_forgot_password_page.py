import allure
from pages.forgot_password_page import ForgotPasswordPage
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from data import Urls
from pages.base_page import driver_wait


class TestForgotPasswordPage:

    @allure.title('Проверка активности поля ввода пароля')
    def test_check_pass_entry_field_highlight(self, browser_driver):
        forgot_page = ForgotPasswordPage(browser_driver)
        forgot_page.hide_password(MainPageLocators.account_button, ForgotPasswordPageLocators.email_entry_field)
        element = browser_driver.find_element(*ForgotPasswordPageLocators.email_entry_field)
        tab = element.find_element(*LoginPageLocators.email_active_field)
        tab_class = tab.get_attribute("class")
        assert tab_class == 'input pr-6 pl-6 input_type_text input_size_default input_status_active'

    @allure.title('Проверка перехода на страницу "Сброс пароля"')
    def test_enter_email_and_click_pass_recovery_button_opens_reset_page(self, browser_driver):
        forgot_page = ForgotPasswordPage(browser_driver)
        forgot_page.password_recovery_page(MainPageLocators.account_button, LoginPageLocators.forgot_password_button)
        browser_driver.implicitly_wait(5)
        result = browser_driver.current_url
        assert result == Urls.forgot_password_url

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_verify_pass_recovery_button_opens_reset_page(self, browser_driver):
        forgot_page = ForgotPasswordPage(browser_driver)
        forgot_page.reset_password(
            MainPageLocators.account_button, LoginPageLocators.forgot_password_button,
            ForgotPasswordPageLocators.email_entry_field, ForgotPasswordPageLocators.recover_button
        )
        driver_wait(browser_driver, Urls.reset_password_url)
        result = browser_driver.current_url
        assert result == Urls.reset_password_url
