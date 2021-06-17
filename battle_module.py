import utils_module
import winsound
battle_sound = "BattleFinal.wav"


def battle_enemy_village():
    winsound.PlaySound(battle_sound, winsound.SND_ASYNC)
    print("You are in the village ...")
    print("From a backside alley a enemy appears")
    utils_module.random_enemy()
    input("what are you going to do? ...")
