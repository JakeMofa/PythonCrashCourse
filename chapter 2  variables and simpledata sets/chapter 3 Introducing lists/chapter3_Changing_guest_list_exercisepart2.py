guests = ['Angela', 'T-sha', 'Amo', 'Tyrone']
cm = 'Tyrone'

for x in guests:
    if cm in guests: # or if cm ==  guests
        print(cm + " can no longer make it")
        guests[3] = 'lena'

    print("hello " + x + " you are invited to my dinner")
