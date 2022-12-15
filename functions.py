import time
from texts import *
from art import *
import random as rand
from classes import *


# PLACEHOLDER VAL

player_damage = 5
inventory = ["hands"]
equippedItem = "hands"

#Objects

SkeletonEnemy = enemy("Skeleton", 20, 5, False)
ZombieEnemy = enemy("Zombie", 30, 4, False)
OrcEnemy = enemy("Orc", 10, 10, False)
GoblinEnemy = enemy("Goblin", 15, 7, False)
BatEnemy = enemy("Bat",2, 2, False)
SpiderEnemy = enemy("Spider", 10, 5, False)

#Weapons

SteelSwordWeapon = weapons("Steel sword", 1, 5, 50)
WoodSwordWeapon = weapons("Wooden sword", 0.5, 1, 10)
AtgeirSpearWeapon = weapons("Atgeir spear", 3, 4, 75)
YariSpearWeapon = weapons("Yari spear", 3, 3, 45)
DanishAxeWeapon = weapons("Danish axe", 20, 0.1, 10)
BattleAxeWeapon = weapons("Battle axe", 2, 6, 60)
GolokSwordWeapon = weapons("Golok sword", 0.5, 5.5, 60)
DaodacSwordWeapon = weapons("Daodac Sword", 1, 8, 95)



#Functions

def ChooseCharacter():
    global player
    global player_name
    global player_house
    print("What Is Your Name Explorer?")
    player_name = input("-> ")

    while True:
        
        print("\n\n\n\n\n\n\n\n\n")
        print("You May Choose Between Three Different Character With Three Different Backgrounds...\n")
        print("      ----------------------------------------\n")
        print("       1.   Knight, Choose To Learn More...")
        print("       2.   Blacksmith, Choose To Learn More...")
        print("       3.   Farmer, Choose To Learn More...\n")
        print("      ----------------------------------------\n")
        try:
            character_choice = int(input("Choose Backstory -> "))
            


            print("\n\n\n")

            if character_choice == 1:
                character = "Knight"
                player_house = "Castle"
                title = "Sir"
                surname = "the Dragon Slayer"
                inventory_size = 6
                print("\n\n\n\n\n\n\n\n\n")
                print_backstory_1()
                print("\n")

                confirm_character = input("Want To Use This Character? y/n -> ")
                if confirm_character == "y":
                    player = Player(player_name, character, player_house, title, surname, 30, 0, inventory_size)
                    player.print_info()
                    print("Character Confirmed...")
                    break
                else:
                    print("")
            elif character_choice == 2:
                character = "Blacksmith"
                player_house = "house"
                title = ""
                surname = "Ironhill"
                inventory_size = 6
                print("\n\n\n\n\n\n\n\n\n")
                print_backstory_2()
                print("\n")

                confirm_character = input("Want To Use This Character? y/n -> ")
                if confirm_character == "y":
                    player = Player(player_name, character, player_house, title, surname, 30, 0, inventory_size)
                    player.print_info()
                    print("Character Confirmed...")
                    break
                else:
                    print("")
            elif character_choice == 3:
                character = "Farmer"
                player_house = "Barn"
                title = ""
                surname = "Fairbairns"
                inventory_size = 6
                print("\n\n\n\n\n\n\n\n\n")
                print_backstory_3()
                print("\n")

                confirm_character = input("Want To Use This Character? y/n -> ")
                if confirm_character == "y":
                    player = Player(player_name, character, player_house, title, surname, 30, 0, inventory_size)
                    player.print_info()
                    print("Character Confirmed...")
                    
                    break
                else:
                    print("")
        except ValueError:
            input("Choose Between The Numbers 1-3. \nPress Enter To Try Again. ")
        except:
            input("An Error Was Detected. \nPress Enter To Try Again. ")
       
def openInventory():
    while True:
        print(inventory, equippedItem)
        inventory_choice = int(input("1: Equip Item, 2: Go Back -> "))

        if inventory_choice == 1:
            print("This is your current equipped item: ",equippedItem)
            print(inventory)
            itemToEquip = int(input("Choose one of the slots, starting with 1 -> "))
            itemToEquip -= 1

            equippedItem = inventory[itemToEquip]
        elif inventory_choice == 2:
            print("You go back...\n")
            break


