from selenium.webdriver.support.wait import WebDriverWait
from curl import main_url
from selenium.webdriver.support import expected_conditions 
from locators import Locators

class TestConstructor:
  
    def test_constructor_sauces_tab(self, driver):
        driver.get(main_url) 
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.sauces_section)).click() # Переход к соусам
        activ_tab = driver.find_element(*Locators.active_section) # Поиск активного раздела 
        assert "Соусы" in activ_tab.text
       
    def test_constructor_fillings_tab(self, driver):
        driver.get(main_url) 
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.fillings_section)).click() # Переход к начинкам
        activ_tab = driver.find_element(*Locators.active_section) # Поиск активного раздела 
        assert "Начинки" in activ_tab.text
          
    def test_constructor_buns_tab(self, driver):
        driver.get(main_url) 
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.sauces_section)).click() # Переход к соусам
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.buns_section)).click() # Переход к булкам
        new_element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.active_section))
        assert new_element.is_displayed() # Проверка наличия активного раздела
        activ_tab = driver.find_element(*Locators.active_section) # Поиск активного раздела 
        assert "Булки" in activ_tab.text