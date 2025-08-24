from selenium.webdriver.support.wait import WebDriverWait
from curl import login_url, register_url
from generator import generate_email, generate_password
from selenium.webdriver.support import expected_conditions 
from locators import Locators
from helper import sign_up
import pytest

class TestRegistration:

    email = generate_email()
    password = generate_password()
    name = "Nametest"

    def test_registration_scenario_valid(self, driver):# Проверка успешной регистрации
        driver.get(register_url)
        driver = sign_up(driver, self.name, self.email, self.password)
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(login_url)) # Проверяем успешную регистрацию - перенаправление на логин
        assert driver.current_url == login_url

    def test_cannot_register_existing_user(self, driver): # Нельзя зарегистрировать существующего пользователя
        driver.get(register_url)
        driver = sign_up(driver, self.name, self.email, self.password)
        assert driver.current_url == register_url  
         
class TestInvalidRegistrations:
    name = "Nametest"

    @pytest.mark.parametrize("name,email,password", [
        ("", generate_email(), generate_password()),  # Пустое имя
        (name, "invalid-email", generate_password()),  # Неверный email
        (name, generate_email(), "123"),  # Короткий пароль
        (name, generate_email(), ""),  # Пустой пароль
    ])
    def test_registration_scenarios_invalid(self, driver, name, email, password):
        driver.get(register_url)
        driver = sign_up(driver, name, email, password)
        error = driver.find_elements(*Locators.password_error)   # Проверяем наличие ошибки
        assert len(error) > 0 or driver.current_url == register_url      
           