def RandomMonster():
    random_monster_int = rand.randint(1, 6)

    if random_monster_int == 1:
        return SkeletonEnemy
    elif random_monster_int == 2:
        return ZombieEnemy
    elif random_monster_int == 3:
        return OrcEnemy
    elif random_monster_int == 4:
        return GoblinEnemy
    elif random_monster_int == 5:
        return BatEnemy
    elif random_monster_int == 6:
        return SpiderEnemy

def FightMonster():
    monster_type = RandomMonster()
    print("A ",monster_type.enemy_name," appeard!")

    while True:
        if monster_type.enemy_health > 0:
            print("What is action",player.PrintPlayerName())
            print("1. Strike, 2. Block, 3. Flee")
            fight_input = int(input("-> "))

            if fight_input == 1:
                print("You strike the enemy!")
                monster_type.enemy_health -= player_damage
                
            enemy_strike_int = rand.randint(1,2)

            if enemy_strike_int == 1:
                print("The enemy hit you!")
                player.player_health -= monster_type.enemy_damage
        else:
            print("You Slain The Enemy!")
            break


def GenerateRoom():
    random_room_int = rand.randint(1, 3)

    if random_room_int == 1:
        print("Chest Room")
        print("You recived an item.. *PLACEHOLDER* ")

    elif random_room_int in (2, 3):
        FightMonster()

        



def ChooseDirection():
    while True:
        print("Where do you wanna go?")
        print('''
            1: Left 
            2: Forward
            3: Right
            4: Open inventory
            5: Go back
            ''')

        direction_choice = input("-> ")

        if direction_choice == "1":
            print("You choose to turn right...")
            GenerateRoom()
        elif direction_choice == "2":
            print("You choose to go forward...")
            GenerateRoom()
        elif direction_choice == "3":
            print("You choose to turn left...")
            GenerateRoom()
        elif direction_choice == "4":
            openInventory()
        elif direction_choice == "5":
            print("Your turn back...")
            break
        


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
            at_house()

        elif home_action_choice == 2:
            blacksmith()

        elif home_action_choice == 3:
            blacksmith()

        elif home_action_choice == 4:
            print("Your going out")
            break
        elif home_action_choice == 5:
            
            QuitGame()
        else:
            print("")


def at_house():
    while True:
        print ("Welcome home to your", player.player_house)
        print ("Choose what to do at your", player_house,",", player_name)
        print ('''
                ----------------------------------------
                1. Eat and sleep
                2. Store items in chest
                3. Go back
                4. Save and quit
                ----------------------------------------
        ''')
        house_action_choice = int(input("What do you want to do", player_name))
        if house_action_choice == 1:
            print("PLACEHOLDER FOR RESTING")
        elif house_action_choice == 2:
            print ("PLACEHOLDER FOR CHEST")
        elif house_action_choice == 3:
            print ("Going back...")
            break
        elif house_action_choice == 4:
            QuitGame()
        else:
            print ("")

def blacksmith():
    while True:
        print ("")

def item_shop():
    while True:
        print ("")

def MovePlayer():
    while True:
        print("What Is Your Action", player_name,"?")
        print('''
            1. Explore the world.
            2. Go Home.
            ''')
        input_what_to_do = input("-> ")

        if input_what_to_do == "1":
            print("You choose to explore...")
            ChooseDirection()
        elif input_what_to_do == "2":
            print("You choose to go home...")
            Home()
                    

def Play():
    ChooseCharacter()
    MovePlayer()

def HowToPlay():
    print("\n This Game Is Based On A Turn Based Fighting System Where You Travel The World By Choosing One Of The Actions Given By The Game To Progress Futher.")
    print("As You Level You Will Encounter New Bosses And Story Events. \n")
    input("Press Enter To Continue")

def ShowCredits():
    print('''
                                                        Created by:

                                                        Alvin Söderberg
                                                        Marcus Broman
                                                        Axel Österberg
    ''')

    input("Press Enter To Continue")

def QuitGame():
    print("Game Shutting Down...")
    time.sleep(2)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    exit()


def MainMenu():
    while True:        
        print('''
                                          ----------------------------------------
                                                       1.    Play
                                                       2. How To Play
                                                       3.   Credits
                                                       4.    Quit
                                          ----------------------------------------
        ''')

        try:
            main_menu_choice = int(input("What Is Your Action? -> "))
            return main_menu_choice
        except:
            print("Please Use Numbers To Choose One Of The Options Above\n")
            time.sleep(2)


