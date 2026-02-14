love = ['char' , 'cupid', 'horse', 'animal']
user = 'horse'


for x in love:
    if x != user:
        print("that user is not found")
    elif x == user:
        print(user.title()+ 'this is the first user')
    else:
        print('none is found')
    break
    