from time import time

def performance_decorator(func):
    def wrapper_func(*args, **kwargs):
        t1=time()
        func()
        t2=time()
        print(f'This task took: {t2-t1} s')
    return wrapper_func

@performance_decorator
def long_task1():
    for i in range(100000):
        i*2

@performance_decorator
def long_task2():
    for i in list(range(100000)):
        i*2
    
long_task1()
long_task2()