import time
from texts import *
from art import *
import random as rand
from classes import *

#Objects

    #Enemies
SkeletonEnemy = enemy("Skeleton", 20, 6, False)
ZombieEnemy = enemy("Zombie", 30, 4, False)
OrcEnemy = enemy("Orc", 10, 10, False)
GoblinEnemy = enemy("Goblin", 15, 7, False)
BatEnemy = enemy("Bat",2, 2, False)
SpiderEnemy = enemy("Spider", 10, 4, False)

SkeletonBoss = enemy("Skeleton King", 40, 10, True)
ZombieBoss = enemy("Zombie king", 45, 6, True)
OrcBoss = enemy("Orc Lord", 30, 10, True)
DragonBoss = enemy("Dragon", 50, 12, True)
BatBoss = enemy("Man Bat",20, 5, True)
SpiderBoss = enemy("Large Spider", 35, 7, True)

    #Weapons

SteelSwordWeapon = weapons("Steel sword", 1, 5, 50, True)
WoodSwordWeapon = weapons("Wooden sword", 0.5, 1, 10, True)
AtgeirSpearWeapon = weapons("Atgeir spear", 3, 4, 75, True)
YariSpearWeapon = weapons("Yari spear", 3, 3, 45, True)
DanishAxeWeapon = weapons("Danish axe", 20, 0.1, 10, True)
BattleAxeWeapon = weapons("Battle axe", 2, 6, 60, True)
GolokSwordWeapon = weapons("Golok sword", 0.5, 5.5, 60, True)
DaodacSwordWeapon = weapons("Daodac Sword", 1, 8, 95, True)
DefaultDaggerWeapon = weapons("Rusty dagger", 3, 1, 1, True)

    #Items

potatoItem = items("Potato", 5, True, 2, False)
beefItem = items("Beef", 10, True, 5, False)
healingPoitionItem = items("Healing potion", 100, True, 100, False)
bronzeArtifactItem = items("Bronze artifact", 50, False, 0, False)
silverArtifactItem = items("Silver artifact", 100, False, 0, False)
goldArtifactItem = items("Gold artifact", 200, False, 0, False)

# VAL
inventory_weapon = [DefaultDaggerWeapon]
inventory_item = [potatoItem]
equippedItem = inventory_weapon[0]
blacksmith_item_list_all = [SteelSwordWeapon, WoodSwordWeapon, AtgeirSpearWeapon, YariSpearWeapon, DanishAxeWeapon, BattleAxeWeapon, GolokSwordWeapon, DaodacSwordWeapon]
item_shop_item_list = [potatoItem, beefItem, healingPoitionItem, bronzeArtifactItem, silverArtifactItem, goldArtifactItem]
full_health = 30
chest_list_item = [potatoItem, beefItem, healingPoitionItem]
chest_list_weapon = []

#Functions

