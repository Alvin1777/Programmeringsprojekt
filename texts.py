from classes import *
from functions import *
from art import *

def HowToPlay():
    print("\n"*45)
   
    print ('''\n 
    ------------------------------------------------------------------------------------------------------------------------------------------

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

    ------------------------------------------------------------------------------------------------------------------------------------------
    ''')
   
    print()
    input("Press Enter To Continue")
    print("\n"*45)

def ShowCredits():
    print("\n"*45)
   
    print('''
                                            -----------------------------------
                                                        Created by:

                                                        Alvin Söderberg
                                                        Marcus Broman
                                                        Axel Österberg
                                            -----------------------------------
    ''')
    print("\n")
   
    print()
    input("Press Enter To Continue")

def print_backstory_1():
    print("\n"*45)
    print ('''\n
    -----------------------------------------------------------------------------------------------------------\n
    The Knight

    Your name and title: Sir name the Dragon Slayer

    The son of a rich nobleman. Knighted by the king and now serving in his personal guard. 
    Lives in his father's castle. The castle has access to a big sleeping-chamber where he can rest. 
    It has chefs and a big hall for feasts where he can drink, eat and feast. 
    Inside the castle walls there is also a blacksmith where weapons can be forged and a shop where items can be bought. 
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Choosing the Knight grants the following modifiers:
        - Honorable title (XP multiplier)
        - Rich family (Starts with much more money)
        - Strong armor (Damage taken reduction)
        - Combat trained (Damage multiplier)
        \n
    ----------------------------------------------------------------------------------------------------------- 
    ''')

def print_backstory_2():
    print("\n"*45)
    print ('''\n
    -----------------------------------------------------------------------------------------------------------\n
    The Blacksmith

    Your name: Name Ironhill

    A blacksmith, the son of a blacksmith, the grandson of a blacksmith. 
    This guy comes from generations and generations of blacksmiths and is still keeping the family legacy alive. 
    The blacksmith lives in a house built by his forefathers years ago, in a prosperous town including a shop where he can buy items. 
    And of course his own blacksmith where he can forge his own weapons and armor. 
    His house has among other things a bedroom where he can rest after a long day of work
    and a kitchen and dining room where he can eat and socialize with friends and family. 
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Choosing the blacksmith grants the following modifiers:
        - Strong weapons (Damage multiplier)
        - Family-legacy (Cheaper weapons)
        \n
    -----------------------------------------------------------------------------------------------------------
    ''')

def print_backstory_3():
    print("\n"*45)
    print ('''\n
    -----------------------------------------------------------------------------------------------------------\n
    The Farmer

    Your name: Name Fairbairns

    Like most people during this age, this guy is a farmer. And a poor one. And comes from a family of more poor farmers. 
    The farmer lives in a poor little village with other farmers and their families. 
    The little village has a communal kitchen where the farmer can cook. 
    The farmer sleeps on haystacks in a barn together with the other farmers. 
    The village has an item-shop where he can buy items and a blacksmith where he can buy weapons and armor, 
    if he can afford it. The farmer also has his own farm where he can grow his own food. 
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Choosing the farmer grants the following modifiers:
        	- Strong (Damage multiplier) 
	        - Self-grown crops (Cheaper food and item)
	        - Poor (Starts with less money)
            \n
    -----------------------------------------------------------------------------------------------------------
    ''')