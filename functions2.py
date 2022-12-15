from classes import *
from texts import *
import time
from functions import *
from art import *



Placeholder_House = "PLACEHOLDER_HOUSE"
def Home():

    if player.character == "Knight":
        at_home_castle_artwork()
        #time.sleep(4)
    elif player.character == "Blacksmith":
        at_home_house_artwork()
        #time.sleep(4)
    elif player.character == "Farmer":
        at_home_village_artwork()
        #time.sleep(4)


    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("You are home at your", player.player_house)
        print ("\n\n")
        print('''You can now decide what to do at home...
                ----------------------------------------
                1. You can stay in your house and rest
                2. You can go to the blacksmith
                3. You can go to the item shop
                4. Go back out in the wild
                5. Quit and save
                ----------------------------------------        
        ''')
        home_action_choice = int(input('''Decide what to do -->  '''))

        if home_action_choice == 1:
            print ("PLACEHOLDER AT HOUSE")

        elif home_action_choice == 2:
            print ("PLACEHOLDER AT BLACKSMITH")

        elif home_action_choice == 3:
            print ("PLACEHOLDER AT ITEM SHOP")
        elif home_action_choice == 4:
            print("Your going out")
            break
        elif home_action_choice == 5:
            QuitGame()
        else:
            print("")
    