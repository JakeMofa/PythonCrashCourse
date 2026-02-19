#page 126 ended
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni' ,  'extra cheese']
requested_toppings = ['mushrooms', 'french fires' , 'extra cheese']


for requesed_topping  in requested_toppings:
    if requesed_topping in available_toppings:
        print(f'adding one items {requesed_topping}')
    else:
        print(f'we dont have {requesed_topping} item')
        
print('\n finished making your pizza')
        
# for x in requested_toppings:
#     if x in available_toppings:
#         print(f'adding {x}')
#     else:
#         print(f'we dont have {x}')
        
