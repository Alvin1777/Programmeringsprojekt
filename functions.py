import time
from texts import *

def ChooseCharacter():
    print("What Is Your Name Explorer?")
    player_name = input("-> ")

    while True:
        print("You May Choose Between Three Different Character With Three Different Backgrounds...\n")
        print("      ----------------------------------------\n")
        print("       1.   Nobleman, Choose To Learn More...")
        print("       2.   Blacksmith, Choose To Learn More...")
        print("       3.   Farmer, Choose To Learn More...\n")
        print("      ----------------------------------------\n")
        character_choice = input("Choose Backstory -> ")

        print("\n\n\n")

        if character_choice == "1":
            print("Stats and Backstory backstory 1")

            confirm_character = input("Want To Use This Character? y/n -> ")
            if confirm_character == "y":
                print("Character Confirmed...")
                break
            else:
                print("")
        elif character_choice == "2":
            print("Stats and Backstory backstory 2")

            confirm_character = input("Want To Use This Character? y/n -> ")
            if confirm_character == "y":
                print("Character Confirmed...")
                break
            else:
                print("")
        elif character_choice == "3":
            print("Stats and Backstory backstory 3")

            confirm_character = input("Want To Use This Character? y/n -> ")
            if confirm_character == "y":
                print("Character Confirmed...")
                break
            else:
                print("")

def Play():
    ChooseCharacter()

def HowToPlay():
    print("This Game Is Based On A Turn Based Fighting System Where You Travel The World By Choosing One Of The Actions Given By The Game To Progress Futher.")
    print("As You Level You Will Encounter New Bosses And Story Events.")
    input("")

def ShowCredits():
    print("")

def QuitGame():
    print("Game Shutting Down...")
    time.sleep(2)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def MainMenu():
    while True:
        print("\n\n\n")
        print("----------------------------------------\n")
        print("            1.    Play")
        print("            2. How To Play")
        print("            3.   Credits")
        print("            4.    Quit\n")
        print("----------------------------------------\n")

        try:
            main_menu_choice = int(input("What Is Your Action? -> "))
            return main_menu_choice
        except:
            print("Please Use Numbers To Choose One Of The Options Above\n")
            time.sleep(2)
