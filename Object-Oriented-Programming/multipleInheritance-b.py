class Player:
    def __init__(self, email):
        self.email = email

    def log_in(self):
        print('Player logged in!!!')

class Wizard(Player):
    def __init__(self, name, email, power=100):
        super().__init__(email)
        self.name = name
        self.power = power
        print("wizard successfuly created")

    def attack(self):
        print(f'Attacking with power {self.power}')


class Archer(Player):
    def __init__(self, name, email, arrows=10):
        super().__init__(email)
        self.name = name
        self.arrows = arrows
        print("archer successfuly created")

    def attack(self):
        print(f'Attacking with arrows {self.arrows}')

    def checkArrows(self):
        print(f'Num of arrows: {self.arrows}')

class HybridBot(Wizard, Archer):
    def __init__(self, name, email, power=100, arrows=50):
        Wizard.__init__(self, name, email, power)
        Archer.__init__(self, name, email, arrows)

wizard1 = Wizard('Potter', 'potter@gmail.com', 100)
archer1 = Archer('Luke', 'luke@gmail.com', 50)

bot1 = HybridBot('Bot', 'bot@gmail.com', 100, 50)