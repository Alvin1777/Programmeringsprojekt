import time
from texts import *
from art import *
import random as rand
from classes import *



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
                            print("Player Inventory:") #players inventory
                            print()
                            print("Weapons:")          #players weapons
                            for items in inventory_weapon:
                                print("",item_slot ,".", items.weapon_name,",")
                                item_slot += 1
                            item_slot = 1
                            print("\n"*2)
                            print("Items:")             #players items
                            for items in inventory_item:
                                print("",item_slot ,".", items.item_name,",")
                                item_slot += 1
                            item_slot = 1
                            print("\n"*4)
                            print("Chest Inventory:")   #chest inventory
                            print()
                            print("Weapons:")           #chest weapons
                            for chest_weapons in chest_list_weapon:
                                print("",item_slot ,".", chest_weapons.weapon_name,",")
                                item_slot += 1
                            item_slot = 1
                            print("\n"*2)
                            print("Items:")             #chest items
                            for chest_items in  chest_list_item:
                                print("",item_slot ,".", chest_items.item_name,",")
                                item_slot += 1
                            item_slot = 1
                            print()
                            print()
                            #Do you want to extract or insert something to the chest?
                            chest_choice = int(input("1. Store to chest, 2. Extract from chest -> "))
                            print("\n"*5)
                            
                            #Store in chest
                            if chest_choice == 1:
                                #Do you want to store an item or a weapon?
                                chest_choice_item = int(input("1. Store Item, 2. Store Weapon -> "))
                                
                                #Store Weapon
                                if chest_choice_item == 1:
                                    item_slot = 1
                                    print("\n"*10)
                                    print("Weapons in inventory: ")
                                    for items in inventory_weapon:
                                        print(item_slot,",",  items.weapon_name)
                                        item_slot += 1
                                    print("\n"*5)
                                    item_to_add_to_chest = int(input("Choose Item To add to chest: "))
                                    item_to_add_to_chest -= 1

                                    chest_list_weapon.append(inventory_weapon[item_to_add_to_chest])
                                    inventory_weapon.pop(item_to_add_to_chest)
                                
                                #Store Item
                                elif chest_choice_item == 2:
                                    item_slot = 1
                                    print("\n"*10)
                                    print("Items in inventory: ")
                                    for items in inventory_item:
                                        print(item_slot,",",  items.item_name)
                                        item_slot += 1
                                    print("\n"*5)
                                    item_to_add_to_chest = int(input("Choose Item To add to chest: "))
                                    item_to_add_to_chest -= 1

                                    chest_list_item.append(inventory_item[item_to_add_to_chest])
                                    inventory_item.pop(item_to_add_to_chest)

                            #Extract from chest
                            elif chest_choice == 2:
                                #Do you want to store an item or a weapon?
                                item_chest_choice = int(input("1. Take Weapons, 2. Take Items -> "))
                                
                                #Take weapons
                                if item_chest_choice == 1:
                                    print("\n"*10)
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
                                
                                #Take items
                                elif item_chest_choice == 2:
                                    print("\n"*10)
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