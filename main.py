from classes import *
from functions import *

while True:
    main_menu_choice = MainMenu()

    if main_menu_choice == 1:
        print("Play Placeholder\n")
        #Play()
        break
    elif main_menu_choice == 2:
        print("How To Play Placeholder\n")
        HowToPlay()
    elif main_menu_choice == 3:
        print("Credits Placeholder\n")
        ShowCredits()
    elif main_menu_choice == 4:
        QuitGame()
        break
    else:
        print("Please Use Numbers To Choose One Of The Options Above\n")
        time.sleep(2)