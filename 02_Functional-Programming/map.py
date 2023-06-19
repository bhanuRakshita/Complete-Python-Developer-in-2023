# map, filter, zip, reduce
#map(action, data)

from functools import reduce

def multiplyBy2(item):
    return item*2

def checkOdd(item):
    return item%2 != 0

def accumulator(acc, item):
    return acc+item

print(f"MAP: {list(map(multiplyBy2, [1,2,3]))}")
print(f"FILTER: {list(filter(checkOdd, [2,4,2,1,5,3,7]))}")
print(f"ZIP: {list(zip([1,2,3,4,5],[10,20,30, 40]))}")
print(f"REDUCE: {reduce(accumulator, [1,2,3,4,5], 0)}")
