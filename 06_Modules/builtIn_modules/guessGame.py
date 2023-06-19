import sys
from random import choice

argsOk=True
try:
    start = int(sys.argv[1])
    finish = int(sys.argv[2])
except ValueError:
    print('Invalid args')
    argsOk=False

if argsOk:
    ch = choice(range(start, finish))
    print(ch)

    while True:
        try:
            num = int(input(f'enter a num b/w {start} and {finish}: '))
            if (num>start-1 and num<finish+1):
                if(num==ch):
                    print('genius')
                    break
            else:
                print(f'NOOB!! Enter num b/w {start-1} and {finish+1}')
        except ValueError:
            print('please enter a number!!!')

        else:
            print('TRY AGAIN')

        

