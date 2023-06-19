class Player:
    def log_in(self):
        print('Player logged in!!!')

    def attack(self):
        print('Cannot Attack')

class Wizard(Player):
    def __init__(self, name, power):
        self.name = name
        self.power = power
      
    def attack(self):
        print(f'Attacking with power {self.power}')


class Archer(Player):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
  
    def attack(self):
        print(f'Attacking with arrows {self.arrows}')

wizard1 = Wizard('Potter', 100)
archer1 = Archer('Luke', 50)
player1 = Player()

for player in [wizard1, archer1, player1]:
    player.attack()