def ChooseCharacter():
    global player
    global player_name
    global player_house
    print("What Is Your Name Explorer?")
    player_name = input("-> ")

    while True:
        
        print("\n"* 35)
        print("You May Choose Between Three Different Character With Three Different Backgrounds...\n")
        print("      ----------------------------------------\n")
        print("       1.   Knight, Choose To Learn More...")
        print("       2.   Blacksmith, Choose To Learn More...")
        print("       3.   Farmer, Choose To Learn More...\n")
        print("      ----------------------------------------\n")
        try:
            character_choice = int(input("Choose Backstory -> "))
            


            print("\n"*3)

            if character_choice == 1:
                character = "Knight"
                player_house = "Castle"
                title = "Sir"
                surname = "the Dragon Slayer"
                inventory_size = 6
                bank = 1000
                xp_multiplier = 1.2
                damage_reduction = 0.9
                damage_multiplier = 1.2
                weapon_price_reduction = 1
                item_price_reduction = 1

                print("\n"*30)
                print_backstory_1()
                print("\n")

                confirm_character = input("Want To Use This Character? y/n -> ")
                if confirm_character == "y":
                    player = Player(player_name, character, player_house, title, surname, 30, 0, inventory_size, bank, xp_multiplier, damage_reduction, damage_multiplier, weapon_price_reduction, item_price_reduction)
                    print("Character Confirmed...")
                    print("\n"*40)
                    break
                else:
                    print("")
            elif character_choice == 2:
                character = "Blacksmith"
                player_house = "house"
                title = ""
                surname = "Ironhill"
                inventory_size = 10
                bank = 700
                xp_multiplier = 1.2
                damage_reduction = 1
                damage_multiplier = 1.2
                weapon_price_reduction = 0.6
                item_price_reduction = 1
                print("\n"*30)
                print_backstory_2()
                print("\n")

                confirm_character = input("Want To Use This Character? y/n -> ")
                if confirm_character == "y":
                    player = Player(player_name, character, player_house, title, surname, 30, 0, inventory_size, bank, xp_multiplier, damage_reduction, damage_multiplier, weapon_price_reduction, item_price_reduction)
                    print("Character Confirmed...")
                    print("\n"*40)
                    break
                else:
                    print("")
            elif character_choice == 3:
                character = "Farmer"
                player_house = "Barn"
                title = ""
                surname = "Fairbairns"
                inventory_size = 6
                bank = 300
                xp_multiplier = 1
                damage_reduction = 1
                damage_multiplier = 1.1
                weapon_price_reduction = 1
                item_price_reduction = 0.5
                print("\n"*40)
                print_backstory_3()
                print("\n")

                confirm_character = input("Want To Use This Character? y/n -> ")
                if confirm_character == "y":
                    player = Player(player_name, character, player_house, title, surname, 30, 0, inventory_size, bank, xp_multiplier, damage_reduction, damage_multiplier, weapon_price_reduction, item_price_reduction)
                    print("Character Confirmed...")
                    print("\n"*40)
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
        print("\n"*3)
        print("Weapons:")
        item_slot = 1
        for items in inventory_weapon:
            print(item_slot,", ",items.weapon_name,",")
            item_slot += 1
        print()
        item_slot = 1
        print("Items:")
        for items in inventory_item:
            print(item_slot,", ",items.item_name,",")
            item_slot += 1
        print("Equipped weapon: ",equippedItem.weapon_name)
        inventory_choice = int(input("1: Equip Item, 2: Use healing item, 3: Go Back -> "))

        if inventory_choice == 1:
            print("This is your current equipped item: ",equippedItem.weapon_name)
            item_slot = 1
            for items in inventory_weapon:
                print(item_slot,", ",items.weapon_name,",")
                item_slot += 1
            print()
            itemToEquip = int(input("Choose one of the slots, starting with 1 -> "))
            itemToEquip -= 1

            equippedItem = inventory_weapon[itemToEquip]

        elif inventory_choice == 2:
            item_slot = 1
            for items in inventory_item:
                print(item_slot,", ",items.item_name,",")
                item_slot += 1
            print()
            while True:
                itemToEquip = int(input("Choose one of the slots, starting with 1 -> "))
                itemToEquip -= 1

                item_to_be_used = inventory_item[itemToEquip]

                if item_to_be_used.isHealingItem == True:
                    player.player_health += item_to_be_used.healing_power
                    print("Health restored!")
                    print("You now have",player.player_health,"HP!")
                    inventory_item.pop(itemToEquip)
                    break
                else: 
                    print("Please choose a healing item")
                    print("1. Try again, 2. Go back")
                    retry_equip_choice = int(input("-> "))

                    if retry_equip_choice == 2:
                        break
                    else:
                        print()

        elif inventory_choice == 3:
            print("You go back...\n")
            break

def addItemToInventory(itemToAdd):
    if itemToAdd.isWeapon == True:
        inventory_weapon.append(itemToAdd)
    elif itemToAdd.isWeapon == False:
        inventory_item.append(itemToAdd)

def getRandomItem():
    rand_item_int = rand.randint(0, 5)
    randomItem = item_shop_item_list[rand_item_int]
    return randomItem

def getRandomWeapon():
    rand_weapon_int = rand.randint(0, 7)
    randomWeapon = blacksmith_item_list_all[rand_weapon_int]
    return randomWeapon

