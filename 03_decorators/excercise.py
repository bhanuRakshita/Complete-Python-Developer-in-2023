# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def check_auth(*args, **kwargs):
        if(args[0]['valid']):
            fn(*args, **kwargs)
        else:
            print('User not authenticated')
    return check_auth

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)