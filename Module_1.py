import random
import string

# Järjendid kasutajate nimede ja paroolide hoidmiseks
usernames = []
passwords = []

# Генерує випадковий пароль, який складається з 12 символів, включаючи цифри, великі та малі літери, а також спеціальні символи.
def generate_password_auto() -> str:
    """ Genereerib juhusliku parooli, mis koosneb 12 märgist.
    Paroolis peab olema vähemalt üks number, suur täht, väike täht ja erimärk.
    :return: Juhuslik parool
    :rtype: str
    """
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    return psword

# Генерує пароль довжиною `k` символів, який включає цифри та літери.
def generate_password_manual(k: int) -> str:
    """ Genereerib k märgist koosneva parooli, mis koosneb vähemalt ühest numbrist ja ühest tähest.
    :param k: Parooli pikkus
    :type k: int
    :return: Juhuslik parool
    :rtype: str
    """
    sala = ""
    for i in range(k):
        t = random.choice(string.ascii_letters)
        num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        t_num = [t, str(num)]
        sala += random.choice(t_num)
    return sala

# Перевіряє, чи відповідає пароль вимогам (містить цифри, великі та малі літери, спеціальні символи).
def is_valid_password(password: str) -> bool:
    """ Kontrollib, kas parool vastab nõuetele.
    Paroolis peab olema vähemalt üks number, suur täht, väike täht ja erimärk.
    :param password: Parool
    :type password: str
    :return: Kas parool vastab nõuetele
    :rtype: bool
    """
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(char in ".,:;!_*-+()/#¤%&" for char in password)
    return has_digit and has_upper and has_lower and has_special

# Реєструє користувача, якщо ім'я користувача ще не існує і пароль відповідає вимогам.
def register_user(username: str, password: str) -> any:
    """ Registreerib kasutaja.
    :param username: Kasutajanimi
    :type username: str
    :param password: Parool
    :type password: str
    :return: Kasutaja registreerimine õnnestus, vastav teade
    :rtype: tuple
    """
    if username in usernames:
        return False, "Username already exists."
    if not is_valid_password(password):
        return False, "Password does not meet the criteria."
    usernames.append(username)
    passwords.append(password)
    return True, "Registration successful."

# Авторизує користувача, якщо ім'я користувача та пароль правильні.
def authorize_user(username: str, password: str) -> any:
    """ Autoriseerib kasutaja.
    :param username: Kasutajanimi
    :type username: str
    :param password: Parool
    :type password: str
    :return: Kasutaja autoriseerimine õnnestus, vastav teade
    :rtype: tuple
    """
    if username in usernames:
        index = usernames.index(username)
        if passwords[index] == password:
            return True, "Authorization successful."
    return False, "Invalid username or password."

# Змінює пароль користувача, якщо старий пароль правильний і новий пароль відповідає вимогам.
def change_password(username: str, old_password: str, new_password: str) -> any:
    """ Muudab kasutaja parooli.
    :param username: Kasutajanimi
    :type username: str
    :param old_password: Vana parool
    :type old_password: str
    :param new_password: Uus parool
    :type new_password: str
    :return: Parooli muutmine õnnestus, vastav teade
    :rtype: tuple
    """
    if authorize_user(username, old_password)[0]:
        if is_valid_password(new_password):
            index = usernames.index(username)
            passwords[index] = new_password
            return True, "Password changed successfully."
        else:
            return False, "New password does not meet the criteria."
    return False, "Authorization failed."

# Відновлює пароль користувача, генеруючи новий випадковий пароль.
def reset_password(username: str) -> any:
    """ Taastab kasutaja parooli.
    :param username: Kasutajanimi
    :type username: str
    :return: Parooli taastamine õnnestus, vastav teade
    :rtype: tuple
    """
    if username in usernames:
        new_password = generate_password_auto()
        index = usernames.index(username)
        passwords[index] = new_password
        return True, f"New password is: {new_password}"
    return False, "Username not found."