def RandomMonster():
    random_monster_int = rand.randint(1, 6)

    if player.boss_spawn == 10:
        player.boss_spawn = 0

        if random_monster_int == 1:
            return SkeletonBoss
        elif random_monster_int == 2:
            return ZombieBoss
        elif random_monster_int == 3:
            return OrcBoss
        elif random_monster_int == 4:
            return DragonBoss
        elif random_monster_int == 5:
            return BatBoss
        elif random_monster_int == 6:
            return SpiderBoss

    else:    
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
    enemy_health_check = 0
    monster_type = RandomMonster()
    print("\n"*6)
    print("A ",monster_type.enemy_name," appeard!")
    
    if monster_type.enemy_health <= 0:
        monster_type.enemy_health = 10


    while True:
        if monster_type.enemy_health <= 0 and enemy_health_check == 0:
            monster_type.enemy_health = 10
            enemy_health_check = 1

        if monster_type.enemy_health > 0:
            enemy_health_check = 1
            print("\n"*2)
            print("What is action",player.player_name)
            print("\n")
            print("Your health: ",player.player_health)
            print("Enemy health: ",monster_type.enemy_health)
            print("\n")
            print("1. Strike, 2. Block, 3. Flee")
            fight_input = int(input("-> "))

            if fight_input == 1:
                damage_dealt = round(equippedItem.weapon_damage * player.damage_multiplier, 1)

                print("You hit the enemy for ",damage_dealt,"HP!")
                monster_type.enemy_health -= equippedItem.weapon_damage * player.damage_multiplier
                monster_type.enemy_health = round(monster_type.enemy_health, 1)

                enemy_strike_int = rand.randint(1,2)

                if enemy_strike_int == 1:
                    damage_taken = round(monster_type.enemy_damage * player.damage_reduction, 1)
                    print("The enemy hit you for",damage_taken,"HP!")
                    player.player_health -= monster_type.enemy_damage * player.damage_reduction
                    player.player_health = round(player.player_health, 1)
                
            elif fight_input == 2:
                print("You blocked an incoming attack!")
                print("Do you wish to open inventory to change weapon or use an item? y/n")
                block_choice = input("-> ")

                if block_choice == "y":
                    openInventory()
                else:
                    pass
            
            elif fight_input == 3:
                print("You choose to flee the battle!")
                print("\n"*2)
                break

            if player.player_health <= 0:
                print("\n"*35)
                print("You died!")
                gameOverArt()
                time.sleep(2)
                print("\n"*10)
                ShowCredits()
                QuitGame()

        elif monster_type.enemy_health <= 0:
            if monster_type.enemy_is_boss == True:
                xp_to_earn = round(rand.randint(5, 8) * player.xp_multi, 1)
                money_to_earn = rand.randint(30, 50)

            else:
                xp_to_earn = round(rand.randint(1, 5) * player.xp_multi, 1)
                money_to_earn = rand.randint(10, 30)

            
            player.bank += money_to_earn

            old_player_level = player.player_level
            player.current_xp += xp_to_earn

            if player.current_xp >= 20:
                player.current_xp -= 20
                player.player_level += 1
                player.boss_spawn += 1

            print("\n\nYou Slain The Enemy!")
            print("You earned ",money_to_earn," coins and ",xp_to_earn," experience points!")
            print("Your bank balance is now ",player.bank," coins!")
            if player.player_level > old_player_level:
                print("You have leveled up!")
            else:
                pass
            print("Your level is",player.player_level,", XP remaining to next level: ",player.current_xp,"/",20,"")
            time.sleep(2)
            break

def chestRoom():
    print("\n"*5)
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
        player.bank += money_to_recive
        print("Player balance is ",player.bank," coins!")

def GenerateRoom():
    random_room_int = rand.randint(1, 2)

    if random_room_int == 1:
        chestRoom()
            
    elif random_room_int == 2:
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
        print("\n"*2)
        if direction_choice == "1":
            print("You choose to turn left...")
            print("\n"*2)
            GenerateRoom()
        elif direction_choice == "2":
            print("You choose to go forward...")
            print("\n"*2)
            GenerateRoom()
        elif direction_choice == "3":
            print("You choose to turn right...")
            print("\n"*2)
            GenerateRoom()
        elif direction_choice == "4":
            print("\n"*2)
            openInventory()
        elif direction_choice == "5":
            print("Your turn back...")
            print("\n"*2)
            break


def Home():

    if player.character == "Knight":
        print("\n"*40)
        at_home_castle_artwork()
        time.sleep(3)
    elif player.character == "Blacksmith":
        print("\n"*40)
        at_home_house_artwork()
        time.sleep(3)
    elif player.character == "Farmer":
        print("\n"*40)
        at_home_village_artwork()
        time.sleep(3)

    while True:
            try:
                print("\n"*40)
                print("You are home at your", player.player_house)
                print ("\n"*2)
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
                print("\n"*2)

                if home_action_choice == 1:
                    at_house()

                elif home_action_choice == 2:
                    blacksmith()

                elif home_action_choice == 3:
                    item_shop()

                elif home_action_choice == 4:
                    print("Your going out")
                    break
                elif home_action_choice == 5:     
                    QuitGame()
            except:
                print("Choose between numbers 1-5")
                input("Press Enter To Continue")
                
            
