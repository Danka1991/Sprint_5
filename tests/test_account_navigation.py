from selenium.webdriver.support.wait import WebDriverWait
from curl import login_url, main_url, profile_url
from selenium.webdriver.support import expected_conditions 
from locators import Locators
from helper import sign_in_and_go_to_personal_account

class TestGoToPersonalAccount: # Переход по клику на «Личный кабинет».
    def test_go_to_personal_account(self, driver): 
        driver = sign_in_and_go_to_personal_account(driver) # Проходим авторизацию на странице /login и проходим в ЛК
        assert driver.current_url == profile_url # Проверяем что мы на странице профиля

class TestTransitionToConstructorByConstructor:  # Переход из личного кабинета в конструктор по кнопке «Конструктор»
    def test_check_transition_by_constructor_btn(self, driver):
        driver = sign_in_and_go_to_personal_account(driver) # Проходим авторизацию на странице /login и проходим в ЛК
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.constructor_button)).click()  # Ожидание появления кнопки Конструктор и нажимаем 
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_url))
        assert driver.current_url == main_url # Проверяем что мы на главной странице

class TestTransitionToConstructorByLogo: # Переход из личного кабинета в конструктор клик по логотипу Stellar Burgers
   def test_transition_to_constructor_by_logo(self, driver):
        driver = sign_in_and_go_to_personal_account(driver) # Проходим авторизацию на странице /login и проходим в ЛК    
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.logo)).click()  # Ожидание перехода на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(main_url))
        assert driver.current_url == main_url # Проверяем что мы на главной странице 

class TestLogOutOfAccount: # Выход из аккаунта
    def test_log_out(self, driver):
        driver = sign_in_and_go_to_personal_account(driver) # Проходим авторизацию на странице /login и проходим в ЛК
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.button_exit)).click() # Нажимаем на кнопку "Выход"
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(login_url))
        assert driver.current_url == login_url # Проверяем что мы на старнице /login
       