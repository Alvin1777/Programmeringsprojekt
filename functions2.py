from classes import *
from texts import *
import time
from functions import *
from art import *



Placeholder_House = "PLACEHOLDER_HOUSE"
def Home():

    #if  charachter == 1:
    time.sleep(2)
    at_home_castle()
    time.sleep(2)

    #if charachter == 2
    time.sleep(2)
    at_home_house()
    time.sleep(2)

    #if charachter == 3
    time.sleep(2)
    at_home_village() 
    time.sleep(2)


    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("You are home at your ", Placeholder_House)
        print ("\n\n")
        print('''You can now decide what to do at home...
                ----------------------------------------
                1. You can stay in your house and rest
                2. You can go to the blacksmith
                3. You can go to the item shop
                ----------------------------------------        
        ''')
        home_action_choise = input('''Decide what to do -->  ''')

        if home_action_choise == 1:
            print ("PLACEHOLDER AT HOUSE")

        elif home_action_choise == 2:
            print ("PLACEHOLDER AT BLACKSMITH")

        elif home_action_choise == 3:
            print ("PLACEHOLDER AT ITEM SHOP")

        else:
            print("")
    