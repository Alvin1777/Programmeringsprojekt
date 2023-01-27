import time


def blacksmith_dialogue():
    try:
        while True:
            print("\n")
            print('''  
                                            The blacksmith greets you....


                                            - Hello Zhere!
                                                                    
                                                                    
                                                                    
                                            Respond with:
                                            1. Hello There 
                                            2. Goodbye (Leave)
                                            
                                            
                                            
                                            ''')
            
            intro_dialogue = int(input("->"))
            if intro_dialogue == 1:
                while True:
                    print('''
                                            Choose what else to say:
                                            1. What do you do here?
                                            2. Tell me a little bit about yourself. 
                                            3. Do you know this area well?
                                            4. Goodbye
                                            
                                            
                                            ''')
                    print ("\n"*3)
                    dialogue_option = int(input("->"))
                    if dialogue_option == 1:
                        print('''           
                                            - I forge veabons und armor for all zee beople around. Arh ! 
                                            Poth for zee farmers vanting broteczion und for zee zoltiers in zee area. 
                                            For eine brice hoffcourze.
                                            
                                            
                                            ''')
                        print("\n"*3)
                    elif dialogue_option == 2:
                        print('''           
                                            -I am zee local placksmith around. Arh ! 
                                            I don't know if you can hear it on mein accent put i come from Germany. 
                                            From zee great city of Bobbritzsch-Hilbersdorf to be exact. Arh ! 
                                            I movfed here vith mein family to sdart ein neues life after our homedovn vas purned dovn py zee French.
                                            
                                            
                                            ''')
                        print("\n"*3)
                    elif dialogue_option == 3:
                        while True:
                            print('''
                                                -Vell, I haffe now liffed here for almost ten years zo I know it guite vell. 
                                                Is zere anhyzing sbecific you vould like to know?
                                                
                                                Choose what to say:
                                                1. Can you tell me about all the monsters in the area?
                                                2.                                                 
                                                3. Not really (Go back)
                                                    
                                                    
                                                ''')
                            print("\n"*3)
                            dialogue_3 = int(input("->"))
                            if dialogue_3 == 1:
                                print ('''
                                                -Zee monsters in zee area? 
                                                Ja zere ist ein lot of zem. 
                                                TEXT PLACEHOLDER
                                ''')
                            elif dialogue_3 == 2:
                                print('''Text Placeholder''')
                            elif dialogue_3 == 3:                                
                                print('''Okej
                                ''')   
                                break 
                            else:
                                print('''-----Please choose between options 1-3-----''')

                    elif dialogue_option == 4:
                        print('''               
                                            - Koodpye, hobe to zee you akain!
                                            
                                            ''')
                        break
                    else:
                        print("Please choose options 1-4")
            elif intro_dialogue == 2: 
                print("")
                break
            else:
                print("Use Numbers Between 1 And 2")

    except ValueError:
        print("Use Numbers Between 1 And 2")
        time.sleep(1)
        input("Press Enter To Continue")
    except:
        print("An Error Was Detected")
        time.sleep(1)
        input("Press Enter To Continue")