


def blacksmith_dialogue():
    try:
        while True:
            print("\n")
            intro_dialogue = int(input('''  
                                            The blacksmith greets you....


                                            - Hello Zhere!
                                                                    
                                                                    
                                                                    
                                            Respond with:
                                            1. Hello There 
                                            2. Goodbye (Leave)
                                            
                                            
                                            
                                            '''))
            if intro_dialogue == 1:
                while True:
                    dialogue_option = int(input('''
                                            Choose what else to say:
                                            1. What do you do here?
                                            2. Tell me a little bit about yourself. 
                                            3. Do you know this area well?
                                            4. Goodbye
                                            
                                            
                                            '''))
                    print ("\n")
                    if dialogue_option == 1:
                        print('''           
                                            - I forge veabons und armor for all zee beople around. Arh ! 
                                            Poth for zee farmers vanting broteczion und for zee zoltiers in zee area. 
                                            For eine brice hoffcourze.
                                            
                                            
                                            ''')
                        print("\n")
                    elif dialogue_option == 2:
                        print('''           
                                            -I am zee local placksmith around. Arh ! 
                                            I don't know if vu can hear it on mein accent put i come from Germany. 
                                            From zee great city of Bobbritzsch-Hilbersdorf to exact. Arh ! 
                                            I movfed here vith mein family to sdart ein neues life after our homedovn vas purned dovn py zee French.
                                            
                                            
                                            ''')
                        print("\n")
                    elif dialogue_option == 3:
                        dialogue_3 = int(input('''
                                            -Vell, I haffe now liffed here for almost ten years zo I know it guite vell. 
                                            Is zere anhyzing sbecific you vould like to know?
                                            
                                            Choose what to say:
                                            1. 
                                            2.                                                 
                                            3. Not really (Go back)
                                                
                                                
                                            '''))
                        print("\n")
                        while True:
                            if dialogue_3 == 1:
                                print ('''Text Placeholder''')
                                break
                            elif dialogue_3 == 2:
                                print('''Text Placeholder''')
                                break
                            elif dialogue_3 == 3:
                                print('''Text Placeholder''')
                                break
                            else:
                                print('''-----Please choose between options 1-3-----''')
                    elif dialogue_option == 4:
                        print('''               - Koodpye, hobe to zee you akain!''')
                        break
                    else:
                        print("Please choose options 1-4")
            elif intro_dialogue == 2: #Intro dialogue - leave option
                print("")
                break
            else:
                print("")
    except:
        print("Please choose a number between 1 and 2")



blacksmith_dialogue()