class SuperList(list):
    def __len__(self):
        return 100

list1 = SuperList()

print(len(list1))
list1.append(5)

print(list1[0])