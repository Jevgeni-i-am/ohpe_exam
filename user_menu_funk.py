import csv

bookkaus = {}
leffalista = []

# Valinta 1.- Selaa kaikki näytökset


def lataa_tiedot() -> list:
    """Lataa leffatiedot"""
    # tyhjennetään ensin kaikki nykyiset tuotteet
    global bookkaus
    bookkaus.clear()

    # Tiedoston nimi on aina sama
    with open("naytokset.csv", "r") as tiedosto:
        count = 0
        reader = csv.reader(tiedosto)
        headers = next(reader)
        if count == 0:
            print('Headers: ', headers[0],
                  headers[1], headers[-1], '# DELETE THIS LINE IN PROD !!!!')
            count += 1
        print("")
        if count != 0:
            for row in reader:
                print(f'Position : {count}')
                print(f'{headers[0]}     : {row[0]}')
                print(f'{headers[1]}    : {row[1]}')
                print(f'{headers[-1]}     : {row[-1]}')
                print("")
                count += 1



# Valinta 6.- Tallenna valintasi


def tallenna_tiedot():
    """Tallentaa varaustiedot tiedostoon"""
    # Tiedoston nimi on aina sama
    global bookkaus
    with open("bookkaus.csv", "w") as tiedosto:
        for nimi, maara in bookkaus.items():
            rivi = f"{nimi},{maara}\n"
            tiedosto.write(rivi)


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
