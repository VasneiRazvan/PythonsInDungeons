import winsound
import os

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
        print("""
Going to Village ...
Press enter to continue""")
    elif path_option == 2:
        os.system("cls")
        print("""
Going in the Dark and Misty Forrest ...
Press enter to continue""")
        os.system("cls")
    elif path_option == 3:
        os.system("cls")
        print("""
Going to the Arid Dessert ...
Press enter to continue""")
    else:
        print("Please choose a valid option")
