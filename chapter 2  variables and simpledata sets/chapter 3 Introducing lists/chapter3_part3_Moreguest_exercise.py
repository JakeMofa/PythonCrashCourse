guests = ['Angela', 'T-sha', 'Amo', 'Tyrone']
cm = 'Tyrone'

if cm in guests:
    print(cm + " can't make it to the dinner")
    guests.remove(cm)
    guests.append('TT')

print("we found a bigger table")

guests.insert(0, 'LL')
guests.insert(0, 'mya')
guests.append('Chris')

for x in guests:
    print("hello " + x + " you are welcome to my  dinner")
    
    
    
