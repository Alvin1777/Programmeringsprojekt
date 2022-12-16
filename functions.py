import time
from texts import *
from art import *
import random as rand
from classes import *
import pickle


#For Save Files
filename = "SaveFile"

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
DefaultDaggerWeapon = weapons("Rusty dagger", 3, 1, 1)

#Items

potatoItem = items("Potato", 5, True, 2)
beefItem = items("Beef", 10, True, 5)
healingPoitionItem = items("Healing potion", 100, True, 100)
bronzeArtifactItem = items("Bronze artifact", 50, False, 0)
silverArtifactItem = items("Silver artifact", 100, False, 0)
goldArtifactItem = items("Gold artifact", 200, False, 0)

# PLACEHOLDER VAL

player_damage = 5
inventory = [DefaultDaggerWeapon]
equippedItem = inventory[0]
blacksmith_item_list_all = [SteelSwordWeapon, WoodSwordWeapon, AtgeirSpearWeapon, YariSpearWeapon, DanishAxeWeapon, BattleAxeWeapon, GolokSwordWeapon, DaodacSwordWeapon]
blacksmith_item_list_1 = [SteelSwordWeapon, WoodSwordWeapon, AtgeirSpearWeapon, YariSpearWeapon]
blacksmith_item_list_2 = [DanishAxeWeapon, BattleAxeWeapon, GolokSwordWeapon, DaodacSwordWeapon]
item_shop_item_list = [potatoItem, beefItem, healingPoitionItem, bronzeArtifactItem, silverArtifactItem, goldArtifactItem]
player_bank = 100
full_health = 30
chest_list = []

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
    global equippedItem
    while True:
        print("\n\n\n")
        for items in inventory:
            print(items.weapon_name, end=", ")
            print()
        print("Equipped weapon: ",equippedItem.weapon_name)
        inventory_choice = int(input("1: Equip Item, 2: Go Back -> "))

        if inventory_choice == 1:
            print("This is your current equipped item: ",equippedItem.weapon_name)
            for items_2 in inventory:
                print(items_2.weapon_name, end=", ")
            print()
            itemToEquip = int(input("Choose one of the slots, starting with 1 -> "))
            itemToEquip -= 1

            equippedItem = inventory[itemToEquip]
        elif inventory_choice == 2:
            print("You go back...\n")
            break

def addItemToInventory(itemToAdd):
    if len(inventory) < player.inventory_size:
        inventory.append(itemToAdd)
    else:
        print("Can't pick up the item. Your inventory is full")

def getRandomItem():
    rand_item_int = rand.randint(0, 5)
    randomItem = item_shop_item_list[rand_item_int]
    return randomItem

def getRandomWeapon():
    rand_weapon_int = rand.randint(0, 8)
    randomWeapon = blacksmith_item_list_all[rand_weapon_int]
    return randomWeapon

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
    global player_bank
    monster_type = RandomMonster()
    print("\n\n\n\n\n\n")
    print("A ",monster_type.enemy_name," appeard!")

    while True:
        if monster_type.enemy_health > 0:
            print("\n\n")
            print("What is action",player.PrintPlayerName())
            print("\n")
            print("Your health: ",player.player_health)
            print("Enemy health: ",monster_type.enemy_health)
            print("\n")
            print("1. Strike, 2. Block, 3. Flee")
            fight_input = int(input("-> "))

            if fight_input == 1:
                print("You hit the enemy for ",equippedItem.weapon_damage,"HP!")
                monster_type.enemy_health -= equippedItem.weapon_damage
                
            enemy_strike_int = rand.randint(1,2)

            if enemy_strike_int == 1:
                print("The enemy hit you for",monster_type.enemy_damage,"HP!")
                player.player_health -= monster_type.enemy_damage

            if player.player_health <= 0:
                print("\n\n")
                print("You died!")
                print("GAME OVER")
                QuitGame()

        else:
            money_to_earn = rand.randint(10, 30)
            player_bank += money_to_earn
            print("\n\nYou Slain The Enemy!")
            print("You earned ",money_to_earn," coins!")
            print("Your bank balance is now ",player_bank," coins!")
            time.sleep(2)
            break

def chestRoom():
    global player_bank
    print("\n\n\n\n\n")
    print("Chest Room")
    chest_recvie_item = rand.randint(1, 3)

    if chest_recvie_item == 1:
        print("You found a weapon!")
        weapon_to_recive = getRandomWeapon()
        print("A ",weapon_to_recive.weapon_name,)
        addItemToInventory(weapon_to_recive)
    elif chest_recvie_item == 2:
        print("You found a item!")
        item_to_recive = getRandomItem()
        print("A",item_to_recive.item_name)
        addItemToInventory(item_to_recive)
    elif chest_recvie_item == 3:
        print("You found coins!")
        money_to_recive = rand.randint(20, 50)
        print("",money_to_recive," coins!")
        player_bank += money_to_recive
        print("Player balance is ",player_bank," coins!")

def GenerateRoom():
    random_room_int = rand.randint(1, 3)

    if random_room_int == 1:
        chestRoom()
            
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
        print("\n\n")
        if direction_choice == "1":
            print("You choose to turn right...")
            print("\n\n")
            GenerateRoom()
        elif direction_choice == "2":
            print("You choose to go forward...")
            print("\n\n")
            GenerateRoom()
        elif direction_choice == "3":
            print("You choose to turn left...")
            print("\n\n")
            GenerateRoom()
        elif direction_choice == "4":
            print("\n\n")
            openInventory()
        elif direction_choice == "5":
            print("Your turn back...")
            print("\n\n")
            break


