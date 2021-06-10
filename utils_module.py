import os
import winsound
import player_module


main_menu_sound = "Main_Menu.wav"
exploring_sound = "Exploring.wav"
battle_sound = "BattleFinal.wav"


def welcome_message():
    welcome = """
    ****************************************************************************************
    *                                   Welcome,stranger.                                  *
    * Here in Hinderlands, You'll get to fight dragons and conquer the deadliest dungeons. *
    *        In a country where magic rules, anything is possible if you wish so.          *
    *                          It all depends on you, brave hero.                          *
    ****************************************************************************************
    """
    print(welcome)


def start_adventure():
    winsound.PlaySound(main_menu_sound, winsound.SND_ASYNC)
    print("Would You like to start the adventure?")
    user_answer = input("Yes or No -> ")
    if user_answer.upper() == "YES":
        print("OK")
        os.system("cls")  # windows
        # os.system("clear")  # mac/linux/bash
        answer = int(input("""What type of player are you?
    1. Warrior
    2. Wizard
    3. Rogue
    -> """))
        if answer == 1:
            player_name = input("Choose a name: ")
            player = player_module.Warrior(player_name)
            print("Intro to the World")
            input("Press enter to continue ...")
            os.system("cls")
            winsound.PlaySound(exploring_sound, winsound.SND_ASYNC)
            print("""
You are at a crossroad.
You have 3 paths in front of you:
1. Going to a Village.
2. Going in a Dark and Misty Forrest
3. Going in the Arid Desert
""")
            path_option = input("Please choose where to go: ")
        elif answer == 2:
            player_name = input("Choose a name: ")
            player = player_module.Wizard(player_name)
            print("Intro to the World")
        elif answer == 3:
            player_name = input("Choose a name: ")
            player = player_module.Rogue(player_name)
            print("Intro to the World")
        else:
            print("Choose a valid option")
    else:
        print("Thank You, good bye!")
