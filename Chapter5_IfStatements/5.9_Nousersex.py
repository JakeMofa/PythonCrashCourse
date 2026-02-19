#usernames = ['jake', 'admin' , 'ashley' , 'leon']
usernames = []

if not usernames:
    print('we need to  find more users!')
else:
    for  user in usernames:
        if user == 'admin':
            print(f'hello, {user} would you like to see a status report')
        else:
            print(f'Hello {user} thank you for logging in again')

        