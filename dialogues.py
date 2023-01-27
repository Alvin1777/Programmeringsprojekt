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
                                                2. How did it all come to this? Why is the Kingdom under siege from so many mobs?                               
                                                3. Not really (Go back)
                                                    
                                                    
                                                ''')
                            print("\n"*3)
                            dialogue_3 = int(input("->"))
                            if dialogue_3 == 1:
                                print ('''
                                                -Zee monsters in zee area? 
                                                Ja zere ist ein lot of zem. 
                                                
                                                Zere are skeledons zey are ein grey mob zat schoots arrovs at vu. Arh ! Hosdile.

                                                Zen zere are sbiters. Ein eight-legged mob zat can cravl up valls. Arh ! Hostile.

                                                Ve alzo haffe zee sompies. Arh ! Ein green schteffe-looking mob zat tries to atdack vu. Hostile

                                                Zere is Hanozer green ugly mob called Gkoplins. Arh ! Zey vill alzo attack vu Hoffcourze. Hosdile. 

                                                Yet Hanozer dangerous ugly mob zat vill try to atdack vu is zee Orcs. Arh ! Fery ugly, alzo. Hostile.

                                                Zen finally ve haffe zee pats. Arh ! Zey vill alzo try to attack vu aber zey are nicht zo dangerous zo it is Halright. 
                                                Bretty Hannoying zough. 
                                ''')
                            elif dialogue_3 == 2:
                                print('''
                                                - I do not know. It makes me fery zad. 


                                                Let me zing you ein sehr gut zong!
                                                
                                                Like zee great CabdainSparklez once sang:

                                                I uzed to rule zee vorld
                                                Chunks vould load ven I kaffe zee vord
                                                Now effery night I ko sdow avay
                                                Hide from zee mops I uzed to slay
                                                Zey once vere terrified
                                                Effery time I looked into zeir eyes
                                                Fillagers vould cheer mein vay
                                                For ein hero I vas, zat's vat zey'd zay
                                                One minute ve had it all
                                                Next our vorld pekan to fall
                                                Avay from all zat it had once pecome
                                                Zey all cried for mein help, put I sdood zere numb
                                                                                
                                                I kase off into zee poundless skyline
                                                Note plock choirs blaying in zee zunschine
                                                Turn around, bick up mein svord und vield
                                                Zee plade zat once forced effil mops to yield
                                                Und hobe one day zat zis chaos und
                                                Destruczion turns for zee petder
                                                Neffer ein pow in hand
                                                Zat vas ven I ruled zee land

                                ''')
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