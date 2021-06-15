class Enemy:

    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self):
        pass


class Goblin(Enemy):
    def __init__(self):
        super(Goblin, self).__init__(100, 5)
        print("GlGlGl!!! I am a Goblin and I will slash You!")


class Orc(Enemy):
    def __init__(self):
        super(Orc, self).__init__(100, 15)
        print("Wraar I am an Orc and I will cut You down!!")


class Rat(Enemy):
    def __init__(self):
        super(Rat, self).__init__(100, 10)
        print("Squil!! I am a Rat and I will eat You alive")
