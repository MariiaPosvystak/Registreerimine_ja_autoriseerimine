from ast import Break
from Module_1 import *
lae_failist()
while True:
    print("Valikud:")
    print("1. Registreeri")
    print("2. Autoriseeri")
    print("3. Välju")
    try:
        valik = int(input("Vali valik: "))
        if valik == 1:
            while True:
                kasutajanimi = str(input("Sisesta kasutajanimi: ")).lower()
                if kasutajanimi in usernames:
                    print("Kasutajanimi on juba olemas. Palun proovi uuesti.")
                    continue
                else:
                    break 
            parooli_valik = str(input("Genereeri parool automaatselt? (jah/ei): ")).lower()
            while True:
                if parooli_valik == "jah" or parooli_valik == "ei":
                    break
                else:
                    print("Sisesta ainult jah või ei")
            
            if parooli_valik.lower() == 'jah':
                parool = generate_password_auto()
                print(f"Genereeritud parool: {parool}")  
            else:
                while True:
                    parool = input("Sisesta parool: ")
                    if is_valid_password(parool):
                        break
                    else:
                        print("Parool ei vasta nõuetele. Palun proovi uuesti.")
            register_user(kasutajanimi, parool)
        elif valik == 2:
            while True:
                kasutajanimi = str(input("Sisesta kasutajanimi: "))
                parool = str(input("Sisesta parool: "))
                if authorize_user(kasutajanimi, parool):
                    print("Sa oled süsteemi sisse loginud")
                    break
                else:
                    print("Parool ei sobi")
        elif valik == 3:
            print("Väljumine...")
            break
        else:
            print("Vale valik. Palun proovi uuesti.")
    except ValueError:
        print("Vale formaat!")