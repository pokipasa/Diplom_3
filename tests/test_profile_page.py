import allure
from data import Urls
from pages.profile_page import ProfilePage
from pages.base_page import driver_wait
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators


class TestProfilePage:

    @allure.title('Проверка перехода на страницу "Профиль"')
    def test_verify_account_button_opens_profile_page(self, browser_driver):
        profile_page = ProfilePage(browser_driver)
        profile_page.redirect_to_dashboard(MainPageLocators.account_button)
        browser_driver.implicitly_wait(3)
        result = browser_driver.current_url
        assert result == Urls.login_url

    @allure.title('Проверка перехода на страницу "История заказов"')
    def test_verify_order_history_url_opens_orders_history_page(self, browser_driver):
        profile_page = ProfilePage(browser_driver)
        profile_page.orders_history(
            MainPageLocators.account_button, LoginPageLocators.email_input_field,
            LoginPageLocators.password_input_field, LoginPageLocators.sign_in_button,
            ProfilePageLocators.orders_history_url
        )
        browser_driver.implicitly_wait(10)
        result = browser_driver.current_url
        assert result == Urls.order_history_url

    @allure.title('Проверка выхода из аккаунта')
    def test_check_logout_after_exit_url_click(self, browser_driver):
        profile_page = ProfilePage(browser_driver)
        profile_page.authorization_and_exit(
            MainPageLocators.account_button, LoginPageLocators.email_input_field,
            LoginPageLocators.password_input_field, LoginPageLocators.sign_in_button, ProfilePageLocators.exit_button
        )
        driver_wait(browser_driver, Urls.login_url)
        result = browser_driver.current_url
        assert result == Urls.login_url
