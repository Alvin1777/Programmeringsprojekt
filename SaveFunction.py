from functions import *
from classes import *
from main import *
from art import *
from texts import *

import pickle
 
filename = 'SaveFile'
 
def NewGame():
    new_user_name = input("New Username: ")
    new_user_age = int(input("New Age: "))
    new_user_town = input("New Town: ")
    new_user_height = int(input("New Height: "))
 
    new_userData = [new_user_name, new_user_age, new_user_town, new_user_height]
 
    return new_userData
 
try:
    testInfile = open(filename, 'rb')
    testInfile.close()
    doesSaveExist = True
except:
    doesSaveExist = False
 
if doesSaveExist == True:
    while True:
        user_save = input("You have an existing save, do you want to see it or create a new one? 1 = yes, 2 = no -> ")
 
        if user_save == "1":
            infile = open(filename,'rb')
            saved_stats = pickle.load(infile)
            infile.close()
 
            print(saved_stats)
               
            user_load = input("Do you want to load save or go back? 1, 2 -> ")
 
            if user_load == "1":
                current_userData = saved_stats
                break
 
            elif user_load == "2":
                print("")
 
        elif user_save == "2":  
            current_userData = NewGame()
            break
 
elif doesSaveExist == False:
    current_userData = NewGame()
 
userData = current_userData
 

 
def SaveData():   
    userData = []

    userData.append(player.player_name)
    userData.append(player.character)
    userData.append(player.player_house)
    userData.append(player.character_name_title)
    userData.append(player.character_name_surname)
    userData.append(player.player_health)
    userData.append(player.player_level)

    outfile = open(filename,'wb')
    pickle.dump(userData,outfile)
    outfile.close()

def InitiateSaveGame():
    while True:
        want_to_quit = input("Want to save files or see them? 1, 2, 3 -> ")
    
        if want_to_quit == "1":
            SaveData()
            quit()
    
        elif want_to_quit == "2":
            print(userData)
    
        elif want_to_quit == "3":
            print("Shutting Down...")
            quit()
