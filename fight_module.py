import random
import player_module
weapons = ["Sword", "Spell", "Fire"]
shields = ["Armour", "Magic", "Water"]


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = 0
        self.shield = 0

    def damage(self):
        points = random.randint(10, 35)
        self.health -= points

    def select_weapon(self):
        choice = int(input("Choose your weapon 1-Sword, 2-Spell or 3-Fire:  "))
        self.weapon = choice - 1

    def select_shield(self):
        choice = int(input("Choose your shield 1-Armour, 2-Magic or 3-Water:  "))
        self.shield = choice - 1


# Child class of player with override methods for weapon
# and shield selection
class AiPlayer(Player):
    def __init__(self,name):
        super().__init__(name)

    def select_weapon(self):
        choice = random.randint(1, 3)
        self.weapon = choice - 1