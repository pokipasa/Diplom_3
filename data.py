from locators.feed_page_locators import FeedPageLocators


class Urls:
    main_url = 'https://stellarburgers.nomoreparties.site/'
    forgot_password_url = f'{main_url}forgot-password'
    order_history_url = f'{main_url}account/order-history'
    login_url = f'{main_url}login'
    feed_url = f'{main_url}feed'
    profile_url = f'{main_url}account/profile'
    reset_password_url = f'{main_url}reset-password'
    register_url = f'{main_url}api/auth/register'
    delete_user_url = f'{main_url}api/auth/user'
    authorization_url = f'{main_url}api/auth/login'
    create_order_url = f'{main_url}api/ingredients'
    get_orders_url = f'{main_url}api/orders'


class CommonData:
    test_email = 'mlivmanis@yandex.ru'
    test_user_password = 'KHj8tW7pQNhtF'
    test_user_name = 'Max'

    counters = [
        [FeedPageLocators.total_orders_counter, 'Completed for all time'],
        [FeedPageLocators.today_orders_counter, 'Completed today']
    ]