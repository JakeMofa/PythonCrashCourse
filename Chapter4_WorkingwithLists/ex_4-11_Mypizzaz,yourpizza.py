pizza = ['pepperoni', 'sausage' , 'cheese' , 'meat']
friend_pizza = pizza[:]


pizza.append('newguy')
friend_pizza.append('newpizza')

print('my favorite pizzas are')
for x in pizza:
    print(x)
    
print('my freinds pizza are')
for i in friend_pizza:
    print(i)