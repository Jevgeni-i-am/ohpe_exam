import sys
import time
import index


def intro_text():
    """ Ensimmäinen valikko, joka kertoa loggaamis ohjeet
    Admin ja User login vaihtoehdot"""
    print("___________________________")
    print("Tervetuloa leffateatteriin! ")
    print("Kirjaudu järjestelmään.")
    print("")
    print("<--------Asiakas:---------> ")
    print("login - user && pass - user")
    print("")
    print("<-------Ylläpitäjä:-------> ")
    print("login - admin && pass - admin")
    print("")
    print("<---------LOPETUS:---------> ")
    print("login - 0 && pass - 0")
    print("________________________")


# Teksti kirjoitettu hitaasti...
def hidas_tekstin_printtaus(mjono: str, nopeus: int):
    for l in mjono:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(nopeus)


def uloskirjautuminen():
    """Kirjaudutaan ulos ja palataan ensimmäiseen INTRO ikkunaan"""
    index.start_screen()


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
    hidas_tekstin_printtaus("Esimerkki merkkijono", 0.1)
