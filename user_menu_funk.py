import csv

bookkaus = {}


# Valinta 1.- Selaa kaikki näytökset


def lataa_tiedot() -> list:
    """Lataa leffatiedot"""
    """Leffalistaa ladataan ulkopuoliselta resursilta, sen ei voi muokata"""
    with open("elokuvat.csv", "r") as tiedosto:
        count = 0
        list_to_dict = []
        leffalista = {}
        reader = csv.reader(tiedosto)
        headers = next(reader)

        print("")

        for row in reader:
            print(f'Position : {count}')
            print(f'{headers[0]}     : {row[0]}')
            print(f'{headers[1]}    : {row[1]}')
            print(f'{headers[-1]}     : {row[-1]}')
            print("")

            list_to_dict = (f'{row[0]}, {row[1]}, {row[-1]}')
            list_to_dict
            leffalista = dict({count: list_to_dict})

            count += 1
        with open('out.txt', 'w') as tiedosto:
            tiedosto.writelines(f'{row}\n' for row in leffalista)

        print("LEFFALISTA::::", leffalista)
        print("Valitse elokuva posiition perusteella:")
        pos = input("Positio: ")

        """Kirjoitetaan leffalistaa tiedostoon ja kaikki toimeenpiteet tehdään vain sen listan kanssa """
        """Haetaan posiition perusteella näytös"""

        with open("bookkaus.txt", "a") as tiedosto:
            for nimi, maara in bookkaus.items():
                rivi = f"{nimi},{maara}\n"
                tiedosto.write(rivi)


# Valinta 6.- Tallenna valintasi
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
    lataa_tiedot()
