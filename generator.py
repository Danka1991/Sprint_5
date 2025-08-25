import random
import string

def generate_email():
    email_lenght = random.randint(5, 10)
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_lenght)) + "@yandex.ru"
    
    return email

def generate_password():
    password_lenght = random.randint(6, 10)
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_lenght))

    return password