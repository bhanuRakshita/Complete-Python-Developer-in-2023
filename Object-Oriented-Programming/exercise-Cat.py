#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Catty', 6)
cat2 = Cat('Kitty', 2)
cat3 = Cat('Lucy', 13)

# 2 Create a function that finds the oldest cat
def get_age(cat):
    return cat.age

def oldestCat(*cats):
    return max(cats, key=get_age)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(oldestCat(cat1, cat2, cat3).name)