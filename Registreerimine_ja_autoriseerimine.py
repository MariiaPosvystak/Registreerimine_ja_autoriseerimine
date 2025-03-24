from Module_1 import *

def main():
    while True:
        print("\nValikud:")
        print("1. Registreeri")
        print("2. Autoriseeri")
        print("3. Muuda parooli")
        print("4. Taasta parool")
        print("5. Välju")
        valik = input("Vali valik: ")

        if valik == '1':
            while True:
                kasutajanimi = input("Sisesta kasutajanimi: ")
                if kasutajanimi in usernames:
                    print("Kasutajanimi on juba olemas. Palun proovi uuesti.")
                    continue
                parooli_valik = input("Genereeri parool automaatselt? (jah/ei): ")
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
                õnnestus, sõnum = register_user(kasutajanimi, parool)
                print(sõnum)
                if õnnestus:
                    break

        elif valik == '2':
            while True:
                kasutajanimi = input("Sisesta kasutajanimi: ")
                parool = input("Sisesta parool: ")
                õnnestus, sõnum = authorize_user(kasutajanimi, parool)
                print(sõnum)
                if õnnestus:
                    break
                else:
                    print("Vale kasutajanimi või parool. Palun proovi uuesti.")

        elif valik == '3':
            while True:
                kasutajanimi = input("Sisesta kasutajanimi: ")
                vana_parool = input("Sisesta vana parool: ")
                uus_parool = input("Sisesta uus parool: ")
                õnnestus, sõnum = change_password(kasutajanimi, vana_parool, uus_parool)
                print(sõnum)
                if õnnestus:
                    break
                else:
                    print("Parooli muutmine ebaõnnestus. Palun proovi uuesti.")

        elif valik == '4':
            while True:
                kasutajanimi = input("Sisesta kasutajanimi: ")
                õnnestus, sõnum = reset_password(kasutajanimi)
                print(sõnum)
                if õnnestus:
                    break
                else:
                    print("Kasutajanime ei leitud. Palun proovi uuesti.")

        elif valik == '5':
            print("Väljumine...")
            break

        else:
            print("Vale valik. Palun proovi uuesti.")

if __name__ == "__main__":
    main()