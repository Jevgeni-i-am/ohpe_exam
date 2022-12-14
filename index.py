import funktiot
import auth
import user_menu
import admin_menu


def start_screen():
    funktiot.intro_text()
    admin, user = auth.login_function()

    if admin == True:
        admin_menu.admin_menu()
    elif user == True:
        user_menu.user_menu()
    else:
        print("Jotai meni pieleen. Auth-tarkastus epäonnistunut.")


#
#
#
#####################
# ----------------- #
# PÄÄOHJELMA        #
# ----------------- #
#####################
#
#
#
if __name__ == "__main__":
    start_screen()


# CREDITS:
# Movie dataset taken from Github, Tiangechen
# https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea#file-movies-csv
