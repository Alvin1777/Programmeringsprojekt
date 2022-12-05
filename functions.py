import time

def HowToPlay():
    print("This Game Is Based On A Trun Based Fighting System Where You Travel The World By Choosing One Of The Actions Given By The Game To Progress Futher.")
    print("As You Level You Will Encounter New Bosses And Story Events.")
    input("")
def ShowCredits():
    print("")

def QuitGame():
    print("Game Shutting Down...")
    time.sleep(2)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def MainMenu():
    while True:
        print("\n\n\n")
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
                HowToPlay()
            elif main_menu_choice == 3:
                print("Credits Placeholder\n")
                ShowCredits()
            elif main_menu_choice == 4:
                QuitGame()
                break
            else:
                print("Please Use Numbers To Choose One Of The Options Above\n")
                time.sleep(2)
        except:
            print("Please Use Numbers To Choose One Of The Options Above\n")
            time.sleep(2)


