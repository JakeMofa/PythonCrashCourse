#ended at chapter 5 page 110
cars  = ['audi', 'bmw', 'subaru', 'toyota' ]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
        

## checking  for equaility
car = 'bmw'
print(car == 'bmw')

#or we can say it is false;

#checking for inequlaities
request_topping = 'mushrooms'
if request_topping  != 'anchovies':
    print("that is not anchovies")



request_tops = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in request_tops)


#check wether users are not in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title(), 'you can post a requesit if you want')