def Home():

    if player.character == "Knight":
        at_home_castle_artwork()
        time.sleep(3)
    elif player.character == "Blacksmith":
        at_home_house_artwork()
        time.sleep(3)
    elif player.character == "Farmer":
        at_home_village_artwork()
        time.sleep(3)

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
        print("\n\n")

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
        print("What do you want to do ",player_name,"?")
        house_action_choice = int(input("-> "))
        if house_action_choice == 1:
            player.player_health = full_health
            print("You rest for the night...")
            restArtwork()
            print("\n\n\n\n")
            print("A new day! Your health has been restored!\n")
            time.sleep(2)
        elif house_action_choice == 2:
            while True:
                print ("Do you want to add an item to the chest? 1. yes, 2. Go back")
                home_chest_choice = int(input("-> "))

                if home_chest_choice == 1:
                    for items in inventory:
                        print(items.weapon_name, end=", ")
                    print()
                    for chest_items in chest_list:
                        try:
                            print(chest_items.weapon_name, end=", ")
                        except:
                            print("Chest is empty...")
                    print()
                    chest_choice = int(input("1. Store item, 2. Take item -> "))
                    if chest_choice == 1:
                        item_to_add_to_chest = int(input("Choose Item To add to chest: "))
                        item_to_add_to_chest -= 1

                        chest_list.append(inventory[item_to_add_to_chest])
                        inventory.pop(item_to_add_to_chest)

                    elif chest_choice == 2:
                        item_to_take_from_chest = int(input("Choose Item To take from the chest: "))
                        item_to_take_from_chest -= 1

                        inventory.append(item_to_take_from_chest)
                        chest_list.pop(item_to_take_from_chest)
                
                elif home_chest_choice == 2:
                    print("You go back..")
                    break

        elif house_action_choice == 3:
            print ("Going back...")
            break
        elif house_action_choice == 4:
            QuitGame()
        else:
            print ("")

def blacksmith():
    global player_bank
    while True:
        print("Look at the weapons/armour to buy: 1, Leave: 2")
        item_menu_choice = int(input("-> "))

        if item_menu_choice == 1:
            print ("Welcome to the blacksmith")
            print("Your bank balance: ",player_bank," coins")
            print("All items that are available: ")
            for items in blacksmith_item_list_1:
                print(items.weapon_name, end=": ")
                print(items.weapon_value, end=" Coins, ")
            print()
            for items_2 in blacksmith_item_list_2:
                print(items_2.weapon_name, end=": ")
                print(items_2.weapon_value, end=" Coins, ")
            print()
            itemToBuy = int(input("Choose What Item To Buy -> "))
            itemToBuy -= 1
            itemToBuyObject = blacksmith_item_list_all[itemToBuy]

            if player_bank >=  itemToBuyObject.weapon_value:
                player_bank -= itemToBuyObject.weapon_value
                addItemToInventory(blacksmith_item_list_all[itemToBuy])
                print("Your balance is now ",player_bank," coins!")
            else:
                print("Your bank balance is to low...")
        elif item_menu_choice == 2:
            break

def item_shop():
    global player_bank
    while True:
        print("Look at the items to buy: 1, Leave: 2")
        item_menu_choice = int(input("-> "))

        if item_menu_choice == 1:
            print ("Welcome to the item shop")
            print("Your bank balance: ",player_bank," coins")
            print("All items that are available: ")
            for items in item_shop_item_list:
                print(items.item_name, end=": ")
                print(items.item_value, end=" Coins, ")
            print()
            for items_2 in item_shop_item_list:
                print(items_2.item_name, end=": ")
                print(items_2.item_value, end=" Coins, ")
            print()
            itemToBuy = int(input("Choose What Item To Buy -> "))
            itemToBuy -= 1
            itemToBuyObject = item_shop_item_list[itemToBuy]

            if player_bank >=  itemToBuyObject.item_value:
                player_bank -= itemToBuyObject.item_value
                addItemToInventory(item_shop_item_list[itemToBuy])
                print("Your balance is now ",player_bank," coins!")
            else:
                print("Your bank balance is to low...")
        elif item_menu_choice == 2:
            break

def MovePlayer():
    while True:
        print("What Is Your Action", player.player_name,"?")
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
                    
def ExistingSave():
    try:
        testInfile = open(filename, 'rb')
        testInfile.close()
        doesSaveExist = True
    except:
        doesSaveExist = False
    return doesSaveExist

def LoadSave():
    global player
    infile = open(filename,'rb')
    saved_stats = pickle.load(infile)
    infile.close()

    user_load = input("Do you want to load save or start a new game? 1, 2 -> ")

    if user_load == "1":
        player = Player(saved_stats[0], saved_stats[1], saved_stats[2], saved_stats[3], saved_stats[4], saved_stats[5], saved_stats[6], saved_stats[7])

    elif user_load == "2":
        ChooseCharacter()


def Play():
    found_save_game = ExistingSave()

    if found_save_game == True:
        LoadSave()
    elif found_save_game == False:
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

def SaveGame():
    save_game_choice = int(input("Do you want to save game? 1. yes, 2. no -> "))

    if save_game_choice == 1:
        user_data = [player.player_name, player.character, player.player_house, player.character_name_title, player.character_name_surname, player.player_health, player.player_level, player.inventory_size]

        outfile = open(filename,'wb')
        pickle.dump(user_data,outfile)
        outfile.close()

    elif save_game_choice == 2:
        pass

def QuitGame():
    SaveGame()
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