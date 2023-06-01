class Player:
    def __init__(self, email):
        self.email = email

    def log_in(self):
        print('Player logged in!!!')

class Wizard(Player):
    def __init__(self, name, power, w_email):

        # Player.__init__(self, w_email) # OR
        super().__init__(w_email)
        self.name = name
        self.power = power
      
    def attack(self):
        print(f'Attacking with power {self.power}')

wiz = Wizard('Bhanzzz', 20000, 'bhanzzz@hogwards.com')

print(wiz.email)
