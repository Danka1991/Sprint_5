from selenium.webdriver.support.wait import WebDriverWait
from curl import login_url, main_url
from selenium.webdriver.support import expected_conditions 
from locators import Locators
from helper import sign_in

class TestLoginFromMainPage: # Вход по кнопке «Войти в аккаунт» на главной странице

    def test_login_from_main_page(self, driver):
        driver.get(main_url)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.login_button_main)).click()
        driver = sign_in(driver) # проходим авторизацию на странице /login
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_url))
        assert driver.current_url == main_url

class TestLoginFromRecoveryPage: # Вход через кнопку в форме восстановления пароля

    def test_login_from_recovery_page(self, driver):
        driver.get(login_url) # Переходим на страницу /login
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.button_recover_the_password)).click()  # Кликаем на восстановить пароль
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.login_link)).click()  # Ожидаем когда появится "Войти"
        driver = sign_in(driver) # проходим авторизацию на странице /login
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_url))
        assert driver.current_url == main_url

             
class TestCheckRegister: # Вход через кнопку в форме регистрации
    def test_login_from_recovery_page(self, driver):
        driver.get(login_url) # Переходим на страницу /login
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.register_link)).click() # Ожидаем появление ссылки на регистрацию
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.login_link)).click()  # Ожидаем когда появится "Войти"
        driver = sign_in(driver) # проходим авторизацию на странице /login
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_url))
        assert driver.current_url == main_url

class TestCheckEntranceFromRecoveryPage: # Вход через кнопку «Личный кабинет»
    def test_button_inscription_login(self, driver):
        driver.get(main_url)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.personal_account_button)).click()
        driver = sign_in(driver) # проходим авторизацию на странице /login
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_url))
        assert driver.current_url == main_url