def at_house():
        try:
            while True:
                print("\n"*40)
                print ("Welcome home to your", player.player_house)
                print ("Choose what to do at your", player_house,",", player_name)
                print ('''
                        ----------------------------------------
                        1. Eat and sleep
                        2. Store items in chest
                        3. Open inventory
                        4. Go back
                        5. Save and quit
                        ----------------------------------------
                ''')
                print("What do you want to do ",player_name,"?")
                house_action_choice = int(input("-> "))
                if house_action_choice == 1:
                    player.player_health = full_health
                    print("You rest for the night...")
                    restArtwork()
                    print("\n"*4)
                    print("A new day! Your health has been restored!\n")
                    time.sleep(2)
                elif house_action_choice == 2:
                    while True:
                        print("\n"*50)
                        print ("Do you want to access the chest? 1. yes, 2. Go back")
                        home_chest_choice = int(input("-> "))
                        print("\n"*5)

                        if home_chest_choice == 1:
                            item_slot = 1
                            print("Player:")
                            print()
                            print("Weapons:")
                            for items in inventory_weapon:
                                print("",item_slot ,".", items.weapon_name,",")
                                item_slot += 1
                            item_slot = 1
                            print()
                            print("Items:")
                            for items in inventory_item:
                                print("",item_slot ,".", items.item_name,",")
                                item_slot += 1
                            item_slot = 1
                            print("\n"*2)
                            print("Chest:")
                            print()
                            print("Weapons:")
                            for chest_weapons in chest_list_weapon:
                                print("",item_slot ,".", chest_weapons.weapon_name,",")
                                item_slot += 1
                            item_slot = 1
                            print()
                            print("Items:")
                            for chest_items in  chest_list_item:
                                print("",item_slot ,".", chest_items.item_name,",")
                                item_slot += 1
                            item_slot = 1
                            print()
                            print()
                            chest_choice = int(input("1. Store item, 2. Take item -> "))
                            print("\n"*5)
                            if chest_choice == 1:
                                chest_choice_item = int(input("1. Store Item, 2. Store Weapon -> "))
                                if chest_choice_item == 1:
                                    item_slot = 1
                                    print("Items: ")
                                    for items in inventory_item:
                                        print(item_slot,",",  items.item_name)
                                        item_slot += 1
                                    item_to_add_to_chest = int(input("Choose Item To add to chest: "))
                                    item_to_add_to_chest -= 1

                                    chest_list_item.append(inventory_item[item_to_add_to_chest])
                                    inventory_item.pop(item_to_add_to_chest)
                                
                                elif chest_choice_item == 2:
                                    item_slot = 1
                                    print("Weapons: ")
                                    for items in inventory_weapon:
                                        print(item_slot,",",  items.weapon_name)
                                        item_slot += 1
                                    item_to_add_to_chest = int(input("Choose Item To add to chest: "))
                                    item_to_add_to_chest -= 1

                                    chest_list_weapon.append(inventory_weapon[item_to_add_to_chest])
                                    inventory_weapon.pop(item_to_add_to_chest)

                            elif chest_choice == 2:
                                
                                print("1. Take Weapons, 2. Take items")
                                item_chest_choice = int(input("-> "))

                                if item_chest_choice == 1:
                                    print("Weapons: ")
                                    item_slot = 1
                                    for items in chest_list_weapon:
                                        print("",item_slot ,".", items.weapon_name,",")
                                        item_slot += 1
                                    item_slot = 1
                                    print()

                                    item_to_take_from_chest = int(input("Choose Item To take from the chest: "))
                                    item_to_take_from_chest -= 1

                                    inventory_weapon.append(chest_list_weapon[item_to_take_from_chest])
                                    chest_list_weapon.pop(item_to_take_from_chest)
                                
                                elif item_chest_choice == 2:
                                    print("Items: ")
                                    item_slot = 1
                                    for items in chest_list_item:
                                        print("",item_slot ,".", items.item_name,",")
                                        item_slot += 1
                                    item_slot = 1
                                    print()

                                    item_to_take_from_chest = int(input("Choose Item To take from the chest: "))
                                    item_to_take_from_chest -= 1

                                    inventory_item.append(chest_list_item[item_to_take_from_chest])
                                    chest_list_item.pop(item_to_take_from_chest)
                        
                        elif home_chest_choice == 2:
                            print("You go back..")
                            break

                elif house_action_choice == 3:
                    print("\n"*50)
                    openInventory()
                elif house_action_choice == 4:
                    print ("Going back...")
                    break
                elif house_action_choice == 5:
                    QuitGame()
        except:
            print ("Use numbers between 1-5")
            input("Press Enter To Continue")

