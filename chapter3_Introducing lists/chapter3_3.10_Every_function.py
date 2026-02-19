list = []

list.append('dallas')
list.append('french')
list.append('english')
list.append('cars')

list.sort()
print(list)

for  x in list:
    if len(list) > 2:
        x = list.pop()
        print('you just got popped from the list' + x)


for guest in  list:
    print('you are still on the list' + guest)