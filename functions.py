def QuitGame():
    print("Game Shutting Down...")

def MainMenu():
    while True:
        print("----------------------------------------\n")
        print("            1.    Play")
        print("            2. How To Play")
        print("            3.   Credits")
        print("            4.    Quit\n")
        print("----------------------------------------\n")

        try:
            main_menu_choice = int(input("What Is Your Action? -> "))

            if main_menu_choice == 1:
                print("Play Placeholder\n")
                #Play()
                break
            elif main_menu_choice == 2:
                print("How To Play Placeholder\n")
                #HowToPlay()
            elif main_menu_choice == 3:
                print("Credits Placeholder\n")
                #Credits()
            elif main_menu_choice == 4:
                QuitGame()
                break
            else:
                print("Please Use Numbers To Choose One Of The Options Above\n")
        except:
            print("Please Use Numbers To Choose One Of The Options Above\n")
MainMenu()
