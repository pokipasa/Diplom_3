import allure
import pytest
from pages.feed_page import FeedPage
from data import CommonData
from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators


class TestFeedPage:

    @allure.title('Проверка появления поп-апа с информацией о заказе')
    def test_check_order_details_popup_appears_on_click(self, browser_driver):
        feed_page = FeedPage(browser_driver)
        feed_page.open_order_in_new_window(MainPageLocators.feed_button, FeedPageLocators.orders_number)
        element = browser_driver.find_element(*FeedPageLocators.current_order_number)
        assert element.text != ""

    @allure.title('Проверка отображения заказов пользователя из "Истории заказов" на странице "Лента заказов"')
    def test_validate_user_order_shows_up_on_feed_page(self, browser_driver, create_user):
        feed_page = FeedPage(browser_driver)
        order_response, order_ui = feed_page.list_user_orders_in_feed(
            create_user, MainPageLocators.feed_button, FeedPageLocators.orders_number,
            FeedPageLocators.current_order_number
        )
        assert order_response == order_ui

    @allure.title('Проверка увеличения счетчиков заказов, выполненных за сегодня и за всё время')
    @pytest.mark.parametrize('counter_locator, description', CommonData.counters)
    def test_verify_counter_increase(self, browser_driver, create_user, counter_locator, description):
        feed_page = FeedPage(browser_driver)
        count_before_order, count_after_order = feed_page.count_increase(
            create_user, MainPageLocators.feed_button, counter_locator
        )
        assert int(count_after_order) == int(count_before_order) + 1

    @allure.title('Проверка отображения номера заказа в разделе "В работе"')
    def test_verify_order_number_in_progress_section(self, browser_driver, create_user):
        feed_page = FeedPage(browser_driver)
        order_number, order_ui = feed_page.order_number_in_progress(
            create_user, MainPageLocators.feed_button, FeedPageLocators.in_progress_order
        )
        order_ui = order_ui[1:]

        assert order_number == order_ui
