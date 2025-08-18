import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    def __init__(self, driver: WebDriver):
        """Инициализация страницы логина.

        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver

    def open(self, url: str) -> None:
        """Открыть страницу авторизации.

        Args:
            url: str - URL страницы авторизации
        """
        self.driver.get(url)

    @allure.step("Ввести логин {username}")
    def enter_username(self, username: str) -> None:
        """Ввод логина.

        Args:
            username: str - имя пользователя
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """Ввод пароля.

        Args:
            password: str - пароль пользователя
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)

    @allure.step("Нажать кнопку входа")
    def click_login_button(self) -> None:
        """Клик по кнопке входа."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "loginButton"))).click()


@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:
    """Тесты для проверки авторизации."""

    @allure.title("Успешная авторизация")
    @allure.description("Проверка входа с корректными учетными данными")
    def test_successful_login(self, driver: WebDriver):
        """Тест успешной авторизации.

        Args:
            driver: WebDriver - экземпляр веб-драйвера
        """
        login_page = LoginPage(driver)
        login_url = "http://example.com/login"  # Укажите правильный URL

        with allure.step("Открыть страницу авторизации"):
            login_page.open(login_url)

        with allure.step("Выполнить вход"):
            login_page.enter_username("admin")
            login_page.enter_password("password123")
            login_page.click_login_button()

        with allure.step("Проверить успешный вход"):
            assert "Dashboard" in driver.title, "Проверка не прошла: Dashboard не найден в заголовке."
