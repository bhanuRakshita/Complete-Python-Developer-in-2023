#parent class
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
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
        print("archer successfuly created")

    def attack(self):
        print(f'Attacking with arrows {self.arrows}')

wizard1 = Wizard('Potter', 100)
archer1 = Archer('Luke', 50)

wizard1.log_in()
wizard1.attack()
archer1.attack()