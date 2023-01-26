from classes import *
from functions import *
from art import *
from texts import *

print("\n"*10)
PrintTitleScreen()
print("\n"*4)
time.sleep(2)


while True:
    if is_game_closed == True:
        break
    print("\n"*45)
    PrintTitleScreen()
    print("\n"*4)
    main_menu_choice = MainMenu()

    if main_menu_choice == 1:
        Play()
    elif main_menu_choice == 2:
        HowToPlay()
    elif main_menu_choice == 3:
        ShowCredits()
    elif main_menu_choice == 4:
        QuitGame()
    else:
        print("Use Numbers Between 1-4")
        time.sleep(1)
        input("Press Enter To Continue")
