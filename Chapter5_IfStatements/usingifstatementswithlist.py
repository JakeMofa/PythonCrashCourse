#checking for special items'
requested_toppings = ['mushroom', 'green peppers', 'cheese']

for x in requested_toppings:
    print(f'Adding {x} to pizza')
    
print('\n finished making your pizza!')



#this is one way to do it now what if i want to put a check infront


requested_topping = ['mushroom', 'green peppers', 'cheese']

for i in requested_topping:
    if i == 'green peppers':
        print("  we are out of green peppers ")
    else:
        print(f' Adding {i} to pizza')
    
print('\n finished making your pizza!')