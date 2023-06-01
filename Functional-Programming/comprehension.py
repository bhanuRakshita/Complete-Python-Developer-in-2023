#list comprehensions
#list of nums 0 to 99
my_list1 = [num for num in range(0,100)]

#list of nums in range(0,100) powered to 2
my_list2 = [num**2 for num in range(0,100)]

#list of nums in range(0,100) powered to 2 but only even
my_list3 = [num**2 for num in range(0,100) if num%2==0]

print(my_list3)

#set comprehensions
# just {} instead of [] just all unique

#dictionary comprehension

my_dict = {
    "first":1,
    "second": 2,
    "third": 3
}

new_dict = {k:v for k,v in my_dict.items() if v%2==0}
new_dict1 = {v:v for v in [1,2,3,4,5]}

print(new_dict1)

#EXCERCISE

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list({val for val in some_list if some_list.count(val)>1})
print(duplicates)