from time import time

def performance(fn):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Time collapsed: {t2-t1} s')
        return result
    return wrapper_func

@performance   
def demo():
    i=0
    for i in range(1000000):
        i*=5
    return i

demo()