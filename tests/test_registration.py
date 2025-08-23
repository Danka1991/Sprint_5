from selenium.webdriver.support.wait import WebDriverWait
from curl import login_url, register_url
from generator import generate_email, generate_password
from selenium.webdriver.support import expected_conditions 
from locators import Locators
import pytest

class TestRegistration:

    email = generate_email()
    password = generate_password()

    @pytest.mark.parametrize("name,email,password,expected", [
        ("Nametest", email, password, True),  # Успешная регистрация
        ("Nametest", email, password, False),  # Попытка зарегистрировать пользователя еще раз
        ("", generate_email(), generate_password(), False),  # Пустое имя
        ("Nametest", "invalid-email", generate_password(), False),  # Неверный email
        ("Nametest", generate_email(), "123", False),  # Короткий пароль
        ("Nametest", generate_email(), "", False),  # Пустой пароль
    ])
    def test_registration_scenarios(self, driver, name, email, password, expected):
        driver.get(register_url)
        
        driver.find_element(*Locators.name_input).send_keys(name)   # Заполняем форму
        driver.find_element(*Locators.email_input_reg).send_keys(email)
        driver.find_element(*Locators.password_input).send_keys(password)
        driver.find_element(*Locators.register_button).click()
        
        if expected:
            WebDriverWait(driver, 10).until(expected_conditions.url_to_be(login_url)) # Проверяем успешную регистрацию - перенаправление на логин
            assert driver.current_url == login_url
        else:
            error = driver.find_elements(*Locators.password_error)   # Проверяем наличие ошибки
            assert len(error) > 0 or driver.current_url == register_url