def blacksmith():
    while True:
        print("Look at the weapons/armour to buy: 1, Leave: 2")
        item_menu_choice = int(input("-> "))

        if item_menu_choice == 1:
            print ("Welcome to the blacksmith")
            print("Your bank balance: ",player.bank," coins")
            print("All items that are available: ")

            item_slot = 1

            for items in blacksmith_item_list_all:
                print(item_slot,", ",items.weapon_name ," ",items.weapon_value,"")
                item_slot += 1
            print()
            itemToBuy = int(input("Choose What Item To Buy -> "))
            itemToBuy -= 1
            itemToBuyObject = blacksmith_item_list_all[itemToBuy]

            if player.bank >=  itemToBuyObject.weapon_value:
                player.bank -= itemToBuyObject.weapon_value
                addItemToInventory(blacksmith_item_list_all[itemToBuy])
                print("Your balance is now ",player.bank," coins!")
            else:
                print("Your bank balance is to low...")
        elif item_menu_choice == 2:
            break

def item_shop():
    while True:
        print("Look at the items to buy: 1, Leave: 2")
        item_menu_choice = int(input("-> "))

        if item_menu_choice == 1:
            print ("Welcome to the item shop")
            print("Your bank balance: ",player.bank," coins")
            print("All items that are available: ")
            item_slot = 1
            for items in item_shop_item_list:
                print(item_slot, items.item_name, end=":")
                print(items.item_value, "Coins")
                item_slot += 1

            print()
            itemToBuy = int(input("Choose What Item To Buy -> "))
            itemToBuy -= 1
            itemToBuyObject = item_shop_item_list[itemToBuy]

            if player.bank >=  itemToBuyObject.item_value:
                player.bank -= itemToBuyObject.item_value
                addItemToInventory(item_shop_item_list[itemToBuy])
                print("Your balance is now ",player.bank," coins!")
            else:
                print("Your bank balance is to low...")
        elif item_menu_choice == 2:
            break

def MovePlayer():
    while True:
        try:
            print("What Is Your Action", player.player_name,"?")
            print('''
                1. Explore the world.
                2. Go Home.
                ''')
            input_what_to_do = int(input("-> "))

            if input_what_to_do == 1:
                print("You choose to explore...")
                ChooseDirection()
            elif input_what_to_do == 2:
                print("You choose to go home...")
                Home()
        except:
                print("Use Numbers Between 1-2")
                input("Press Enter To Continue")    
                    

def Play():
    ChooseCharacter()
    MovePlayer()

def HowToPlay():
    print ('''\n 
    
    The Start:
    The game starts with a choice of three different charachters: A knighted Noblesman, a blacksmith or a farmer.    
    Whichever charachter you choose has access to a house, were you can rest or manage your chest and inventory.
    Each charachter also has a different background and life-experiences and therefore a different skillset. 
    Each charachter is thereby given a set of uniqe boosts which you can read more about in the charachter selection page. 
    Close to every charachters house you can go to the blacksmith for weapons and armor purchases and an item shop for item purchases.


    In-game systems:
    The game comes with a few systems to enhance gaming-experience. Among those are the Money-, XP- and the fighting-systems. 
    
    You can use money for buying weapons, armor and items in the blacksmith or the item shop and you can earn said money by defeating enemies in battle.
    Or by taking your rich parents money *cough *cough the Knight *cough *cough. 

    As for experience you can only gain it by defeating enemies in battle. 
    By gaining experience you will level up and by leveling up you will get chances to fight bosses in battle. 
        
    The game itself is based on a turn based fighting system where you travel the world while fighting enemies 
    by choosing one of the actions given by the game to progress further. 

    ''')

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
    print("\n"*20)
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