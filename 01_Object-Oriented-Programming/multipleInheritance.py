class Player:
    def log_in(self):
        print('Player logged in!!!')

class Wizard(Player):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        print("wizard successfuly created")

    def attack(self):
        print(f'Attacking with power {self.power}')


class Archer(Player):
    def __init__(self, name, arrows=10):
        self.name = name
        self.arrows = arrows
        print("archer successfuly created")

    def attack(self):
        print(f'Attacking with arrows {self.arrows}')

    def checkArrows(self):
        print(f'Num of arrows: {self.arrows}')

class HybridBot(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


wizard1 = Wizard('Potter', 100)
archer1 = Archer('Luke', 50)

bot1 = HybridBot('Bot', 50, 100)

bot1.checkArrows()