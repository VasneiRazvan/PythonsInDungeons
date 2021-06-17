import os
import random
import winsound
import player_module
import exploring_module
import enemy_module
battle_sound = "BattleFinal.wav"
main_menu_sound = "Main_Menu.wav"
exploring_sound = "Exploring.wav"


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
    game_sound_menu()
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
            exploring_module.start_exploring()
        elif answer == 2:
            player_name = input("Choose a name: ")
            player = player_module.Wizard(player_name)
            print("Intro to the World")
            input("Press enter to continue ...")
            os.system("cls")
            exploring_module.start_exploring()
        elif answer == 3:
            player_name = input("Choose a name: ")
            player = player_module.Rogue(player_name)
            print("Intro to the World")
            input("Press enter to continue ...")
            os.system("cls")
            exploring_module.start_exploring()
        else:
            print("Choose a valid option")
    else:
        print("Thank You, good bye!")


def random_enemy():
    random_number = random.randint(0, 2)
    if random_number == 0:
        enemy = enemy_module.Goblin()
    elif random_number == 1:
        enemy = enemy_module.Orc()
    elif random_number == 2:
        enemy = enemy_module.Rat()


def game_sound_menu():
    winsound.PlaySound(main_menu_sound, winsound.SND_ASYNC)


def game_sound_exploring():
    winsound.PlaySound(exploring_sound, winsound.SND_ASYNC)


def game_sound_battle():
    winsound.PlaySound(battle_sound, winsound.SND_ASYNC)


def random_help():
    random_win = random.randint(0, 1)
    if random_win == 0:
        print("""Gods have heard your help and sent someone to help you!
                                You Have Won!""")
    elif random_win == 1:
        print("""Gods didn't had mercy for you
                   You Have Lost Your Life""")
