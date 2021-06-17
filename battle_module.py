import utils_module
import os


def battle_enemy_village():
    utils_module.game_sound_battle()
    os.system("cls")
    print("You are in the village ...")
    print("From a backside alley a enemy appears")
    utils_module.random_enemy()
    print("What are you going to do?")
    input("""
1. Fight the enemy
2. Call for help
3. Run for your life
-> """)


def battle_enemy_forest():
    utils_module.game_sound_battle()
    os.system("cls")
    print("You are in the forest ...")
    print("You hear a sound behind a bush ...")
    utils_module.random_enemy()
    print("What are you going to do?")
    input("""
    1. Fight the enemy
    2. Call for help
    3. Run for your life
    -> """)


def battle_enemy_desert():
    utils_module.game_sound_battle()
    os.system("cls")
    print("You are in the desert ...")
    print("Like a mirage an enemy appears in front of you ...")
    print("What are you going to do?")
    input("""
        1. Fight the enemy
        2. Call for help
        3. Run for your life
        -> """)
