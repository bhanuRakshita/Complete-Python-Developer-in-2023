#0 1 1 2 3 5 8......

print("####USING GENERATORS####")
def fib(num):
    a=0
    b=1
    
    for i in range(num):
        yield(a)
        temp = a
        a=b
        b=temp+b

for n in fib(10):
    print(n)

print("##### USING LIST####")
def fib1(num):
    a=0
    b=1
    fibSeq = []
    for i in range(num):
        fibSeq.append(a)
        temp = a
        a = b
        b= temp + b
    return fibSeq

print(fib1(10))