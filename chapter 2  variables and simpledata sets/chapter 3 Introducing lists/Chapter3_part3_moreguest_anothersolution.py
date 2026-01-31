guests = ['Angela', 'T-sha', 'Amo', 'Tyrone']
cm = 'Tyrone'


for  i in range(len(guests)):
    if guests[i] == cm:
        print(cm + ' cant make it ')
        guests[i] = 'lena'
        

guests.insert(0, 'TT')
guests.insert(2, 'LL')
guests.append('lay')


for x in guests:
    print('Hello ' + x + 'you are all invited')