# while True:  
#     try:
#         num=int(input('Please enter age: '))
#         10/num
#     except ZeroDivisionError:
#         print('Enter age greater than 0')
#     except ValueError:
#         print('Please enter a number')
#         continue
#     else:
#         break
#     finally:
#         print("Ok I'm finally done")
#     print("continueeeeeeeeeee")

def sum(num1,num2):
    try:
        return num1+num2
    except(TypeError, ZeroDivisionError) as err:
        print(f"Oooopppsss {err}")

print(sum(1,'2'))