from selenium.webdriver.common.by import By

class Locators:
    # Кнопка "Войти в аккаунт" на главной странице
    login_button_main = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')

    # Логотип на главной странице
    logo = (By.XPATH, '//*[@id="root"]/div/header/nav/div')

    # Поле ввода "Email" на странице /login
    email_input_login = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')

    # Поле ввода "Имя"
    name_input = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    
    # Поле ввода "Email" на странице /register
    email_input_reg = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')

    # Поле ввода "Пароля"
    password_input = (By.XPATH, '//*/input[@type="password"]')

    # Кнопка Войти на странице /login
    button_entrance = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

    # Кнопка "Восстановить пароль" 
    button_recover_the_password = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')

    # Ссылка "Войти" 
    login_link = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')

    # Ссылка "Зарегистрироваться"
    register_link = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')

    # Кнопка "Личный Кабинет" на главной странице
    personal_account_button = (By.XPATH, '//*[@id="root"]/div/header/nav/a')

    # Кнопка "Конструктор" на главной странице
    constructor_button = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a')

    # Кнопка "Лента Заказов" на главной странице
    order_feed_button = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[2]/a/p')

    # Вкладка "Булки"
    buns_section = (By.XPATH, '//div[contains(@class,"tab_tab__1SPyG")]/span[contains(text(),"Булки")]')

    # Вкладка "Соусы"
    sauces_section = (By.XPATH, '//div[contains(@class,"tab_tab__1SPyG")]/span[contains(text(),"Соусы")]')
    
    # Вкладка "Начинки"
    fillings_section = (By.XPATH, '//div[contains(@class,"tab_tab__1SPyG")]/span[contains(text(),"Начинки")]')

    # Индикатор активного раздела
    active_section = (By.XPATH, '//div[contains(@class,"tab_tab_type_current")]') 

    # Кнопка "Регистрации"
    register_button = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

    # Ссылка "Некорректный пароль"
    password_error = (By.XPATH, '//p[contains(@class, "input__error")]')

    # Кнопка выхода
    button_exit = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')

    


    

    

    



    

