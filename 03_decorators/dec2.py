#Decorators

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("**********")
        func(*args, **kwargs)
        print("**********")
    return wrap_func

@my_decorator
def hello(a,b,c,d, e=';)'):
    print("Helloooooo",a,b,c,d,e)

hello('Bhanu', 'Aryan', 'Jastej', 'Yuvi')
