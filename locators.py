from selenium.webdriver.common.by import By

class Locators:
    # Кнопка "Войти в аккаунт" на главной странице
    login_button_main = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")

    # Логотип на главной странице
    logo = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo_')]/a")

    # Поле ввода "Email" на странице /login
    email_input_login = (By.XPATH, '//form[contains(@class,"Auth_form")]/fieldset[1]//input')

    # Поле ввода "Имя"
    name_input = (By.XPATH, '//form[contains(@class,"Auth_form")]/fieldset[1]//input')
    
    # Поле ввода "Email" на странице /register
    email_input_reg = (By.XPATH, '//form[contains(@class,"Auth_form")]/fieldset[2]//input')

    # Поле ввода "Пароля"
    password_input = (By.XPATH, '//*/input[@type="password"]')

    # Кнопка Войти на странице /login
    button_entrance = (By.XPATH, "//button[contains(text(), 'Войти')]")

    # Кнопка "Восстановить пароль" 
    button_recover_the_password = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")

    # Ссылка "Войти" 
    login_link = (By.XPATH, "//a[contains(text(), 'Войти')]")

    # Ссылка "Зарегистрироваться"
    register_link = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")

    # Кнопка "Личный Кабинет" на главной странице
    personal_account_button = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

    # Кнопка "Конструктор" на главной странице
    constructor_button = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    # Вкладка "Булки"
    buns_section = (By.XPATH, '//div[contains(@class,"tab_tab__1SPyG")]/span[contains(text(),"Булки")]')
    active_buns_section = (By.XPATH, '//div[contains(@class,"tab_tab__1SPyG tab_tab_type_current")]/span[contains(text(),"Булки")]')

    # Вкладка "Соусы"
    sauces_section = (By.XPATH, '//div[contains(@class,"tab_tab__1SPyG")]/span[contains(text(),"Соусы")]')
    
    # Вкладка "Начинки"
    fillings_section = (By.XPATH, '//div[contains(@class,"tab_tab__1SPyG")]/span[contains(text(),"Начинки")]')

    # Индикатор активного раздела
    active_section = (By.XPATH, '//div[contains(@class,"tab_tab_type_current")]') 

    # Кнопка "Регистрации"
    register_button = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

    # Ссылка "Некорректный пароль"
    password_error = (By.XPATH, '//p[contains(@class, "input__error")]')

    # Кнопка выхода
    button_exit = (By.XPATH, "//button[contains(text(), 'Выход')]")

    


    

    

    



    

