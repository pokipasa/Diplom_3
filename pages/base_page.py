import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Убедиться в видимости определенного элемента')
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Клик на определенный элемент')
    def click_on_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Добавление значений в указанное поле')
    def enter_text_into_element(self, locator, text):
        element = self.wait_for_element(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.send_keys(text)

    @allure.step('Получение текста из указанного элемента')
    def get_text_from_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return element.text

    @allure.step('Перемещение элемента')
    def drag_and_drop_element(self, locator_start, locator_final):
        action_chains = ActionChains(self.driver)
        element_start = self.wait_for_element(locator_start)
        element_final = self.wait_for_element(locator_final)
        action_chains.drag_and_drop(element_start, element_final).perform()


@allure.step('Ожидание элемента')
def driver_wait(self, url):
    WebDriverWait(self, 3).until(expected_conditions.url_to_be(url))
