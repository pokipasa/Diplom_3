import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверка видимости указанного элемента')
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Нажатие на указанный элемент')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Заполнение указанного поля данными')
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.send_keys(text)

    @allure.step('Возврат текста указанного элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return element.text

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_element(self, locator_start, locator_final):
        action_chains = ActionChains(self.driver)
        element_start = self.find_element_with_wait(locator_start)
        element_final = self.find_element_with_wait(locator_final)
        action_chains.drag_and_drop(element_start, element_final).perform()


def driver_wait(self, url):
    WebDriverWait(self, 3).until(expected_conditions.url_to_be(url))
