from classes import *
from functions import *
from art import *

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
PrintTitleScreen()
print("\n\n\n\n")
time.sleep(3)

while True:
    main_menu_choice = MainMenu()

    if main_menu_choice == 1:
        Play()
        break
    elif main_menu_choice == 2:
        HowToPlay()
    elif main_menu_choice == 3:
        ShowCredits()
    elif main_menu_choice == 4:
        QuitGame()
        break
    else:
        print("Please Use Numbers To Choose One Of The Options Above\n")
        time.sleep(2)
