#slicing a list
players = ['charles' , 'martina', 'michael', 'florence' , 'eli']

print(players[3:])
print(players[:3])
print(players[-3:])

#looping through a slice

print("here are the first three players on the team")
for player in players[:3]:
    print(player + ".\n")