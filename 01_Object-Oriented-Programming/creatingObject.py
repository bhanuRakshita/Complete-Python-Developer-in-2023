# OOP

class PlayerCharacter:

    # Class Object Atrribute
    membership = True

    def __init__(self, name):
        # attribute
        self._name = name # _ means plz keep in unmodified

    def run(self):
        print("run")

    #when we care about state of obj
    @classmethod
    def demoClassMethod(cls, p1, p2):
        print(f'p1 id {p1} and p2 is {p2}')
        return (cls('Jastej')) #creating an instance

    # We don't care about attributes
    @staticmethod
    def demoStaticMethod(para1, para2):
        print(f'para1 id {para1} and para2 is {para2}')
        return para1+para2


player1 = PlayerCharacter('Bhanu')
player2 = PlayerCharacter('Aryan')

print(PlayerCharacter.demoClassMethod(12,21))
print(PlayerCharacter.demoStaticMethod(2,1))

