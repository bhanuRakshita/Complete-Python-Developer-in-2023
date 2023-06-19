# def make_list(num):
#     new_list = []
#     for item in range(num):
#         new_list.append(item)
#     return new_list

# my_list = make_list(100)
# print(my_list)

def my_genarator(num):
    for item in range(num):
        yield item
# for num in my_genarator(100):
#     print(num)
g = my_genarator(100)
next(g)
next(g)
next(g)
next(g)


print(next(g))
