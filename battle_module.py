import utils_module
import winsound
import os
battle_sound = "BattleFinal.wav"


def battle_enemy_village():
    winsound.PlaySound(battle_sound, winsound.SND_ASYNC)
    print("You are in the village ...")
    print("From a backside alley a enemy appears")
    os.system("cls")
    utils_module.random_enemy()
    print("What are you going to do?")
    input("""
1. Fight the enemy
2. Call for help
3. Run for your life
-> """)
