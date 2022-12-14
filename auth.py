def login_function():

    while True:
        tunnnus = input("Syötä käyttäjätunnuksen: ")
        salasana = input("Syötä salasana: ")
        if tunnnus == "admin" and salasana == "admin":
            adminIsLogged = True
            userIsLogged = False
            break
        elif tunnnus == "user" and salasana == "user":
            userIsLogged = True
            adminIsLogged = False
            break
        elif tunnnus == "0" and salasana == "0":
            print("Lopetetaan ohjelmaa....")
            break

        else:
            print("Väärä käyttäjätunnus tai salasana.")
            print("Kokeile uudestaan!")

    return adminIsLogged, userIsLogged


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
    login_function()
