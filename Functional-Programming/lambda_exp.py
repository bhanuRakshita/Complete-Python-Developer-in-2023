#  lambda param: action(param)
from functools import reduce

print(f"MAP: {list(map(lambda item: item*2, [1,2,3]))}")

print(f"FILTER: {list(filter(lambda item: item%2!=0, [1,2,3,4,5]))}")

print(f"REDUCE: {reduce(lambda acc, item: acc+item, [1,2,3,4,5], 0)}")

#EXCERCISE

#square
list1 = [5,4,3]
new_list1 = list(map(lambda x: x**2, [1,2,3,4,5]))
print(new_list1)

#list sorting
a = [(0,2), (4,3), (10,-1), (9,9)]
a.sort(key= lambda x: x[1])
print(a)