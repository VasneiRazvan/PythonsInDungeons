import winsound
import os
import battle_module
exploring_sound = "Exploring.wav"


def start_exploring():
    winsound.PlaySound(exploring_sound, winsound.SND_ASYNC)
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
    elif path_option == 3:
        os.system("cls")
    else:
        print("Please choose a valid option")
