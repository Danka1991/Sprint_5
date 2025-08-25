from data import Credantial
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from curl import profile_url, main_url

def sign_in(driver):
    # Проходим авторизацию
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.email_input_login))       
    driver.find_element(*Locators.email_input_login).send_keys(Credantial.email)
    driver.find_element(*Locators.password_input).send_keys(Credantial.password)
    driver.find_element(*Locators.button_entrance).click()
    return driver

def sign_in_and_go_to_personal_account(driver):
    driver.get(main_url) # Стартуем с главной страницы
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.personal_account_button)).click() # Ждем появление кнопки ЛК и нажимаем
    driver = sign_in(driver) # проходим авторизацию на странице /login
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.personal_account_button)).click() # Ждем появление кнопки ЛК, т.к. нас снова на мейн перекидывает и нажимаем
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(profile_url))
    return driver

def sign_up(driver, name, email, password):
    # Проходим авторизацию для регистрации
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.email_input_reg))       
    driver.find_element(*Locators.name_input).send_keys(name)   # Заполняем форму
    driver.find_element(*Locators.email_input_reg).send_keys(email)
    driver.find_element(*Locators.password_input).send_keys(password)
    driver.find_element(*Locators.register_button).click()
    return driver