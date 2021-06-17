import os
import battle_module
import utils_module


def start_exploring():
    utils_module.game_sound_exploring()
    print("""
You are at a crossroad.
You have 3 paths in front of you:
1. Going to a Village.
2. Going in a Dark and Misty Forrest
3. Going in the Arid Desert""")
    path_option = int(input("Please choose where to go: "))
    if path_option == 1:
        os.system("cls")
        print("Going to the village ...")
        input("Press enter to continue ...")
        battle_module.battle_enemy_village()
    elif path_option == 2:
        os.system("cls")
        print("Going to the village ...")
        input("Press enter to continue ...")
        battle_module.battle_enemy_forest()
    elif path_option == 3:
        os.system("cls")
        print("Going to the village ...")
        input("Press enter to continue ...")
        battle_module.battle_enemy_desert()
    else:
        print("Please choose a valid option")
