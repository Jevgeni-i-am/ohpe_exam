import funktiot
import user_menu_funk


def user_menu():
    """Näyttää käyttöliittymän USER-oikeuksilla"""

    while True:
        print("")
        funktiot.hidas_tekstin_printtaus(
            "Tervetuloa leffateatterin!!!\n", 0.025)
        print(" ")
        print("Käytät USER-oikeudet.")
        print("Valitse seuraavista vaihtoehdoista:")
        print("")
        print("1.- Selaa kaikki näytökset ### _____OK")
        print("2.- Valitse näytös  ### _____NOK")
        print("3.- Valitse sali ### _____NOK")
        print("4.- Valitse kellonaika ### _____NOK")
        print("5.- Valitse istumapaikka ### _____NOK")
        print("6.- Tallenna valintasi ### _____NOK")
        print("7.- Tarkista oma varaus ### _____NOK")
        print("0.- Kirjaudu ulos ### _____OK")
        print("")
        try:
            valinta = input("Valintasi: ")
            valinta = int(valinta)
        except ValueError:
            print("Virhellinen valinta. Kokeilepas uudelleen.")
        if valinta == 1:
            print("1.- Selaa kaikki näytökset")
            user_menu_funk.lataa_tiedot()

        elif valinta == 2:
            print("2.- Valitse näytös")

        elif valinta == 3:
            print("3.- Valitse sali")

        elif valinta == 4:
            print("4.- Valitse kellonaika")

        elif valinta == 5:
            print("5.- Valitse istumapaikka")
        elif valinta == 6:
            print("6.- Tallenna valintasi")
            user_menu_funk.tallenna_tiedot()
        elif valinta == 7:
            print("7.- Tarkista oma varaus")
        elif valinta == 0:
            funktiot.hidas_tekstin_printtaus(
                "Kirjaudutaan ulos........\n", 0.05)
            funktiot.uloskirjautuminen()
            break
       # Ylimääräinen rivinvaihto
        print()


#
#
#
#####################
# ----------------- #
# -----TESTAUS----- #
# ----------------- #
#####################
#
#
#
if __name__ == "__main__":
    user_menu()
