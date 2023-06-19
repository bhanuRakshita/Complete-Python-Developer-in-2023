from typing import Any


class Toy:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.dict={'owner':'Bhanu'}

    def __str__(self):
        return(self.name)
    
    def __len__(self):
        return 5
        
    def __getitem__(self,item):
        return self.dict[item]
    
    # def __del__(self):
    #     print('Toy destroyed')

    def __call__(self):
        print('yess????')

action_figure = Toy('Super Man', 0)


print(action_figure) #overloaded __str__ will give the name
action_figure() #__call__
print(action_figure['owner'])
