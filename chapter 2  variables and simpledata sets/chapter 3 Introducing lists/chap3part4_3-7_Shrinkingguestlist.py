guests = ['Angela', 'T-sha', 'Amo', 'Tyrone']
cm = 'Tyrone'

if cm in guests:
    print(cm + " can't make it to the dinner")
    guests.remove(cm)
    guests.append('TT')
    

print("we can only invite 2 people for dinner")


guests.insert(0, 'LL')
guests.insert(0, 'mya')
guests.append('Chris')


for x in range(len(guests)):
    if len(guests) > 2 :
        l = guests.pop()
        print(" sorry you cant make it to dinner you just got popped " + l)
    
for guest in guests:
    print("  you are still invited " + guest)

del guests[:]
print(guests)
        
        
        
    
    
    
