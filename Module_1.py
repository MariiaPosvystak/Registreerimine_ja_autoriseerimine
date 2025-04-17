import random
import string

# Järjendid kasutajate nimede ja paroolide hoidmiseks
usernames = {}
passwords ={}


def salvesta_faili():
    try:
        with open ('Nimi.txt', 'w') as f:
            for username in usernames:
                    f.write(f"{username}:{passwords[username]}\n")
    except IOError as e:
            print(f"Error saving to file: {e}")

def lae_failist():
    try:
        with open('Nimi.txt', 'r') as f:
            for line in f:
                if line.strip():
                    username, password = line.strip().split(': ')
                    usernames[username] = username
                    passwords[username] = password
    except IOError as e:
        print(f"Error reading file: {e}")

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
def is_valid_password(parool: str) -> bool:
    """ Kontrollib, kas parool vastab nõuetele.
    Paroolis peab olema vähemalt üks number, suur täht, väike täht ja erimärk.
    :param password: Parool
    :type password: str
    :return: Kas parool vastab nõuetele
    :rtype: bool
    """
    has_digit = any(char.isdigit() for char in parool)
    has_upper = any(char.isupper() for char in parool)
    has_lower = any(char.islower() for char in parool)
    has_special = any(char in ".,:;!_*-+()/#¤%&" for char in parool)
    return has_digit and has_upper and has_lower and has_special

# Реєструє користувача, якщо ім'я користувача ще не існує і пароль відповідає вимогам.
def register_user(kasutajanimi: str, parool:str) -> any:
    """ Registreerib kasutaja.
    :param username: Kasutajanimi
    :type username: str
    :param password: Parool
    :type password: str
    :return: Kasutaja registreerimine õnnestus, vastav teade
    :rtype: any
    """
    kasutajanimi = kasutajanimi.lower()
    if kasutajanimi in usernames:
        print("Kasutajanimi on juba olemas!")
        return False
    if not is_valid_password(parool):
        print("Parool ei vasta nõuetele!")
        return False
    usernames[kasutajanimi] = kasutajanimi
    passwords[kasutajanimi] = parool
    try:
        with open('Nimi.txt', 'a') as f:
            f.write(f"{kasutajanimi}:{parool}\n")
    except IOError as e:
        print(f"Error appending to file: {e}")
        return False
    print("Kasutaja registreeritud!")
    return True

# Авторизує користувача, якщо ім'я користувача та пароль правильні.
def authorize_user(kasutajanimi: str, parool: str) -> any:
    """ Autoriseerib kasutaja.
    :param username: Kasutajanimi
    :type username: str
    :param password: Parool
    :type password: str
    :return: Kasutaja autoriseerimine õnnestus, vastav teade
    :rtype: any
    """
    if kasutajanimi in usernames and passwords[kasutajanimi] == parool:
        return True
    return False