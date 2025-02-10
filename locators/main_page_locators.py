from selenium.webdriver.common.by import By


class MainPageLocators:
    account_button = (By.XPATH, "//p[text()='Личный Кабинет']")
    feed_button = (By.XPATH, "//p[text()='Лента Заказов']")
    constructor_button = (By.XPATH, "//p[text()='Конструктор']")
    place_order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    object_order = (By.XPATH, "//*[@alt='Флюоресцентная булка R2-D3']")
    base_order_button = (By.XPATH, "//li[@class='BurgerConstructor_basket__listItem__aWMu1 mr-4']")
    ingredient_details = (By.XPATH, "//h2[text()='Детали ингредиента']")
    window_button_class = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    section_class = (By.XPATH, "//section[@class = 'Modal_modal__P3_V5']")
    total_price = (By.XPATH, "//p[@class = 'text text_type_digits-medium mr-3']")
    order_number = (
        By.XPATH,
        "//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']"
    )

